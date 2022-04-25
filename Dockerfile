FROM python:3
FROM gorialis/discord.py
RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot
COPY server.py ./
COPY requirements.txt ./
COPY config.txt ./
RUN pip3 install -r requirements.txt
CMD [ "python3", "server.py" ]