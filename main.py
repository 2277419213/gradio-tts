import gradio as gr
import pyttsx3
from pydub import AudioSegment
import os

def text_to_speech(text, rate):
    # 获取输入文本的前五个字作为文件名
    file_prefix = text[:5] if len(text) >= 5 else text
    output_file = f"{file_prefix}.wav"
    
    # 使用 pyttsx3 将文本转换为 WAV
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)  # 设置语速
    engine.save_to_file(text, "temp.wav")
    engine.runAndWait()

    # 使用 pydub 将 WAV 文件转换为指定格式
    audio = AudioSegment.from_wav("temp.wav")
    audio = audio.set_frame_rate(8000)
    audio = audio.set_channels(1)
    audio = audio.set_sample_width(2)
    audio.export(output_file, format="wav", bitrate="128k")

    # 删除临时文件
    os.remove("temp.wav")

    return output_file

# 创建 Gradio 接口
with gr.Blocks() as demo:
    gr.Markdown("# 文本转语音")
    
    text_input = gr.Textbox(label="请输入文本", lines=4, placeholder="在此输入文本...")
    rate_input = gr.Slider(label="语速", minimum=50, maximum=300, value=200, step=1)
    generate_button = gr.Button("开始转换")
    
    audio_output = gr.Audio(label="生成的音频", type="filepath")
    download_button = gr.File(label="下载音频", file_count="single", file_types=["audio"])

    def generate_audio(text, rate):
        audio_file = text_to_speech(text, rate)
        return audio_file, audio_file

    generate_button.click(generate_audio, [text_input, rate_input], [audio_output, download_button])

    gr.Markdown("## 工具介绍及使用方法")
    gr.Markdown(
        """
        文本转语音是一款多功能、高效率的文本转换为语音的在线工具。它可以将各种类型的文本转换为高质量的语音，包括段落、文章、电子邮件等等。
        """
    )

# 启动 Gradio 应用
demo.launch(server_name='0.0.0.0', server_port=7860)