import os
import psutil
import subprocess
import time

import sched
import threading
import openxlab

def is_port_in_use(port):
    """
    检查指定端口是否被占用
    """
    for conn in psutil.net_connections():
        if conn.laddr.port == port:
            return True
    return False

def start_jupyter_lab(port=8899):
    """
    启动 JupyterLab
    """
    if not is_port_in_use(port):
        #环境变量的内网穿透账号
        ak = os.getenv("OPENXLAB_AK")
        if not ak:
            print("Environment variable OPENXLAB_AK is not set.")
            return
        ngrok_command = ak
        jupyter_command = f"jupyter-lab --no-browser --ip=0.0.0.0 --allow-root --notebook-dir=/ --port={port} --LabApp.allow_origin=* --LabApp.token= --LabApp.base_url="
        # 启动 ngrok 进程
        ngrok_process = subprocess.Popen(ngrok_command, shell=True)
        # 启动 Jupyter 进程
        jupyter_process = subprocess.Popen(jupyter_command, shell=True)
    else:
        print(f"Port {port} is already in use, JupyterLab cannot be started.")

#多进程启动
import multiprocessing
if __name__ == '__main__':
    ls = multiprocessing.Process(target=start_jupyter_lab) # 创建子进程
    ls.start() # 子进程 开始执行
    ls.join() # 等待子进程结束
