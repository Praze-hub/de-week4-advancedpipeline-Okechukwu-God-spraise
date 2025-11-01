# OmniCart Multi-Source Data Enrichment Pipeline

A **data engineering pipeline** that fetches data from multiple API endpoints, handles pagination, enriches product data with seller information, and generates analytical insights into seller performance.  
This project simulates a real-world **ETL (Extract, Transform, Load)** pipeline designed for data engineers working with APIs and complex datasets.

---

##  Project Overview

OmniCart Analytics provides insights into online marketplace dynamics.  
The goal of this pipeline is to answer questions like:

> “Who are our top-performing sellers, and what are their most profitable product categories?”

Since product and seller information come from **different systems**, this project:
1. Fetches data from multiple API endpoints (`/products`, `/users`).
2. Handles **pagination** for large datasets.
3. **Enriches** product data with seller information.
4. Computes **revenue** for each product.
5. Generates aggregated **seller performance metrics**.
6. Saves final results as a JSON report.

---
## Project Structure
```bash
omnicart_pipeline/
├── pipeline/
│ ├── init.py
│ ├── config.py
│ ├── api_client.py 
│ ├── data_enricher.py 
│ ├── data_analyzer.py 
│ └── pipeline.py 
│
├── tests/
│ ├── test_api_client.py
│ ├── test_data_enricher.py
│ ├── test_data_analyzer.py 
│ └── test_config.py 
│
├── main.py
├── pipeline.cfg
├── requirements.txt 
├── .gitignore
└── README.md
```
---
## Running the tests
```bash
pytest -v
```
---
## Installation & Setup
### Clone the repo
```bash
git clone  https://github.com/Praze-hub/de-week4-advancedpipeline-Okechukwu-God-spraise.git
```
### Create a virtual environment
```bash
python -m venv myenv
source myenv/bin/activate
```
### Install requirements.txt
```bash
pip install -r requirements.txt
```
### Run the pipeline
```bash
python pipeline/pipeline.py
```




