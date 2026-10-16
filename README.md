# Bio Utils

Python package for working with biological sequence files.

## Features

- **`filter_fastq`** — filters FASTQ reads by GC content, sequence length, and average quality score.
- **`convert_multiline_fasta_to_oneline`** — converts multiline FASTA sequences into single-line sequences.

## Project Structure

```text
bio-utils/
├── README.md
├── bio_utils.py
└── helpers/
    ├── __init__.py
    ├── fastq.py
    └── bio_files.py
```

## Requirements

- Python 3.10 or newer
- Python standard library only

## Usage

Import the functions from `bio_utils.py`:

```python
from bio_utils import filter_fastq, convert_multiline_fasta_to_oneline
```

### Filter FASTQ

```python
filter_fastq(
    input_fastq="reads.fastq",
    output_fastq="filtered_reads.fastq",
    gc_bounds=(40, 60),
    length_bounds=(100, 1000),
    quality_threshold=20
)
```

The filtered file is saved in the `filtered/` directory.

### Convert FASTA

```python
convert_multiline_fasta_to_oneline(
    input_fasta="sequences.fasta",
    output_fasta="sequences_oneline.fasta"
)
```

If `output_fasta` is not specified, the function generates an output filename automatically.

## Author

Violetta Shtol
