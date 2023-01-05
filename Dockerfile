FROM rasa/rasa:3.4.0
RUN mkdir -p /app
COPY . /app
WORKDIR  '/app'
USER root

RUN  rasa train 

VOLUME /app/models


CMD [ "run","-m","/app/models","--enable-api","--cors","*","--debug" ,"--endpoints", "endpoints.yml", "--debug"]

EXPOSE 5005