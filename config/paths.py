import os

from constants import BRCA_PAPER_FILE

# Root directory path
ROOT_DIR = os.path.abspath(os.getcwd())

# Data directories paths
DATA_DIR = os.path.join(ROOT_DIR, 'data')
EXTERNAL_DATA_DIR = os.path.join(DATA_DIR, 'external')
INTERIM_DATA_DIR = os.path.join(DATA_DIR, 'interim')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# Data subdirectories paths
GDC_EXTERNAL_DATA_DIR = os.path.join(EXTERNAL_DATA_DIR, 'gdc-api')
BRCA_EXTERNAL_DATA_DIR = os.path.join(EXTERNAL_DATA_DIR, 'tcga-brca')
GDC_INTERIM_DATA_DIR = os.path.join(INTERIM_DATA_DIR, 'gdc-api')
BRCA_INTERIM_DATA_DIR = os.path.join(INTERIM_DATA_DIR, 'tcga-brca')

# TCGA-BRCA article file path
BRCA_PAPER_FILE_PATH = os.path.join(BRCA_EXTERNAL_DATA_DIR, BRCA_PAPER_FILE)

# Genomic Data Commons (GDC) API URLs
GDC_API_BASE_URL = os.path.join('https://api.gdc.cancer.gov')
DATA_ENDPOINT = os.path.join(GDC_API_BASE_URL, 'data')
CASES_ENDPOINT = os.path.join(GDC_API_BASE_URL, 'cases')
FILES_ENDPOINT = os.path.join(GDC_API_BASE_URL, 'files')
PROJECTS_ENDPOINT = os.path.join(GDC_API_BASE_URL, 'projects')
STATUS_ENDPOINT = os.path.join(GDC_API_BASE_URL, 'status')