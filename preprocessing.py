import cv2
import numpy as np
import random

def padding(img, expected_width, expected_height):
    height, width = img.shape[0], img.shape[1]
    padded_width = ((expected_width - width) // 2, (expected_width - width + 1) // 2)
    padded_height = ((expected_height - height) // 2, (expected_height - height + 1) // 2)
    padded_channel = (0, 0)

    # padding
    img = np.pad(img, (padded_height, padded_width, padded_channel), constant_values=255)
    return img

def shear(img, expected_width, expected_height):
    height, width = img.shape[0], img.shape[1]

    co1 = [0, 0]
    co2 = [width, 0]
    co3 = [0, height]
    co4 = [width, height]

    height_range1 = range(-7, 8)
    height_range2 = range(-5, 6)
    width_range1 = range(-5, 6)
    width_range2 = range(-2, 3)

    pts_o = np.float32([co1, co2, co3, co4])

    height_bias1 = random.choice(height_range1)
    height_bias2 = random.choice(height_range2)
    width_bias1 = random.choice(width_range1)
    width_bias2 = random.choice(width_range2)

    pts_d = np.float32([[width_bias1, height_bias1],
                        [width - width_bias1, height_bias2],
                        [width_bias2, height - height_bias1],
                        [width - width_bias2, height - height_bias2]])

    M = cv2.getPerspectiveTransform(pts_o, pts_d)

    final_img = cv2.warpPerspective(img, M, (expected_width, expected_height), borderMode=cv2.BORDER_REPLICATE)
    return final_img

def rotate(img):
    height, width = img.shape[:2]
    cX, cY = width / 2, height / 2
    angle = random.choice(range(-10, 11)) * 0.01

    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    nW = int(height * sin + width * cos)
    nH = int(height * cos + width * sin)

    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    return cv2.warpAffine(img, M, (nW, nH), borderMode=cv2.BORDER_TRANSPARENT)

def shift(img):
    dx = random.choice(range(-3, 3))
    dy = random.choice(range(-3, 3))

    height, width = img.shape[:2]
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    dst = cv2.warpAffine(img, M, (width, height), borderMode=cv2.BORDER_TRANSPARENT)
    return dst

def crop(img, params):
    left, right, up, down, size = params
    left_range = range(left-5, left+1)
    right_range = range(right, right+6)
    up_range = range(up-3, up+1)
    down_range = range(down, down+4)

    left_final = max(0, random.choice(left_range))
    right_final = min(random.choice(right_range), size)
    up_final = random.choice(up_range)
    down_final = random.choice(down_range)

    img = img[up_final:down_final, left_final: right_final, :]
    return img