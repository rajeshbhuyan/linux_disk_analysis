#!/usr/bin/python3 # Give your python path here

import threading
import os
import random
import time
import shutil
from tabulate import tabulate
import subprocess as sp

def disk_analyze(disk, mem_usage):
    user_list =[]
    usage_list=[]
    idx = 0
    cmd = "ls -l "+disk+" | awk '{print $3}'"
    users = sp.getoutput(cmd).split('\n')
    del user[0]
    cmd = "ls -l "+disk+" | awk '{print $9}'"
    directories = sp.getoutput(cmd).split('\n')
    del directories[0]
    

print("Disk analysis Completed!")
