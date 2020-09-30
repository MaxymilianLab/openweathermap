FROM python:3.8
RUN pip install requests
ENV OWM_API_KEY=aad6d7413cab9990727f0968775ccd3b
WORKDIR usr/local/share/
COPY weather.py .
CMD ["python","./weather.py","Gdansk"]