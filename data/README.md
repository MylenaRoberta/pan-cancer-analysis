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

---

## [1] Family AT_OR

* Family Name: TCGA Origin Artifacts

### Artifact AT_OR/PM

* Name: TCGA Origin Project Metadata
(data/processed/tcga-brca/project-files/project-metadata.csv; vou mover o artefato para a pasta /raw depois)

### Artifact AT_OR/CM

* Name: TCGA Origin Cases Metadata
(não criei um artefato anterior à filtragem, depois vou salvar em /raw;
é esse arquivo sem as colunas de flag: data/processed/tcga-brca/project-files/cases-metadata.csv)

| field name                      | description | unique id       | descendant of | data type | role                    | URI |
| ------------------------------- | ----------- | --------------- | ------------- | --------- | ----------------------- | --- |
| case_id                         | Unique identifier for each case/patient in the TCGA database | trp:ORCM01 |               | string    | edam:data_identifier    | http://edamontology.org/data_0842 |
| submitter_id                    | Identifier assigned by the data submitter/contributor | trp:ORCM02 |               | string    | edam:data_identifier    | http://edamontology.org/data_0842 |
| disease_type                    | Type of cancer/disease for the case | trp:ORCM03 |               | string    | edam:data_classification| http://edamontology.org/data_2914 |
| pam50_mrna                      | PAM50 molecular subtype classification based on mRNA expression | trp:ORCM04 |               | string    | sbo:molecular_type      | http://purl.obolibrary.org/obo/SBO_0000250 |

### Artifact AT_OR/FM

* Name: TCGA Origin Files Metadata
(não criei um artefato anterior à filtragem, depois vou salvar em /raw;
é esse arquivo sem as colunas de flag: data/processed/tcga-brca/project-files/files-metadata.csv)

---

## [2] Family AT_FOR

* Family Name: TCGA Filtered Origin Artifacts

### Artifact AT_FOR/CM

* Name: TCGA Filtered Origin Cases Metadata (data/processed/tcga-brca/project-files/cases-metadata.csv)

| field name                      | description | unique id       | descendant of | data type | role                    | URI |
| ------------------------------- | ----------- | --------------- | ------------- | --------- | ----------------------- | --- |
| case_id                         | Unique identifier for each case/patient in the TCGA database | trp:FORCA01 | trp:ORCM01 | string    | edam:data_identifier    | http://edamontology.org/data_0842 |
| submitter_id                    | Identifier assigned by the data submitter/contributor | trp:FORCA02 | trp:ORCM02 | string    | edam:data_identifier    | http://edamontology.org/data_0842 |
| disease_type                    | Type of cancer/disease for the case | trp:FORCA03 | trp:ORCM03 | string    | edam:data_classification| http://edamontology.org/data_2914 |
| pam50_mrna                      | PAM50 molecular subtype classification based on mRNA expression | trp:FORCA04 | trp:ORCM04 | string    | sbo:molecular_type      | http://purl.obolibrary.org/obo/SBO_0000250 |
| has_tumor_files_of_interest     | Indicates if the case has tumor files relevant to the analysis | trp:FORCA05 |               | boolean   | edam:data_filtering     | http://edamontology.org/operation_3695 |
| has_normal_files_of_interest    | Indicates if the case has normal tissue files relevant to the analysis | trp:FORCA06 |               | boolean   | edam:data_filtering     | http://edamontology.org/operation_3695 |
| is_case_of_interest             | Indicates if the case meets criteria for inclusion in the study | trp:FORCA07 |               | boolean   | edam:data_filtering     | http://edamontology.org/operation_3695 |

### Artifact AT_FOR/FM

* Name: TCGA Filtered Origin Files Metadata (data/processed/tcga-brca/project-files/files-metadata.csv)

### Artifact AT_FOR/PC

* Name: TCGA Origin Paper Cases Data
(artefato suplementar do artigo do TCGA-BRCA: data/raw/tcga-brca/brca-paper-supplementary-tables-1-to-4.xls;
uso somente as colunas "Complete TCGA ID" e "PAM50 mRNA" da "SuppTable1")

### Artifact AT_FOR/FPC

* Name: TCGA Filtered Origin Paper Cases Metadata (data/processed/tcga-brca/project-files/paper-cases-data.csv)

---

## [3] Family AT_FD

* Family Name: TCGA File Data Artifacts

### Artifact AT_FD/MOF

* Name: TCGA MicroRNA-Seq Origin File
(exemplo em: data/raw/gdc-api/63d7ceb1-b280-43a0-8f19-02fb6dfba18c.mirnaseq.isoforms.quantification.txt)

### Artifact AT_FD/ROF

