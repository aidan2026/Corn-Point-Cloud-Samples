#!/usr/bin/env python3
"""Lightweight reader for the OctPlantNet representative TXT samples."""

from pathlib import Path
import argparse
import numpy as np

def load_sample(path):
    path = Path(path)
    data = np.loadtxt(path)
    if data.ndim != 2:
        raise ValueError("Expected a 2D numeric TXT file.")
    if data.shape[1] == 4:
        return {
            "format": "annotated_pre_vfps",
            "xyz": data[:, 0:3].astype(float),
            "instance_labels": data[:, 3].astype(np.int64),
            "semantic_labels": None,
        }
    if data.shape[1] == 5:
        return {
            "format": "model_input_4096",
            "xyz": data[:, 0:3].astype(float),
            "instance_labels": data[:, 3].astype(np.int64),
            "semantic_labels": data[:, 4].astype(np.int64),
        }
    raise ValueError(
        f"Unsupported column count: {data.shape[1]}. "
        "Expected 4 columns (X Y Z instance_label) for pre-VFPS samples "
        "or 5 columns (X Y Z instance_label semantic_label) for 4096-point samples."
    )

def summarize(sample, path):
    xyz = sample["xyz"]
    inst = sample["instance_labels"]
    sem = sample["semantic_labels"]
    print(f"File: {path}")
    print(f"Format: {sample['format']}")
    print(f"Number of points: {len(xyz)}")
    print(f"XYZ shape: {xyz.shape}")
    print("XYZ min:", np.min(xyz, axis=0))
    print("XYZ max:", np.max(xyz, axis=0))
    print("Instance IDs:", np.unique(inst))
    if sem is not None:
        print("Semantic labels:", np.unique(sem))
        for label in np.unique(sem):
            print(f"  semantic {int(label)}: {int(np.sum(sem == label))} points")

def main():
    parser = argparse.ArgumentParser(description="Read and summarize an OctPlantNet representative TXT sample.")
    parser.add_argument("file", help="Path to a sample TXT file")
    args = parser.parse_args()
    sample = load_sample(args.file)
    summarize(sample, args.file)

if __name__ == "__main__":
    main()
