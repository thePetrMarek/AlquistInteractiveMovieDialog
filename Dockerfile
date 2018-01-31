FROM python:3.6

# Install dependencies
RUN pip install -U flask-cors \
  && git clone https://github.com/facebookresearch/fastText.git \
  && cd fastText \
  && pip install .

ADD . /command-recognizer

WORKDIR /command-recognizer

CMD ["python3","-u", "main.py"]

# Expose port
EXPOSE 5678

