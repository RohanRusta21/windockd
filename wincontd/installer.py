# wincontd/installer.py

import os
from pathlib import Path
from zipfile import ZipFile
from importlib.resources import files
import wincontd.resources

def extract_zip(zip_path, extract_to):
    print(f"[+] Extracting {zip_path} to {extract_to}")
    try:
        with ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    except Exception as e:
        raise RuntimeError(f"Failed to extract {zip_path}: {e}")

def install_dependencies():
    BIN_DIR = Path(os.getenv("SystemRoot")) / "System32" / "wincontd"
    print(f"[+] Installing dependencies to {BIN_DIR}")

    if not BIN_DIR.exists():
        BIN_DIR.mkdir(parents=True)

    containerd_zip = str(files(wincontd.resources).joinpath("containerd.zip"))
    nerdctl_zip = str(files(wincontd.resources).joinpath("nerdctl.zip"))

    print("[+] Installing containerd...")
    extract_zip(containerd_zip, BIN_DIR)

    print("[+] Installing nerdctl...")
    extract_zip(nerdctl_zip, BIN_DIR)

    # Create docker.bat shim
    docker_shim = BIN_DIR / "docker.bat"
    with open(docker_shim, "w") as f:
        f.write('@echo off\nnerdctl %*')

    print(f"[+] Add {BIN_DIR} to PATH for Docker compatibility")