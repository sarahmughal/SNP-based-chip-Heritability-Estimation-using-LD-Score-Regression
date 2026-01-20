import gzip

# Load HapMap3 SNP list into a set
with open("tmp/eur_w_ld_chr/w_hm3.snplist") as f:
    hm = {l.split("\t")[0] for l in f if l.strip()}

print(f"loaded in {len(hm)} hapmap3 snps.")

# Stream the GWAS file and write out only HapMap3 SNPs
count_in = 0
count_out = 0

with (
    gzip.open("tmp/GERA-sqrtHDL.tsv.gz", "rt") as f_in,
    gzip.open("tmp/GERA-sqrtHDL-hm3.tsv.gz", "wt") as f_out,
):
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
