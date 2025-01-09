# gradio-tts

## 项目介绍

这是一个基于 Gradio 的文本转语音应用。用户可以输入文本并调整语速，应用会将文本转换为语音，并生成音频文件。生成的音频文件可以在线播放并下载。音频文件的名称是输入文本的前五个字。

## 功能特点

- 支持文本输入并转换为语音
- 可调节语速
- 生成的音频文件可以在线播放和下载
- 音频文件名称根据输入文本的前五个字命名

## 使用方法

### 1. 克隆项目

首先，克隆项目到本地：

```bash
git clone https://github.com/yourusername/gradio-tts.git
cd gradio-tts
```

### 2. 安装依赖

确保你已经安装了 Python 3.11。然后使用以下命令安装依赖：

```bash
pip install -r requirements.txt
```

### 3. 运行应用

使用以下命令启动应用：

```bash
python main.py
```

应用将会在本地的 `7860` 端口启动。你可以在浏览器中访问 `http://localhost:7860` 进行使用。

### 4. 使用 Docker 运行

你也可以使用 Docker 来运行此应用。首先，构建 Docker 镜像：

```bash
docker build -t gradio-tts-app .
```

然后，运行 Docker 容器：

```bash
docker run -p 7860:7860 gradio-tts-app
```

应用同样会在本地的 `7860` 端口启动。

## 文件说明

- `main.py`：主程序文件，包含文本转语音的实现和 Gradio 接口的定义。
- `requirements.txt`：Python 依赖库列表。
- `Dockerfile`：用于构建 Docker 镜像的文件。
- `README.md`：项目介绍和使用方法。
- `LICENSE`：开源协议。

## 贡献

如果你有任何改进建议或发现了问题，请提交 issue 或 pull request。

## 许可证

此项目遵循 MIT 许可证。详情请参阅 `LICENSE` 文件。
