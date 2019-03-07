# Batik Image Recognition
Is an educational app that allows user to learn history and meaning of Batik by recognizing and classifying Batik motifs (image) uploaded by users.

*[Video for Application Simulation](https://drive.google.com/open?id=1ZSZ8w06kbT2Prvq0KRKQfTPsS1d6InZF)
*[Introduction Presentation](https://drive.google.com/open?id=1xPbcjj85uPE7QhHale769-sBuKFGSY0z)

## Research Focus
As my [graduation project](https://drive.google.com/open?id=1zfx8tkr1wb61fqYbYHi3vU6mbEuu2baD) for finishing Computer Science & Technology Bachelor Degree in Tianjin University back in 2017, my research is focus on recognizing and classifying Batik motifs so that it can be used to match similar motif then display the history behind it.
1. Recognizing Batik pattern's unique characteristic from several images
2. Classify each patterns into database
3. Finding most similar pattern provided by user with pattern in the database

### Main Goal
Minimizing error when finding the similar pattern provided by user with the pattern inside the database. In order to do achieve this, it depends on retrieving characteristic features from several images which has the same pattern during the learning process. However, user feedback will also be an important step to the system next learning process.

### Algorithm Used
- Image Recognition with SIFT (Scale Invariant Feature Transform)
- Classification with BOW (Bag Of Words)
- Machine Learning with SVM (Support Vector Machine)
![N|Solid](https://i.imgur.com/tnQxyi7l.png)

## Getting Started
I am using Python language and Open CV library. For the user interface I am using Kivy to work with Python

### Prerequisites
For the software I am using Microsoft Visual Studio 2015. Don't forget to add Open CV & Kivy Library after installing MS Visual Studio.

## Running the Program
Double click the Batik.py to run the program. Please tell me if something is wrong so I can fix it, thank you!
