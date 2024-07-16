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

def is_prime(num):
    """
    检查一个数是否为质数
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def start_jupyter_lab(port=8889):
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
#         num_threads = threading.active_count()
#         print("当前运行的线程数：%d" % num_threads)
        #检查当前线程数小于 20 且为质数或者等于 2 的条件下，会执行等待时间以保持系统活力。
#        if num_threads < 20 and (is_prime(num_threads) or num_threads == 2):
#            scheduler = sched.scheduler(time.time, time.sleep)
#            print(f"Start 6 hours : {time.ctime()}")
#            scheduler.enter(6 * 60 * 60, 1, print, argument=(f"End 6 hours : {time.ctime()}",))# 维持系统活力,等待6小时
#            scheduler.enter(12 * 60 * 60, 1, print, argument=(f"End 12 hours : {time.ctime()}",))# 维持系统活力,等待12小时
#            scheduler.enter(24 * 60 * 60, 1, print, argument=(f"End 24 hours : {time.ctime()}",))# 维持系统活力,等待24小时
#            scheduler.run()

#多进程启动
import multiprocessing
if __name__ == '__main__':
    ls = multiprocessing.Process(target=start_jupyter_lab) # 创建子进程
    ls.start() # 子进程 开始执行
    ls.join() # 等待子进程结束

#多线程启动
#if __name__ == '__main__':
#    ls = threading.Thread(target=start_jupyter_lab) # 创建子线程
#    ls.start() # 子线程 开始执行
#    ls.join() # 等待子线程结束
