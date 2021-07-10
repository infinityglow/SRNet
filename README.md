# SRNet
## Introduction

Adapted from [Youdao AI](https://github.com/youdao-ai/SRNet), the project is intended to transfer the text style from one image background to another image background. In particular, we would like to generate novel samples based on the existing samples by editing the contents in the image, in order to improve the accuracy of OCR model. The language on the image is Thai, which is relatively scarce in the real world.

Original paper: [Editing Text in the wild](https://arxiv.org/abs/1908.03047) by Liang Wu, Chengquan Zhang, Jiaming Liu, Junyu Han, Jingtuo Liu, Errui Ding and Xiang Bai.

## Data Preparation

- Extract Background Images: Randomly choose 100 real images, remove their texts on the images manually to get 100 background images.

- Prepare Thai Name Dataset: Prepare a dataset that contains common Thai family names, surnames, and all names are categorized into male names and female names. The Thai name corpus we used is from this [repository](https://github.com/korkeatw/thai-names-corpus).

- Training Set for GAN: Run [`datagen.py`](https://github.com/infinityglow/SRNet/blob/master/SRNet-Datagen/datagen.py) to generate as many artificial compound images as you want. There are two configuration file, [one](https://github.com/infinityglow/SRNet/blob/master/SRNet-Datagen/cfg.py) is to specify the number of training samples and saving directories, [another](https://github.com/infinityglow/SRNet/blob/master/SRNet-Datagen/Synthtext/data_cfg.py) config is to adapt the parameters of generated images, such as width, height, image variations, etc.

## Training

The training script is [train.py](https://github.com/infinityglow/SRNet/blob/master/train.py). The configuration for GAN training is from [cfg.py](https://github.com/infinityglow/SRNet/blob/master/cfg.py) to adapt the hyperparameters, e.g., learning rate, batch size, input shape, etc. After 50,000 epochs for training 50,000 training images, the model will eventually converge and the model parameters file will be saved in `./log/params.model`.

## Genaration

After training a model, we can generate novel images by running [`test.py`](https://github.com/infinityglow/SRNet/blob/master/test.py), and the final generated images are listed in the directory [`./test/output`](https://github.com/infinityglow/SRNet/tree/master/test/output). The input file we should feed into the model is in the directory [`./test/input`](https://github.com/infinityglow/SRNet/tree/master/test/input).

![effect](https://github.com/infinityglow/SRNet/blob/master/test/output/effect.png)

## References

* [Editing Text in the Wild](https://arxiv.org/abs/1908.03047): An innovative idea of using GAN's in an unorthodox manner. 

* [Youdao-ai's original repository](https://github.com/youdao-ai/SRNet): The original tensorflow implementation which helped me understand the paper from a different perspective. Also, credit to youdao for the [data synthesis code](https://github.com/youdao-ai/SRNet-Datagen). If anyone is interested in understanding the way data is synthesized for training, examine his repository.

* [SynthText project](https://github.com/ankush-me/SynthText): This work provides the background dataset that is instrumental for data synthesis.

* [Streamlit docs](https://www.streamlit.io/): One of the best libraries to build and publish apps. Severely underrated.
