# YOLOv8_cityscapes
 
This repository provides guidelines on how to apply the Cityscapes[1] dataset to YOLOv8[2] semantic segmentation.
 
## Features 
Due to the incompatibility between the datasets, a conversion process is necessary. The Cityscapes dataset is primarily annotated with polygons in image coordinates for semantic segmentation. However, YOLOv8 requires a different format where objects are segmented with polygons in normalized coordinates. Therefore, the JSON files from the Cityscapes dataset need to be converted to .txt format, removing entries with a label value of 255. After this, the names of the images and the converted .txt annotation files should be made identical. Finally, a data.yaml file should be created at the root of the dataset directory, specifying the train, valid, and test folders containing the data, and entering the label values.

## CLI command

```python
python convert.py <annotation_folder_path>
``` 
## Demo
Inside the result_example folder, you will find model files trained with a small subset of the Cityscapes dataset. This repository includes a few images as examples to show how to input data into the YOLOv8 model. For actual training, please use more data.

The model trained with this data has been applied to the Cityscapes video.
Below is the GIF.
![alt text](https://github.com/Hyounjun-Oh/YOLOv8_cityscapes/blob/main/yolov8_cityscapes_.gif?raw=true 'YOLOv8 Cityscapes semantic segmentation')

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Attribution and Usage

This project uses data from the [Cityscapes Dataset](https://www.cityscapes-dataset.com/). The usage of this dataset is subject to the following terms:

- The dataset can only be used for non-commercial purposes.
- Proper attribution to the [Cityscapes Dataset](https://www.cityscapes-dataset.com/license/) is required.
- Any modifications or adaptations to the data must be distributed under the same license.

For more details, please refer to the [Cityscapes License Agreement](https://www.cityscapes-dataset.com/license/).


##  Cites
[1] M. Cordts, M. Omran, S. Ramos, T. Rehfeld, M. Enzweiler, R. Benenson, U. Franke, S. Roth, and B. Schiele, “The Cityscapes Dataset for Semantic Urban Scene Understanding,” in Proc. of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016.

[2] YOLOv8 : https://github.com/ultralytics/ultralytics





