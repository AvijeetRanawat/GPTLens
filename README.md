# Welcome to GPTLens! 🚀🤖

Hi there! 👋 We're thrilled to introduce you to GPTLens, your next-generation tool for uncovering vulnerabilities in smart contracts using the power of LLMs.

GPTLens is designed with a unique two-stage approach to ensure thorough analysis and minimize false positives. Here's how it works:

## The GPTLens Approach

1. **Auditor Stage**: In this initial phase, GPTLens acts as an auditor agent. The agent scrutinizes your smart contract code to identify potential vulnerabilities, casting a wide net to ensure nothing is missed. The auditor is trained to think like seasoned contract auditor, bringing a broad spectrum of expertise to the table.

2. **Critic Stage**: Here, GPTLens switches gears to its critic role. The critic evaluates the vulnerabilities flagged by the auditor, focusing on minimizing false positives. It assesses each finding based on correctness, severity, and profitability to attackers, ensuring that only the most relevant issues are brought to your attention.

This two-pronged approach, inspired by adversarial frameworks, allows GPTLens to balance the generation of potential vulnerabilities with the critical assessment of their validity, offering you a refined and reliable analysis.

## Why GPTLens?

- **Generality**: Unlike traditional tools, GPTLens isn't limited by predefined patterns. It can conceptualize a wide array of vulnerabilities, thanks to its LLM foundation.
- **Interpretability**: GPTLens provides not just detections but also detailed reasoning behind each finding, giving you insights into the 'why' and 'how' of vulnerabilities.
- **User-Friendly**: Designed with you in mind, GPTLens offers an intuitive interface and seamless interaction, making smart contract auditing more accessible than ever.

## Process Overview
##
1. **API Key Configuration**: Upon starting, you may be prompted to enter your OpenAI API key. The key is securely stored for future sessions.
##
2. **Model Selection**: Choose between `GPT-3.5 Turbo`, `GPT-4`, or `GPT-4 Turbo Preview` for your analysis.
##
3. **Temperature Setting**: Set the "temperature" to control the creativity of the responses (range: 0-1).
##
4. **File Upload**: Upload a `.txt` or `.sol` file containing the smart contract you wish to analyze.
##
5. **Auditor Analysis**: GPTLens initiates the auditor's analysis, meticulously reviewing the contract for potential vulnerabilities. The output includes:
   - **Function Name**: Identifies the function where a vulnerability is detected.
   - **Code**: Highlights the susceptible code snippet within the function.
   - **Vulnerability**: Names the potential vulnerability (e.g., Integer Underflow, Integer Overflow).
   - **Reason**: Provides a comprehensive explanation of the vulnerability, including exploitable conditions.
##
6. **Critic Analysis**: Builds on the auditor's findings with a detailed critique for each identified vulnerability, offering:
   - **Function Name**: Reiterates the function under scrutiny.
   - **Vulnerability**: Specifies the vulnerability type.
   - **Criticism**: Evaluates the auditor's reasoning, with insights to validate or refute the findings.
   - **Correctness**: Scores the accuracy of the identified vulnerability.
   - **Severity**: Rates the potential impact, where a higher score indicates greater severity.
   - **Profitability**: Assesses the attacker's potential gain, with higher scores indicating more lucrative vulnerabilities.
##
7. **Further Analysis?**: Decide whether to analyze another contract or conclude your session.
##
## Getting Started

Dive into the world of smart contract security with GPTLens:

- **Documentation**: Find all the information you need to get started and make the most of GPTLens in our comprehensive [documentation](https://github.com/git-disl/GPTLens/tree/main).

We're excited to see how you leverage GPTLens to enhance your smart contract security. Happy debugging! 💻😊
