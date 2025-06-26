from setuptools import setup, find_packages

setup(
    name="wincontd",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "wincontd=winc.cli:cli"
        ]
    },
    install_requires=[
        "requests",
        "click",
    ],
    author="Rohan Rustagi",
    description="Lightweight Windows Container CLI compatible with Docker commands",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RohanRusta21/wincontd",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
)
