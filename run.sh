#!/bin/bash

# Usage: ./run.sh <video_file> <datadir> <outdir>

# video_file="$1"
datadir="$1"
outdir="$2"

# rm -r "${datadir}"
# rm -r "${outdir}"

# # Step 1: Create directories
# mkdir -p "${datadir}/images"

# # Step 2: Convert video to images using ffmpeg
# ffmpeg -i "${video_file}" -vf "fps=2" "./${datadir}/images/%05d.jpg"
conda activate GS
python convert.py --source_path "./${datadir}"

# Step 4: Convert COLMAP model to text format
mkdir "${datadir}/sparse_txt"
colmap model_converter --input_path "${datadir}/sparse/0" --output_path "${datadir}/sparse_txt" --output_type TXT

# Step 5: Run Python script for selecting samples
conda deactivate
python scripts/select_samples.py --dset mipnerf360 --path "${datadir}"

# Step 6: Train models
# Original 3DGS (method1)
python train.py -s "${datadir}" --eval --port 6311 --model_path "${outdir}/method1" --resolution 1 --kshot 5 --seed 3

# DepthRegularization (method2)
python train.py -s "${datadir}" --eval --port 6312 --model_path "${outdir}/method2" --resolution 1 --kshot 75 --seed 3 --depth --usedepthReg