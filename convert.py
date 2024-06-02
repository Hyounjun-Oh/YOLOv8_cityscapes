import os
import json
import sys

def polygon_to_normalized_coords(polygon, img_width, img_height):
    normalized_coords = []
    for point in polygon:
        x_norm = point[0] / img_width
        y_norm = point[1] / img_height
        normalized_coords.append((x_norm, y_norm))
    return normalized_coords

def convert_cityscapes_to_yolov8(json_path, output_dir, class_mapping):
    with open(json_path) as f:
        data = json.load(f)

    img_width = data['imgWidth']
    img_height = data['imgHeight']
    
    annotations = []
    for obj in data['objects']:
        label = obj['label']
        if label not in class_mapping or class_mapping[label] == 255:
            continue
        class_id = class_mapping[label]
        polygon = obj['polygon']
        norm_coords = polygon_to_normalized_coords(polygon, img_width, img_height)
        flattened_coords = [coord for point in norm_coords for coord in point]
        annotations.append((class_id, *flattened_coords))

    # Create output text file
    image_name = os.path.basename(json_path).replace('.json', '.txt')
    output_path = os.path.join(output_dir, image_name)
    
    with open(output_path, 'w') as out_file:
        for ann in annotations:
            out_file.write(' '.join(map(str, ann)) + '\n')

def process_folder(folder_path, class_mapping):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".json"):
                json_path = os.path.join(root, file)
                convert_cityscapes_to_yolov8(json_path, root, class_mapping)

# Example class mapping based on trainId from Cityscapes labels
class_mapping = {
    'unlabeled': 255,
    'ego vehicle': 255,
    'rectification border': 255,
    'out of roi': 255,
    'static': 255,
    'dynamic': 255,
    'ground': 255,
    'road': 0,
    'sidewalk': 1,
    'parking': 255,
    'rail track': 255,
    'building': 2,
    'wall': 3,
    'fence': 4,
    'guard rail': 255,
    'bridge': 255,
    'tunnel': 255,
    'pole': 5,
    'polegroup': 255,
    'traffic light': 6,
    'traffic sign': 7,
    'vegetation': 8,
    'terrain': 9,
    'sky': 10,
    'person': 11,
    'rider': 12,
    'car': 13,
    'truck': 14,
    'bus': 15,
    'caravan': 255,
    'trailer': 255,
    'train': 16,
    'motorcycle': 17,
    'bicycle': 18,
    'license plate': 255,
}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert.py <annotation_folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    process_folder(folder_path, class_mapping)

    # You can use the rename command to make the names of the original image files and annotation files the same.
    # rename 's/gtFine_polygons/leftImg8bit/' *.txt
