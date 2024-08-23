import subprocess
import psutil

process = subprocess.Popen("notepad")
proc_info = psutil.Process(process.pid)

try:
    process.wait(timeout=10)
    # print(proc_info.cpu_times().system, proc_info.cpu_times().user)
except:
    process.terminate()
    print("o programa acabou")
    print(proc_info.cpu_times().system, proc_info.cpu_times().user)