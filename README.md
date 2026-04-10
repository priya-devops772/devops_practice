# Data Pipeline Project (Docker + Automation)

## 📌 Overview
This project demonstrates a simple data pipeline using Python and Docker.

## ⚙️ Features
- Reads input CSV data
- Processes data using pandas
- Adds new column (age after 5 years)
- Saves output to CSV
- Runs inside Docker container
- Supports volume persistence
- Automated using shell script

## 🚀 How to Run

### Build Docker Image
docker build -t pipelineapp .

### Run Pipeline
docker run -v $(pwd)/pipeline:/app pipelineapp

### Run Automated Script
cd pipeline
./run_pipeline.sh

## 📂 Tech Used
- Python
- Pandas
- Docker
- Linux (Shell Script)

## 👤 Author
Priya#


