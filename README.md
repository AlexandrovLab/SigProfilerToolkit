
# SigProfilerToolkit

SigProfilerToolkit is a unified toolkit for mutational signature analysis, combining tools for matrix generation, plotting, assignment, and extraction.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
  - [Local](#local)
  - [Docker](#docker)
  - [Singularity](#singularity)
- [Usage](#usage)
  - [Matrix Generation Example Workflow](#matrix-generation-example-workflow)
- [SigProfilerToolkit Example Commands](#sigprofilertoolkit-example-commands)
  - [SigProfilerMatrixGenerator](#sigprofilermatrixgenerator)
  - [SigProfilerPlotting](#sigprofilerplotting)
  - [SigProfilerAssignment](#sigprofilerassignment)
  - [SigProfilerExtractor](#sigprofilerextractor)
- [Citations](#citations)
- [License](#license)

## Features
- **Matrix Generation**: Generate mutational matrices using SigProfilerMatrixGenerator.
- **Plotting**: Create mutation plots using SigProfilerPlotting.
- **Assignment**: Assign extracted or known mutational signatures to samples using SigProfilerAssignment.
- **Extraction**: Extract de novo mutational signatures using SigProfilerExtractor.

## Installation
### Python
To install in a Python environment using pip:
```bash
pip install git+https://github.com/AlexandrovLab/SigProfilerToolkit.git@main
```

### Docker
To create a Docker container:
1. Clone the repository:
   ```bash
   git clone https://github.com/AlexandrovLab/SigProfilerToolkit.git
   cd SigProfilerToolkit
   ```
2. Build the Docker image:
    ```bash
    docker build -t sigprofilertoolkit .
    docker run --rm sigprofilertoolkit <command> [<args>]
    ```
3. Run the container:
    ```bash
    docker run --rm \
    -e SIGPROFILERPLOTTING_VOLUME=<host_directory> \
    -e SIGPROFILERMATRIXGENERATOR_VOLUME=<host_directory> \
    -e SIGPROFILERASSIGNMENT_VOLUME=<host_directory> \
    sigprofilertoolkit <command> [<args>]
    ```

### Singularity
For Singularity users, convert the Docker image to a Singularity image:
1. Save the Docker image:
   ```bash
   docker save -o sigprofilertoolkit.tar sigprofilertoolkit
   ```
2. Build the Singularity image:
   ```bash
   singularity build sigprofilertoolkit.sif docker-archive://sigprofilertoolkit.tar
   ```
3. Run with Singularity:
   ```bash
   singularity exec \
   --env SIGPROFILERPLOTTING_VOLUME=<host_directory> \
   --env SIGPROFILERMATRIXGENERATOR_VOLUME=<host_directory> \
   --env SIGPROFILERASSIGNMENT_VOLUME=<host_directory> \
   sigprofilertoolkit.sif <command> [<args>]
   ```

**Note**: The environment variables `SIGPROFILERPLOTTING_VOLUME`, `SIGPROFILERMATRIXGENERATOR_VOLUME`, and `SIGPROFILERASSIGNMENT_VOLUME` are **recommended** for Docker and **required** for Singularity containers, as Singularity containers are non-writable.

## Usage

### Matrix Generation Example Workflow

1. **Download Example Data**
   Download the example dataset `21BRCA.zip` from the Alexandrov Lab FTP server:
   ```bash
   wget ftp://alexandrovlab-ftp.ucsd.edu/pub/tools/SigProfilerExtractor/Example_data/21BRCA.zip
   unzip 21BRCA.zip
   ```

2. **Install the Reference Genome**
   Download and install the GRCh37 reference genome using the `matrix_generator` tool:
   ```bash
   SigProfilerToolkit matrix_generator install GRCh37
   ```

3. **Generate Mutational Matrices**
   Use the unzipped `21BRCA` directory as input to generate mutational matrices:
   ```bash
   SigProfilerToolkit matrix_generator matrix_generator example GRCh37 ./21BRCA/21BRCA_vcf/
   ```

4. **Create a Mutation Plot**
   Plot the Single Base Substitution (SBS) matrix using `plotSBS`:
   ```bash
   SigProfilerToolkit plotting plotSBS ./21BRCA/21BRCA_vcf/output/SBS/example.SBS96.all ./results/plots ExampleProject 96
   ```

5. **Run Signature Extraction**
   Perform de novo signature extraction using the `extractor` tool. Set the number of signatures and other parameters:
   ```bash
   SigProfilerToolkit extractor sigprofilerextractor \
   --input_type matrix \
   --input_data ./21BRCA/21BRCA_vcf/output/SBS/example.SBS96.all \
   --output ./results/extraction \
   --minimum_signatures 3 \
   --maximum_signatures 10
   ```

## SigProfilerToolkit Example Commands

Call `SigProfilerToolkit` with the desired tool and command. The following are example commands for each tool:

### SigProfilerMatrixGenerator
| Command                                   | Description                                                             |
|-------------------------------------------|-------------------------------------------------------------------------|
| `matrix_generator install <genome>`       | Install reference genome files (required to generate SBS, DBS, and INDEL matrices).         |
| `matrix_generator matrix_generator <project> <genome> <input_path>` | Generate mutational matrices for SBSs, DBSs, and INDELs.                |
| `matrix_generator sv_matrix_generator <project> <genome> <input_path>` | Generate structural variation (SV) matrices.                           |
| `matrix_generator cnv_matrix_generator <project> <genome> <input_path>` | Generate copy number variation (CNV) matrices.                         |

### SigProfilerPlotting
| Command                      | Description                                                      |
|------------------------------|------------------------------------------------------------------|
| `plotting plotSBS <input> <output>` | Plot Single Base Substitutions (SBS) mutations.                   |
| `plotting plotID <input> <output>`  | Plot Small Insertions and Deletions (ID).                        |
| `plotting plotDBS <input> <output>` | Plot Doublet Base Substitutions (DBS).                           |
| `plotting plotSV <input> <output>`  | Plot Structural Variations (SV).                                 |
| `plotting plotCNV <input> <output>` | Plot Copy Number Variations (CNV).                               |

### SigProfilerAssignment
| Command                                | Description                                                              |
|----------------------------------------|--------------------------------------------------------------------------|
| `assignment decompose_fit <input> <output>` | Perform decomposition fitting on the input samples.                      |
| `assignment denovo_fit <input> <output>`    | Perform de novo fitting on the input samples.                           |
| `assignment cosmic_fit <input> <output>`    | Perform COSMIC signature fitting on the input samples.                  |

### SigProfilerExtractor
| Command                                          | Description                                                              |
|--------------------------------------------------|--------------------------------------------------------------------------|
| `extractor sigprofilerextractor <input> <output>` | Extract de novo mutational signatures from matrix-formatted input samples. |

## Citations

### SigProfilerMatrixGenerator and SigProfilerPlotting
- **For SBSs, DBSs, and INDELs:**

  Bergstrom EN, Huang MN, Mahto U, Barnes M, Stratton MR, Rozen SG, and Alexandrov LB (2019) SigProfilerMatrixGenerator: a tool for visualizing and exploring patterns of small mutational events. *BMC Genomics* 20, Article number: 685.
  [https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-019-6041-2](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-019-6041-2)

- **For SVs and CNVs:**

  Khandekar A, Vangara R, Barnes M, Díaz-Gay M, Abbasi A, Bergstrom EN, Steele CD, Pillay N, and Alexandrov LB (2023) Visualizing and exploring patterns of large mutational events with SigProfilerMatrixGenerator. *BMC Genomics* 24, Article number: 469.
  [https://doi.org/10.1186/s12864-023-09584-y](https://doi.org/10.1186/s12864-023-09584-y)


### SigProfilerAssignment
Díaz-Gay, M., Vangara, R., Barnes, M., ... & Alexandrov, L. B. (2023). Assigning mutational signatures to individual samples and individual somatic mutations with SigProfilerAssignment, *Bioinformatics*, 2023-07. doi: [https://doi.org/10.1093/bioinformatics/btad756](https://doi.org/10.1093/bioinformatics/btad756)

### SigProfilerExtractor
Islam SMA, Díaz-Gay M, Wu Y, Barnes M, Vangara R, Bergstrom EN, He Y, Vella M, Wang J, Teague JW, Clapham P, Moody S, Senkin S, Li YR, Riva L, Zhang T, Gruber AJ, Steele CD, Otlu B, Khandekar A, Abbasi A, Humphreys L, Syulyukina N, Brady SW, Alexandrov BS, Pillay N, Zhang J, Adams DJ, Martincorena I, Wedge DC, Landi MT, Brennan P, Stratton MR, Rozen SG, and Alexandrov LB (2022) Uncovering novel mutational signatures by _de novo_ extraction with SigProfilerExtractor. *Cell Genomics*. doi: [10.1016/j.xgen.2022.100179](https://doi.org/10.1016/j.xgen.2022.100179).

## License
Copyright (c) 2024, Alexandrov Lab [University of California, San Diego] All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.