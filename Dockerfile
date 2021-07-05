FROM python:3.7

# RUN echo "Europe/Sarajevo" > /etc/timezone
# RUN dpkg-reconfigure -f noninteractive tzdata

RUN pip3 install fastapi uvicorn minio pydantic urlib3

COPY ./minio_rest_api /minio_rest_api

CMD ["uvicorn", "minio_rest_api.index:app", "--host", "0.0.0.0", "--port", "15400"]