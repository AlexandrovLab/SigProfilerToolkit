# SigProfilerToolkit

SigProfilerToolkit is a unified toolkit for mutational signature analysis, combining tools for matrix generation, plotting, assignment, and extraction.

## Features
- **Matrix Generation**: Generate mutational matrices using SigProfilerMatrixGenerator.
- **Plotting**: Create mutation plots using SigProfilerPlotting.
- **Assignment**: Assign extracted or known mutational signatures to samples using SigProfilerAssignment.
- **Extraction**: Extract de novo mutational signatures using SigProfilerExtractor.

## Installation
### Local
```bash
pip install git+https://github.com/yourusername/SigProfilerToolkit.git@main
```

### Docker
```bash
docker build -t sigprofilertoolkit .
docker run --rm sigprofilertoolkit <command> [<args>]
```

## Usage
### Matrix Generation
```bash
SigProfilerToolkit matrix_generator install GRCh37
SigProfilerToolkit matrix_generator matrix_generator ExampleProject GRCh37 /data/input_files
```

### Plotting
```bash
SigProfilerToolkit plotting plotSBS /data/matrix/SBS_matrix.txt /results/sbs_plots ExampleProject 96
```

### Assignment
```bash
SigProfilerToolkit assignment decompose_fit /data/input/matrix.txt /results/output_dir
```

### Extraction
```bash
SigProfilerToolkit extractor sigprofilerextractor /data/input /results/output_dir
```

## License
This project is licensed under the MIT License.
