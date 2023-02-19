# FinalProject-Object_Detector-Analyzer

The primary challenge in object detection is the variation and amount of the objects,
their positions and distortions at acting making it difficult to create a generic model
that can detect all objects accurately. This project aimed to overcome this problem by
using a large, collected diverse dataset and deep learning techniques. In modern days,
we can face with it almost everywhere, for example, traffic cameras, face id on our
gadgets, qr scanners and list goes on. But what if we collect every data that appears
and classificate them, which allows us to analyze every single moment, and then to
take a corresponded actions.

There have been several solutions proposed for object detection in real time. Some of
the popular techniques include using color-based segmentation, feature-based
methods, and deep learning techniques such as Convolutional Neural Networks
(CNNs) and Recurrent Neural Networks (RNNs). In this project, we focused on using
deep learning techniques, which have shown promising results in recent years. Some
of the notable works in this field include "Recent advances in deep learning for object
detection" by Xiongwei Wu , and "Deep learning in multi-object detection and
tracking: state of the art" by Sankar K. Pal and Anima Paramanik.

Data and methods
Object detection models include famous SSD Mobilenet and Faster RCNN, as well
as, a recent state-of-the-art efficient debt and trained on coco object detection dataset.
We collected our images using python and opencv, after then we labeled them using
the label img package. We then split the data into training, and testing sets. We used a
CNN model with four convolutional layers and two fully connected layers as our
baseline model. We also experimented with Faster R-CNN, a state-of-the-art object
detection model that can detect multiple objects in an image. For taking images we
imported time to take little bit of a break between each images, we moved objects,
ourselves in order to collect different angels, and imported uuid to specify img path.
We classificated to such labels as [bicycle, car, motorcycle, airplane, bus, ... ] and put
them into the file "coco.names".![изображение](https://user-images.githubusercontent.com/125818480/219961975-267f70e6-b6a6-4c8e-84df-588e5d82c7c6.png)


![изображение](https://user-images.githubusercontent.com/125818480/219961945-d85de3cd-2792-4912-b671-9ec17501d2a9.png)
![Uploading изображение.png…]()


Results
Our best model achieved an mAP of 0.85 on the testing set, with an average detection
time of 0.15 seconds per image. The confusion matrix showed that the model had the
highest detection rate for objects with certain size. The training and validation curves
showed that the model did not overfit, and using data augmentation improved the
model's generalization ability. We also compared our results with the state-of-the-art
models in the literature review and found that our model achieved comparable
performance.
