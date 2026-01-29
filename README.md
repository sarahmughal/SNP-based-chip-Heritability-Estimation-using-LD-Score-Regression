# EPI 217: Molecular and Genetic Epidemiology I
## SNP-Based (“Chip”) Heritability Estimation Using LD Score Regression

This project estimates SNP-based (chip) heritability (h²) using LD Score Regression (LDSC) on GWAS summary statistics. The analysis uses the `gwaslab` Python package along with a European LD reference panel and HapMap3 SNP filtering.

---

## Project Goals

- Download GWAS summary statistics  
- Filter SNPs to HapMap3 variants  
- Download and prepare a European LD reference panel  
- Set up a clean Python environment  
- Run LD Score Regression using `gwaslab`  
- Report SNP heritability (h²), calculate a 95% confidence interval, and interpret the result  

---

## Data Sources

**GWAS Summary Statistics**
- Trait: HDL cholesterol  
- File: `GERA-sqrtHDL.tsv.gz`  
- Source: EBI GWAS Catalog  
- https://www.ebi.ac.uk/gwas/  
- https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST007001-GCST008000/GCST007140/

**LD Reference Panel**
- European LD scores  
- https://zenodo.org/records/8182036  

---

## Project Structure

```text
assign2_ldsc/
├── assign2_ldsc.ipynb
├── filter_hm3.py
├── .venv/
└── tmp/
    ├── GERA-sqrtHDL.tsv.gz
    ├── GERA-sqrtHDL-hm3.tsv.gz
    └── eur_w_ld_chr/
        └── w_hm3.snplist
