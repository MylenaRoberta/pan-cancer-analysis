# Towards an automated pipeline to model a complex-network-driven analysis of microRNAs in cancer: a TCGA-BRCA case study

## Abstract

We present the Transparent Reproducible Pipeline (TRP), a core component of our framework for systematizing the comparative analysis of cancer microRNA networks. The TRP is an open, stepwise pipeline for modeling these networks. It provides transparency in materializing intermediary artifacts as tables with schemas, affording explicit semantics and annotation-based provenance. It also offers reproducibility through its open-source code and comprehensive documentation, all accessible without restrictions. To apply and validate the TRP, we conducted a controlled study on breast cancer based on the Breast Invasive Carcinoma (BRCA) project of The Cancer Genome Atlas (TCGA), achieving promising results.

## Repository Structure

```code
├── data  
│ |── examples         <- Example data to demonstrate uncommitted files 
│ ├── external         <- Data downloaded from external sources  
│ ├── interim          <- Intermediate data generated during preprocessing  
│ ├── processed        <- Final datasets used for analysis and modeling  
│ ├── raw              <- Original raw datasets  
| └── README.md        <- TRP artifact documentation  
|  
├── figures            <- Paper figures  
│  
├── notebooks          <- Jupyter Notebooks for each stage of the pipeline  
│ ├── 01_metadata-selective-access.ipynb  
│ ├── 02_metadata-filtering.ipynb  
│ ├── 03_expression-retrieval-and-aggregation.ipynb  
│ ├── 04_molecule-filtering-by-expression.ipynb  
│ |── 05_interaction-inference.ipynb  
| |── 06_network-construction.ipynb  
| └── README.md        <- Notebooks brief description 
│
|── .gitignore         <- Git ignore rules for temporary files and data  
├── config.py          <- Project configuration and parameters  
├── requirements.txt   <- Python dependencies  
└── README.md          <- Repository introduction
```

## Installation Instructions

This document describes how to set up the environment for this project on **Linux (Ubuntu/Debian)**.

### 1. System Requirements

- Python 3.9+  
- R 4.1+  

Make sure you have the necessary system dependencies installed:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-dev r-base r-base-dev \
    build-essential libssl-dev libcurl4-openssl-dev libxml2-dev
```

### 2. Clone the Repository

```bash
git clone https://github.com/LIS-Unicamp/pan-cancer-analysis.git
cd pan-cancer-analysis
```

### 3. Python Environment Setup

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

### 4. R Dependencies

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
