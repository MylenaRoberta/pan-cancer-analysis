import os
from urllib.parse import urljoin

# ======================================================================
# PIPELINE PARAMETER SETUP
# ======================================================================

# Parameter setup of the [1] metadata selective access stage
METADATA_SELECTIVE_ACCESS_SETUP = {
    'project_ids': ['TCGA-BRCA'],
}

# Parameter setup of the [2] metadata filtering stage
METADATA_FILTERING_SETUP = {
    'data_types': ['Isoform Expression Quantification', 'Gene Expression Quantification'],
    'disease_types': ['Ductal and Lobular Neoplasms'],
    'molecular_subtypes': ['Basal-like', 'HER2-enriched', 'Luminal A', 'Luminal B'],
    'sample_types': ['Primary Tumor', 'Solid Tissue Normal'],
}

# Parameter setup of the [3] expression retrieval and aggregation stage
EXPRESSION_RETRIEVAL_AND_AGGREGATION_SETUP = {
    
}

# Parameter setup of the [4] molecule filtering by expression stage
MOLECULE_FILTERING_BY_EXPRESSION_SETUP = {
    
}

# Parameter setup of the [5] interaction inference stage
INTERACTION_INFERENCE_SETUP = {
    
}

# Parameter setup of the [6] network construction stage
NETWORK_CONSTRUCTION_SETUP = {
    
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
BRCA_PAPER_FILE = 'tcga-brca-paper-supplementary-tables-1-to-4.xls'


# Aggregated miRNA-Seq and RNA-Seq reads file names
AGGREGATED_READS_FILES = {
    'mir-normalized': 'aggregated-mir-normalized-reads.csv',
    'mir-raw': 'aggregated-mir-raw-reads.csv',
    'rna-normalized': 'aggregated-rna-normalized-reads.csv',
    'rna-raw': 'aggregated-rna-raw-reads.csv',
}

# EdgeR's filterByExpr() parameters [all default]
FILTER_BY_EXPR_PARAMETERS = {
    'min_count': 10,
    'min_total_count': 15,
    'large_n': 10,
    'min_prop': 0.7,
}

# Expressed molecules file names
EXPRESSED_MOLECULES_FILES = {
    'mir': 'expressed-mirs.csv',
    'rna': 'expressed-rnas.csv',
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
    'alternative': 'less',
    'axis': 0,
    'fdr-method': 'bh', # Benjamini-Hochberg
    'file-name': 'inferred-interactions.csv',
}

# Interaction (microRNA - messenger RNA) filtering parameters
INTERACTION_FILTERING_PARAMETERS = {
    'edges_file_name': 'interaction-network-edges.csv',
    'nodes_file_name': 'interaction-network-nodes.csv',
    'max_correlation': -0.3,
    'max_qvalue': 0.05,
}

# Association (microRNA - microRNA) filtering parameters
ASSOCIATION_FILTERING_PARAMETERS = {
    'inferred_associations': 'inferred-associations.csv',
    'edges_file_name': 'association-network-edges.csv',
    'nodes_file_name': 'association-network-nodes.csv',
    'min_index': 0.1,
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
}
MIRWALK_PROCESSED_DATA_DIR = os.path.join(PROCESSED_DATA_DIR, 'mirwalk')
CYTOSCAPE_PROCESSED_DATA_DIR = os.path.join(PROCESSED_DATA_DIR, 'cytoscape')
CYTOSCAPE_PROCESSED_FILES_DIRS = {
    'basal-like': os.path.join(CYTOSCAPE_PROCESSED_DATA_DIR, 'basal-like-files'),
    'her2-enriched': os.path.join(CYTOSCAPE_PROCESSED_DATA_DIR, 'her2-enriched-files'),
    'luminal-a': os.path.join(CYTOSCAPE_PROCESSED_DATA_DIR, 'luminal-a-files'),
    'luminal-b': os.path.join(CYTOSCAPE_PROCESSED_DATA_DIR, 'luminal-b-files'),
    'paired-normal': os.path.join(CYTOSCAPE_PROCESSED_DATA_DIR, 'paired-normal-files'),
}

# ======================================================================
# FILE PATHS
# ======================================================================

# TCGA-BRCA raw files paths
BRCA_RAW_FILES_PATHS = {
    'cases': os.path.join(BRCA_RAW_DATA_DIR, 'cases-metadata.csv'),
    'files': os.path.join(BRCA_RAW_DATA_DIR, 'files-metadata.csv'),
    'paper': os.path.join(BRCA_RAW_DATA_DIR, BRCA_PAPER_FILE),
    'project': os.path.join(BRCA_RAW_DATA_DIR, 'project-metadata.csv'),
}

# TCGA-BRCA processed files paths
BRCA_PROCESSED_FILES_PATHS = {
    'cases': os.path.join(BRCA_PROCESSED_DATA_DIR, 'cases-metadata.csv'),
    'files': os.path.join(BRCA_PROCESSED_DATA_DIR, 'files-metadata.csv'),
    'paper': os.path.join(BRCA_PROCESSED_DATA_DIR, 'paper-cases-data.csv'),
}

# miRWalk default file path
MIRWALK_DEFAULT_FILE_PATH = os.path.join(
    MIRWALK_EXTERNAL_DATA_DIR, MIRWALK_DOWNLOAD_PARAMETERS['default-file-name']
)

# miRWalk accession ID to microRNA name file path
MIRWALK_MIR_MAPPING_FILE_PATH = os.path.join(
    MIRWALK_PROCESSED_DATA_DIR, MIRWALK_DOWNLOAD_PARAMETERS['mir-mapping-file-name']
)
