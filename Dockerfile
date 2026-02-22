FROM python:3.12-slim

WORKDIR /sge

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && apt -y install cron && apt -y install nano

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./cron /etc/cron.d/cron

# 1. Remove os finais de linha do Windows (\r)
# 2. Adiciona uma linha em branco no final para o cron funcionar
# 3. Ajusta as permissões e carrega no crontab
RUN sed -i 's/\r$//' /etc/cron.d/cron && \
    echo "" >> /etc/cron.d/cron && \
    chmod 0644 /etc/cron.d/cron && \
    crontab /etc/cron.d/cron

# Cria o arquivo de log antecipadamente para evitar erro de "No such file"
RUN touch /var/log/cron.log

EXPOSE 8000

CMD ["sh", "-c", "cron && python manage.py migrate && exec python manage.py runserver 0.0.0.0:8000"]
