FROM python:3.11-slim AS runtime
COPY ./ /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["python", "-m", "notification.notif_app"]