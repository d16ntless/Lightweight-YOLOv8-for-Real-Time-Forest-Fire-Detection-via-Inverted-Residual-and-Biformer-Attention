import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/yolov8s-ircb-BiLevelRoutingAttention.yaml')
    # model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='',
                cache=False,
                imgsz=640,
                epochs=100,
                batch=16,
                close_mosaic=10,
                workers=8,
                device='0',
                optimizer='SGD', # using SGD
                project='',
                name='',
                )
