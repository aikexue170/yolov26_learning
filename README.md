# YOLOv26 Learning

基于 YOLOv26 模型的目标检测学习项目。

## 环境要求

- Python
- PyTorch
- OpenCV
- Ultralytics

## 功能

### 1. 静态图片推理
```bash
python test_model.py
```
使用 YOLOv26 模型对 `bus.jpg` 进行目标检测推理，支持 CUDA 加速。

### 2. 摄像头测试
```bash
python test_camera.py
```
测试摄像头连接是否正常，显示实时画面。按 `q` 键退出。

### 3. 实时目标检测
```bash
python test_model_use_camera.py
```
使用摄像头进行实时目标检测，支持 CUDA 加速。按 `q` 键退出。

## 文件说明

| 文件 | 说明 |
|------|------|
| `yolo26x.pt` | YOLOv26 预训练模型权重 |
| `bus.jpg` | 测试用图片 |
| `test_model.py` | 静态图片推理脚本 |
| `test_camera.py` | 摄像头测试脚本 |
| `test_model_use_camera.py` | 实时目标检测脚本 |

## 设备说明

脚本会自动检测 CUDA 是否可用：
- 可用：使用 GPU (cuda:0)
- 不可用：使用 CPU
