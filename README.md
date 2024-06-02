# YOLOv8_cityscapes
 
This repository provides guidelines on how to apply the Cityscapes[1] dataset to YOLOv8[2] semantic segmentation.
 
## Features 
Due to the incompatibility between the datasets, a conversion process is necessary. The Cityscapes dataset is primarily annotated with polygons in image coordinates for semantic segmentation. However, YOLOv8 requires a different format where objects are segmented with polygons in normalized coordinates. Therefore, the JSON files from the Cityscapes dataset need to be converted to .txt format, removing entries with a label value of 255. After this, the names of the images and the converted .txt annotation files should be made identical. Finally, a data.yaml file should be created at the root of the dataset directory, specifying the train, valid, and test folders containing the data, and entering the label values.

## CLI command

```python
python convert.py <annotation_folder_path>
``` 
## Demo

![alt text](https://github.com/Hyounjun-Oh/YOLOv8_cityscapes/blob/main/yolov8_cityscapes_.gif?raw=true 'YOLOv8 Cityscapes semantic segmentation')

##  Cites
[1] M. Cordts, M. Omran, S. Ramos, T. Rehfeld, M. Enzweiler, R. Benenson, U. Franke, S. Roth, and B. Schiele, “The Cityscapes Dataset for Semantic Urban Scene Understanding,” in Proc. of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016.

[2] YOLOv8 : https://github.com/ultralytics/ultralytics





