# 使用官方的 Python 基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录的内容到工作目录
COPY . .

# 安装依赖库
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 Gradio 默认端口
EXPOSE 7860

# 运行应用
CMD ["python", "main.py"]
