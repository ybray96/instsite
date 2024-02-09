FROM python:3

ENV PYTHONDONTTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR ~/instsite

#RUN python -m venv ~/opt/instsite/venv

#ENV PATH="/optvenv/bin:$PATH"
RUN echo "Check version Python:" && python --version
RUN pip install --upgrade pip setuptools


COPY ./requirements.txt .
RUN echo "Check version pip:" && pip --version
RUN echo "Content requirements.txt:" && cat requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt --extra-index-url=https://pypi.org/simple/

COPY . .

EXPOSE 8000

#RUN ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
