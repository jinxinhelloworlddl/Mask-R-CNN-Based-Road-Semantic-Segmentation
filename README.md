# Mask-R-CNN-Based-Road-Semantic-Segmentation
## demo
![Alt Text](https://github.com/jinxinhelloworlddl/Mask-R-CNN-Based-Road-Semantic-Segmentation/blob/master/assets/demo.gif)

## installation
conda create -n mrcnn python=3.5

conda install pip

pip install -r requirements.txt

## download weights
To speed up the training, it is recommended to train from [coco weights](https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5). The program will automatically download the coco weights if you start a fresh training. Alternatively, you can download it yourself, and put the weights file in the regarding path.

To run the prediction directly, the well trained [weights](https://drive.google.com/open?id=10h8HU0ezOUGNj-NvLNX_jAAMJ_jCqi74) are provided.

## check directories
When you get everything ready, check the file directories
![directories](https://github.com/jinxinhelloworlddl/Mask-R-CNN-Based-Road-Semantic-Segmentation/blob/master/assets/directories.jpg)
<!---
ProjectRoot
|----datasets
|    |----road
|        |----train
|            |----001.jpg
|            |----002.jpg
|            |----...
|            |----via_region_data.json
|        |----val
|            |----001.jpg
|            |----002.jpg
|            |----...
|            |----via_region_data.json
|----logs
|    |----road20200428T0636
|        |----mask_rcnn_road_0030.h5
|----mask_rcnn_coco.h5
|----maskrcnn.py
|----requirements.txt
|----road.JPG
|----road.mp4
|----test_maskrcnn.py
-->

## run
activate mrcnn

python test_maskrcnn.py

You will see the welcome screen, then you can start either training or prediction
![directories](https://github.com/jinxinhelloworlddl/Mask-R-CNN-Based-Road-Semantic-Segmentation/blob/master/assets/welcome.png)
 

