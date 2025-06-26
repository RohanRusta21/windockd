import os
import subprocess
import requests
import zipfile
from pathlib import Path

WINDIR = os.getenv("SystemRoot")
INSTALL_DIR = Path(WINDIR) / "System32" / "winc"
CONTAINERD_URL = "https://github.com/containerd/containerd/releases/download/v1.7.0/containerd-1.7.0-windows-amd64.zip "
NERDCTL_URL = "https://github.com/containerd/nerdctl/releases/download/v1.0.0/nerdctl-full-1.0.0-windows-amd64.zip "

def download_file(url, filename):
    with requests.get(url, stream=True) as r:
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def install_dependencies():
    print("[+] Installing containerd...")
    download_file(CONTAINERD_URL, "containerd.zip")
    extract_zip("containerd.zip", INSTALL_DIR)
    os.remove("containerd.zip")

    print("[+] Installing nerdctl...")
    download_file(NERDCTL_URL, "nerdctl.zip")
    extract_zip("nerdctl.zip", INSTALL_DIR)
    os.remove("nerdctl.zip")

    print("[+] Creating docker shim...")
    docker_shim = INSTALL_DIR / "docker.bat"
    with open(docker_shim, "w") as f:
        f.write('@echo off\nnerdctl %*')

    print(f"[+] Add {INSTALL_DIR} to PATH")