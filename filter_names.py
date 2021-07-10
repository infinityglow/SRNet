from paddleocr import PaddleOCR
import pandas as pd
import cv2
import os

ocr_india_name = PaddleOCR(use_angle_cls=False, lang='ch',
                           rec_model_dir='/Users/fenlai/Desktop/SRNet/model',
                           max_text_length=34,
                           rec_char_dict_path='/Users/fenlai/Desktop/SRNet/th_base_dict.txt',
                           use_gpu=False)


src = '/Users/fenlai/Desktop/SRNet/test/name/data/'
with open("/Users/fenlai/Desktop/SRNet/test/name/label.txt", 'r') as f:
    names = f.readlines()

error_count = 0
total_count = 0
drop_list = []

def resize_img_keep_ratio(img,target_size):
      # img = cv2.imread(img_name)
      old_size= img.shape[0:2]
      #ratio = min(float(target_size)/(old_size))
      ratio = min(float(target_size[i])/(old_size[i]) for i in range(len(old_size)))
      new_size = tuple([int(i*ratio) for i in old_size])
      img = cv2.resize(img,(new_size[1], new_size[0]))
      pad_w = target_size[1] - new_size[1]
      pad_h = target_size[0] - new_size[0]
      top,bottom = pad_h//2, pad_h-(pad_h//2)
      left,right = pad_w//2, pad_w -(pad_w//2)
      img_new = cv2.copyMakeBorder(img,top,bottom,left,right,cv2.BORDER_CONSTANT,None,(0,0,0))
      return img_new

def resize_img_with_padding(type):
    src = '/Users/fenlai/Desktop/SRNet/test/name/'+type+'/'
    for root, dirs, files in os.walk(src):
        for file in files:
            if '.png' in str(file):
                img = cv2.imread(src+file)
                if img is None:
                    continue
                img=resize_img_keep_ratio(img,[32,320])
                cv2.imwrite(src+file,img)

# resize_img_with_padding('data')


for name in names:
    img_name = name.strip('\n').split('\t')[0]
    label_name = name.strip('\n').split('\t')[-1]
    total_count = total_count + 1
    img = cv2.imread(src + img_name)

    paddle_reuslt = ocr_india_name.ocr(src + img_name, det=False, rec=True, cls=False)
    predict_result = paddle_reuslt[0][0]

    if predict_result != label_name:
        print("image name" + img_name)
        print("predicted name" + predict_result)
        print("true name" + label_name)

    # if paddle_reuslt is not None:
    #     predict_result = paddle_reuslt[0][0]
    #     sim_score = fuzz.ratio(predict_result.replace(' ', ''), v['name'].replace(' ', ''))
    #     if sim_score <= 70:
    #         print(img_name, predict_result, v['name'], sim_score, sep=',')
    #         error_count = error_count + 1
    #         drop_list.append(i)
    #     if total_count % 200 == 0:
    #         print(total_count, error_count)

print("total number of mispredicted example: %d" % error_count)
print("Accuracy: %.2f" % (error_count / total_count))
