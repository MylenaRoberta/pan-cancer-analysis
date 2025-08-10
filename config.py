import os
from urllib.parse import urljoin

# ======================================================================
# PIPELINE PARAMETER SETUP
# ======================================================================

# Parameter setup of the [1] metadata selective access stage
METADATA_SELECTIVE_ACCESS_SETUP = {
    'project-ids': ['TCGA-BRCA'],
}

# Parameter setup of the [2] metadata filtering stage
METADATA_FILTERING_SETUP = {
    'data-types': ['Isoform Expression Quantification', 'Gene Expression Quantification'],
    'disease-types': ['Ductal and Lobular Neoplasms'],
    'molecular-subtypes': ['Basal-like', 'HER2-enriched', 'Luminal A', 'Luminal B'],
    'sample-types': ['Primary Tumor', 'Solid Tissue Normal'],
}

# Parameter setup of the [3] expression retrieval and aggregation stage
EXPRESSION_RETRIEVAL_AND_AGGREGATION_SETUP = {
    'rna-seq-raw-reads-column': 'unstranded',
    'rna-seq-norm-reads-column': 'tpm_unstranded', 
}

# Parameter setup of the [4] molecule filtering by expression stage
MOLECULE_FILTERING_BY_EXPRESSION_SETUP = {
    'large-n': 10,
    'min-count': 10,
    'min-prop': 0.7,
    'min-total-count': 15,
}

# Parameter setup of the [5] interaction inference stage
INTERACTION_INFERENCE_SETUP = {
    'species-selection': 'human',
    'fdr-method': 'bh', # Benjamini-Hochberg
    'inference-alternative': 'less',
    'inference-axis': 0,
}

# Parameter setup of the [6] network construction stage
NETWORK_CONSTRUCTION_SETUP = {
    'max-correlation': -0.3,
    'max-qvalue': 0.05,
    'min-association': 0.1,
}

# ======================================================================
# CONSTANTS
# ======================================================================

# Genomic Data Commons (GDC) API endpoints of interest
GDC_API_BASE_URL = 'https://api.gdc.cancer.gov'
GDC_API_ENDPOINTS = {
    'data': urljoin(GDC_API_BASE_URL, 'data'),
    'cases': urljoin(GDC_API_BASE_URL, 'cases'),
    'files': urljoin(GDC_API_BASE_URL, 'files'),
    'projects': urljoin(GDC_API_BASE_URL, 'projects'),
    'status': urljoin(GDC_API_BASE_URL, 'status'),
}

# TCGA-BRCA paper table file name
TCGA_BRCA_PAPER_FILE = 'tcga-brca-paper-supplementary-tables-1-to-4.xls'

# miRWalk base URL
MIRWALK_BASE_URL = 'http://mirwalk.umm.uni-heidelberg.de'

# ======================================================================
# DIRECTORY PATHS
# ======================================================================

# Root directory path
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# Data directory paths
DATA_DIR = os.path.join(ROOT_DIR, 'data')
DATA_DIRS = {
    'external': os.path.join(DATA_DIR, 'external'),
    'interim': os.path.join(DATA_DIR, 'interim'),
    'processed': os.path.join(DATA_DIR, 'processed'),
    'raw': os.path.join(DATA_DIR, 'raw'),
}

# Data subdirectories names
DATA_SUBDIRS = ['basal-like', 'her2-enriched', 'luminal-a', 'luminal-b', 'paired-normal']

# TCGA-related data directories paths
TCGA_DATA_DIRS = {
    dir: {
        'root': os.path.join(DATA_DIRS[dir], 'tcga-brca'),
        **{
            subdir: os.path.join(DATA_DIRS[dir], 'tcga-brca', subdir)
            for subdir in DATA_SUBDIRS
        }
    }
    for dir in ['interim', 'processed', 'raw']
}

# miRWalk-related data directories paths
MIRWALK_DATA_DIRS = {
    dir: os.path.join(DATA_DIRS[dir], 'mirwalk')
    for dir in ['external', 'processed']
}

# Network-related data directories paths
NETWORK_DATA_DIRS = {
    dir: {
        subdir: os.path.join(DATA_DIRS[dir], 'networks', subdir)
        for subdir in DATA_SUBDIRS
    }
    for dir in ['interim', 'processed']
}

# ======================================================================
# ENSURE THE EXISTENCE OF DATA DIRECTORIES
# ======================================================================

def ensure_directories(*dir_dicts):
    """
    Recursively ensure that all directories in the given dictionaries exist.

    This function accepts one or more dictionaries whose values are:
    - strings representing directory paths; or
    - nested dictionaries containing more directory paths.

    For each path, it creates the directory (and any missing parent 
    directories) if it does not already exist.

    Parameters
    ----------
    *dir_dicts : dict
        One or more dictionaries containing directory paths or nested 
        dictionaries of directory paths.

    Examples
    --------
    >>> ensure_directories(DATA_DIRS, TCGA_DATA_DIRS)
    """
    for dir_dict in dir_dicts:
        for path in dir_dict.values():
            if isinstance(path, dict):
                # If the value is another dictionary, go deeper
                ensure_directories(path)
            else:
                # Create the directory if it does not exist
                os.makedirs(path, exist_ok=True)

# Create all data directories if necessary
ensure_directories(
    DATA_DIRS,
    TCGA_DATA_DIRS,
    MIRWALK_DATA_DIRS,
    NETWORK_DATA_DIRS,
)

# ======================================================================
# FILE NAMES
# ======================================================================

# TCGA-related file names
TCGA_FILES = {
    'cases': 'cases-metadata.csv',
    'files': 'files-metadata.csv',
    'paper': 'paper-cases-data.csv',
    'project': 'project-metadata.csv',
}

# Expression-related file names
EXPRESSION_FILES = {
    'agg-mirs-norm-reads': 'aggregated-mirna-normalized-reads.csv',
    'agg-mirs-raw-reads': 'aggregated-mirna-raw-reads.csv',
    'agg-mrnas-norm-reads': 'aggregated-mrna-normalized-reads.csv',
    'agg-mrnas-raw-reads': 'aggregated-mrna-raw-reads.csv',
    'expressed-mirs': 'expressed-mirnas.csv',
    'expressed-mrnas': 'expressed-mrnas.csv',
}

# miRWalk-related file names
MIRWALK_FILES = {
    'default-file': 'miRWalk_miRNA_Targets.csv',
    'mirs-mapping': 'mapping-mirna-accession-id-to-name.csv',
}

# Network-related file names
NETWORK_FILES = {
    'association-edges': 'association-network-edges.csv',
    'association-nodes': 'association-network-nodes.csv',
    'inferred-associations': 'inferred-associations.csv',
    'inferred-interactions': 'inferred-interactions.csv',
    'interaction-edges': 'interaction-network-edges.csv',
    'interaction-nodes': 'interaction-network-nodes.csv',
}
