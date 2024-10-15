import os
import shutil

validation_data_filename = "/home/xlab-app-center/stable-diffusion-webui/models/Stable-diffusion"
shutil.rmtree(validation_data_filename)  #直接删除该文件夹
os.mkdir(validation_data_filename)  #创建空文件夹
