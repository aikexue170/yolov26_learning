import cv2
import os
os.environ['QT_QPA_FONTDIR'] = '/usr/share/fonts'
#这个是让它使用系统字体，避免一堆QT字体报错弹出来。无伤大雅。这个是linux路径，不需要的话就注释掉

#摄像头的编号是2。linux中使用v4l2-ctl --list-devices可以获取到摄像头的文件。我这边0和1都是电脑摄像头，0是主视频流。2和3是另一个摄像头，就是这个，选取主视频流2
cap = cv2.VideoCapture(2)

if not cap.isOpened():

    print("Cannot open camera")
    exit()

while True:

    #返回的两个参数,ret是代表返回单帧是否成功。frame是帧本身
    ret, frame = cap.read()

    if not ret:
        print("frame error")
        break

    #显示帧
    cv2.imshow("frame", frame)

    #退出键
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break