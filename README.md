# SASS-FER

The goal of this project is to create a tool that could be used to identify a subject's emotions through their eye movement, lip profile and other facial cues.

We’ll work on two types of emotion representation systems:

Discrete Categories: image input
Continuous Dimensions: video input, which aims to determine the emotion of the person by analyzing various dimensions. 

# Drowsiness Detection 
## Dependencies to install before running the detector:
1. opencv - pip install opencv-python
2. scipy - pip install scipy
3. dlib - conda install -c conda-forge dlib
4. sounddevice - pip install sounddevice
5. soundfile - pip install soundfile
6. numpy 


Using the dlib library, we can find the facial landmarks such as eyes, nose, ears, mouth,etc as illustrated in the below figure.

![image](https://user-images.githubusercontent.com/83316095/215728024-ed33e3f2-9be7-4ba6-a436-657e3836b6c0.png)

Eye Aspect Ratio(EAR) is given by the following formula :

![image](https://user-images.githubusercontent.com/83316095/215727326-5ae04015-7804-4632-9845-73cd9c24a39d.png)

To run the program, simply type the following command :
python3 Drownsiness_Detection.py

or 

Run the cell on jupyter notebook to invoke the camera. 


