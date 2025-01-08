FROM codercom/code-server
# https://coder.com/docs/code-server/FAQ

USER root
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

USER coder
RUN python3 -m venv /home/coder/genai_venv
RUN /home/coder/genai_venv/bin/pip install jupyterlab
RUN /home/coder/genai_venv/bin/pip install openai langchain langchain_community langchain-openai

RUN code-server --install-extension ms-python.python
RUN code-server --install-extension ms-toolsai.jupyter

COPY ./config.yaml /home/coder/.config/code-server/config.yaml
COPY ./settings.json /home/coder/.local/share/code-server/User/settings.json