## **TMAP_OBJECT_POSITIONING**

### Overview
Given two contiguous pictures of any given building interior, TMAP_OBJECT_POSITIONING returns 3D coordinates of identified objects in a TMAP (a 2D foldout of a 3D box). The goal of this project is to take this TMAP and produce a generic (for now) 3D rendering of the interior of a room.

### Motivation

During the first week of our Machine Learning course, Tom & I were required to propose a final project. The professor offered a list of potential projects. Many of the final projects could be solved with multivariate linear or logistic regression models or with a neural network containing a few hidden layers. None of these projects excited us. Rather than choose from the professor's pre-determined list of projects, we chose to make up a project. We knew we wanted to work with CNNs. We agreed that we wanted to create 3D environments from 2D images. 

### Build Status
    - [x] Build Dimensional Orientation Block (DOB)
    - [x] Upload training images of DOB
    - [x] Create synthetic DOB data for CNN training
    - [in process] CNN for DOB ID, positioning, and classification
             - [x] CNN Block
             - [x] Regression Block
             - [x] Classification Block
             - [x] One Hot Encoding for Foreground Object detection
             - [x] Exportable Untrained Model
             - [waiting on GPU] Trained Model
             - [pseudocode] Scaling Factor for image pairs
             - [psuedocode] Scaled and reformatted image with DOB classification
             - [ ] Method with bridge object return {file_path_to_image_pair, DOB classifications}
    - [x] YOLO - Real-time object detection
    - [x] TMAP object orientation

### Code Style

All requirements are completed in Python3. For any additional home-baked functionality, abstraction and modularity are preferred.

### Tech/Framework Used

|Stack|
|---------|
|Python3|
|Numpy|
|Pandas|
|Pyplot|
|OpenCV|
|Pillow|
|Glob|
|TensorFlow|
|Keras|
|YOLO Real-Time Object Detection|


 