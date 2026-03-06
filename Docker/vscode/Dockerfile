FROM codercom/code-server:latest
# https://coder.com/docs/code-server/FAQ

USER root
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

USER coder
RUN python3 -m venv /home/coder/genai_venv
RUN /home/coder/genai_venv/bin/pip install uv
COPY --chown=coder:coder ./requirements.txt /tmp/requirements.txt
RUN /home/coder/genai_venv/bin/uv pip install --python /home/coder/genai_venv/bin/python -r /tmp/requirements.txt

ENV PATH="/home/coder/genai_venv/bin:$PATH"

COPY  --chown=coder:coder ./config.yaml /home/coder/.config/code-server/config.yaml
COPY  --chown=coder:coder ./settings.json /home/coder/.local/share/code-server/User/settings.json

RUN code-server --install-extension ms-python.python
RUN code-server --install-extension ms-toolsai.jupyter
