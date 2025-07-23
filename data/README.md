# Transparent Reproducible Pipeline (TRP)

## Ontologies

* [Gene Regulation Ontology](https://bioportal.bioontology.org/ontologies/GRO)
* [Systems Biology Ontology](https://bioportal.bioontology.org/ontologies/SBO)
* [Statistics Ontology](https://bioportal.bioontology.org/ontologies/STATO)
* [EDAM - Ontology of bioscientific data analysis and data management](https://edamontology.org)

## Schema Documentation Fields

* `field name`: Name of the field in the artifact’s table.
* `unique id`: ID attributed to the field, which is unique among all artifacts/tables.
* `descendant of`: When the field descends from another artifact, it refers to the unique ID of the original field.
* `data type`: Data type of the field content.
* `role`: Role of the field in the artifact. It can contain biological data, statistical metrics, or transformation operations. The field prefix (namespace) indicates its role:
  * `biological`
    * [Gene Regulation Ontology](https://bioportal.bioontology.org/ontologies/GRO): `gro:`
    * [Systems Biology Ontology](https://bioportal.bioontology.org/ontologies/SBO): `sbo:`
  * `statistical`
    * [Statistics Ontology](https://bioportal.bioontology.org/ontologies/STATO): `sto:`
  * `transformation`
    * [EDAM](https://edamontology.org): `edam:`
* `uri`: URI of the concept related to this field in an ontology defined by role.

## Family of Artifacts AT_OR

* Name: TCGA Origin Artifacts

### Artifact AT_OR/PM

* Name: TCGA Origin Project Metadata
* File: [project-metadata.csv](raw/tcga-brca/project-metadata.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| project_id | Unique identifier for the TCGA project | trp:ORPM01 | - | string | edam:data_identifier | http://edamontology.org/data_0842 |
| project_name | Human-readable name of the TCGA project describing the cancer type | trp:ORPM02 | - | string | edam:data_label | http://edamontology.org/data_0842 |
| primary_site | JSON array containing the primary anatomical site(s) where the cancer originated | trp:ORPM03 | - | string | gro:GRO_0000061 | http://purl.obolibrary.org/obo/GRO_0000061 |
| disease_type | JSON array containing the histological classification types of the diseases/cancers in the project | trp:ORPM04 | - | string | gro:Disease | http://www.bootstrep.eu/ontology/GRO#Disease |
| experimental_strategies | JSON array containing details about experimental strategies used, including file counts and case counts for each strategy | trp:ORPM05 | - | string | edam:data_protocol | http://edamontology.org/data_2531 |
| data_categories | JSON array containing information about data categories available, including file counts and case counts for each category | trp:ORPM06 | - | string | edam:data_classification | http://edamontology.org/operation_2990 |
| case_count | Total number of cases/patients included in the project | trp:ORPM07 | - | integer | sto:sample_size | http://purl.obolibrary.org/obo/OBI_0000938 |
| file_count | Total number of data files available in the project | trp:ORPM08 | - | integer | edam:data_quantity | http://edamontology.org/data_0006 |

### Artifact AT_OR/CM

* Name: TCGA Origin Cases Metadata
* File: [cases-metadata.csv](raw/tcga-brca/cases-metadata.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| case_id | Unique identifier for each case/patient in the TCGA database | trp:ORCM01 | - | string | edam:data_identifier | http://edamontology.org/data_0842 |
| submitter_id | Identifier assigned by the data submitter/contributor | trp:ORCM02 | - | string | edam:data_identifier | http://edamontology.org/data_0842 |
| disease_type | Type of cancer/disease for the case | trp:ORCM03 | - | string | edam:data_classification| http://edamontology.org/data_2914 |

### Artifact AT_OR/FM

* Name: TCGA Origin Files Metadata
* File: [files-metadata.csv](raw/tcga-brca/files-metadata.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| file_id | Unique identifier for each file in the TCGA database | trp:ORFM01 | - | string | edam:data_identifier | http://edamontology.org/data_0842 |
| case_id | Unique identifier for each case/patient in the TCGA database | trp:ORFM02 | - | string | edam:data_identifier | http://edamontology.org/data_0842 |
| access | Access level for the file (controlled, open, etc.) | trp:ORFM03 | - | string | wac:accessTo | http://www.w3.org/ns/auth/acl#accessTo |
| experimental_strategy | Experimental approach used to generate the data (WXS, RNA-Seq, etc.) | trp:ORFM04 | - | string | sbo:ExperimentalMethod | http://www.bootstrep.eu/ontology/GRO#ExperimentalMethod |
| data_type | Type of data contained in the file (Annotated Somatic Mutation, Aligned Reads, etc.) | trp:ORFM05 | - | string | gro:GRO_0000008 | http://purl.obolibrary.org/obo/GRO_0000008 |
| data_format | File format of the data (VCF, BAM, etc.) | trp:ORFM06 | - | string | edam:format_1915 | http://edamontology.org/format_1915 |
| samples | JSON array containing sample information including sample type and tissue type | trp:ORFM07 | - | string | gro:GRO_0000061 | http://purl.obolibrary.org/obo/GRO_0000061 |


## Family of Artifacts AT_FOR

* Family Name: TCGA Filtered Origin Artifacts

### Artifact AT_FOR/CM

* Name: TCGA Filtered Origin Cases Metadata
* File: [cases-metadata.csv](processed/tcga-brca/cases-metadata.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| case_id | Unique identifier for each case/patient in the TCGA database | trp:FORCM01 | trp:ORCM01 | string | edam:data_identifier | http://edamontology.org/data_0842 |
| submitter_id | Identifier assigned by the data submitter/contributor | trp:FORCM02 | trp:ORCM02 | string | edam:data_identifier | http://edamontology.org/data_0842 |
| disease_type | Type of cancer/disease for the case | trp:FORCM03 | trp:ORCM03 | string | edam:data_classification| http://edamontology.org/data_2914 |
| pam50_mrna | PAM50 molecular subtype classification based on mRNA expression | trp:FORCM04 | trp:ORCM04 | string | sbo:molecular_type | http://purl.obolibrary.org/obo/SBO_0000250 |
| has_tumor_files_of_interest | Indicates if the case has tumor files relevant to the analysis | trp:FORCM05 | - | boolean | edam:data_filtering | http://edamontology.org/operation_3695 |
| has_normal_files_of_interest | Indicates if the case has normal tissue files relevant to the analysis | trp:FORCM06 | - | boolean | edam:data_filtering | http://edamontology.org/operation_3695 |
| is_case_of_interest | Indicates if the case meets criteria for inclusion in the study | trp:FORCM07 | - | boolean | edam:data_filtering | http://edamontology.org/operation_3695 |

### Artifact AT_FOR/FM

* Name: TCGA Filtered Origin Files Metadata
* File: [files-metadata.csv](processed/tcga-brca/files-metadata.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| file_id | Unique identifier for each file in the TCGA database | trp:FORFM01 | trp:ORFM01 | string | edam:data_identifier | http://edamontology.org/data_0842 |
| case_id | Unique identifier for each case/patient in the TCGA database | trp:FORFM02 | trp:ORFM02 | string | edam:data_identifier | http://edamontology.org/data_0842 |
| access | Access level for the file (controlled, open, etc.) | trp:FORFM03 | trp:ORFM03 | string | wac:accessTo | http://www.w3.org/ns/auth/acl#accessTo |
| experimental_strategy | Experimental approach used to generate the data (WXS, RNA-Seq, etc.) | trp:FORFM04 | trp:ORFM04 | string | sbo:ExperimentalMethod | http://www.bootstrep.eu/ontology/GRO#ExperimentalMethod |
| data_type | Type of data contained in the file (Annotated Somatic Mutation, Aligned Reads, etc.) | trp:FORFM05 | trp:ORFM05 | string | gro:GRO_0000008 | http://purl.obolibrary.org/obo/GRO_0000008 |
| data_format | File format of the data (VCF, BAM, etc.) | trp:FORFM06 | trp:ORFM06 | string | edam:format_1915 | http://edamontology.org/format_1915 |
| samples | JSON array containing sample information including sample type and tissue type | trp:FORFM07 | trp:ORFM07 | string | gro:GRO_0000061 | http://purl.obolibrary.org/obo/GRO_0000061 |
| is_tumor_file_of_interest | Boolean flag indicating if the file is a tumor file of interest | trp:FORFM08 | - | integer | edam:data_filtering | http://edamontology.org/operation_3695 |
| is_normal_file_of_interest | Boolean flag indicating if the file is a normal file of interest | trp:FORFM09 | - | integer | edam:data_filtering | http://edamontology.org/operation_3695 |
| is_file_of_interest | Boolean flag indicating if the file is of general interest | trp:FORFM10 | - | integer | edam:data_filtering | http://edamontology.org/operation_3695 |

### Artifact AT_FOR/PC

* Name: TCGA Origin Paper Cases Data
* File: [tcga-brca-paper-supplementary-tables-1-to-4.xls](raw/tcga-brca/tcga-brca-paper-supplementary-tables-1-to-4.xls)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_FOR/FPC

* Name: TCGA Filtered Origin Paper Cases Metadata
* File: [paper-cases-data.csv](processed/tcga-brca/paper-cases-data.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |


## Family of Artifacts AT_EF

* Family Name: TCGA File Data Artifacts

### Artifact AT_FD/MOF

* Name: TCGA MicroRNA-Seq Origin File
(exemplo em: data/raw/gdc-api/63d7ceb1-b280-43a0-8f19-02fb6dfba18c.mirnaseq.isoforms.quantification.txt)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_FD/ROF

* Name: TCGA RNA-Seq Origin File
(exemplo em: data/raw/gdc-api/a6f6d0c2-4309-48c3-829a-7fd30fde6d71.rna_seq.augmented_star_gene_counts.tsv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_FD/MPF

* Name: TCGA MicroRNA-Seq Processed File
(arquivo original + quebra de colunas + coluna "is_mirna_of_interest"; 
exemplos em notebooks/01_tcga-brca/04_brca-file-processing.ipynb)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_FD/RPF

* Name: TCGA RNA-Seq Processed File
(arquivo original + coluna "is_mrna_of_interest";
exemplos em notebooks/01_tcga-brca/04_brca-file-processing.ipynb)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_FD/AMN

* Name: TCGA Aggregated MicroRNA Normalized Reads (data/interim/tcga-brca/.../aggregated-mir-normalized-reads.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_FD/AMR

* Name: TCGA Aggregated MicroRNA Raw Reads (data/interim/tcga-brca/.../aggregated-mir-raw-reads.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_FD/ARN

* Name: TCGA Aggregated Messenger RNA Normalized Reads (data/interim/tcga-brca/.../aggregated-rna-normalized-reads.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_FD/ARR

* Name: TCGA Aggregated Messenger RNA Raw Reads (data/interim/tcga-brca/.../aggregated-rna-raw-reads.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |


## Family of Artifacts AT_MF

* Family Name: TCGA Molecule Filtering Artifacts

### Artifact AT_MF/ER

* Name: edgeR's filterByExpr Expressed Messenger RNAs (data/processed/tcga-brca/expressed-rnas.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_MF/EM

* Name: edgeR's filterByExpr Expressed MicroRNAs (data/processed/tcga-brca/expressed-mirs.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_MF/AMN

* Name: TCGA Aggregated MicroRNA Normalized Reads (data/processed/tcga-brca/.../aggregated-mir-normalized-reads.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_MF/AMR

* Name: TCGA Aggregated MicroRNA Raw Reads (data/processed/tcga-brca/.../aggregated-mir-raw-reads.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_MF/ARN

* Name: TCGA Aggregated Messenger RNA Normalized Reads (data/processed/tcga-brca/.../aggregated-rna-normalized-reads.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_MF/ARR

* Name: TCGA Aggregated Messenger RNA Raw Reads (data/processed/tcga-brca/.../aggregated-rna-raw-reads.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |


## Family of Artifacts AT_II

* Family Name: TCGA Interaction Inference Artifacts

### Artifact AT_II/MO

* Name: miRWalk Origin Target File 
(arquivos estão sendo salvos em data/external/mirwalk)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_II/MP

* Name: miRWalk Processed Origin Target File 
(arquivo original + coluna "is_interaction_of_interest";
arquivos estão sendo salvos em data/processed/mirwalk)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_II/MNP

* Name: miRWalk MIMAT ID to Name Mapping (data/processed/mirwalk/mapping-mir-accession-id-to-name.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_II/IS

* Name: TCGA Inferred Interactions Set (data/interim/tcga-brca/.../inferred-interactions.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |


## Family of Artifacts AT_MN

* Family Name: TCGA MicroRNA Network Artifacts

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_MN/FI

* Name: TCGA Filtered Inferred Interactions Set (data/processed/tcga-brca/.../inferred-interactions.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_MN/INN

* Name: TCGA MicroRNA Interaction Network Nodes (data/processed/cytoscape/.../interaction-network-nodes.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_MN/INE

* Name: TCGA MicroRNA Interaction Network Edges (data/processed/cytoscape/.../interaction-network-edges.csv)

| field name   | unique id  | descendant_of | data type | role                | URI |
| ------------ | ---------- | --------------| --------- | ------------------- | --- |
| is_expressed | trp:AGMR02 |               | boolean   | edam:data_filtering | http://edamontology.org/operation_3695 |
| qvalue       | trp:INE05  |               | real      | sto:q-value         | http://purl.obolibrary.org/obo/OBI_0001442    |

### Artifact AT_MN/ANN

* Name: TCGA MicroRNA Association Network Nodes (data/processed/cytoscape/.../association-network-nodes.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_MN/ANE

* Name: TCGA MicroRNA Association Network Edges (data/processed/cytoscape/.../association-network-edges.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
