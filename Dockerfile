FROM python:3
RUN git clone https://github.com/um-computacion-tm/parcial-2-2022-tomasgrau2.git
WORKDIR /parcial-2-2022-tomasgrau2
RUN pip install -r requirements.txt
CMD ["python3", "-m", "unittest"]
