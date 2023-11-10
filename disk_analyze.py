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
    #Collect list of users having directories in this disk
    users = sp.getoutput(cmd).split('\n')
    del user[0]
    cmd = "ls -l "+disk+" | awk '{print $9}'"
    #Collect the list of directories present in the disk
    directories = sp.getoutput(cmd).split('\n')
    del directories[0]
    print(disk, ": Number of Users: ", len(set(users)), " Number of directories: ", len(directories))
    for i,j in zip(users, directories):
        if i not in user_list:
            user_list.append(i)
            cmd1="du -sh "+disk+"/"+j
            try:
                mem = sp.getoutput(cmd1).split("\t")
                usage_list.append(int(mem[0]))
            except:
                usage_list.append(0)
                print("No read permission to the disrectory ", j, " By user: ",i)
        else:
            idx = user_list.index(i)
            cmd2 = "du -sh "+disk+"/"+j
            try:
                mem2 = sp.getoutput(cmd2).split("\t")
                usage_list += int(mem2[0])
            except:
                print("Read permission is notavailable for ",j, "User: ", i)
    print("Disk: ", disk, "Users List: ", user_list)
    usage_in_gb = [round(i/1048576) for i in usage_list]
    print("Disk Usage: ", usage_in_gb)

print("Disk analysis Completed!")
