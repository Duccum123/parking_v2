from ultralytics import YOLO
import cv2
import threading
import time


model = YOLO("D:/Documents/src_py/PBL5/smart_parking/modelAI/empty_space/runs/detect/train/weights/best.pt") 




def scanEmptySpace():
    # đọc ảnh
    cap = cv2.VideoCapture(2)
    if not cap.isOpened():
        raise IOError("Không thể mở camera")

    ret, image = cap.read()
    cap.release()

    if not ret or image is None:
        raise ValueError("Không thể đọc khung hình từ camera")

    results = model(image)

    empty_space = []
    tmp = []
    for r in results:
        for box in r.boxes:
            # tạo độ các góc
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            # độ tin cậy của góc thứ nhất
            conf = box.conf[0].item() 
            # lấy tên thông qua chỉ số của class (box.cls[])

            if (x1 < 215):
                tmp.append("C")
            elif (x1 > 415):
                tmp.append("A")
            else:
                tmp.append("B")
            # cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # cv2.putText(image, f"{label}", (x1, y1 - 10),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    print(tmp)
    empty_space.append("A") if "A" in tmp else None
    empty_space.append("B") if "B" in tmp else None
    empty_space.append("C") if "C" in tmp else None
    print(empty_space)
    return empty_space


    # cv2.imshow("Detection", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
