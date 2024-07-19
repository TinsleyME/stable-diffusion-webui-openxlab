import os
import shutil
os.chdir(f"/home/xlab-app-center")
os.system(f"git clone -b release_candidate https://github.com/AUTOMATIC1111/stable-diffusion-webui /home/xlab-app-center/stable-diffusion-webui")
os.chdir(f"/home/xlab-app-center/stable-diffusion-webui")
os.system(f"git lfs install")
os.system(f"git reset --hard")

#extensions
os.system(f"git clone https://github.com/mcmonkeyprojects/sd-dynamic-thresholding /home/xlab-app-center/stable-diffusion-webui/extensions/sd-dynamic-thresholding")
os.system(f"git clone https://github.com/zanllp/sd-webui-infinite-image-browsing /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-infinite-image-browsing")
os.system(f"git clone https://github.com/Mikubill/sd-webui-controlnet /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet")
os.system(f"git clone https://github.com/P2Enjoy/sd-webui-roop-uncensored /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-roop-uncensored")
os.system(f"git clone https://github.com/djbielejeski/a-person-mask-generator.git /home/xlab-app-center/stable-diffusion-webui/extensions/a-person-mask-generator")
os.system(f"git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete /home/xlab-app-center/stable-diffusion-webui/extensions/a1111-sd-webui-tagcomplete")
os.system(f"git clone https://github.com/Bing-su/adetailer.git /home/xlab-app-center/stable-diffusion-webui/extensions/adetailer")
os.system(f"git clone https://github.com/Scholar01/sd-webui-mov2mov.git /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-mov2mov")
os.system(f"git clone https://github.com/glucauze/sd-webui-faceswaplab /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-faceswaplab")
os.system(f"git clone https://github.com/Iyashinouta/sd-model-downloader /home/xlab-app-center/stable-diffusion-webui/extensions/sd-model-downloader")
os.system(f"git clone https://github.com/Uminosachi/sd-webui-inpaint-anything /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-inpaint-anything")
os.system(f"git clone https://gitcode.net/overbill1683/stable-diffusion-webui-localization-zh_Hans /home/xlab-app-center/stable-diffusion-webui/extensions/stable-diffusion-webui-localization-zh_Hans")
os.system(f"git clone https://github.com/SenshiSentou/sd-webui-qic-console /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-qic-console")

#model cn
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//control_instant_id_sdxl.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_instant_id_sdxl.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//control_v11e_sd15_ip2p_fp16.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11e_sd15_ip2p_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//control_v11e_sd15_shuffle_fp16.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11e_sd15_shuffle_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//control_v11f1e_sd15_tile_fp16.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11f1e_sd15_tile_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//control_v11f1p_sd15_depth_fp16.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11f1p_sd15_depth_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//control_v11p_sd15_canny_fp16.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_canny_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//control_v11p_sd15_inpaint_fp16.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_inpaint_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//control_v11p_sd15_lineart_fp16.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_lineart_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//control_v11p_sd15_mlsd_fp16.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_mlsd_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//control_v11p_sd15_normalbae_fp16.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_normalbae_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//control_v11p_sd15_openpose_fp16.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_openpose_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//control_v11p_sd15_scribble_fp16.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_scribble_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//control_v11p_sd15_seg_fp16.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_seg_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//control_v11p_sd15_softedge_fp16.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_softedge_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//control_v11p_sd15s2_lineart_anime_fp16.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15s2_lineart_anime_fp16.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//control_v1p_sd15_qrcode.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v1p_sd15_qrcode.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//ioclab_sd15_recolor.safetensors -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ioclab_sd15_recolor.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//ip-adapter-faceid-plus_sd15.bin -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-faceid-plus_sd15.bin")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//ip-adapter-faceid-plusv2_sd15.bin -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-faceid-plusv2_sd15.bin")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//ip-adapter-faceid_sd15.bin -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-faceid_sd15.bin")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//ip-adapter_instant_id_sdxl.bin -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter_instant_id_sdxl.bin")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//ip-adapter_sd15_vit-G.bin -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter_sd15_vit-G.bin")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//photomaker-v1.bin -d /home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o photomaker-v1.bin")
#lora cn
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//ip-adapter-faceid-plusv2_sd15_lora.safetensors -d /home/xlab-app-center/stable-diffusion-webui/models/Lora -o ip-adapter-faceid-plusv2_sd15_lora.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//ip-adapter-faceid_sd15_lora.safetensors -d /home/xlab-app-center/stable-diffusion-webui/models/Lora -o ip-adapter-faceid_sd15_lora.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/ControlNet/weight//ip-adapter-faceid-plus_sd15_lora.safetensors -d /home/xlab-app-center/stable-diffusion-webui/models/Lora -o ip-adapter-faceid-plus_sd15_lora.safetensors")

#Stable-diffusion
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/danbrown/RevAnimated-v1-2-2/resolve/main/rev-animated-v1-2-2.safetensors -d /home/xlab-app-center/stable-diffusion-webui/models/Stable-diffusion -o rev-animated-v1-2-2.safetensors")
#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Lykon/DreamShaper/resolve/main/DreamShaper_8_pruned.safetensors -d /home/xlab-app-center/stable-diffusion-webui/models/Stable-diffusion -o DreamShaper_8_pruned.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//realisticasianthaila_v20.ckpt -d /home/xlab-app-center/stable-diffusion-webui/models/Stable-diffusion -o realisticasianthaila_v20.ckpt")

#os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/GFPGAN/weight//GFPGANv1.4.pth -d /home/xlab-app-center/stable-diffusion-webui/models/GFPGAN -o GFPGANv1.4.pth")

shutil.copy('/home/xlab-app-center/file_other/styles.py','/home/xlab-app-center/stable-diffusion-webui/modules/styles.py',follow_symlinks=True)
shutil.copy('/home/xlab-app-center/file_password/.env','/home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-infinite-image-browsing/.env',follow_symlinks=True)
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/roop/weight//inswapper_128.onnx -d /home/xlab-app-center/stable-diffusion-webui/models/faceswaplab -o inswapper_128.onnx")

os.system(f"python launch.py --cors-allow-origins=* --xformers --enable-insecure-extension-access --allow-code --theme dark --gradio-queue")
