# Corn Point Cloud Samples

This repository provides four representative annotated maize individual-plant point clouds and four corresponding 4096-point samples associated with the OctPlantNet study.

## Repository contents

- `annotated_samples/`: four processed individual-plant point clouds before VFPS-based fixed-size sampling.
- `example_model_inputs/`: four corresponding 4096-point samples.
- `visualization_examples/representative_samples_pre_vfps_vs_4096_rotation.gif`: rotating visualization of the four paired samples. The top row shows the pre-VFPS point clouds and the bottom row shows the corresponding 4096-point samples. Colors distinguish instance IDs.
- `scripts/load_sample.py`: example script for loading and summarizing the TXT files.
- `sample_manifest.csv`: file names, point counts, columns, and observed label values for the released samples.
- `LICENSE`: license for the repository materials.

## File formats

### Pre-VFPS annotated samples

Files in `annotated_samples/` use four whitespace-separated columns:

```text
X  Y  Z  instance_label
```

`X`, `Y`, and `Z` are point coordinates, and `instance_label` is the annotated organ-instance identifier.

These files are processed individual-plant point clouds rather than raw plot-level TLS scans.

### 4096-point samples

Files in `example_model_inputs/` use five whitespace-separated columns:

```text
X  Y  Z  instance_label  semantic_label
```

For these samples:

- `semantic_label = 0`: stem
- `semantic_label = 1`: leaf

The `instance_label` column stores instance identifiers. Semantic class information should be read from the `semantic_label` column.

## Paired samples

The four sample IDs are:

- `corn_0303`
- `corn_0427`
- `corn_1120`
- `corn_1244`

For each sample ID, the file in `annotated_samples/` is paired with the corresponding `_4096.txt` file in `example_model_inputs/`.

## Loading the data

Example for a 4096-point sample:

```bash
python scripts/load_sample.py example_model_inputs/corn_0303_4096.txt
```

Example for a pre-VFPS sample:

```bash
python scripts/load_sample.py annotated_samples/corn_0303.txt
```

## License

See `LICENSE` for reuse terms.
