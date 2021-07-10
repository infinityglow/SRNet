import os
import shutil

cur_path = "./SRNet-Datagen/Synthtext/datasets/srnet_data"
des_path = "./test/input"

for img_name in os.listdir(os.path.join(cur_path, "i_t")):
    img, type = os.path.splitext(img_name)
    img += "_i_t"
    img_name_ = img + type
    shutil.copy(os.path.join(cur_path, "i_t", img_name), des_path)
    os.rename(os.path.join(des_path, img_name), os.path.join(des_path, img_name_))

# list = []
# dirs = os.listdir("/Users/fenlai/Desktop/SRNet/test/input")

# for dir1 in dirs:
#     for dir2 in os.listdir("/Users/fenlai/Desktop/SRNet/test/output"):
#         if int(dir1.split('_')[0]) == int(dir2.split('_')[0]):
#             break
#     else:
#         shutil.copy("/Users/fenlai/Desktop/SRNet/test/input/"+dir1, "/Users/fenlai/Desktop/SRNet/test/new_input")
    # print(int(dir.split('_')[0]))
    # print(os.listdir("/Users/fenlai/Desktop/SRNet/test/output")[0].split("_")[0])
