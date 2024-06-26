FROM python:3.12.2
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH
WORKDIR $HOME/app
COPY --chown=user . .
RUN pip install -r requirements.txt
CMD ["chainlit", "run", "app.py", "--port", "7860"]