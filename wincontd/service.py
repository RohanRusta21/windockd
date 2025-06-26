import os
import subprocess

def start_containerd():
    print("[+] Starting containerd...")
    cmd = f'{os.getenv("SystemRoot")}\\System32\\winc\\containerd.exe --register-service'
    subprocess.run(cmd, shell=True)
    subprocess.run("net start containerd", shell=True)

def stop_containerd():
    print("[+] Stopping containerd...")
    subprocess.run("net stop containerd", shell=True)

def check_status():
    print("[+] Checking containerd status...")
    subprocess.run("sc query containerd", shell=True)