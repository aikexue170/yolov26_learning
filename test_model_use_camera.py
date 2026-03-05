import cv2
from ultralytics import YOLO
import torch
import os
os.environ['QT_QPA_FONTDIR'] = '/usr/share/fonts'

# 这部分在别的两个test里注释了

cap = cv2.VideoCapture(2)

if torch.cuda.is_available():
    device = torch.device("cuda:0")
else:
    device = torch.device("cpu")

model = YOLO('yolo26x.pt').to(device)
print("推理设备: ", model.device)

if not cap.isOpened():

    print("Cannot open camera")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        print("frame error")
        break

    results = model(frame)

    # results是一个列表，理论上可以同时推理多个帧，解耦后可以实现视频流队列，一次推理多张图片，性能会更好。测试的话还没做
    # 从列表里取出第一个（也就是第一个帧），用它的方法直接把数据标进图里
    annotated_frame = results[0].plot() #BGR格式的numpy数组

    # 展示图片。文字是名字，后面的数组是帧
    cv2.imshow("YOLOv26 Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 清理资源
cap.release()
cv2.destroyAllWindows()