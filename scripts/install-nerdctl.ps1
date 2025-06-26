# install-nerdctl.ps1

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$NERDCTL_URL = "https://github.com/containerd/nerdctl/releases/download/v1.0.0/nerdctl-full-1.0.0-windows-amd64.zip "
$INSTALL_DIR = "$env:SystemRoot\System32\winc"

Write-Host "[+] Installing nerdctl..." -ForegroundColor Green

if (-not (Test-Path $INSTALL_DIR)) {
    New-Item -ItemType Directory -Path $INSTALL_DIR | Out-Null
}

$zipFile = "$INSTALL_DIR\nerdctl.zip"

# Download
Write-Host "[-] Downloading nerdctl..."
Invoke-WebRequest -Uri $NERDCTL_URL -OutFile $zipFile

# Extract
Write-Host "[-] Extracting nerdctl..."
Expand-Archive -Path $zipFile -DestinationPath $INSTALL_DIR -Force

# Cleanup
Remove-Item $zipFile

Write-Host "[+] nerdctl installed to $INSTALL_DIR" -ForegroundColor Green