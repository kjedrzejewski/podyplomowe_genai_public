FROM codercom/code-server
# https://coder.com/docs/code-server/FAQ

USER root
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

USER coder
RUN python3 -m venv /home/coder/genai_venv
RUN /home/coder/genai_venv/bin/pip install jupyterlab ipywidgets
RUN /home/coder/genai_venv/bin/pip install openai langchain langchain_community langchain-openai
RUN /home/coder/genai_venv/bin/pip install huggingface_hub
RUN /home/coder/genai_venv/bin/pip install Pillow
RUN /home/coder/genai_venv/bin/pip install wikipedia-api fandom-py
RUN /home/coder/genai_venv/bin/pip install mathparse

ENV PATH="/home/coder/genai_venv/bin:$PATH"

RUN code-server --install-extension ms-python.python
RUN code-server --install-extension ms-toolsai.jupyter

COPY  --chown=coder:coder ./config.yaml /home/coder/.config/code-server/config.yaml
COPY  --chown=coder:coder ./settings.json /home/coder/.local/share/code-server/User/settings.json