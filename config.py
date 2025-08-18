"""
Configuration module for the TCGA-BRCA analysis pipeline.

This module defines parameters, constants, directory paths, and file names
used across the pipeline. It centralizes setup to ensure its consistency,
reproducibility, and maintainability.

Parameters
----------
METADATA_SELECTIVE_ACCESS_SETUP : dict
    Configuration for metadata selective access (project IDs).
METADATA_FILTERING_SETUP : dict
    Configuration for metadata filtering (data types, disease types,
    molecular subtypes, sample types).
EXPRESSION_RETRIEVAL_AND_AGGREGATION_SETUP : dict
    Configuration for expression retrieval and aggregation (RNA-seq columns).
MOLECULE_FILTERING_BY_EXPRESSION_SETUP : dict
    Configuration for filtering molecules by expression thresholds.
INTERACTION_INFERENCE_SETUP : dict
    Configuration for interaction inference (binding site, FDR, inference
    method, species, etc.).
NETWORK_CONSTRUCTION_SETUP : dict
    Configuration for network construction (correlation, q-values,
    associations).

Constants
---------
GDC_API_BASE_URL : str
    Base URL of the Genomic Data Commons API.
GDC_API_ENDPOINTS : dict
    API endpoints for data, cases, files, projects, and status.
TCGA_BRCA_PAPER_FILE : str
    Filename of TCGA-BRCA supplementary data.
MIRWALK_BASE_URL : str
    Base URL of miRWalk database.

Paths
-----
ROOT_DIR : str
    Root directory of the repository.
DATA_DIR : str
    Path to the main data directory.
DATA_DIRS : dict
    Paths for external, interim, processed, and raw data.
DATA_SUBDIRS : list of str
    Names of TCGA-BRCA subtype subdirectories.
TCGA_DATA_DIRS : dict
    Nested dictionary of TCGA-BRCA data directories.
MIRWALK_DATA_DIRS : dict
    Paths for miRWalk data.
NETWORK_DATA_DIRS : dict
    Paths for network data.

Functions
---------
ensure_directories(*dir_dicts)
    Ensure that all directories in one or more nested directory
    dictionaries exist.

Files
-----
TCGA_FILES : dict
    Filenames for TCGA-related data (cases, files, projects, paper).
EXPRESSION_FILES : dict
    Filenames for aggregated and expressed miRNA/mRNA data.
MIRWALK_FILES : dict
    Filenames for miRWalk data (downloaded targets, mapping).
NETWORK_FILES : dict
    Filenames for inferred interactions and constructed networks.

Examples
--------
>>> from config import DATA_DIRS, TCGA_FILES
>>> DATA_DIRS['raw']
'/path/to/repo/data/raw'
>>> TCGA_FILES['cases']
'cases-metadata.csv'
"""

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
    'binding-position': '3UTR',
    'fdr-method': 'bh',
    'inference-alternative': 'less',
    'inference-axis': 0,
    'min-binding-probability': 0.9,
    'species-selection': 'human',
    'targetscan-prediction': 1,
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
    Ensure that all directories in one or more nested directory dictionaries exist.

    This function takes one or more dictionaries mapping keys to directory paths.
    Values can themselves be nested dictionaries. It recursively traverses the
    dictionaries, creating any directories that do not already exist.

    Parameters
    ----------
    *dir_dicts : dict
        One or more dictionaries where values are either:
        - strings: paths to directories to create, or
        - dicts: nested dictionaries containing further paths.

    Returns
    -------
    None
        This function is called for its side effects of ensuring directories exist.

    Notes
    -----
    - Uses :func:`os.makedirs` with ``exist_ok=True`` to avoid errors if a directory
      already exists.
    - Handles arbitrarily nested dictionaries of directory paths.
    - Typically used with global configuration variables such as
      ``TCGA_DATA_DIRS`` or ``TCGA_FILES``.

    Examples
    --------
    >>> dirs = {
    ...     "raw": "/data/raw",
    ...     "processed": {
    ...         "group1": "/data/processed/group1",
    ...         "group2": "/data/processed/group2"
    ...     }
    ... }
    >>> ensure_directories(dirs)
    # Creates /data/raw, /data/processed/group1, and /data/processed/group2
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
    'download': 'miRWalk_miRNA_Targets.csv',
    'mapping': 'mapping-mirna-accession-id-to-name.csv',
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
