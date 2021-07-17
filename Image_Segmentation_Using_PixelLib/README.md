# Image Segmentation Using Pixellab


![image](https://user-images.githubusercontent.com/62799332/125184412-2b293200-e23b-11eb-8da9-461d9003b44b.png)

[Pixellib](https://github.com/ayoolaolafenwa/PixelLib) is a library for performing segmentation of objects in images and videos. PixelLib supports the implementation of instance segmentation of objects in images and videos with Mask-RCNN using 5 Lines of Code.

## Installation
Install PixelLib and its dependencies

**Install Tensorflow**:

PixelLib supports **tensorflow's version (2.0 - 2.4.1)**. Install tensorflow using:

```
pip3 install tensorflow
```

If you have have a pc enabled GPU, Install tensorflow--gpu's version that is compatible with the cuda installed on your pc:


```
pip3 install tensorflow--gpu
```


**Install Pixellib with**:

```
pip3 install pixellib --upgrade
```

**Visit PixelLib's official documentation on** [readthedocs](https://pixellib.readthedocs.io/en/latest/)


## Important Step
Download  Mask RCNN model file  `mask_rcnn_coco.h5` to load it for the above task and place it in the same folder where your python file will be.
**[Click to download](https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5)**

**Note-** Deeplab and mask r-ccn models are available in the [release](https://github.com/ayoolaolafenwa/PixelLib/releases) of this repository.