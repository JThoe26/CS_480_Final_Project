FROM python:3.11-slim AS runtime
COPY ./ /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5002
CMD ["python", "-m" "login.login_app"]