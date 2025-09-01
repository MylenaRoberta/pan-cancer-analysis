# Installation Instructions

This document describes how to set up the environment for this project on **Ubuntu Linux**.

## 1. System Requirements

- Ubuntu 20.04 or later  
- Python 3.9+  
- R 4.1+  

Make sure you have the following system packages installed:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-dev r-base r-base-dev \
    build-essential libssl-dev libcurl4-openssl-dev libxml2-dev
```

## 2. Clone the Repository

```bash
git clone https://github.com/MylenaRoberta/pan-cancer-analysis.git
cd pan-cancer-analysis
```

## 3. Python Environment Setup

It is recommended to use a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Then install Python dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 4. R Dependencies

This project requires the **edgeR** package from **Bioconductor**.

Start R and install the required dependencies:

```bash
R

# Install BiocManager if not already installed
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

# Install edgeR from Bioconductor
BiocManager::install("edgeR")

# Install common helper packages
install.packages(c("ggplot2", "statmod"))

q()
```
