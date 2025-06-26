# wincontd/utils.py

import os

def activate_docker_env():
    print("[+] Activating Docker environment...")
    os.environ["DOCKER_HOST"] = "npipe:////./pipe/containerd-containerd"
    print("Now you can use 'docker' commands!")