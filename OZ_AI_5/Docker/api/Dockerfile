FROM python:3.13-slim
WORKDIR /app
COPY . .
# RUN: 이미지를 빌드하는 과정에 실행할 명령어
RUN pip install -r requirements.txt
# CMD: 이미지를 Run할 때, 사용하는 명령어
CMD ["fastapi", "dev", "--host", "0.0.0.0"]