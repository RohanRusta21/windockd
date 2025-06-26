@echo off
:: set-docker-env.bat

echo Setting DOCKER_HOST environment variable...
set DOCKER_HOST=npipe:////./pipe/containerd-containerd

echo Docker environment activated.
echo You can now use 'docker' commands.