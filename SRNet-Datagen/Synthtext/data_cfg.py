"""
Some configurations.
Copyright (c) 2019 Netease Youdao Information Technology Co.,Ltd.
Licensed under the GPL License 
Written by Yu Qian
"""
import numpy as np

# font
font_size = [20, 20]
oblique_rate = 0
font_dir = 'datasets/fonts/thai_ttf'
standard_font_path = 'datasets/fonts/thai_ttf/Krub-SemiBold.ttf'

# background
bg_filepath = 'datasets/imnames.cp'
temp_bg_path = 'datasets/bg_data/bg_img/'

## background augment
brightness_rate = 0.8
brightness_min = 0.7
brightness_max = 1.5
color_rate = 0.8
color_min =0.7
color_max = 1.3
contrast_rate = 0.8
contrast_min = 0.7
contrast_max = 1.3

# curve
is_curve_rate = 0
curve_rate_param = [0, 0] # scale, shift for np.random.randn()

# perspective
rotate_param = [0, 0] # scale, shift for np.random.randn()
zoom_param = [0.05, 1] # scale, shift for np.random.randn()
shear_param = [0, 0] # scale, shift for np.random.randn()
perspect_param = [0, 0] # scale, shift for np.random.randn()

# render

## surf augment
elastic_rate = 0.000000000000000001
elastic_grid_size = 4
elastic_magnitude = 2

## colorize
padding_ud = [0, 5]
padding_lr = [0, 10]
is_border_rate = 0
is_shadow_rate = 0
shadow_angle_degree = [1] # shift for shadow_angle_param
shadow_angle_param = [0.5, None] # scale, shift for np.random.randn()
shadow_shift_param = np.array([[0, 1, 3], [2, 7, 15]], dtype = np.float32) # scale, shift for np.random.randn()
shadow_opacity_param = [0.1, 0.5] # shift for shadow_angle_param
color_filepath = 'data/colors.cp'
use_random_color_rate = 0
