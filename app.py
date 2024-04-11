import os
import json
import chainlit as cl
from openai import AsyncOpenAI
from config import AUDITOR_PROMPT, CRITIC_PROMPT
from dotenv import load_dotenv

client = AsyncOpenAI()

# Instrument the OpenAI client
cl.instrument_openai()

settings = {
    "model": "gpt-3.5-turbo",
    "temperature": 0,
    # Additional settings can be added here
}

# Function to write the OpenAI API key to a .env file
def write_api_key_to_env(api_key):
    with open('.env', 'w') as env_file:
        env_file.write(f"OPENAI_API_KEY={api_key}\n")

# Function to load the OpenAI API key from the .env file
def load_api_key():
    load_dotenv()  # Load .env file
    return os.getenv("OPENAI_API_KEY")

async def initiate_analysis(file_content):
    # Informing the user that the auditor's analysis is starting with an appropriate emoji
    await cl.Message(content="🔍 Starting auditor analysis...").send()

    auditor_response = await perform_auditor_analysis(file_content)
    
    # Formatting and sending the auditor's response with an emoji and in pretty-printed JSON format
    await cl.Message(content=f"📝 Auditor response:\n```json\n{format_response(auditor_response)}\n```").send()

    # Informing the user that the critic's analysis is starting with an appropriate emoji
    await cl.Message(content="🕵️ Starting critic analysis...").send()

    critic_response = await perform_critic_analysis(auditor_response)
    
    # Formatting and sending the critic's response with an emoji and in pretty-printed JSON format
    await cl.Message(content=f"💡 Critic response:\n```json\n{format_response(critic_response)}\n```").send()

    # Ask the user if they would like to continue with emoji for options
    continue_further = await cl.AskActionMessage(
        content="Would you like to continue? 🔄",
        actions=[
            cl.Action(name="yes", value="yes", label="✅ Yes, continue"),
            cl.Action(name="no", value="no", label="❌ No, stop"),
        ],
    ).send()
    
    if continue_further.get("value") == "yes":
        await initiate_analysis(file_content)  # Recursive call to continue the analysis with the same file content
    else:
        await cl.Message(content="🎉 Thanks for using GPTLens!").send()

async def perform_auditor_analysis(file_content):
    auditor = await client.chat.completions.create(
        messages=[
            {"content": AUDITOR_PROMPT, "role": "system"},
            {"content": file_content, "role": "user"}
        ],
        **settings
    )
    return auditor.choices[0].message.content

async def perform_critic_analysis(auditor_response):
    critic = await client.chat.completions.create(
        messages=[
            {"content": CRITIC_PROMPT, "role": "system"},
            {"content": auditor_response, "role": "user"}
        ],
        **settings
    )
    return critic.choices[0].message.content

def format_response(response):
    try:
        # Attempt to load the response as JSON and format it
        json_obj = json.loads(response)
        formatted_json = json.dumps(json_obj, indent=2)  # Pretty-print JSON
        return formatted_json
    except json.JSONDecodeError:
        # If the response is not valid JSON, return it as is
        return response


@cl.on_chat_start
async def prestart():
    pass

@cl.on_message
async def start():
    # api_key_message = await cl.AskUserMessage(content="🔑 Please enter your OpenAI API key:").send()
    # write_api_key_to_env(api_key_message['output'])
    # await cl.Message(content="✅ API key saved!").send()
    api_key = load_api_key()
    global client
    client = AsyncOpenAI(api_key=api_key)

    model_type = await cl.AskActionMessage(
        content="Pick a model!",
        actions=[
            cl.Action(name="gpt3", value="gpt3", label="GPT-3.5 Turbo"),
            cl.Action(name="gpt4", value="gpt4", label="GPT-4"),
            cl.Action(name="gpt4turbo", value="gpt4turbo", label="GPT-4 Turbo Preview"),
        ],
    ).send()

    if model_type:
        settings['model'] = {
            "gpt3": "gpt-3.5-turbo",
            "gpt4": "gpt-4",
            "gpt4turbo": "gpt-4-turbo-preview"
        }.get(model_type.get("value"), settings['model'])

    temperature = await cl.AskUserMessage(content="Give the temperature value (between 0 and 1):").send()
    if temperature:
        try:
            temperature_value = float(temperature['output'])
            if 0 <= temperature_value <= 1:
                settings["temperature"] = temperature_value
        except ValueError:
            await cl.Message(content="Invalid temperature value provided. Using default.").send()

    files = []
    while not files:
        files = await cl.AskFileMessage(
            content="Please upload a text file (.txt) or a Solidity file (.sol) to begin!",
            accept={"text/plain": [".sol", ".txt"]}
        ).send()
    await cl.Message(content="🚀 Setup complete! Ready to start analysis.").send()
    if files:
        text_file = files[0]
        with open(text_file.path, "r", encoding="utf-8") as f:
            file_content = f.read()

        # Initiate the analysis with the uploaded file content
        await initiate_analysis(file_content)
