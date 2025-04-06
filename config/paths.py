import os

from config.constants import BRCA_PAPER_FILE

# ================================================================
# ROOT PATH
# ================================================================

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# ================================================================
# BASE DATA DIRECTORIES
# ================================================================

DATA_DIR = os.path.join(ROOT_DIR, 'data')
EXTERNAL_DATA_DIR = os.path.join(DATA_DIR, 'external')
INTERIM_DATA_DIR = os.path.join(DATA_DIR, 'interim')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# ================================================================
# EXTERNAL SOURCES (RAW DATA)
# ================================================================

GDC_EXTERNAL_DATA_DIR = os.path.join(EXTERNAL_DATA_DIR, 'gdc-api')
BRCA_EXTERNAL_DATA_DIR = os.path.join(EXTERNAL_DATA_DIR, 'tcga-brca')
BRCA_PAPER_FILE_PATH = os.path.join(BRCA_EXTERNAL_DATA_DIR, BRCA_PAPER_FILE)

# ================================================================
# INTERIM / STAGING DATA
# ================================================================

GDC_INTERIM_DATA_DIR = os.path.join(INTERIM_DATA_DIR, 'gdc-api')
BRCA_INTERIM_DATA_DIR = os.path.join(INTERIM_DATA_DIR, 'tcga-brca')