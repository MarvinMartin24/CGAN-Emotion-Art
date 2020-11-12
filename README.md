# CGAN-Emotion-Art

## Project overview
* From [Wiki-Art Emotion](http://saifmohammad.com/WebPages/wikiartemotions.html), We built a VGG16 Classifier (98% train acc - 50 val acc) with 3 emotion classes (positive, negative and neutral).
* From this classifier, we labelised the all dataset [WikiArt](https://www.kaggle.com/ipythonx/wikiart-gangogh-creating-art-gan).
* With this new annoted dataset (more than 90 000 images), we created a Deep Conditional GAN (64*64) using pytorch, we trained it for 4 seperated style (portrait, abstract, landscape, flower-painting).
* For now thoses Gan's (generators) are store in `./weights` folder.

## Requirements
* torch
* numpy
* PIL
* matplotlib
* flask

## Usage
```bash
git clone https://github.com/MarvinMartin24/CGAN-Emotion-Art/
# STYLE can be portrait or abstract or landscape or flower-painting
# EMOTION can be positive or negative or neutral
# s will save the images in animation/img
python3 generator_64.py STYLE EMOTION NUM_IMG_TO_GENERATE s
```
## Example
```bash
python3 generator_64.py landscape positive 20 s
python3 generator_64.py portrait negative 2
```
