import os
from urllib.parse import urljoin

# ======================================================================
# CONSTANTS
# ======================================================================

# TCGA-BRCA file name
BRCA_PAPER_FILE = 'brca-paper-supplementary-tables-1-to-4.xls'

# Genomic Data Commons (GDC) API endpoints
GDC_API_BASE_URL = 'https://api.gdc.cancer.gov'
GDC_API_ENDPOINTS = {
    'data': urljoin(GDC_API_BASE_URL, 'data'),
    'cases': urljoin(GDC_API_BASE_URL, 'cases'),
    'files': urljoin(GDC_API_BASE_URL, 'files'),
    'projects': urljoin(GDC_API_BASE_URL, 'projects'),
    'status': urljoin(GDC_API_BASE_URL, 'status'),
}

# Constants used in filters for GDC API requests
GDC_API_REQUESTS_CONSTANTS = {
    'projects': ['TCGA-BRCA'],
    'disease_types': ['Ductal and Lobular Neoplasms'],
    'sample_types': ['Primary Tumor', 'Solid Tissue Normal'],
}

# ======================================================================
# PATHS
# ======================================================================

# Root directory path
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# Data directory paths
DATA_DIR = os.path.join(ROOT_DIR, 'data')
EXTERNAL_DATA_DIR = os.path.join(DATA_DIR, 'external')
INTERIM_DATA_DIR = os.path.join(DATA_DIR, 'interim')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# External data directory paths
GDC_EXTERNAL_DATA_DIR = os.path.join(EXTERNAL_DATA_DIR, 'gdc-api')
BRCA_EXTERNAL_DATA_DIR = os.path.join(EXTERNAL_DATA_DIR, 'tcga-brca')
BRCA_RAW_FILES_DIRS = {
    'basal': os.path.join(BRCA_EXTERNAL_DATA_DIR, 'basal-like-files'),
    'her2': os.path.join(BRCA_EXTERNAL_DATA_DIR, 'her2-enriched-files'),
    'lum_a': os.path.join(BRCA_EXTERNAL_DATA_DIR, 'luminal-a-files'),
    'lum_b': os.path.join(BRCA_EXTERNAL_DATA_DIR, 'luminal-b-files'),
    'normal': os.path.join(BRCA_EXTERNAL_DATA_DIR, 'normal-tissue-files'),
}

# Interim data directory paths
GDC_INTERIM_DATA_DIR = os.path.join(INTERIM_DATA_DIR, 'gdc-api')
BRCA_INTERIM_DATA_DIR = os.path.join(INTERIM_DATA_DIR, 'tcga-brca')

# External file path
BRCA_PAPER_FILE_PATH = os.path.join(BRCA_EXTERNAL_DATA_DIR, BRCA_PAPER_FILE)