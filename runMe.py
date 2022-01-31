from time import sleep
# from shared_memory_dict import SharedMemoryDict
import os

os.system(f"start cmd /k py mainScript.py ")
# scriptManager = SharedMemoryDict(name="scriptManager", size=1024)

import psutil
import os

def is_running(script):
    for q in psutil.process_iter():
        if q.name().startswith('python'):
            if len(q.cmdline())>1 and script in q.cmdline()[1] and q.pid !=os.getpid():
                print("'{}' Process is already running".format(script))
                return True

    return False

files = ["fasterScript.py","gasPriceCatcher.py","anotherOne.py"]

while True:
    
    for file in files:
        if not is_running(file):
            print(file," not Running")
            os.system(f"start cmd /k py {file} ")
   
    sleep(30)