# Notebooks

This directory contains the Jupyter notebooks implementing the **Transparent Reproducible Pipeline (TRP)** for modeling microRNA (miR) regulatory networks in cancer.

The pipeline comprises procedures for data acquisition, preprocessing, interaction inference, and network construction. For the current publication, it is extended to support the **layered quadripartite network (LQN)** architecture, incorporating pathway locations derived from biological pathway representations.

## Notebook Descriptions

### Data Acquisition and Preprocessing

| Notebook | Description |
|---|---|
| `01_metadata-selective-access.ipynb` | Selectively retrieves metadata from The Cancer Genome Atlas (TCGA) through the Genomic Data Commons (GDC) API. |
| `02_metadata-filtering.ipynb` | Filters the retrieved metadata to identify the samples and files relevant to the analysis. |
| `03_expression-retrieval-and-aggregation.ipynb` | Retrieves and aggregates miRNA and mRNA expression data for the selected samples. |
| `04_molecule-filtering-by-expression.ipynb` | Filters lowly expressed molecules from the expression datasets. |

### Interaction Inference and Network Construction

| Notebook | Description |
|---|---|
| `05_interaction-inference.ipynb` | Infers miR–mRNA regulatory associations from expression data using statistical correlation analysis. |
| `06_network-construction.ipynb` | Constructs network representations from inferred regulatory associations. |

### Pathway-Contextualized Network Analysis

The current LQN release extends the workflow to include pathway structure processing, the identification of pathway locations, and the construction and analysis of layered quadripartite networks.

| Notebook | Description |
|---|---|
| `06a_pathway-enrichment.ipynb` | Performs pathway enrichment analysis and constructs layered miR–mRNA–pathway tripartite networks. |
| `06b_pathway-network-projection-and-flattening.ipynb` | Projects and flattens pathway networks to support pathway-contextualized network construction. |
| `06c_layered-quadripartite-network-construction.ipynb` | Constructs LQNs by integrating regulatory associations with pathway structural information. |

## Execution Instructions

Before running the notebooks, follow the environment setup instructions in the [root README](../README.md) and install the dependencies listed in [`requirements.txt`](../requirements.txt).

The pipeline uses shared configuration settings defined in [`config.py`](../config.py).

The notebooks should be executed according to their data dependencies, as outputs from earlier processing stages may serve as inputs to subsequent analyses.

For information about the required datasets, intermediate files, and generated artifacts, refer to the [Data Artifact Documentation](../data/README.md).
