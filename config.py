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
        'Basal-like', 'HER2-enriched', 'Luminal A', 'Luminal B',
    ],
    'project_ids': ['TCGA-BRCA'],
    'sample_types': ['Primary Tumor', 'Solid Tissue Normal'],
}

# Aggregated miRNA-Seq and RNA-Seq reads file names
AGGREGATED_READS_FILES = {
    'mir': 'aggregated-mir-reads.csv',
    'rna': 'aggregated-rna-reads.csv',
}

# Molecules (microRNAs and messenger RNAs) expression definition parameters
EXPRESSION_DEFINITION_PARAMETERS = {
    'read-threshold': 10,
    'read-percentage-threshold': 80,
}

# miRWalk website download parameters
MIRWALK_DOWNLOAD_PARAMETERS = {
    'base-url': 'http://mirwalk.umm.uni-heidelberg.de',
    'default-file-name': 'miRWalk_miRNA_Targets.csv',
    'mir-mapping-file-name': 'mapping-mir-accession-id-to-name.csv',
    'species-selection': 'human',
}

# Interaction (microRNA - messenger RNA) inference parameters
INTERACTION_INFERENCE_PARAMETERS = {
    'correlation': -0.3,
    'interim-file': 'spearman-correlation-analysis.csv',
    'processed-file': 'inferred-interactions.csv',
    'pvalue': 0.01,
}

# ======================================================================
# DIRECTORY PATHS
# ======================================================================

# Root directory path
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# Data directory paths
DATA_DIR = os.path.join(ROOT_DIR, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
EXTERNAL_DATA_DIR = os.path.join(DATA_DIR, 'external')
INTERIM_DATA_DIR = os.path.join(DATA_DIR, 'interim')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# Raw data directory paths
GDC_RAW_DATA_DIR = os.path.join(RAW_DATA_DIR, 'gdc-api')
BRCA_RAW_DATA_DIR = os.path.join(RAW_DATA_DIR, 'tcga-brca')
BRCA_RAW_FILES_DIRS = {
    'basal-like': os.path.join(BRCA_RAW_DATA_DIR, 'basal-like-files'),
    'her2-enriched': os.path.join(BRCA_RAW_DATA_DIR, 'her2-enriched-files'),
    'luminal-a': os.path.join(BRCA_RAW_DATA_DIR, 'luminal-a-files'),
    'luminal-b': os.path.join(BRCA_RAW_DATA_DIR, 'luminal-b-files'),
    'paired-normal': os.path.join(BRCA_RAW_DATA_DIR, 'paired-normal-files'),
}

# External data directory paths
MIRWALK_EXTERNAL_DATA_DIR = os.path.join(EXTERNAL_DATA_DIR, 'mirwalk')

# Interim data directory paths
GDC_INTERIM_DATA_DIR = os.path.join(INTERIM_DATA_DIR, 'gdc-api')
BRCA_INTERIM_DATA_DIR = os.path.join(INTERIM_DATA_DIR, 'tcga-brca')
BRCA_INTERIM_FILES_DIRS = {
    'basal-like': os.path.join(BRCA_INTERIM_DATA_DIR, 'basal-like-files'),
    'her2-enriched': os.path.join(BRCA_INTERIM_DATA_DIR, 'her2-enriched-files'),
    'luminal-a': os.path.join(BRCA_INTERIM_DATA_DIR, 'luminal-a-files'),
    'luminal-b': os.path.join(BRCA_INTERIM_DATA_DIR, 'luminal-b-files'),
    'paired-normal': os.path.join(BRCA_INTERIM_DATA_DIR, 'paired-normal-files'),
}

# Processed data directory paths
BRCA_PROCESSED_DATA_DIR = os.path.join(PROCESSED_DATA_DIR, 'tcga-brca')
BRCA_PROCESSED_FILES_DIRS = {
    'basal-like': os.path.join(BRCA_PROCESSED_DATA_DIR, 'basal-like-files'),
    'her2-enriched': os.path.join(BRCA_PROCESSED_DATA_DIR, 'her2-enriched-files'),
    'luminal-a': os.path.join(BRCA_PROCESSED_DATA_DIR, 'luminal-a-files'),
    'luminal-b': os.path.join(BRCA_PROCESSED_DATA_DIR, 'luminal-b-files'),
    'paired-normal': os.path.join(BRCA_PROCESSED_DATA_DIR, 'paired-normal-files'),
    'project': os.path.join(BRCA_PROCESSED_DATA_DIR, 'project-files'),
}
MIRWALK_PROCESSED_DATA_DIR = os.path.join(PROCESSED_DATA_DIR, 'mirwalk')

# ======================================================================
# FILE PATHS
# ======================================================================

# GDC API interim files paths
GDC_INTERIM_FILES_PATHS = {
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

# TCGA data interim files paths
TCGA_INTERIM_FILES_PATHS = {
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

# TCGA-BRCA paper table file path
BRCA_PAPER_FILE_PATH = os.path.join(BRCA_RAW_DATA_DIR, BRCA_PAPER_FILE)

# TCGA-BRCA processed files paths
BRCA_PROCESSED_FILES_PATHS = {
    'cases': os.path.join(
        BRCA_PROCESSED_FILES_DIRS['project'], 'cases-metadata.csv'
    ),
    'files': os.path.join(
        BRCA_PROCESSED_FILES_DIRS['project'], 'files-metadata.csv'
    ),
    'paper': os.path.join(
        BRCA_PROCESSED_FILES_DIRS['project'], 'paper-cases-data.csv'
    ),
    'project': os.path.join(
        BRCA_PROCESSED_FILES_DIRS['project'], 'project-metadata.csv'
    ),
}

# miRWalk default file path
MIRWALK_DEFAULT_FILE_PATH = os.path.join(
    MIRWALK_EXTERNAL_DATA_DIR, MIRWALK_DOWNLOAD_PARAMETERS['default-file-name']
)

# miRWalk accession ID to microRNA name file path
MIRWALK_MIR_MAPPING_FILE_PATH = os.path.join(
    MIRWALK_PROCESSED_DATA_DIR, MIRWALK_DOWNLOAD_PARAMETERS['mir-mapping-file-name']
)
