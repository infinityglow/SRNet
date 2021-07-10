import os
import cv2
import random
import pandas as pd
from preprocessing import *

src_dir = "/Users/fenlai/Desktop/SRNet/test/output"
tar_dir = ""

df = pd.read_csv("/Users/fenlai/Desktop/SRNet/thai_5w_thrid_parity_predict_names.csv")

img_list = [img for img in os.listdir(src_dir) if not img.startswith(".")]
random.shuffle(img_list)

with open("/Users/fenlai/Desktop/SRNet/thai_5w_thrid_parity_predict_names.csv", "r") as f:
    for i in range(100000):

        img_name = random.choice(img_list)
        img = cv2.imread(os.path.join(src_dir, img_name))

        img = cv2.resize(img, (316, 50))

        # shear
        img = shear(img, 316, 50)
        # rotate
        img = rotate(img)

        idx = int(img_name.split('_')[0])

        cv2.imwrite("/Users/fenlai/Desktop/SRNet/train image/data/%d.jpg" % i, img)
        with open("/Users/fenlai/Desktop/SRNet/train image/label.txt", "a") as fw:
            line = "%d.jpg\t%s\n" % (i, df.iloc[idx, 1])
            fw.writelines(line)

        if i % 1000 == 0:
            print("Already generated %d images." % i)



