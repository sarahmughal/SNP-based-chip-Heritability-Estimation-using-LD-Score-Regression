# SNP-based-chip-Heritability-Estimation-using-LD-Score-Regression

Download GWAS summary statistics
https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST007001-GCST008000/GCST007140/
Retrieved from https://www.ebi.ac.uk/gwas/ and a cholesterol paper by Hoffman
Download an LD reference panel
Set up a clean Python environment
Run LD Score Regression using gwaslab
Report h², calculate a 95% CI, and explain it in words

Project Overview:

Desktop/
└── assign2_ldsc/
    ├── filter_hm3.py      
    ├── assign2_ldsc.ipynb
    ├── .venv/
    └── tmp/
        ├── GERA-sqrtHDL.tsv.gz
        └── eur_w_ld_chr/
            └── w_hm3.snplist

Open Terminal

mkdir assign2_ldsc
cd assign2_ldsc
mkdir tmp
cd tmp

Now download the GWAS summary statistics:

brew install wget
wget https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST007001-GCST008000/GCST007140/GERA-sqrtHDL.tsv.gz

Quick sanity check:

gunzip -c GERA-sqrtHDL.tsv.gz | head -n 5

Download European reference panel, and extract it

wget https://zenodo.org/records/8182036/files/eur_w_ld_chr.tar.gz
tar -zxvf eur_w_ld_chr.tar.gz

Install gwaslab (may need to run brew install python@3.12 first)

python -m venv .venv
source .venv/bin/activate
pip install gwaslab

Create filter_hm3.py

import gzip

# Load HapMap3 SNP list into a set
with open("tmp/eur_w_ld_chr/w_hm3.snplist") as f:
    hm = {l.split("\t")[0] for l in f if l.strip()}

print(f"loaded in {len(hm)} hapmap3 snps.")

# Stream the GWAS file and write out only HapMap3 SNPs
count_in = 0
count_out = 0

with gzip.open("tmp/GERA-sqrtHDL.tsv.gz", "rt") as f_in, \
     gzip.open("tmp/GERA-sqrtHDL-hm3.tsv.gz", "wt") as f_out:

    header = f_in.readline()
    f_out.write(header)

    for line in f_in:
        count_in += 1
        snp_id = line.split("\t", 1)[0]  # first column is SNP_ID
        if snp_id in hm:
            f_out.write(line)
            count_out += 1

print(f"read in {count_in} snps.")
print(f"wrote out {count_out} hapmap3 snps.")

Create a Jupyter notebook and conduct LD Score Regression (LDSC) utilizing gwaslab

		mkdir assign2_ldsc.ipynb





