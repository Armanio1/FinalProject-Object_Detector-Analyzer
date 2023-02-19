from Detector1 import *

modelURL = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz'
#modelURL = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d4_coco17_tpu-32.tar.gz'
#modelURL = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_inception_resnet_v2_1024x1024_coco17_tpu-8.tar.gz'
classFile = "labels.names"
imagePath = "test\cars.png"
#videoPath = 0
threshold = 0.5

detector = Detector()
detector.readClasses(classFile)
detector.downloadModel(modelURL)
detector.loadModel()
detector.predictImage(imagePath, threshold)
#detector.predictVideo(videoPath, threshold)