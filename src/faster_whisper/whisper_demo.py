# 导入WhisperModel
from faster_whisper import WhisperModel
import time

# 设置模型大小
# model_size = "large-v3"

def transcribe_audio(file_path, model_size="large-v3", device="cpu", compute_type="int8", beam_size=5):
    """
    转录音频文件并打印转录结果。

    参数:
    file_path (str): 音频文件路径。
    model_size (str): 模型大小，默认为 "large-v3"。
    device (str): 运行设备，默认为 "cpu"。
    compute_type (str): 计算类型，默认为 "int8"。
    beam_size (int): 波束搜索大小，默认为 5。

    返回:
    None
    """
    # 创建WhisperModel实例
    model = WhisperModel(model_size, device=device, compute_type=compute_type)
    start_time = time.time()
    # 转录音频文件
    segments, info = model.transcribe(file_path, beam_size=beam_size)
    end_time = time.time()

    # 打印转录时间
    print(f"Transcription took {end_time - start_time:.2f} seconds")
    # 打印检测到的语言及其概率
    print(f"Detected language '{info.language}' with probability {info.language_probability:.6f}")

    # 打印每个音频片段的转录文本
    for segment in segments:
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

# 调用示例
if __name__ == "__main__":
    # 调用transcribe_audio函数并传入音频文件路径
    transcribe_audio("/workspaces/copilot-demo/src/faster_whisper/sources/G1001_S0309.wav")