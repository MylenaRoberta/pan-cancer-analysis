import os

from urllib.parse import urljoin

# ======================================================================
# CONSTANTS
# ======================================================================

# TCGA-BRCA paper table file name
BRCA_PAPER_FILE = 'brca-paper-supplementary-tables-1-to-4.xls'

# Genomic Data Commons (GDC) API endpoint of interest
GDC_API_BASE_URL = 'https://api.gdc.cancer.gov'
GDC_API_ENDPOINTS = {
    'annotations': urljoin(GDC_API_BASE_URL, 'annotations'),
    'data': urljoin(GDC_API_BASE_URL, 'data'),
    'cases': urljoin(GDC_API_BASE_URL, 'cases'),
    'files': urljoin(GDC_API_BASE_URL, 'files'),
    'manifest': urljoin(GDC_API_BASE_URL, 'manifest'),
    'projects': urljoin(GDC_API_BASE_URL, 'projects'),
    'status': urljoin(GDC_API_BASE_URL, 'status'),
}

# TCGA-BRCA metadata preprocessing parameters
BRCA_PREPROCESSING_PARAMETERS = {
    'data_types': [
        'Isoform Expression Quantification',
        'Gene Expression Quantification'
    ],
    'disease_types': ['Ductal and Lobular Neoplasms'],
    'molecular_subtypes': [
        'Basal-like', 'HER2-enriched', 'Luminal A', 'Luminal B'
    ],
    'project_ids': ['TCGA-BRCA'],
    'sample_types': ['Primary Tumor', 'Solid Tissue Normal'],
}

# miRWalk website related constants
MIRWALK_BASE_URL = 'http://mirwalk.umm.uni-heidelberg.de'
MIRWALK_DEFAULT_FILE = 'miRWalk_miRNA_Targets.csv'
MIRWALK_SPECIES_SELECTION = 'human'

# ======================================================================
# DIRECTORY PATHS
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
MIRWALK_EXTERNAL_DATA_DIR = os.path.join(EXTERNAL_DATA_DIR, 'mirwalk')

# Interim data directory paths
GDC_INTERIM_DATA_DIR = os.path.join(INTERIM_DATA_DIR, 'gdc-api')
BRCA_INTERIM_DATA_DIR = os.path.join(INTERIM_DATA_DIR, 'tcga-brca')

# Processed data directory paths
BRCA_PROCESSED_FILES_DIRS = {
    'basal': os.path.join(PROCESSED_DATA_DIR, 'basal-like-files'),
    'her2': os.path.join(PROCESSED_DATA_DIR, 'her2-enriched-files'),
    'lum_a': os.path.join(PROCESSED_DATA_DIR, 'luminal-a-files'),
    'lum_b': os.path.join(PROCESSED_DATA_DIR, 'luminal-b-files'),
    'normal': os.path.join(PROCESSED_DATA_DIR, 'normal-tissue-files'),
}

# ======================================================================
# FILE PATHS
# ======================================================================

# TCGA-BRCA paper table file path
BRCA_PAPER_FILE_PATH = os.path.join(
    BRCA_EXTERNAL_DATA_DIR, BRCA_PAPER_FILE
)

# miRWalk default file path
MIRWALK_DEFAULT_FILE_PATH = os.path.join(
    MIRWALK_EXTERNAL_DATA_DIR, MIRWALK_DEFAULT_FILE
)

# GDC API interim file paths
GDC_INTERIM_FILE_PATHS = {
    'all-projects': os.path.join(
        GDC_INTERIM_DATA_DIR, 'gdc-all-projects.csv'
    ),
    'cases': os.path.join(
        GDC_INTERIM_DATA_DIR, 'gdc-cases-of-interest.csv'
    ),
    'files': os.path.join(
        GDC_INTERIM_DATA_DIR, 'gdc-files-of-interest.csv'
    ),
    'projects': os.path.join(
        GDC_INTERIM_DATA_DIR, 'gdc-projects-of-interest.csv'
    ),
}

# TCGA data interim file paths
TCGA_INTERIM_FILE_PATHS = {
    'cases': os.path.join(
        GDC_INTERIM_DATA_DIR, 'tcga-cases-of-interest.csv'
    ),
    'files': os.path.join(
        GDC_INTERIM_DATA_DIR, 'tcga-files-of-interest.csv'
    ),
    'projects': os.path.join(
        GDC_INTERIM_DATA_DIR, 'tcga-projects.csv'
    ),
}

# TCGA-BRCA interim file paths
BRCA_INTERIM_FILE_PATHS = {
    'cases': os.path.join(
        BRCA_INTERIM_DATA_DIR, 'brca-cases-metadata.csv'
    ),
    'files': os.path.join(
        BRCA_INTERIM_DATA_DIR, 'brca-files-metadata.csv'
    ),
    'paper': os.path.join(
        BRCA_INTERIM_DATA_DIR, 'brca-paper-cases-metadata.csv'
    ),
    'project': os.path.join(
        BRCA_INTERIM_DATA_DIR, 'brca-project-metadata.csv'
    ),
}
