from ultralytics import YOLO
import torch
print("torch version: ", torch.__version__)
print("测试CUDA可用性")

# 看一下CUDA是否可用，如果可用，设置设备为cuda
if torch.cuda.is_available():
    device = torch.device("cuda:0")

# 没有CUDA就CPU
else:
    device = torch.device("cpu")

# ultralytics的YOLO库，从路径中加载YOLO模型。指定使用我们刚刚设定好的设备
model = YOLO('yolo26x.pt').to(device)

# 检查一下设备是哪个
print(model.device)

# 用路径图片推理
results = model("bus.jpg")
print(results)


