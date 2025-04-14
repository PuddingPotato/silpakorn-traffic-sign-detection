import cv2
import time
import os

directory = r'C:\Users\tesyp\OneDrive\Desktop\RM Project\Videos\new mp4'
files = os.listdir(directory)

for file in files:
    video_path = os.path.join(directory, file)
        
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f'Can not open file name {file}')
    else:
        print(f'Opening file name {file}')
    frame_count = 0
    start = time.time()
    frame_time = 0
    while True:
        ret, frame = cap.read()
        frame_time += 1
        
        if frame_time % 6 == 0:
            if not ret:
                break

            frame_count += 1
            img_name = f'frame{frame_count}'
            storage = rf'C:\Users\tesyp\OneDrive\Desktop\RM Project\new mp4 frames\{img_name} from {file}.jpg'
            cv2.imwrite(storage, frame)
            print(img_name, 'Saved')

    stop = time.time()

    cap.release()
    cv2.destroyAllWindows()

    print(f'{stop-start} seconds')
