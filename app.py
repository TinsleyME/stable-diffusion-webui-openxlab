import os
import shutil
os.chdir(f"/home/xlab-app-center")
os.system(f"git init")
os.system(f"git lfs install")
os.system(f"git lfs update")

os.system(f"git clone https://github.com/mcmonkeyprojects/sd-dynamic-thresholding /home/xlab-app-center/extensions/sd-dynamic-thresholding")
os.system(f"git clone https://github.com/zanllp/sd-webui-infinite-image-browsing /home/xlab-app-center/extensions/sd-webui-infinite-image-browsing")
os.system(f"git clone https://github.com/Mikubill/sd-webui-controlnet /home/xlab-app-center/extensions/sd-webui-controlnet")
os.system(f"git clone https://github.com/P2Enjoy/sd-webui-roop-uncensored /home/xlab-app-center/extensions/sd-webui-roop-uncensored")
os.system(f"git clone https://github.com/djbielejeski/a-person-mask-generator.git /home/xlab-app-center/extensions/a-person-mask-generator")
os.system(f"git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete /home/xlab-app-center/extensions/a1111-sd-webui-tagcomplete")
os.system(f"git clone https://github.com/Bing-su/adetailer.git /home/xlab-app-center/extensions/adetailer")
os.system(f"git clone https://github.com/Scholar01/sd-webui-mov2mov.git /home/xlab-app-center/extensions/sd-webui-mov2mov")
#os.system(f"git clone https://github.com/glucauze/sd-webui-faceswaplab /home/xlab-app-center/extensions/sd-webui-faceswaplab")
os.system(f"git clone https://github.com/Iyashinouta/sd-model-downloader /home/xlab-app-center/extensions/sd-model-downloader")
os.system(f"git clone https://gitcode.net/overbill1683/stable-diffusion-webui-localization-zh_Hans /home/xlab-app-center/extensions/stable-diffusion-webui-localization-zh_Hans")
os.system(f"git clone https://github.com/SenshiSentou/sd-webui-qic-console /home/xlab-app-center/extensions/sd-webui-qic-console")

#model cn
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_ip2p_fp16.safetensors -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11e_sd15_ip2p_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_shuffle_fp16.safetensors -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11e_sd15_shuffle_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny_fp16.safetensors -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_canny_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11f1p_sd15_depth_fp16.safetensors -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11f1p_sd15_depth_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_inpaint_fp16.safetensors -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_inpaint_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart_fp16.safetensors -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_lineart_fp16.safetensors")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_mlsd_fp16.safetensors -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_mlsd_fp16.safetensors")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_normalbae_fp16.safetensors -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_normalbae_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose_fp16.safetensors -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_openpose_fp16.safetensors")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_scribble_fp16.safetensors -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_scribble_fp16.safetensors")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_seg_fp16.safetensors -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_seg_fp16.safetensors")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_softedge_fp16.safetensors -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_softedge_fp16.safetensors")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15s2_lineart_anime_fp16.safetensors -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15s2_lineart_anime_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11f1e_sd15_tile_fp16.safetensors -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11f1e_sd15_tile_fp16.safetensors")
#yaml cn
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11e_sd15_ip2p_fp16.yaml -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11e_sd15_ip2p_fp16.yaml")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11e_sd15_shuffle_fp16.yaml -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11e_sd15_shuffle_fp16.yaml")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_canny_fp16.yaml -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_canny_fp16.yaml")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11f1p_sd15_depth_fp16.yaml -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11f1p_sd15_depth_fp16.yaml")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_inpaint_fp16.yaml -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_inpaint_fp16.yaml")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_lineart_fp16.yaml -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_lineart_fp16.yaml")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_mlsd_fp16.yaml -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_mlsd_fp16.yaml")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_normalbae_fp16.yaml -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_normalbae_fp16.yaml")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_openpose_fp16.yaml -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_openpose_fp16.yaml")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_scribble_fp16.yaml -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_scribble_fp16.yaml")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_seg_fp16.yaml -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_seg_fp16.yaml")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_softedge_fp16.yaml -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15_softedge_fp16.yaml")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15s2_lineart_anime_fp16.yaml -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11p_sd15s2_lineart_anime_fp16.yaml")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11f1e_sd15_tile_fp16.yaml -d /home/xlab-app-center/extensions/sd-webui-controlnet/models -o control_v11f1e_sd15_tile_fp16.yaml")

#
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//realisticasianthaila_v20.ckpt -d /home/xlab-app-center/models/Stable-diffusion -o realisticasianthaila_v20.ckpt")

#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth -d /home/xlab-app-center/models/GFPGAN -o GFPGANv1.4.pth")

os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/roop/weight//inswapper_128.onnx -d /home/xlab-app-center/models/faceswaplab -o inswapper_128.onnx")

os.system(f"python launch.py --cors-allow-origins=* --xformers --enable-insecure-extension-access --allow-code --theme dark --gradio-queue")
