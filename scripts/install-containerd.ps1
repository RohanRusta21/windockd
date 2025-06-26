# install-containerd.ps1

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$CONTAINERD_URL = "https://github.com/containerd/containerd/releases/download/v1.7.0/containerd-1.7.0-windows-amd64.zip "
$INSTALL_DIR = "$env:SystemRoot\System32\winc"

Write-Host "[+] Installing containerd..." -ForegroundColor Green

if (-not (Test-Path $INSTALL_DIR)) {
    New-Item -ItemType Directory -Path $INSTALL_DIR | Out-Null
}

$zipFile = "$INSTALL_DIR\containerd.zip"

# Download
Write-Host "[-] Downloading containerd..."
Invoke-WebRequest -Uri $CONTAINERD_URL -OutFile $zipFile

# Extract
Write-Host "[-] Extracting containerd..."
Expand-Archive -Path $zipFile -DestinationPath $INSTALL_DIR -Force

# Cleanup
Remove-Item $zipFile

Write-Host "[+] containerd installed to $INSTALL_DIR" -ForegroundColor Green