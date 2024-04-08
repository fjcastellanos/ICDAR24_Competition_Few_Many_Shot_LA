"""
@author: Silvia Zottin
Evaluation code for SAM 2024: few and many shot segmentation ICDAR 2024 competition.

@author: Francisco J. Castellanos
Corrections in the original script.

"""

from skimage import io
from sklearn.metrics import f1_score, jaccard_score, precision_score, recall_score
import os
import os.path
import numpy as np

# Layers
LAYER_BACKGROUND = 0
LAYER_PARATEXT = 1
LAYER_DECORATION = 2
LAYER_TEXT = 3
LAYER_TITLE = 4
LAYER_HEADINGS = 5

DICT_COLORS_GT = {
    LAYER_BACKGROUND: (0, 0, 0),
    LAYER_PARATEXT: (255, 255, 0),
    LAYER_DECORATION: (0, 255, 255),
    LAYER_TEXT: (255, 0, 255),
    LAYER_TITLE: (255, 0, 0),
    LAYER_HEADINGS: (0, 255, 0)
}



gt_images = []
result_images = []


def encodeClassesAccordingToColor(img, dict_colors):
    
    encoded_img = np.zeros((img.shape[0], img.shape[1]))
    for class_idx, color in dict_colors.items():
        encoded_img = encoded_img + np.all(img == np.array(color), axis=-1)*class_idx

    return encoded_img
        
def udiads_evaluate(result_directory, gt_directory):
    """
    Evaluate the results provided by the files in result_directory with respect
    to the ground truth information given by the files in gt_directory.
    """

    # Check whether result_directory and gt_directory are directories
    if not os.path.isdir(result_directory):
        print("The result folder is not a directory")
        return

    if not os.path.isdir(gt_directory):
        print("The gt folder is not a directory")
        return


    for f in sorted(os.listdir(gt_directory)):
        gt_image_path = os.path.join(gt_directory, f)
        gt_image_path = os.path.splitext(gt_image_path)[0] + ".png"
        gt_image = io.imread(gt_image_path)
        encoded_img = encodeClassesAccordingToColor(gt_image, DICT_COLORS_GT)
        gt_images.append(encoded_img.flatten())

        result_image_path = os.path.join(result_directory, f)
        result_image_path = os.path.splitext(result_image_path)[0] + ".png"
        result_image = io.imread(result_image_path)
        encoded_img = encodeClassesAccordingToColor(result_image, DICT_COLORS_GT)
        result_images.append(encoded_img.flatten())

        print(f"############## {DS} Scores ##############")
        precision = precision_score(np.array(gt_images).flatten(), np.array(result_images).flatten(), average=None)
        recall = recall_score(np.array(gt_images).flatten(), np.array(result_images).flatten(), average=None)
        f1_sc = f1_score(np.array(gt_images).flatten(), np.array(result_images).flatten(), average=None)
        iou_sc = jaccard_score(np.array(gt_images).flatten(), np.array(result_images).flatten(), average=None)

        macro_precision = precision_score(np.array(gt_images).flatten(), np.array(result_images).flatten(), average="macro")
        macro_recall = recall_score(np.array(gt_images).flatten(), np.array(result_images).flatten(), average="macro")
        macro_f1_sc = f1_score(np.array(gt_images).flatten(), np.array(result_images).flatten(), average="macro")
        macro_iou_sc = jaccard_score(np.array(gt_images).flatten(), np.array(result_images).flatten(), average="macro")
        
        weighted_precision = precision_score(np.array(gt_images).flatten(), np.array(result_images).flatten(), average="weighted")
        weighted_recall = recall_score(np.array(gt_images).flatten(), np.array(result_images).flatten(), average="weighted")
        weighted_f1_sc = f1_score(np.array(gt_images).flatten(), np.array(result_images).flatten(), average="weighted")
        weighted_iou_sc = jaccard_score(np.array(gt_images).flatten(), np.array(result_images).flatten(), average="weighted")

        print("Macro Precision: ", macro_precision)
        print("Macro Recall: ", macro_recall)
        print("Macro F1 score: ", macro_f1_sc)
        print("Macro Intersection Over Union: ", macro_iou_sc)
        
        print("weighted Precision: ", weighted_precision)
        print("weighted Recall: ", weighted_recall)
        print("weighted F1 score: ", weighted_f1_sc)
        print("weighted Intersection Over Union: ", weighted_iou_sc)
        
        print("Precision per class: ", precision)
        print("Recall: ", recall)
        print("F1 score: ", f1_sc)
        print("Intersection Over Union: ", iou_sc)
        
        
        return macro_precision, macro_recall, macro_f1_sc, macro_iou_sc, weighted_precision, weighted_recall, weighted_f1_sc, weighted_iou_sc

list_macro_precision = []
list_macro_recall = []
list_macro_f1_sc = []
list_macro_iou_sc = []
list_weighted_precision = []
list_weighted_recall = []
list_weighted_f1_sc = []
list_weighted_iou_sc = []

for DS in ["Latin2FS", "Latin14396FS", "Latin16746FS", "Syr341FS"]:

    macro_precision, macro_recall, macro_f1_sc, macro_iou_sc, weighted_precision, weighted_recall, weighted_f1_sc, weighted_iou_sc = udiads_evaluate(result_directory=f"dataset/U-DIADS-Bib-FS/{DS}/pixel-level-gt-{DS}/val_results", gt_directory=f"dataset/U-DIADS-Bib-FS/{DS}/pixel-level-gt-{DS}/validation")
    
    
    list_macro_precision.append(macro_precision)
    list_macro_recall.append(macro_recall)
    list_macro_f1_sc.append(macro_f1_sc)
    list_macro_iou_sc.append(macro_iou_sc)
    list_weighted_precision.append(weighted_precision)
    list_weighted_recall.append(weighted_recall)
    list_weighted_f1_sc.append(weighted_f1_sc)
    list_weighted_iou_sc.append(weighted_iou_sc)


print(f"############## Final Scores ##############")

print("Final result of Macro Precision: ", np.mean(list_macro_precision))
print("Final result of Macro Recall: ", np.mean(list_macro_recall))
print("Final result of Macro F1 score: ", np.mean(list_macro_f1_sc))
print("Final result of Macro Intersection Over Union: ", np.mean(list_macro_iou_sc))


print("Final result of Weighted Precision: ", np.mean(list_weighted_precision))
print("Final result of Weighted Recall: ", np.mean(list_weighted_recall))
print("Final result of Weighted F1 score: ", np.mean(list_weighted_f1_sc))
print("Final result of Weighted Intersection Over Union: ", np.mean(list_weighted_iou_sc))
    
