FROM python
RUN pip install flask redis
COPY server.py /
CMD ["flask", "--app", "server.py","run", "--host", "0.0.0.0"]

