import subprocess

import os 
import re 
def check_size():
    r = subprocess.check_output("ls",shell=True).decode().replace("\n","'")
    #r_3 = r.replace(" '","'")
    #t = subprocess.call("cd /media/horus/HORUS/Python/pyqt5/movie/ahmedd")
    r_1 = os.getcwd()
    y  = "du "+"-s {}/'"+str(r)
    while True:
        r_2 =subprocess.check_output(y.format(r_1),shell=True).decode()
        #result = "cd "+r_1+"/'{}'".format(r).replace(" '","'")
        #t_2 = os.chdir(result)
        rea = re.search(r"\d+",r_2)
        rea_1 = rea.group()
        return rea_1 
check_size()                        