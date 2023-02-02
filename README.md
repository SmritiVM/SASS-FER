# SASS-FER

The goal of this project is to create a tool that could be used to identify a subject's emotions through their eye movement, lip profile and other facial cues.

We’ll work on two types of emotion representation systems:

- Discrete Categories: image input, and

- Continuous Dimensions: video input, which aims to determine the emotion of the person by analyzing various dimensions. 

# Drowsiness Detection 
## Dependencies to install before running the detector:
1. opencv - pip install opencv-python
2. scipy - pip install scipy
3. dlib - conda install -c conda-forge dlib
4. sounddevice - pip install sounddevice
5. soundfile - pip install soundfile
6. numpy 


Eye Aspect Ratio(EAR) is given by the following formula :

![image](https://user-images.githubusercontent.com/83316095/215727326-5ae04015-7804-4632-9845-73cd9c24a39d.png)

To run the program, simply type the following command :
python3 Drownsiness_Detection.py

or 

Run the cell on jupyter notebook to invoke the camera. 

References: http://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf


