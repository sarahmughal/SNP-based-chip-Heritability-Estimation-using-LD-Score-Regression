#!/usr/bin/env python3
"""
setup_data.py

Downloads and prepares the Assignment 2 LDSC data:
- GWAS summary statistics (GERA-sqrtHDL.tsv.gz)
- European LD reference panel (eur_w_ld_chr.tar.gz), then extracts to tmp/eur_w_ld_chr/

Safe to re-run: it skips downloads/extraction if files already exist.
"""

from __future__ import annotations

import os
import sys
import tarfile
import urllib.request
from pathlib import Path


GWAS_URL = (
    "https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/"
    "GCST007001-GCST008000/GCST007140/GERA-sqrtHDL.tsv.gz"
)
REF_URL = "https://zenodo.org/records/8182036/files/eur_w_ld_chr.tar.gz"


def download(url: str, dest: Path) -> None:
    """Download url -> dest with a simple progress indicator."""
    dest.parent.mkdir(parents=True, exist_ok=True)

    if dest.exists() and dest.stat().st_size > 0:
        print(f"✅ Already exists, skipping download: {dest}")
        return

    print(f"⬇️  Downloading {url}")
    print(f"    -> {dest}")

    def report(block_num: int, block_size: int, total_size: int) -> None:
        if total_size <= 0:
            return
        downloaded = block_num * block_size
        pct = min(downloaded / total_size * 100, 100)
        sys.stdout.write(f"\r    {pct:5.1f}%")
        sys.stdout.flush()

    try:
        urllib.request.urlretrieve(url, dest, reporthook=report)
    finally:
        sys.stdout.write("\n")

    if not dest.exists() or dest.stat().st_size == 0:
        raise RuntimeError(f"Download failed or produced empty file: {dest}")

    print(f"✅ Downloaded: {dest} ({dest.stat().st_size / (1024**2):.1f} MB)")


def extract_tar_gz(archive_path: Path, out_dir: Path) -> None:
    """Extract a .tar.gz file if the target folder doesn't already look extracted."""
    out_dir.mkdir(parents=True, exist_ok=True)

    # If it already contains expected files, assume extracted
    hm3 = out_dir / "w_hm3.snplist"
    if hm3.exists() and hm3.stat().st_size > 0:
        print(f"✅ Reference panel already extracted: {out_dir}")
        return

    if not archive_path.exists():
        raise FileNotFoundError(f"Archive not found: {archive_path}")

    print(f"📦 Extracting {archive_path} -> {out_dir.parent}")
    # The tar contains a folder "eur_w_ld_chr", so extract into tmp/
    with tarfile.open(archive_path, "r:gz") as tf:
        tf.extractall(path=out_dir.parent)

    if not hm3.exists():
        print("⚠️ Extraction finished, but w_hm3.snplist was not found where expected.")
        print("   Check tmp/eur_w_ld_chr/ contents.")
    else:
        print(f"✅ Extracted reference panel to: {out_dir}")


def main() -> None:
    project_dir = Path(__file__).resolve().parent
    tmp_dir = project_dir / "tmp"

    gwas_path = tmp_dir / "GERA-sqrtHDL.tsv.gz"
    ref_tar_path = tmp_dir / "eur_w_ld_chr.tar.gz"
    ref_dir = tmp_dir / "eur_w_ld_chr"

    print(f"Project: {project_dir}")
    print(f"tmp/:    {tmp_dir}")

    download(GWAS_URL, gwas_path)
    download(REF_URL, ref_tar_path)
    extract_tar_gz(ref_tar_path, ref_dir)

    print("\nAll set ✅")
    print(f"- GWAS: {gwas_path}")
    print(f"- Ref:  {ref_dir}")


if __name__ == "__main__":
    main()
