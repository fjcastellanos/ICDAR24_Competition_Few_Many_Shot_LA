# ICDAR 2024 International Competition on Few-Shot and Many-Shot Layout Segmentation of Ancient Manuscripts
## FSAE: Few-shot Selectional Auto-Encoder

This source code was used for the ICDAR 2024 "International Competition on Few-Shot and Many-Shot Layout Segmentation of Ancient Manuscripts" to participate with the FSAE method.
This code is based on the work published in the International Society for Music Information Retrieval Conference (ISMIR), Milan (Italy), 2023, titled **A Few-shot Neural Approach for Layout Analysis of Music Score Images**.

Please, cite the following work for any use of the code or for a reference to the published work:

```
@inproceedings{Castellanos23_Ismir,
  author    = {Francisco J. Castellanos and
               Antonio Javier Gallego and
               Ichiro Fujinaga},
  title     = {A Few-shot Neural Approach for Layout Analysis of Music Score Images},
  booktitle = {Proceedings of the 24th International Society for Music Information
               Retrieval Conference, Milan, Italy, November 5-9, 2023},
  pages     = {106--113},
  year      = {2023}
  }
```

# Installation Dependencies

## Python dependencies:

  * h5py (2.10.0)
  * Keras (2.2.4)
  * numpy (1.16.0)
  * scipy (1.2.2)
  * Tensorflow (2.4)
  * opencv-python (4.2.0.32)


## Keras configuration

The code needs *Keras* and *TensorFlow* to be installed. It can be easily done through **pip**. 

*Keras* works over both Theano and Tensorflow, so after the installation check **~/.keras/keras.json** so that it looks like:

~~~
{
    "image_dim_ordering": "tf",
    "epsilon": 1e-07,
    "floatx": "float32",
    "backend": "tensorflow"
}
~~~

# How to use
The source code is a python code with the main function in "main.py".
It accepts several parameters to configure the experiments:
  * **-m** `Path used to save the trained model.` (**Example:** *models/Latin2FS_BG.h5*)
  * **-db_train_src** `Path to the file with a list of paths to the images to be employed as training data.` (**Example:** *dataset/Latin2FS/training.txt*)
  * **-db_val_src** `Path to the file with a list of paths to the images to be employed as validating data.` (**Example:** *datasets/Latin2FS/validation.txt*)
  * **-aug** `List of data augmentation types for training the model. Possible modes are: "none", "random", "flipH", "flipV", "rot", "scale". `(**Example:** *random scale rot flipV flipH* (to use all possible augmentations)
  * **-window_w** `Window width for the samples extracted from the images. (**Example:** *512*)
  * **-window_h** `Window height for the samples extracted from the images. (**Example:** *512*)
  * **-lay** `Name of the layer of information to be processed. The rest of the layers are ignored. (**Example:** *BG*)
  * **-l** `Depth of the encoder/decoder of the neural network. (**Example:** *5*)
  * **-f** `Number of filters for the architecture. (**Example:** *64*)
  * **-k** `Kernel size. (**Example:** *3*)
  * **-drop** `Dropout rate. (**Example:** *0.2*)
  * **-pages_train** `Number of pages to be used in training. Value -1 uses all the images in the provided list. (**Example:** *-1*)
  * **-npatches** `Number of patches extracted from each page. Value -1 uses all the patches. For random augmentation (proposal), use a number different from -1. (**Example:** *2048*)
  * **-n_annotated_patches** `Number of patches annotated within the image. This simulates partial annotations of the images. Value -1 stands for annotating the entire images. (**Example:** *-1*)
  * **-e** `Maximum number of epochs to train the model. (**Example:** *200*)
  * **-b** `Batch size. (**Example:** *32*)
  * **-verbose** `To show more details. (**Example:** *1*)
  * **-gpu** `Index of the GPU to be used. (**Example:** *0*)
  

Example of use:

~~~
  python -u main.py
            -m models/Latin2FS_BG.h5
            -db_train_src dataset/Latin2FS/training.txt 
            -db_test_src dataset/Latin2FS/validation.txt  
            -aug random scale rot flipV flipH
            -window_w 512  
            -window_h 512 
            -l 5  
            -f 64  
            -k 3  
            -drop 0.2  
            -pages_train -1  
            -npatches 2048  
            -n_annotated_patches -1  
            -e 200  
            -b 32
            -verbose 1
            -gpu 0
            -b 32
~~~


The models are saved in the folder "models" automatically, and after testing, the resulting images are saved in folder "test" within the parent folder (not the datasets folder). 


## Prediction with Colab
After training, an additional parameter **--test** evaluates the model and another parameter **-res results/out.txt** for dumping the results in a file. This is optional, since the results are shown in the console.
However, for the competition, we used a Google Colab notebook to perform the inference process.

https://colab.research.google.com/drive/1hpc5sY1ee0BuEMNN6IOxNlMZBRt2en53?usp=sharing 


## Training with Colab
Also, there is another Colab notebook for training, but it is not recommended for resource requirements. Note that the following colab is prepared to be provided by the zip file published by the organizers of the competition. 

https://colab.research.google.com/drive/1F2vO3YGHQoIAP5jp0hg-robepSCysrbO?usp=sharing


