# Transparent Reproducible Pipeline (TRP)

## Ontologies

* [Web Access Control Ontology](https://www.w3.org/wiki/WebAccessControl)
* [Gene Regulation Ontology](https://bioportal.bioontology.org/ontologies/GRO)
* [National Cancer Institute Thesaurus](https://bioportal.bioontology.org/ontologies/NCIT)
* [Ontology for Biomedical Investigations](https://bioportal.bioontology.org/ontologies/OBI)
* [Sequence Types and Features Ontology](https://bioportal.bioontology.org/ontologies/SO)
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
    * [Sequence Types and Features Ontology](https://bioportal.bioontology.org/ontologies/SO): `so:`
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

* Family Name: TCGA Origin Filtered Artifacts

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

* Name: TCGA Origin Filtered Paper Cases Data
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
| is_case_of_interest | Indicates if the case meets criteria for inclusion in the study (1: yes, 0: no) | trp:FORFPC31 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |


### Artifact AT_FOR/CM

* Name: TCGA Origin Filtered Cases Metadata
* File: [cases-metadata.csv](processed/tcga-brca/cases-metadata.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| case_id | Unique identifier for each case/patient in the TCGA database | trp:FORCM01 | trp:ORCM01 | string | edam:Identifier | http://edamontology.org/data_0842 |
| submitter_id | Identifier assigned to the case by the submitting institution | trp:FORCM02 | trp:ORCM02 | string | edam:Identifier | http://edamontology.org/data_0842 |
| disease_type | Histological classification of the cancer for the given case | trp:FORCM03 | trp:ORCM03 | string | gro:Disease | http://www.bootstrep.eu/ontology/GRO#Disease |
| pam50_mrna | PAM50 molecular subtype classification based on mRNA expression | trp:FORCM04 | trp:FORFPC21 | string | edam:Classification | http://edamontology.org/operation_2990 |
| has_tumor_files_of_interest | Indicates if the case has tumor files relevant to the analysis (1: yes, 0: no) | trp:FORCM05 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| has_normal_files_of_interest | Indicates if the case has normal tissue files relevant to the analysis (1: yes, 0: no) | trp:FORCM06 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| is_case_of_interest | Indicates if the case meets criteria for inclusion in the study (1: yes, 0: no) | trp:FORCM07 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |

### Artifact AT_FOR/FM

* Name: TCGA Origin Filtered Files Metadata
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
| is_tumor_file_of_interest | Indicates if the file corresponds to a tumor sample relevant to the analysis (1: yes, 0: no) | trp:FORFM09 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| is_normal_file_of_interest | Indicates if the file corresponds to a normal sample relevant to the analysis (1: yes, 0: no) | trp:FORFM11 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| is_file_of_interest | Indicates if the file meets criteria for inclusion in the study (1: yes, 0: no) | trp:FORFM11 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |


## Family of Artifacts AT_EF

* Family Name: TCGA Origin Expression File Artifacts

### Artifact AT_EF/MOF

* Name: TCGA Origin MicroRNA-Seq File
* Example File: [mirna-seq-origin-file.txt](examples/mirna-seq-origin-file.txt)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| miRNA_ID | Identifier of the microRNA (miRNA) as annotated in miRBase | trp:EFMOF01 | - | string | so:MicroRNA | http://purl.obolibrary.org/obo/SO_0000276 |
| isoform_coords | Genomic coordinates and strand of the miRNA isoform based on the hg38 assembly | trp:EFMOF02 | - | string | so:SequenceFeature | http://purl.obolibrary.org/obo/SO_0000110 |
| read_count | Number of reads mapped to the isoform | trp:EFMOF03 | - | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |
| reads_per_million_miRNA_mapped | Normalized abundance of the isoform (reads per million mapped miRNA reads) | trp:EFMOF04 | - | real | obi:NormalizedDataSet | http://purl.obolibrary.org/obo/OBI_0000451 |
| cross-mapped | Indicates whether the reads are cross-mapped to other loci (Y/N) | trp:EFMOF05 | - | string | edam:DataFiltering | http://edamontology.org/operation_3695 |
| miRNA_region | Region classification of the isoform (e.g., mature, precursor) with optional miRBase accession | trp:EFMOF06 | - | string | so:MicroRNARegion | http://purl.obolibrary.org/obo/SO_0000836 |


### Artifact AT_EF/MPF

* Name: TCGA Origin MicroRNA-Seq Processed File
* Example File: [mirna-seq-processed-file.csv](examples/mirna-seq-processed-file.txt)


| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| mirna_id | Identifier of the microRNA (miRNA) as annotated in miRBase | trp:EFMPF01 | trp:EFMOF01 | string | so:MicroRNA | http://purl.obolibrary.org/obo/SO_0000276 |
| genome_assembly | Reference genome assembly version | trp:EFMPF02 | trp:EFMOF02 | string | edam:SequenceAssembly | http://edamontology.org/data_0925 |
| chromosome | Chromosome on which the miRNA isoform is located | trp:EFMPF03 | trp:EFMOF02 | string | so:Chromosome | http://purl.obolibrary.org/obo/SO_0000340 |
| position_range | Genomic coordinate range of the isoform, start-end | trp:EFMPF04 | trp:EFMOF02 | string | so:SequenceLocation | http://purl.obolibrary.org/obo/SO_0000735 |
| strand | DNA strand of the isoform, '+' for forward or '-' for reverse | trp:EFMPF05 | trp:EFMOF02 | string | so:StrandAttribute | http://purl.obolibrary.org/obo/SO_0000983 |
| cross_mapped | Indicates whether the reads are cross-mapped to other loci (Y/N) | trp:EFMPF06 | trp:EFMOF05 | string | edam:DataFiltering | http://edamontology.org/operation_3695 |
| region_type | Classification of the miRNA region (e.g., mature, precursor) | trp:EFMPF07 | trp:EFMOF06 | string | so:MicroRNARegion | http://purl.obolibrary.org/obo/SO_0000836 |
| accession_id | miRBase accession identifier corresponding to the miRNA isoform | trp:EFMPF08 | trp:EFMOF06 | string | edam:Identifier | http://edamontology.org/data_0842 |
| read_count | Number of reads mapped to the isoform | trp:EFMPF09 | trp:EFMOF03 | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |
| reads_per_million | Normalized abundance of the isoform (reads per million mapped miRNA reads) | trp:EFMPF10 | trp:EFMOF04 | real | obi:NormalizedDataSet | http://purl.obolibrary.org/obo/OBI_0000451 |
| is_mirna_of_interest | Indicates if the isoform meets criteria for inclusion in the study (1: yes, 0: no) | trp:EFMPF11 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |

### Artifact AT_EF/AMR

* Name: Aggregated MicroRNA Raw Reads
* Example File: [aggregated-mir-raw-reads.csv](interim/tcga-brca/basal-like-files/aggregated-mir-raw-reads.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| accession_id | Accession identifier for mature miRNA from miRBase | trp:EFAMR01 | trp:EFMPF08 | string | edam:Identifier | http://edamontology.org/data_0842 |
| \<UUID\> | Aggregated raw read count from the file identified by this UUID | trp:EFAMR02+ | trp:EFMPF09 | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |

### Artifact AT_EF/AMN

* Name: Aggregated MicroRNA Normalized Reads
* Example File: [aggregated-mir-normalized-reads.csv](interim/tcga-brca/basal-like-files/aggregated-mir-normalized-reads.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| accession_id | Accession identifier for mature miRNA from miRBase | trp:EFAMN01 | trp:EFMPF08 | string | edam:Identifier | http://edamontology.org/data_0842 |
| \<UUID\> | Aggregated normalized read count from the file identified by this UUID | trp:EFAMN02+ | trp:EFMPF10 | real | obi:NormalizedDataSet | http://purl.obolibrary.org/obo/OBI_0000451 |


### Artifact AT_EF/ROF

* Name: TCGA Origin RNA-Seq File
* Example File: [rna-seq-origin-file.tsv](examples/rna-seq-origin-file.tsv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| gene_id | Ensembl gene identifier with version | trp:EFROF01 | - | string | edam:Identifier | http://edamontology.org/data_0842 |
| gene_name | Human-readable symbol for the gene | trp:EFROF02 | - | string | so:Gene | http://purl.obolibrary.org/obo/SO_0000704 |
| gene_type | Gene biotype classification (e.g., protein_coding, pseudogene) | trp:EFROF03 | - | string | edam:Classification | http://edamontology.org/operation_2990 |
| unstranded | Raw read count for unstranded protocol | trp:EFROF04 | - | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |
| stranded_first | Raw read count for first-strand protocol | trp:EFROF05 | - | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |
| stranded_second | Raw read count for second-strand protocol | trp:EFROF06 | - | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |
| tpm_unstranded | Normalized expression in TPM (Transcripts Per Million), unstranded protocol | trp:EFROF07 | - | real | obi:NormalizedDataSet | http://purl.obolibrary.org/obo/OBI_0000451 |
| fpkm_unstranded | Normalized expression in FPKM (Fragments Per Kilobase Million), unstranded | trp:EFROF08 | - | real | obi:NormalizedDataSet | http://purl.obolibrary.org/obo/OBI_0000451 |
| fpkm_uq_unstranded | Upper quartile normalized FPKM expression, unstranded | trp:EFROF09 | - | real | obi:NormalizedDataSet | http://purl.obolibrary.org/obo/OBI_0000451 |

### Artifact AT_EF/RPF

* Name: TCGA Origin RNA-Seq Processed File
* Example File: [rna-seq-processed-file.csv](examples/rna-seq-processed-file.tsv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| gene_id | Ensembl gene identifier with version | trp:EFRPF01 | trp:EFROF01 | string | edam:Identifier | http://edamontology.org/data_0842 |
| gene_name | Human-readable symbol for the gene | trp:EFRPF02 | trp:EFROF02 | string | so:Gene | http://purl.obolibrary.org/obo/SO_0000704 |
| gene_type | Gene biotype classification (e.g., protein_coding, pseudogene) | trp:EFRPF03 | trp:EFROF03 | string | edam:Classification | http://edamontology.org/operation_2990 |
| unstranded | Raw read count for unstranded protocol | trp:EFRPF04 | trp:EFROF04 | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |
| stranded_first | Raw read count for first-strand protocol | trp:EFRPF05 | trp:EFROF05 | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |
| stranded_second | Raw read count for second-strand protocol | trp:EFRPF06 | trp:EFROF06 | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |
| tpm_unstranded | Normalized expression in TPM (Transcripts Per Million), unstranded protocol | trp:EFRPF07 | trp:EFROF07 | real | obi:NormalizedDataSet | http://purl.obolibrary.org/obo/OBI_0000451 |
| fpkm_unstranded | Normalized expression in FPKM (Fragments Per Kilobase Million), unstranded | trp:EFRPF08 | trp:EFROF08 | real | obi:NormalizedDataSet | http://purl.obolibrary.org/obo/OBI_0000451 |
| fpkm_uq_unstranded | Upper quartile normalized FPKM expression, unstranded | trp:EFRPF09 | trp:EFROF09 | real | obi:NormalizedDataSet | http://purl.obolibrary.org/obo/OBI_0000451 |
| is_mrna_of_interest | Indicates if the gene meets criteria for inclusion in the study (1: yes, 0: no) | trp:EFRPF10 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |

### Artifact AT_EF/ARR

* Name: Aggregated Messenger RNA Raw Reads
* Example File: [aggregated-rna-raw-reads.csv](interim/tcga-brca/basal-like-files/aggregated-rna-raw-reads.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| gene_id | Ensembl gene identifier with version | trp:EFARR01 | trp:EFRPF01 | string | edam:Identifier | http://edamontology.org/data_0842 |
| gene_name | Human-readable symbol for the gene | trp:EFARR02 | trp:EFRPF02 | string | so:Gene | http://purl.obolibrary.org/obo/SO_0000704 |
| \<UUID\> | Aggregated raw read count from the file identified by this UUID | trp:EFARR03+ | trp:EFRPF04 | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |

### Artifact AT_EF/ARN

* Name: Aggregated Messenger RNA Normalized Reads
* Example File: [aggregated-rna-normalized-reads.csv](interim/tcga-brca/basal-like-files/aggregated-rna-normalized-reads.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| gene_id | Ensembl gene identifier with version | trp:EFARN01 | trp:EFRPF01 | string | edam:Identifier | http://edamontology.org/data_0842 |
| gene_name | Human-readable symbol for the gene | trp:EFARN02 | trp:EFRPF02 | string | so:Gene | http://purl.obolibrary.org/obo/SO_0000704 |
| \<UUID\> | Aggregated normalized read count from the file identified by this UUID | trp:EFARN03+ | trp:EFRPF07 | real | obi:NormalizedDataSet | http://purl.obolibrary.org/obo/OBI_0000451 |


## Family of Artifacts AT_MF

* Family Name: TCGA Molecule Filtering Artifacts

### Artifact AT_MF/EM

* Name: edgeR's filterByExpr Expressed MicroRNAs
* File: [expressed-mirs.csv](processed/tcga-brca/expressed-mirs.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| accession_id | Accession identifier for mature miRNAs from miRBase | trp:MFEM01 | trp:EFAMR01 | string | edam:Identifier | http://edamontology.org/data_0842 |
| is_expressed | Indicates if the miRNA is expressed according to edgeR's filterByExpr function (1: yes, 0: no) | trp:MFEM02 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |


### Artifact AT_MF/AMR

* Name: Aggregated MicroRNA Raw Reads
* Example file: [aggregated-mir-raw-reads.csv](processed/tcga-brca/basal-like-files/aggregated-mir-raw-reads.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| accession_id | Accession identifier for mature miRNA from miRBase | trp:MFAMR01 | trp:EFAMR01 | string | edam:Identifier | http://edamontology.org/data_0842 |
| is_expressed | Indicates if the miRNA is expressed according to edgeR's filterByExpr function (1: yes, 0: no) | trp:MFAMR02 | trp:MFEM02 | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| \<UUID\> | Aggregated raw read count from the file identified by this UUID | trp:MFAMR03+ | trp:EFAMR02+ | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |

### Artifact AT_MF/AMN

* Name: Aggregated MicroRNA Normalized Reads
* Example file: [aggregated-mir-normalized-reads.csv](processed/tcga-brca/basal-like-files/aggregated-mir-normalized-reads.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| accession_id | Accession identifier for mature miRNA from miRBase | trp:MFAMN01 | trp:EFAMN01 | string | edam:Identifier | http://edamontology.org/data_0842 |
| is_expressed | Indicates if the miRNA is expressed according to edgeR's filterByExpr function (1: yes, 0: no) | trp:MFAMN02 | trp:MFEM02 | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| \<UUID\> | Aggregated normalized read count from the file identified by this UUID | trp:MFAMN03+ | trp:EFAMN02+ | real | obi:NormalizedDataSet | http://purl.obolibrary.org/obo/OBI_0000451 |

### Artifact AT_MF/ER

* Name: edgeR's filterByExpr Expressed Messenger RNAs
* File: [expressed-rnas.csv](processed/tcga-brca/expressed-rnas.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| gene_id | Ensembl gene identifier with version | trp:MFER01 | trp:EFARR01 | string | edam:Identifier | http://edamontology.org/data_0842 |
| gene_name | Human-readable symbol for the gene | trp:MFER02 | trp:EFARR02 | string | so:Gene | http://purl.obolibrary.org/obo/SO_0000704 |
| is_expressed | Indicates if the mRNA is expressed according to edgeR's filterByExpr function (1: yes, 0: no) | trp:MFER03 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |

### Artifact AT_MF/ARR

* Name: Aggregated Messenger RNA Raw Reads
* Example file: [aggregated-rna-raw-reads.csv](processed/tcga-brca/basal-like-files/aggregated-rna-raw-reads.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| gene_id | Ensembl gene identifier with version | trp:MFARR01 | trp:EFARR01 | string | edam:Identifier | http://edamontology.org/data_0842 |
| gene_name | Human-readable symbol for the gene | trp:MFARR02 | trp:EFARR02 | string | so:Gene | http://purl.obolibrary.org/obo/SO_0000704 |
| is_expressed | Indicates if the mRNA is expressed according to edgeR's filterByExpr function (1: yes, 0: no) | trp:MFARR03 | trp:MFER03 | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| \<UUID\> | Aggregated raw read count from the file identified by this UUID | trp:MFARR04+ | trp:EFARR03+ | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |

### Artifact AT_MF/ARN

* Name: Aggregated Messenger RNA Normalized Reads
* Example file: [aggregated-rna-normalized-reads.csv](processed/tcga-brca/basal-like-files/aggregated-rna-normalized-reads.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| gene_id | Ensembl gene identifier with version | trp:MFARN01 | trp:EFARN01 | string | edam:Identifier | http://edamontology.org/data_0842 |
| gene_name | Human-readable symbol for the gene | trp:MFARN02 | trp:EFARN02 | string | so:Gene | http://purl.obolibrary.org/obo/SO_0000704 |
| is_expressed | Indicates if the mRNA is expressed according to edgeR's filterByExpr function (1: yes, 0: no) | trp:MFARN03 | trp:MFER03 | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| \<UUID\> | Aggregated normalized read count from the file identified by this UUID | trp:MFARN04+ | trp:EFARN03+ | real | obi:NormalizedDataSet | http://purl.obolibrary.org/obo/OBI_0000451 |


## Family of Artifacts AT_II

* Family Name: MicroRNA-Messenger RNA Interaction Inference Artifacts

### Artifact AT_II/MO

* Name: miRWalk Origin Targets File 
* Example file: [mirwalk-origin-file.csv](examples/mirwalk-origin-file.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| mirnaid | miRNA identifier indicating the microRNA | trp:IIMO01 | - | string | so:MicroRNA | http://purl.obolibrary.org/obo/SO_0000276 |
| refseqid | RefSeq accession number for the target transcript | trp:IIMO02 | - | string | so:MessengerRNA | http://purl.obolibrary.org/obo/SO_0000234 |
| genesymbol | Human-readable gene symbol of the target gene | trp:IIMO03 | - | string | so:Gene | http://purl.obolibrary.org/obo/SO_0000704 |
| duplex | RNA duplex structure between miRNA and target mRNA | trp:IIMO04 | - | string | edam:SecondaryStructureData | http://edamontology.org/data_2973 |
| start | Start position of the binding site on the transcript | trp:IIMO05 | - | integer | so:Region | http://purl.obolibrary.org/obo/SO_0000001 |
| end | End position of the binding site on the transcript | trp:IIMO06 | - | integer | so:Region | http://purl.obolibrary.org/obo/SO_0000001 |
| bindingp | Probability of miRNA binding at the site | trp:IIMO07 | - | real | stato:Statistic | http://purl.obolibrary.org/obo/STATO_0000039 |
| energy | Minimum free energy of miRNA-mRNA duplex | trp:IIMO08 | - | real | sbo:ThermodynamicParameter | http://biomodels.net/SBO/SBO_0000571 |
| seed | Indicates if the seed region of the miRNA is matched (1: yes, 0: no) | trp:IIMO09 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| accessibility | Accessibility score of the target region | trp:IIMO10 | - | real | stato:Score | http://purl.obolibrary.org/obo/STATO_0000569 |
| au | AU content in the binding region | trp:IIMO11 | - | real | so:SequenceAttribute | http://purl.obolibrary.org/obo/SO_0000400 |
| phylopstem | PhyloP conservation score of the binding stem region | trp:IIMO12 | - | real | stato:Score | http://purl.obolibrary.org/obo/STATO_0000569 |
| phylopflank | PhyloP conservation score of the binding flanking region | trp:IIMO13 | - | real | stato:Score | http://purl.obolibrary.org/obo/STATO_0000569 |
| me | Log-odds score (mirSVR or similar) for interaction effectiveness | trp:IIMO14 | - | real | stato:Score | http://purl.obolibrary.org/obo/STATO_0000569 |
| number_of_pairings | Total number of paired bases in the duplex | trp:IIMO15 | - | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |
| binding_region_length | Length of the binding region in nucleotides | trp:IIMO16 | - | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |
| longest_consecutive_pairings | Maximum number of consecutive base pairings in the duplex | trp:IIMO17 | - | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |
| position | Region of the transcript where the binding occurs (e.g., 3UTR, CDS, 5UTR) | trp:IIMO18 | - | string | so:TranscriptRegion | http://purl.obolibrary.org/obo/SO_0000833 |
| validated | Indicates if miRTarBase validated the interaction | trp:IIMO19 | - | string | edam:Identifier | http://edamontology.org/data_0842 |
| TargetScan | Indicates if TargetScan predicts the interaction (1: yes, 0: no) | trp:IIMO20 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| miRDB | Indicates if miRDB predicts the interaction (1: yes, 0: no) | trp:IIMO21 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |

### Artifact AT_II/MP

* Name: miRWalk Origin Processed Targets File 
* Example file: [mirwalk-processed-file.csv](examples/mirwalk-processed-file.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| mirna_name | miRNA identifier indicating the microRNA | trp:IIMP01 | trp:IIMO01 | string | so:MicroRNA | http://purl.obolibrary.org/obo/SO_0000276 |
| refseq_id | RefSeq accession number for the target transcript | trp:IIMP02 | trp:IIMO02 | string | so:MessengerRNA | http://purl.obolibrary.org/obo/SO_0000234 |
| gene_name | Human-readable gene symbol of the target gene | trp:IIMP03 | trp:IIMO03 | string | so:Gene | http://purl.obolibrary.org/obo/SO_0000704 |
| duplex | RNA duplex structure between miRNA and target mRNA | trp:IIMP04 | trp:IIMO04 | string | edam:SecondaryStructureData | http://edamontology.org/data_2973 |
| start | Start position of the binding site on the transcript | trp:IIMP05 | trp:IIMO05 | integer | so:Region | http://purl.obolibrary.org/obo/SO_0000001 |
| end | End position of the binding site on the transcript | trp:IIMP06 | trp:IIMO06 | integer | so:Region | http://purl.obolibrary.org/obo/SO_0000001 |
| binding_probability | Probability of miRNA binding at the site | trp:IIMP07 | trp:IIMO07 | real | stato:Statistic | http://purl.obolibrary.org/obo/STATO_0000039 |
| energy | Minimum free energy of miRNA-mRNA duplex | trp:IIMP08 | trp:IIMO08 | real | sbo:ThermodynamicParameter | http://biomodels.net/SBO/SBO_0000571 |
| seed | Indicates if the seed region of the miRNA is matched (1: yes, 0: no) | trp:IIMP09 | trp:IIMO09 | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| accessibility | Accessibility score of the target region | trp:IIMP10 | trp:IIMO10 | real | stato:Score | http://purl.obolibrary.org/obo/STATO_0000569 |
| au | AU content proportion in the binding region | trp:IIMP11 | trp:IIMO11 | real | so:SequenceAttribute | http://purl.obolibrary.org/obo/SO_0000400 |
| phylopstem | PhyloP conservation score of the binding stem region | trp:IIMP12 | trp:IIMO12 | real | stato:Score | http://purl.obolibrary.org/obo/STATO_0000569 |
| phylopflank | PhyloP conservation score of the binding flanking region | trp:IIMP13 | trp:IIMO13 | real | stato:Score | http://purl.obolibrary.org/obo/STATO_0000569 |
| me | Log-odds score (mirSVR or similar) for interaction effectiveness | trp:IIMP14 | trp:IIMO14 | real | stato:Score | http://purl.obolibrary.org/obo/STATO_0000569 |
| number_of_pairings | Total number of paired bases in the duplex | trp:IIMP15 | trp:IIMO15 | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |
| binding_region_length | Length of the binding region in nucleotides | trp:IIMP16 | trp:IIMO16 | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |
| longest_consecutive_pairings | Maximum number of consecutive base pairings in the duplex | trp:IIMP17 | trp:IIMO17 | integer | stato:Count | http://purl.obolibrary.org/obo/STATO_0000047 |
| binding_position | Region of the transcript where the binding occurs (e.g., 3UTR, CDS, 5UTR) | trp:IIMP18 | trp:IIMO18 | string | so:TranscriptRegion | http://purl.obolibrary.org/obo/SO_0000833 |
| mirtarbase | Indicates if miRTarBase validated the interaction | trp:IIMP19 | trp:IIMO19 | string | edam:Identifier | http://edamontology.org/data_0842 |
| targetscan | Indicates if TargetScan predicts the interaction (1: yes, 0: no) | trp:IIMP20 | trp:IIMO20 | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| mirdb | Indicates if miRDB predicts the interaction (1: yes, 0: no) | trp:IIMP21 | trp:IIMO21 | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |
| is_interaction_of_interest | Indicates if the interaction meets criteria for inclusion in the study (1: yes, 0: no) | trp:IIMP22 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |


### Artifact AT_II/MNP

* Name: MIMAT ID to MicroRNA Name Mapping
* File: [mapping-mir-accession-id-to-name.csv](processed/mirwalk/mapping-mir-accession-id-to-name.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| accession_id | Accession identifier for mature miRNAs from miRBase | trp:IIMNP01 | trp:MFEM01 | string | edam:Identifier | http://edamontology.org/data_0842 |
| mirna_name | Human-readable name for the mature miRNA | trp:IIMNP02 | trp:IIMP01 | string | so:MicroRNA | http://purl.obolibrary.org/obo/SO_0000276 |


### Artifact AT_II/IS

* Name: MicroRNA-Messenger RNA Inferred Interactions Set
* Example file: [inferred-interactions.csv](interim/tcga-brca/basal-like-files/inferred-interactions.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| accession_id | Accession identifier for mature miRNAs from miRBase | trp:IIIS01 | trp:MFAMN01 | string | edam:Identifier | http://edamontology.org/data_0842 |
| mirna_name | Name of the microRNA according to miRBase nomenclature | trp:IIIS02 | trp:IIMNP02 | string | so:MicroRNA | http://purl.obolibrary.org/obo/SO_0000276 |
| gene_name | Name of the target gene tested for correlation with the microRNA | trp:IIIS03 | trp:MFARN02 | string | gro:Gene | http://purl.obolibrary.org/obo/SO_0000704 |
| mirtarbase | Indicates if the interaction is supported by experimental evidence in miRTarBase | trp:IIIS04 | trp:IIMP19 | boolean | edam:Identifier | http://edamontology.org/data_0842 |
| correlation  | Correlation coefficient between microRNA and gene expression | trp:IIIS05 | - | real | stato:CorrelationCoefficient | http://purl.obolibrary.org/obo/STATO_0000142 |
| pvalue | Nominal p-value for the correlation significance test | trp:IIIS06 | - | real | stato:PValue | http://purl.obolibrary.org/obo/STATO_0000700 |
| qvalue | Adjusted p-value for multiple hypothesis testing | trp:IIIS07 | - | real | obi:QValue | http://purl.obolibrary.org/obo/OBI_0001442 |


## Family of Artifacts AT_MN

* Family Name: MicroRNA Networks Artifacts

### Artifact AT_MN/FI

* Name: MicroRNA-Messenger RNA Filtered Inferred Interactions Set
* Example file: [inferred-interactions.csv](processed/tcga-brca/basal-like-files/inferred-interactions.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| accession_id | Accession identifier for mature miRNAs from miRBase | trp:MNFI01 | trp:IIIS01 | string | edam:Identifier | http://edamontology.org/data_0842 |
| mirna_name | Name of the microRNA according to miRBase nomenclature | trp:MNFI02 | trp:IIIS02 | string | so:MicroRNA | http://purl.obolibrary.org/obo/SO_0000276 |
| gene_name | Name of the target gene tested for correlation with the microRNA | trp:MNFI03 | trp:IIIS03 | string | gro:Gene | http://purl.obolibrary.org/obo/SO_0000704 |
| mirtarbase | Indicates if the interaction is supported by experimental evidence in miRTarBase | trp:MNFI04 | trp:IIIS04 | boolean | edam:Identifier | http://edamontology.org/data_0842 |
| correlation  | Correlation coefficient between microRNA and gene expression | trp:MNFI05 | trp:IIIS05 | real | stato:CorrelationCoefficient | http://purl.obolibrary.org/obo/STATO_0000142 |
| pvalue | Nominal p-value for the correlation significance test | trp:MNFI06 | trp:IIIS06 | real | stato:PValue | http://purl.obolibrary.org/obo/STATO_0000700 |
| qvalue | Adjusted p-value for multiple hypothesis testing | trp:MNFI07 | trp:IIIS07 | real | obi:QValue | http://purl.obolibrary.org/obo/OBI_0001442 |
| is_interaction_of_interest | Indicates if the interaction meets criteria for inclusion in the study (1: yes, 0: no) | trp:MNFI08 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |

### Artifact AT_MN/INE

* Name: MicroRNA-Messenger RNA Interaction Network Edges for Cytoscape
* Example file: [interaction-network-edges.csv](processed/cytoscape/basal-like-files/interaction-network-edges.csv)

| field name | description | unique id | descendant_of | data type | role | URI |
| ---------- | ----------- | --------- | --------------| --------- | ---- | --- |
| source | Name of the microRNA according to miRBase nomenclature | trp:MNINE01 | trp:MNFI02 | string | so:MicroRNA | http://purl.obolibrary.org/obo/SO_0000276 |
| target | Name of the target gene tested for correlation with the microRNA | trp:MNINE02 | trp:MNFI03 | string | gro:Gene | http://purl.obolibrary.org/obo/SO_0000704 |
| mirtarbase | Indicates if the interaction is supported by experimental evidence in miRTarBase | trp:MNINE03 | trp:MNFI04 | boolean | edam:Identifier | http://edamontology.org/data_0842 |
| correlation  | Correlation coefficient between microRNA and gene expression | trp:MNINE04 | trp:MNFI05 | real | stato:CorrelationCoefficient | http://purl.obolibrary.org/obo/STATO_0000142 |
| qvalue | Adjusted p-value for multiple hypothesis testing | trp:MNINE05 | trp:MNFI07 | real | obi:QValue | http://purl.obolibrary.org/obo/OBI_0001442 |

### Artifact AT_MN/INN

* Name: MicroRNA-Messenger RNA Interaction Network Nodes for Cytoscape
* Example file: [interaction-network-nodes.csv](processed/cytoscape/basal-like-files/interaction-network-nodes.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| id | Unique identifier for the node, using standardized gene or microRNA symbols | trp:MNINN01 | trp:MNINE01 and trp:MNINE02 | string | edam:Identifier | http://edamontology.org/data_0842 |
| label | Display label for the node, typically matching the identifier | trp:MNINN02 | trp:MNINE01 and trp:MNINE02 | string | edam:Identifier | http://edamontology.org/data_0842 |
| type | Biological entity type (MicroRNA/Messenger RNA) | trp:MNINN03 | - | string | edam:Classification | http://edamontology.org/operation_2990 |

### Artifact AT_MN/AS

* Name: MicroRNA-MicroRNA Inferred Associations Set
* Example file: [inferred-associations.csv](interim/tcga-brca/basal-like-files/inferred-associations.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| node_a | First microRNA in the pair being associated | trp:MNAS01 | - | string | so:MicroRNA | http://purl.obolibrary.org/obo/SO_0000276 |
| node_b | Second microRNA in the pair being associated | trp:MNAS02 | - | string | so:MicroRNA | http://purl.obolibrary.org/obo/SO_0000276 |
| association | Strength of the association between the microRNA pair | trp:MNAS03 | - | real | stato:MeasureOfAssociation | http://purl.obolibrary.org/obo/STATO_0000610 |

### Artifact AT_MN/FAS

* Name: MicroRNA-MicroRNA Filtered Inferred Associations Set
* Example file: [inferred-associations.csv](processed/tcga-brca/basal-like-files/inferred-associations.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| node_a | First microRNA in the pair being associated | trp:MNFAS01 | trp:MNAS01 | string | so:MicroRNA | http://purl.obolibrary.org/obo/SO_0000276 |
| node_b | Second microRNA in the pair being associated | trp:MNFAS02 | trp:MNAS02 | string | so:MicroRNA | http://purl.obolibrary.org/obo/SO_0000276 |
| association | Strength of the association between the microRNA pair | trp:MNFAS03 | trp:MNAS03 | real | stato:MeasureOfAssociation | http://purl.obolibrary.org/obo/STATO_0000610 |
| is_association_of_interest | Indicates if the association meets criteria for inclusion in the study (1: yes, 0: no) | trp:MNFAS04 | - | boolean | edam:DataFiltering | http://edamontology.org/operation_3695 |

### Artifact AT_MN/ANE

* Name: MicroRNA Association Network Edges for Cytoscape
* Example file: [association-network-edges.csv](processed/cytoscape/basal-like-files/association-network-edges.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| source | Source miRNA in the association pair | trp:MNANE01 | trp:MNFAS01 | string | so:MicroRNA | http://purl.obolibrary.org/obo/SO_0000276 |
| target | Target miRNA in the association pair | trp:MNANE02 | trp:MNFAS02 | string | so:MicroRNA | http://purl.obolibrary.org/obo/SO_0000276 |
| association | Association index between the pair of miRNAs | trp:MNANE03 | trp:MNFAS03 | real | stato:MeasureOfAssociation | http://purl.obolibrary.org/obo/STATO_0000610 |

### Artifact AT_MN/ANN

* Name: MicroRNA Association Network Nodes for Cytoscape
* Example file: [association-network-nodes.csv](processed/cytoscape/basal-like-files/association-network-nodes.csv)

| field name | description | unique id | descendant of | data type | role | URI |
| ---------- | ----------- | --------- | ------------- | --------- | ---- | --- |
| id | Unique identifier for the microRNA node | trp:MNANN01 | trp:MNANE01 and trp:MNANE02 | string | so:MicroRNA | http://purl.obolibrary.org/obo/SO_0000276 |
| label | Display label for the microRNA | trp:MNANN02 | trp:MNANE01 and trp:MNANE02 | string | so:MicroRNA | http://purl.obolibrary.org/obo/SO_0000276 |
| type | Type of biological entity represented by the node | trp:MNANN03 | - | string | edam:Classification | http://edamontology.org/operation_2990 |
