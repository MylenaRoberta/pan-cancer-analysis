# Transparent Reproducible Pipeline (TRP)

## Ontologies

* [Web Access Control Ontology](https://www.w3.org/wiki/WebAccessControl)
* [Gene Regulation Ontology](https://bioportal.bioontology.org/ontologies/GRO)
* [National Cancer Institute Thesaurus](https://bioportal.bioontology.org/ontologies/NCIT)
* [Ontology for Biomedical Investigations](https://bioportal.bioontology.org/ontologies/OBI)
* [Systems Biology Ontology](https://bioportal.bioontology.org/ontologies/SBO)
* [Statistics Ontology](https://bioportal.bioontology.org/ontologies/STATO)
* [EDAM - Ontology of bioscientific data analysis and data management](https://edamontology.org)

## Schema Documentation Fields

* `field name`: Name of the field in the artifact’s table.
* `unique id`: ID attributed to the field, which is unique among all artifacts/tables.
* `descendant of`: When the field descends from another artifact, it refers to the unique ID of the original field.
* `data type`: Data type of the field content.
* `role`: Role of the field in the artifact. It can contain biological data, statistical metrics, or transformation operations. The field prefix (namespace) indicates its role:
  * `access`
    * [Web Access Control Ontology](https://www.w3.org/wiki/WebAccessControl): `wac:`
  * `biological`
    * [Gene Regulation Ontology](https://bioportal.bioontology.org/ontologies/GRO): `gro:`
    * [National Cancer Institute Thesaurus](https://bioportal.bioontology.org/ontologies/NCIT): `ncit:`
    * [Ontology for Biomedical Investigations](https://bioportal.bioontology.org/ontologies/OBI): `obi:`
    * [Systems Biology Ontology](https://bioportal.bioontology.org/ontologies/SBO): `sbo:`
  * `statistical`
    * [Statistics Ontology](https://bioportal.bioontology.org/ontologies/STATO): `stato:`
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
| project_id | Unique identifier for the TCGA project | trp:ORPM01 | - | string | edam:Identifier | http://edamontology.org/data_0842 |
| project_name | Full name of the TCGA project | trp:ORPM02 | - | string | edam:Identifier | http://edamontology.org/data_0842 |
| primary_site | JSON array containing the primary anatomical site(s) where the cancer originated | trp:ORPM03 | - | string | edam:Classification | http://edamontology.org/operation_2990 |
| disease_type | JSON array containing the histological classification types of the diseases/cancers in the project | trp:ORPM04 | - | string | gro:Disease | http://www.bootstrep.eu/ontology/GRO#Disease |
| experimental_strategies | JSON array containing information about experimental strategies used, including file counts and case counts for each strategy | trp:ORPM05 | - | string | edam:Classification | http://edamontology.org/operation_2990 |
| data_categories | JSON array containing information about data categories available, including file counts and case counts for each category | trp:ORPM06 | - | string | edam:Classification | http://edamontology.org/operation_2990 |
| case_count | Total number of cases/patients included in the project | trp:ORPM07 | - | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |
| file_count | Total number of data files available in the project | trp:ORPM08 | - | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |

### Artifact AT_OR/CM

* Name: TCGA Origin Cases Metadata
* File: [cases-metadata.csv](raw/tcga-brca/cases-metadata.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| case_id | Unique identifier for each case/patient in the TCGA database | trp:ORCM01 | - | string | edam:Identifier | http://edamontology.org/data_0842 |
| submitter_id | Identifier assigned to the case by the submitting institution | trp:ORCM02 | - | string | edam:Identifier | http://edamontology.org/data_0842 |
| disease_type | Histological classification of the cancer for the given case | trp:ORCM03 | - | string | gro:Disease | http://www.bootstrep.eu/ontology/GRO#Disease |

### Artifact AT_OR/FM

* Name: TCGA Origin Files Metadata
* File: [files-metadata.csv](raw/tcga-brca/files-metadata.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| file_id | Unique identifier of the data file in the TCGA database | trp:ORFM01 | - | string | edam:Identifier | http://edamontology.org/data_0842 |
| case_id | Identifier linking the file to a specific case | trp:ORFM02 | - | string | edam:Identifier | http://edamontology.org/data_0842 |
| access | Access level of the file (open or controlled) | trp:ORFM03 | - | string | wac:AccessControl | https://www.w3.org/ns/auth/acl#accessControl |
| experimental_strategy | Experimental approach used to generate the data (e.g., RNA-Seq, WGS) | trp:ORFM04 | - | string | edam:Classification | http://edamontology.org/operation_2990 |
| data_category | Broad category of data in the file (e.g., Transcriptome Profiling, DNA Methylation) | trp:ORFM05 | - | string | edam:Classification | http://edamontology.org/operation_2990 |
| data_type | Type of data represented in the file (e.g., Gene Expression Quantification, Annotated Somatic Mutation) | trp:ORFM06 | - | string | edam:Classification | http://edamontology.org/operation_2990 |
| data_format | Format of the file content (e.g., TXT, TSV, BEDPE) | trp:ORFM07 | - | string | edam:Format | http://edamontology.org/format_1915 |
| samples | JSON array containing sample metadata, including sample type and tissue type | trp:ORFM08 | - | string | obi:Specimen | http://purl.obolibrary.org/obo/OBI_0100051 |


## Family of Artifacts AT_FOR

* Family Name: TCGA Filtered Origin Artifacts

### Artifact AT_FOR/PC

* Name: TCGA Origin Paper Cases Data
* File (SuppTable1): [tcga-brca-paper-supplementary-tables-1-to-4.xls](raw/tcga-brca/tcga-brca-paper-supplementary-tables-1-to-4.xls)

| field name | description | unique id | descendant of | data type | role | URI |
|------------|-------------|-----------|----------------|-----------|------|-----|
| complete_tcga_id | TCGA barcode identifying the specific case/sample | trp:FORPC01 | - | string | edam:Identifier | http://edamontology.org/data_0842 |
| gender | Biological sex of the individual | trp:FORPC02 | - | string | ncit:Sex | http://purl.obolibrary.org/obo/NCIT_C28421 |
| age_at_initial_pathologic_diagnosis | Age of the patient at diagnosis time (in years) | trp:FORPC03 | - | integer | ncit:Age | http://purl.obolibrary.org/obo/NCIT_C25150 |
| er_status | Estrogen receptor status (Positive/Negative) | trp:FORPC04 | - | string | ncit:ReceptorStatus | http://purl.obolibrary.org/obo/NCIT_C94299 |
| pr_status | Progesterone receptor status (Positive/Negative) | trp:FORPC05 | - | string | ncit:ReceptorStatus | http://purl.obolibrary.org/obo/NCIT_C94299 |
| her2_final_status | HER2 receptor status (Positive/Negative) | trp:FORPC06 | - | string | ncit:ReceptorStatus | http://purl.obolibrary.org/obo/NCIT_C94299 |
| tumor | Clinical tumor (T) classification | trp:FORPC07 | - | string | ncit:T2bTNMFinding | http://purl.obolibrary.org/obo/NCIT_C48726 |
| tumor--t1_coded | Coded/normalized value of the tumor field | trp:FORPC08 | - | string | edam:Calculation | http://edamontology.org/operation_3438 |
| node | Clinical node (N) classification | trp:FORPC09 | - | string | ncit:T2cTNMFinding | http://purl.obolibrary.org/obo/NCIT_C48727 |
| node-coded | Coded/normalized value of the node field | trp:FORPC10 | - | string | edam:Calculation | http://edamontology.org/operation_3438 |
| metastasis | Clinical metastasis (M) classification | trp:FORPC11 | - | string | ncit:T3TNMFinding | http://purl.obolibrary.org/obo/NCIT_C48728 |
| metastasis-coded | Coded/normalized value of the metastasis field | trp:FORPC12 | - | string | edam:Calculation | http://edamontology.org/operation_3438 |
| ajcc_stage | AJCC staging based on TNM values | trp:FORPC13 | - | string | ncit:DiseaseStageQualifier | http://purl.obolibrary.org/obo/NCIT_C28108 |
| converted_stage | Adjusted version of the AJCC stage | trp:FORPC14 | - | string | edam:Calculation | http://edamontology.org/operation_3438 |
| survival_data_form | Source form of survival information (e.g., enrollment, followup) | trp:FORPC15 | - | string | edam:Identifier | http://edamontology.org/data_0842 |
| vital_status | Vital status of the patient (e.g., Alive, Deceased) | trp:FORPC16 | - | string | ncit:VitalStatus | http://purl.obolibrary.org/obo/NCIT_C25717 |
| days_to_date_of_last_contact | Time until last contact (in days) | trp:FORPC17 | - | integer | ncit:Day | http://purl.obolibrary.org/obo/NCIT_C25301 |
| days_to_date_of_death | Time until death (in days) | trp:FORPC18 | - | integer | ncit:Day | http://purl.obolibrary.org/obo/NCIT_C25301 |
| os_event | Overall survival event indicator (0: censored, 1: death) | trp:FORPC19 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| os_time | Overall survival time (in days) | trp:FORPC20 | - | integer | ncit:Day | http://purl.obolibrary.org/obo/NCIT_C25301 |
| pam50_mrna | PAM50 molecular subtype classification | trp:FORPC21 | - | string | edam:Classification | http://edamontology.org/operation_2990 |
| sigclust_unsupervised_mrna | Unsupervised clustering score (sigClust) based on mRNA data | trp:FORPC22 | - | real | stato:P-value | http://purl.obolibrary.org/obo/STATO_0000700 |
| sigclust_intrinsic_mrna | Intrinsic subtype clustering score (sigClust) based on mRNA | trp:FORPC23 | - | real | stato:P-value | http://purl.obolibrary.org/obo/STATO_0000700 |
| mirna_clusters | Cluster assignment based on miRNA expression | trp:FORPC24 | - | integer | edam:Clustering | http://edamontology.org/operation_3432 |
| methylation_clusters | Cluster assignment based on DNA methylation data | trp:FORPC25 | - | integer | edam:Clustering | http://edamontology.org/operation_3432 |
| rppa_clusters | Cluster assignment based on RPPA proteomics data | trp:FORPC26 | - | integer | edam:Clustering | http://edamontology.org/operation_3432 |
| cn_clusters | Cluster assignment based on copy number variation data | trp:FORPC27 | - | integer | edam:Clustering | http://edamontology.org/operation_3432 |
| integrated_clusters_(with_pam50) | Final integrated cluster including PAM50 subtype | trp:FORPC28 | - | integer | edam:Clustering | http://edamontology.org/operation_3432 |
| integrated_clusters_(no_exp) | Integrated cluster excluding expression-based features | trp:FORPC29 | - | integer | edam:Clustering | http://edamontology.org/operation_3432 |
| integrated_clusters_(unsup_exp) | Integrated cluster using unsupervised expression-based features only | trp:FORPC30 | - | integer | edam:Clustering | http://edamontology.org/operation_3432 |

### Artifact AT_FOR/FPC

* Name: TCGA Filtered Origin Paper Cases Metadata
* File: [paper-cases-data.csv](processed/tcga-brca/paper-cases-data.csv)

| field name | description | unique id | descendant of | data type | role | URI |
|------------|-------------|-----------|----------------|-----------|------|-----|
| complete_tcga_id | TCGA barcode identifying the specific case/sample | trp:FORFPC01 | trp:FORPC01 | string | edam:Identifier | http://edamontology.org/data_0842 |
| gender | Biological sex of the individual | trp:FORFPC02 | trp:FORPC02 | string | ncit:Sex | http://purl.obolibrary.org/obo/NCIT_C28421 |
| age_at_initial_pathologic_diagnosis | Age of the patient at diagnosis time (in years) | trp:FORFPC003 | trp:FORPC03 | integer | ncit:Age | http://purl.obolibrary.org/obo/NCIT_C25150 |
| er_status | Estrogen receptor status (Positive/Negative) | trp:FORFPC04 | trp:FORPC04 | string | ncit:ReceptorStatus | http://purl.obolibrary.org/obo/NCIT_C94299 |
| pr_status | Progesterone receptor status (Positive/Negative) | trp:FORFPC05 | trp:FORPC05 | string | ncit:ReceptorStatus | http://purl.obolibrary.org/obo/NCIT_C94299 |
| her2_final_status | HER2 receptor status (Positive/Negative) | trp:FORFPC06 | trp:FORPC06 | string | ncit:ReceptorStatus | http://purl.obolibrary.org/obo/NCIT_C94299 |
| tumor | Clinical tumor (T) classification | trp:FORFPC07 | trp:FORPC07 | string | ncit:T2bTNMFinding | http://purl.obolibrary.org/obo/NCIT_C48726 |
| tumor--t1_coded | Coded/normalized value of the tumor field | trp:FORFPC08 | trp:FORPC08 | string | edam:Calculation | http://edamontology.org/operation_3438 |
| node | Clinical node (N) classification | trp:FORFPC09 | trp:FORPC09 | string | ncit:T2cTNMFinding | http://purl.obolibrary.org/obo/NCIT_C48727 |
| node-coded | Coded/normalized value of the node field | trp:FORFPC10 | trp:FORPC10 | string | edam:Calculation | http://edamontology.org/operation_3438 |
| metastasis | Clinical metastasis (M) classification | trp:FORFPC11 | trp:FORPC11 | string | ncit:T3TNMFinding | http://purl.obolibrary.org/obo/NCIT_C48728 |
| metastasis-coded | Coded/normalized value of the metastasis field | trp:FORFPC12 | trp:FORPC12 | string | edam:Calculation | http://edamontology.org/operation_3438 |
| ajcc_stage | AJCC staging based on TNM values | trp:FORFPC13 | trp:FORPC13 | string | ncit:DiseaseStageQualifier | http://purl.obolibrary.org/obo/NCIT_C28108 |
| converted_stage | Adjusted version of the AJCC stage | trp:FORFPC14 | trp:FORPC14 | string | edam:Calculation | http://edamontology.org/operation_3438 |
| survival_data_form | Source form of survival information (e.g., enrollment, followup) | trp:FORFPC15 | trp:FORPC15 | string | edam:Identifier | http://edamontology.org/data_0842 |
| vital_status | Vital status of the patient (e.g., Alive, Deceased) | trp:FORFPC16 | trp:FORPC16 | string | ncit:VitalStatus | http://purl.obolibrary.org/obo/NCIT_C25717 |
| days_to_date_of_last_contact | Time until last contact (in days) | trp:FORFPC17 | trp:FORPC17 | integer | ncit:Day | http://purl.obolibrary.org/obo/NCIT_C25301 |
| days_to_date_of_death | Time until death (in days) | trp:FORFPC18 | trp:FORPC18 | integer | ncit:Day | http://purl.obolibrary.org/obo/NCIT_C25301 |
| os_event | Overall survival event indicator (0: censored, 1: death) | trp:FORFPC19 | trp:FORPC19 | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| os_time | Overall survival time (in days) | trp:FORFPC20 | trp:FORPC20 | integer | ncit:Day | http://purl.obolibrary.org/obo/NCIT_C25301 |
| pam50_mrna | PAM50 molecular subtype classification | trp:FORFPC21 | trp:FORPC21 | string | edam:Classification | http://edamontology.org/operation_2990 |
| sigclust_unsupervised_mrna | Unsupervised clustering score (sigClust) based on mRNA data | trp:FORFPC22 | trp:FORPC22 | real | stato:P-value | http://purl.obolibrary.org/obo/STATO_0000700 |
| sigclust_intrinsic_mrna | Intrinsic subtype clustering score (sigClust) based on mRNA | trp:FORFPC23 | trp:FORPC23 | real | stato:P-value | http://purl.obolibrary.org/obo/STATO_0000700 |
| mirna_clusters | Cluster assignment based on miRNA expression | trp:FORFPC24 | trp:FORPC24 | integer | edam:Clustering | http://edamontology.org/operation_3432 |
| methylation_clusters | Cluster assignment based on DNA methylation data | trp:FORFPC25 | trp:FORPC25 | integer | edam:Clustering | http://edamontology.org/operation_3432 |
| rppa_clusters | Cluster assignment based on RPPA proteomics data | trp:FORFPC26 | trp:FORPC26 | integer | edam:Clustering | http://edamontology.org/operation_3432 |
| cn_clusters | Cluster assignment based on copy number variation data | trp:FORFPC27 | trp:FORPC27 | integer | edam:Clustering | http://edamontology.org/operation_3432 |
| integrated_clusters_(with_pam50) | Final integrated cluster including PAM50 subtype | trp:FORFPC28 | trp:FORPC28 | integer | edam:Clustering | http://edamontology.org/operation_3432 |
| integrated_clusters_(no_exp) | Integrated cluster excluding expression-based features | trp:FORFPC29 | trp:FORPC29 | integer | edam:Clustering | http://edamontology.org/operation_3432 |
| integrated_clusters_(unsup_exp) | Integrated cluster using unsupervised expression-based features only | trp:FORFPC30 | trp:FORPC30 | integer | edam:Clustering | http://edamontology.org/operation_3432 |
| is_case_of_interest | Indicates if the case meets criteria for inclusion in the study | trp:FORFPC31 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |


### Artifact AT_FOR/CM

* Name: TCGA Filtered Origin Cases Metadata
* File: [cases-metadata.csv](processed/tcga-brca/cases-metadata.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| case_id | Unique identifier for each case/patient in the TCGA database | trp:FORCM01 | trp:ORCM01 | string | edam:Identifier | http://edamontology.org/data_0842 |
| submitter_id | Identifier assigned to the case by the submitting institution | trp:FORCM02 | trp:ORCM02 | string | edam:Identifier | http://edamontology.org/data_0842 |
| disease_type | Histological classification of the cancer for the given case | trp:FORCM03 | trp:ORCM03 | string | gro:Disease | http://www.bootstrep.eu/ontology/GRO#Disease |
| pam50_mrna | PAM50 molecular subtype classification based on mRNA expression | trp:FORCM04 | trp:FORFPC21 | string | edam:Classification | http://edamontology.org/operation_2990 |
| has_tumor_files_of_interest | Indicates if the case has tumor files relevant to the analysis | trp:FORCM05 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| has_normal_files_of_interest | Indicates if the case has normal tissue files relevant to the analysis | trp:FORCM06 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| is_case_of_interest | Indicates if the case meets criteria for inclusion in the study | trp:FORCM07 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |

### Artifact AT_FOR/FM

* Name: TCGA Filtered Origin Files Metadata
* File: [files-metadata.csv](processed/tcga-brca/files-metadata.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| file_id | Unique identifier of the data file in the TCGA database | trp:FORFM01 | trp:ORFM01 | string | edam:Identifier | http://edamontology.org/data_0842 |
| case_id | Identifier linking the file to a specific case | trp:FORFM02 | trp:ORFM02 | string | edam:Identifier | http://edamontology.org/data_0842 |
| access | Access level of the file (open or controlled) | trp:FORFM03 | trp:ORFM03 | string | wac:AccessControl | https://www.w3.org/ns/auth/acl#accessControl |
| experimental_strategy | Experimental approach used to generate the data (e.g., RNA-Seq, WGS) | trp:FORFM04 | trp:ORFM04 | string | edam:Classification | http://edamontology.org/operation_2990 |
| data_category | Broad category of data in the file (e.g., Transcriptome Profiling, DNA Methylation) | trp:FORFM05 | trp:ORFM05 | string | edam:Classification | http://edamontology.org/operation_2990 |
| data_type | Type of data represented in the file (e.g., Gene Expression Quantification, Annotated Somatic Mutation) | trp:FORFM06 | trp:ORFM06 | string | edam:Classification | http://edamontology.org/operation_2990 |
| data_format | Format of the file content (e.g., TXT, TSV, BEDPE) | trp:FORFM07 | trp:ORFM07 | string | edam:Format | http://edamontology.org/format_1915 |
| samples | JSON array containing sample metadata, including sample type and tissue type | trp:FORFM08 | trp:ORFM08 | string | obi:Specimen | http://purl.obolibrary.org/obo/OBI_0100051 |
| is_tumor_file_of_interest | Indicates if the file corresponds to a tumor sample relevant to the analysis | trp:FORFM09 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| is_normal_file_of_interest | Indicates if the file corresponds to a normal sample relevant to the analysis | trp:FORFM11 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| is_file_of_interest | Indicates if the file meets criteria for inclusion in the study | trp:FORFM11 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |


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
| qvalue       | trp:INE05  |               | real      | stato:q-value         | http://purl.obolibrary.org/obo/OBI_0001442    |

### Artifact AT_MN/ANN

* Name: TCGA MicroRNA Association Network Nodes (data/processed/cytoscape/.../association-network-nodes.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |

### Artifact AT_MN/ANE

* Name: TCGA MicroRNA Association Network Edges (data/processed/cytoscape/.../association-network-edges.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
