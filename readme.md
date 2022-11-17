## **TMAP_OBJECT_POSITIONING**

### Overview
Given two contiguous pictures of any given building interior, TMAP_OBJECT_POSITIONING returns 3D coordinates of identified objects in a TMAP (a 2D foldout of a 3D box). The goal of this project is to take this TMAP and produce a generic (for now) 3D rendering of the interior of a room.

### Motivation

During the first week of our Machine Learning course, Tom & I were required to choose a final project. Many of the final projects could be solved with multivariate linear or logistic regression models or with a neural network containing minimal hidden layers. Tom & I felt that this was our opportunity to take a deep dive into ML and Deep Learning and move beyond the scope of our class. So rather than choose from the professor's pre-determined list of projects, we chose to solve a problem that encompassed a great number of interesting topics. We wanted to learn more than we figured we might given the pace of the course, and we wanted to the fulfillment of having solved a difficult problem. 

### Build Status
    - [x] Build Dimensional Orientation Block (DOB)
    - [x] Upload training images of DOB
    - [x] Create synthetic DOB data for CNN training
    - [in process] CNN for DOB ID, positioning, and classification
    - [ ] YOLO - Real-time object detection
    - [x] TMAP object orientation

### Code Style

All requirements are completed in Python3. For any additional home-baked functionality, abstraction and modularity are preferred.

### Tech/Framework Used

|Stack|
|---------|
|Python3|
|Numpy|
|Pandas|
|OpenCV|
|Pillow|
|Glob|
|TensorFlow|
|Keras|
|YOLO Real-Time Object Detection|


 