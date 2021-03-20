import os
import time

while True:
    try:
        os.system('python core.py')
        time.sleep(1000)
    except:
        time.sleep(5)