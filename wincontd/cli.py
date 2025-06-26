# wincontd/cli.py

import click
from wincontd.installer import install_dependencies
from wincontd.service import start_containerd, stop_containerd, check_status
from wincontd.utils import activate_docker_env

@click.group()
def cli():
    """wincontd: Lightweight Windows Container Runtime CLI"""
    pass

@cli.command()
def install():
    """Install required dependencies (containerd, nerdctl)"""
    install_dependencies()

@cli.command()
def start():
    """Start containerd service"""
    start_containerd()

@cli.command()
def stop():
    """Stop containerd service"""
    stop_containerd()

@cli.command()
def status():
    """Check runtime status"""
    check_status()

@cli.command()
def activate():
    """Activate Docker-compatible environment"""
    activate_docker_env()

if __name__ == '__main__':
    cli()