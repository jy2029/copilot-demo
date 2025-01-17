# 导入WhisperModel
from faster_whisper import WhisperModel

# 设置模型大小
model_size = "large-v3"

# 在GPU上运行，使用FP16
# model = WhisperModel(model_size, device="cuda", compute_type="float16")

# 或者在GPU上运行，使用INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# 或者在CPU上运行，使用INT8
model = WhisperModel(model_size, device="cpu", compute_type="int8")

# 转录音频文件
segments, info = model.transcribe("D:/ai-workspace/copilot-demo/src/faster_whisper/sources/G1003_S0309.wav", beam_size=5)

# 打印检测到的语言及其概率
print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

# 打印每个音频片段的开始时间、结束时间和文本
for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))