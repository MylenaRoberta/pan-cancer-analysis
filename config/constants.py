from urllib.parse import urljoin

# ================================================================
# FILE NAMES / EXTENSIONS
# ================================================================

BRCA_PAPER_FILE = 'brca-paper-supplementary-tables-1-to-4.xls'

# ================================================================
# GENOMIC DATA COMMONS (GDC) API ENDPOINTS
# ================================================================

GDC_API_BASE_URL = 'https://api.gdc.cancer.gov'
GDC_API_ENDPOINTS = {
    'data': urljoin(GDC_API_BASE_URL, 'data'),
    'cases': urljoin(GDC_API_BASE_URL, 'cases'),
    'files': urljoin(GDC_API_BASE_URL, 'files'),
    'projects': urljoin(GDC_API_BASE_URL, 'projects'),
    'status': urljoin(GDC_API_BASE_URL, 'status'),
}

# ================================================================
# CONSTANTS SPECIFIC TO GENOMIC DATA COMMONS (GDC) API REQUESTS
# ================================================================

GDC_API_REQUESTS_CONSTANTS = {
    'projects': ['TCGA-BRCA'],
    'disease_types': ['Ductal and Lobular Neoplasms'],
    'sample_types': ['Primary Tumor', 'Solid Tissue Normal'],
}