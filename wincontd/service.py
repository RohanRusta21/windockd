# wincontd/service.py

import os
import subprocess

def start_containerd():
    BIN_DIR = os.path.join(os.getenv("SystemRoot"), "System32", "wincontd")
    containerd_path = os.path.join(BIN_DIR, "containerd.exe")

    print("[+] Starting containerd service...")
    try:
        subprocess.run(f'{containerd_path} --register-service', shell=True, check=True)
        subprocess.run("net start containerd", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Failed to start containerd: {e}")

def stop_containerd():
    print("[+] Stopping containerd service...")
    subprocess.run("net stop containerd", shell=True)

def check_status():
    print("[+] Checking containerd status...")
    subprocess.run("sc query containerd", shell=True)