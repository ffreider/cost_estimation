# Cost Distribution and Tornado Diagram Visualization

This repository contains two scripts for visualizing cost distributions and tornado diagrams. The first script generates PDF and CDF plots based on expected value and standard deviation. The second script cleans WBS data and plots a tornado diagram.

## Requirements

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

