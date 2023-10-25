# HF-Image-Encryption
Project Repository for Human Factors Group 13

## Create Developement Environment:

First, you will need to install miniconda. [Here](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html) is the installation guide
with download links. Once miniconda is installed, run the 'Anaconda Prompt'.

Then, create a new python environment using:
```bash
conda create --name env_name python=3.11.4
```

Activate the environment with:
```bash
conda activate env_name
```

Once the environment is activate, it should switch you into that environment. That change
can be seen by (base) changing to (env_name), where 'env_name' is what you named the 
environment when creating it with the above commands. Now in the newly created environment,
use the pip install commands outlined below to install necessary Python libraries. You will
need to switch into this environment in your desired IDE as well.

## Requirements:

Python - 3.11.4

PyQt5 - 5.19.9
```bash
pip install PyQt5
```

Pillow - 10.1.0
```bash
pip install Pillow
```

## Current Techniques Implemented:

- XOR (In progress)
