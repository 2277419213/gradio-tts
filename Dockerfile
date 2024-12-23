# 使用官方 Python 镜像作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装 FFmpeg
RUN apt-get update && apt-get install -y espeak-ng ffmpeg

# 复制当前目录的内容到工作目录
COPY . /app

# 安装 Python 依赖
RUN pip install -r requirements.txt

# 暴露应用运行的端口
EXPOSE 7860

# 启动应用
CMD ["python", "main.py"]
