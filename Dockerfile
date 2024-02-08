FROM python:3.8

ENV PYTHONDONTTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR ~/opt/instsite

RUN python -m venv ~/opt/instsite/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN echo "Проверка версии Python:" && python --version

COPY ./requirements.txt .
RUN echo "Проверка версии pip:" && pip --version
RUN echo "Содержимое requirements.txt:" && cat requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# RUN ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
