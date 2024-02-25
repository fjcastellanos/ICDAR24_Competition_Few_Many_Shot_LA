


import sys, os, re
import shutil
import cv2
import numpy as np
from os.path import dirname
import copy


def createParentDirectory(path_file):
    pathdir = dirname(path_file)
    mkdirp(pathdir)

def mkdirp(directory):
    if not os.path.isdir(directory):
        os.makedirs(directory)

def deleteFolder(directory):
    if os.path.isdir(directory):
        shutil.rmtree(directory, ignore_errors=True)



def listFilesRecursive(path_dir):
    
    try:
        listOfFile = os.listdir(path_dir)
    except Exception:
        pathdir_exec = os.path.dirname(os.path.abspath(__file__))
        path_dir = pathdir_exec + "/" + path_dir
        listOfFile = os.listdir(path_dir)

    list_files = list()
    
    for entry in listOfFile:
        fullPath = os.path.join(path_dir, entry)
        if os.path.isdir(fullPath):
            list_files = list_files + listFilesRecursive(fullPath)
        else:
            list_files.append(fullPath)
    
    list_files.sort()            
    return list_files


def match_SRC_GT_Images(list_src_images, list_gt_images):
    list_matched_data = []
    for idx_image in range(len(list_src_images)):
        src_image = list_src_images[idx_image]
        gt_image = list_gt_images[idx_image]

        src_basename = os.path.basename(src_image).split(".")[0]
        gt_basename = os.path.basename(gt_image).split(".")[0]

        print('*'*80)
        print("Image %d:" % (idx_image))
        print("\t%s" % (src_image))
        print("\t%s" % (gt_image))

        assert(src_basename == gt_basename)

        list_matched_data.append( (src_image, gt_image))
        

    print("SRC and GT images are match.")
    return list_matched_data


def load_gt_image(path_file, regions_mask=None):
    file_img = cv2.imread(path_file, cv2.IMREAD_UNCHANGED,)  # 4-channel
    if file_img is None : 
        raise Exception(
            'It is not possible to load the image\n'
            "Path: " + str(path_file)
        )
    
    return file_img

def load_src_image(path_file, mode=cv2.IMREAD_COLOR):

    file_img = cv2.imread(path_file, mode)
    if file_img is None : 
        raise Exception(
            'It is not possible to load the image\n'
            "Path: " + str(path_file)
        )

    return file_img


def saveImage (image, path_file):
    assert 'numpy.ndarray' in str(type(image))
    assert type(path_file) == str
    
    path_dir = dirname(path_file)

    if not os.path.exists(path_dir):
        os.makedirs(path_dir, 493)

    cv2.imwrite(path_file, image)


def appendString(content_string, path_file, close_file = True):
    assert type(content_string) == str
    assert type(path_file) == str
    
    path_dir = dirname(path_file)

    if not os.path.exists(path_dir):
        os.makedirs(path_dir, 493)
            
    f = open(path_file,"a")
    f.write(content_string + "\n")
    
    if close_file == True:
        f.close()
    
        
def writeString(content_string, path_file, close_file = True):
    assert type(content_string) == str
    assert type(path_file) == str
    
    path_dir = dirname(path_file)

    if not os.path.exists(path_dir):
        os.makedirs(path_dir, 493)
            
    f = open(path_file,"w")
    f.write(content_string + "\n")
    
    if close_file == True:
        f.close()
    
def readStringFile(path_file):
    assert type(path_file) == str

    f = open(path_file)
    
    content = f.read()
    f.close()
    
    assert type(content) == str

    return content
    
        
def __remove_attribute_namespace(config, key):
    try:
        delattr(config, key)
    except:
        pass

def getPathModel(config):
    config_copy = copy.deepcopy(config)
    
    __remove_attribute_namespace(config_copy, 'test')
    
    __remove_attribute_namespace(config_copy, 'db_test_src')
    __remove_attribute_namespace(config_copy, 'db_test_gt')
    __remove_attribute_namespace(config_copy, 'gpu')
    __remove_attribute_namespace(config_copy, 'verbose')
    __remove_attribute_namespace(config_copy, 'res')
    __remove_attribute_namespace(config_copy, 'save')
    __remove_attribute_namespace(config_copy, 'aug_test')
    __remove_attribute_namespace(config_copy, 'n_aug')
    __remove_attribute_namespace(config_copy, 'drop_test')
    __remove_attribute_namespace(config_copy, 'm')

    if config.no_mask is None or config.no_mask == False:
        __remove_attribute_namespace(config_copy, 'no_mask')

    
    str_config = str(config_copy).replace("Namespace", "modelCNN_").replace("(", "").replace(")", "").replace("=", "_").replace("'", "").replace(",","").replace(" ", "__").replace("[", "_").replace("]","_").replace("]","_").replace("/", "_")
    str_config = "models/modelCNN/"+str_config + ".h5"
    str_config = str_config.replace("datasets","dbs").replace("training", "train").replace("db_train","dtr").replace("pages_train", "pt")
    return str_config


'''
ltrain = ["training/img-p/ej1.png", "training/img-p/ej2.png", "training/img-p/ej3.png",
     "training/pixel-p/ej1.png", "training/pixel-p/ej2.png", "training/pixel-p/ej3.png" ]

lval = ["validation/img-p/ej1.png", "validation/img-p/ej2.png", "validation/img-p/ej3.png",
     "validation/pixel-p/ej1.png", "validation/pixel-p/ej2.png", "validation/pixel-p/ej3.png" ]

list_training_data_images = [item for item in ltrain if "/img-" in item]
list_validation_data_images = [item for item in lval if "/img-" in item]

str_list_training_data_images = "\n".join(list_training_data_images)
str_list_validation_data_images = "\n".join(list_validation_data_images)

writeString(str_list_training_data_images, "prueba/prueba_train.txt", close_file = True)
writeString(str_list_validation_data_images, "prueba/prueba_val.txt", close_file = True)


'''