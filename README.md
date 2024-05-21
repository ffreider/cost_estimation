# Cost Distribution and Tornado Diagram Visualization

This repository contains two scripts for visualizing cost distributions and tornado diagrams. The first script generates PDF and CDF plots based on expected value and standard deviation. The second script cleans WBS data and plots a tornado diagram.

Example cost estimation csv file from the BioSat satellite project in Orbit NTNU: https://docs.google.com/spreadsheets/d/1yTV-oQwlPQQAkIKiMaMXk4J_56CKUK3r6yJO3o5KUvE/edit#gid=1507483010

## Setup

### Clone the repository
```sh
git clone https://github.com/ffreider/cost_estimation.git
cd cost_estimation
```
### Requirements

- Python 3.x
- numpy
- matplotlib
- scipy
- pandas

You can install the required libraries using pip:

```sh
pip install -r requirements.txt
```

## Usage

### 1. Cost Distribution Visualization
To run the script:
```sh
python plot_pdf_and_cdf.py <expected_value> <std_deviation>
```
Example:
```sh
python plot_pdf_and_cdf.py 1000000 150000
```
### 2. Tornado Diagram Visualization
To run the script:
```sh
python plot_tornado.py <file_path> <level>
```
Example:
```sh
python plot_tornado.py "path_to_file.csv" 3
```

## Contact Information
For any questions or suggestions, please contact freider.floan@gmail.com

