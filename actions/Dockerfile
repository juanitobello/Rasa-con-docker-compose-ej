FROM rasa/rasa-sdk:3.4.0
WORKDIR /app
USER root
COPY requirements.txt requirements.txt 
COPY base.csv base.csv
RUN python -m pip install -U pip
#RUN pip3 install -r requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5055
#USER root