* Name: TCGA RNA-Seq Origin File
(exemplo em: data/raw/gdc-api/a6f6d0c2-4309-48c3-829a-7fd30fde6d71.rna_seq.augmented_star_gene_counts.tsv)

### Artifact AT_FD/MPF

* Name: TCGA MicroRNA-Seq Processed File
(arquivo original + quebra de colunas + coluna "is_mirna_of_interest"; 
exemplos em notebooks/01_tcga-brca/04_brca-file-processing.ipynb)

### Artifact AT_FD/RPF

* Name: TCGA RNA-Seq Processed File
(arquivo original + coluna "is_mrna_of_interest";
exemplos em notebooks/01_tcga-brca/04_brca-file-processing.ipynb)

### Artifact AT_FD/AMN

* Name: TCGA Aggregated MicroRNA Normalized Reads (data/interim/tcga-brca/.../aggregated-mir-normalized-reads.csv)

### Artifact AT_FD/AMR

* Name: TCGA Aggregated MicroRNA Raw Reads (data/interim/tcga-brca/.../aggregated-mir-raw-reads.csv)

### Artifact AT_FD/ARN

* Name: TCGA Aggregated Messenger RNA Normalized Reads (data/interim/tcga-brca/.../aggregated-rna-normalized-reads.csv)

### Artifact AT_FD/ARR

* Name: TCGA Aggregated Messenger RNA Raw Reads (data/interim/tcga-brca/.../aggregated-rna-raw-reads.csv)

---

## [4] Family AT_MF

* Family Name: TCGA Molecule Filtering Artifacts

### Artifact AT_MF/ER

* Name: edgeR's filterByExpr Expressed Messenger RNAs (data/processed/tcga-brca/expressed-rnas.csv)

### Artifact AT_MF/EM

* Name: edgeR's filterByExpr Expressed MicroRNAs (data/processed/tcga-brca/expressed-mirs.csv)

### Artifact AT_MF/AMN

* Name: TCGA Aggregated MicroRNA Normalized Reads (data/processed/tcga-brca/.../aggregated-mir-normalized-reads.csv)

### Artifact AT_MF/AMR

* Name: TCGA Aggregated MicroRNA Raw Reads (data/processed/tcga-brca/.../aggregated-mir-raw-reads.csv)

### Artifact AT_MF/ARN

* Name: TCGA Aggregated Messenger RNA Normalized Reads (data/processed/tcga-brca/.../aggregated-rna-normalized-reads.csv)

### Artifact AT_MF/ARR

* Name: TCGA Aggregated Messenger RNA Raw Reads (data/processed/tcga-brca/.../aggregated-rna-raw-reads.csv)

---

## [5] Family AT_II

* Family Name: TCGA Interaction Inference Artifacts

### Artifact AT_II/MO

* Name: miRWalk Origin Target File 
(arquivos estão sendo salvos em data/external/mirwalk)

### Artifact AT_II/MP

* Name: miRWalk Processed Origin Target File 
(arquivo original + coluna "is_interaction_of_interest";
arquivos estão sendo salvos em data/processed/mirwalk)

### Artifact AT_II/MNP

* Name: miRWalk MIMAT ID to Name Mapping (data/processed/mirwalk/mapping-mir-accession-id-to-name.csv)

### Artifact AT_II/IS

* Name: TCGA Inferred Interactions Set (data/interim/tcga-brca/.../inferred-interactions.csv)

---

## [6] Family AT_MN

* Family Name: TCGA MicroRNA Network Artifacts

### Artifact AT_MN/FI

* Name: TCGA Filtered Inferred Interactions Set (data/processed/tcga-brca/.../inferred-interactions.csv)

### Artifact AT_MN/INN

* Name: TCGA MicroRNA Interaction Network Nodes (data/processed/cytoscape/.../interaction-network-nodes.csv)

### Artifact AT_MN/INE

* Name: TCGA MicroRNA Interaction Network Edges (data/processed/cytoscape/.../interaction-network-edges.csv)

| field name   | unique id  | descendant_of | data type | role                | URI |
| ------------ | ---------- | --------------| --------- | ------------------- | --- |
| is_expressed | trp:AGMR02 |               | boolean   | edam:data_filtering | http://edamontology.org/operation_3695 |
| qvalue       | trp:INE05  |               | real      | sto:q-value         | http://purl.obolibrary.org/obo/OBI_0001442    |

### Artifact AT_MN/ANN

* Name: TCGA MicroRNA Association Network Nodes (data/processed/cytoscape/.../association-network-nodes.csv)

### Artifact AT_MN/ANE

* Name: TCGA MicroRNA Association Network Edges (data/processed/cytoscape/.../association-network-edges.csv)
