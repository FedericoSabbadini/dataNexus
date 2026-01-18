# dataNexus 🗄️

**Big Data Project Collection** — Advanced Information Systems and Big Data Course (A.Y. 2025-2026)

A comprehensive collection of four homework assignments exploring modern database technologies and distributed computing paradigms for big data processing.

## 📊 Project Overview

| Module | Database/Technology | Dataset | Key Concepts |
|--------|---------------------|---------|--------------|
| **Amazon Fine Food Reviews** | Document Store | Amazon Fine Food Reviews (568K reviews) | Sentiment Analysis, Recommendations |
| **LAPD Crime Data** | Time-Series DB | LAPD Crime Data (1M+ records) | Time-Series Analysis, Clustering |
| **arXiv** | Graph Database | arXiv AI Publications (8K papers) | Graph Modeling, Network Analysis |
| **Distributed Computing** | Map-reduce approach | Highway Toll Data (100K synthetic) | PySpark vs MRJob Comparison |

## 📁 Repository Structure

```
dataNexus/
├── Amazon Fine Food Reviews/         # MongoDB
│   ├── soluzione/
│   │   ├── homework_mongodb.ipynb    # Main notebook
│   │   └── relazione/                # Report (PDF + DOCX)
│   └── consegna.pdf                  # Assignment spec
│
├── LAPD Crime Data/                  # InfluxDB
│   ├── soluzione/
│   │   ├── homework_influxdb.ipynb   # Main notebook  
│   │   └── relazione/                # Report (PDF + DOCX)
│   └── consegna.pdf                  # Assignment spec
│
├── arXiv AI Publications/            # Neo4J
│   ├── soluzione/
│   │   ├── homework_neo4j.ipynb      # Main notebook
│   │   ├── visualisation1.png        # Graph visualizations
│   │   ├── visualisation2.png
│   │   └── relazione/                # Report (PDF + DOCX)
│   └── consegna/
│       ├── consegna.pdf              # Assignment spec
│       └── MaterialeUtile_Homework/  # Source data files
│
├── Distributed Computing/            # map-reduce
│   ├── soluzione/
│   │   ├── homework_mapreduce.ipynb  # Main notebook
│   │   ├── output/                   # Generated scripts & data
│   │   │   ├── mapreduce_pyspark.py
│   │   │   ├── mapreduce_mrjob.py
│   │   │   └── caselli_autostradali.csv
│   │   └── relazione/                # Report (PDF + DOCX)
│   └── consegna.pdf                  # Assignment spec
│
├── LICENSE
├── .gitignore
└── README.md
```

## 🛠️ Technologies & Tools

- **Databases:** MongoDB 6.0, InfluxDB 2.7, Neo4J with APOC
- **Languages:** Python 3.10+, Cypher, Flux
- **Frameworks:** PySpark, MRJob
- **Libraries:** pymongo, influxdb-client, neo4j, pandas, scikit-learn, matplotlib, networkx, vaderSentiment

## 📝 Module Descriptions

### 1. MongoDB — Sentiment Analysis on Product Reviews
Analysis of Amazon Fine Food Reviews dataset using MongoDB's aggregation framework:
- Sentiment scoring with VADER
- Product recommendation system using TF-IDF and cosine similarity
- Temporal trend analysis for detecting review anomalies

### 2. InfluxDB — Crime Pattern Analysis
Time-series analysis of Los Angeles Police Department crime data:
- Temporal crime pattern detection
- Geographical clustering using K-Means
- Flux queries for time-windowed aggregations

### 3. Neo4J — Academic Publication Network
Graph modeling of arXiv AI papers and their relationships:
- Author co-authorship networks
- Topic clustering and research trend analysis
- Cypher queries for path finding and centrality metrics

### 4. MapReduce — Highway Toll Analysis
Comparison of distributed computing approaches:
- Synthetic dataset generation (100K highway transits)
- MRJob implementation (Hadoop simulation)
- PySpark implementation (in-memory processing)
- Performance benchmarking: 2015 vs 2025 toll variations

## 🚀 Getting Started

### Prerequisites
```bash
# Python environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common dependencies
pip install pandas numpy matplotlib scikit-learn jupyter
```

### Running the Notebooks
Each module is self-contained. Navigate to the desired module and run the Jupyter notebook:

```bash
cd MongoDB/soluzione
jupyter notebook homework_mongodb.ipynb
```

> **Note:** Some notebooks include setup cells for installing databases (MongoDB, InfluxDB) designed for Google Colab environments. For local execution, ensure the respective databases are installed and running.

## 📈 Sample Results

### MongoDB — Top 5 Products by Average Rating
| Product ID | Average Rating | Review Count |
|------------|---------------|--------------|
| B001EO5Y8Q | 5.00 | 41 |
| B002QWP8K2 | 5.00 | 40 |
| B007PA32L2 | 5.00 | 37 |
| B004I8W7AM | 5.00 | 35 |
| B003LSTDKK | 5.00 | 31 |

### MapReduce — Toll Variation 2015 → 2025
| Vehicle Type | 2015 Avg (€) | 2025 Avg (€) | Variation |
|--------------|--------------|--------------|-----------|
| Auto | 7.17 | 9.33 | +30.1% |
| Moto | 4.31 | 5.74 | +33.2% |
| Furgone | 11.46 | 15.06 | +31.4% |
| Camion | 21.54 | 28.60 | +32.8% |
| Bus | 17.29 | 22.99 | +33.0% |

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 🎓 Acknowledgments

- Course: *Advanced Information Systems and Big Data* — A.Y. 2025-2026
- Datasets: Amazon Fine Food Reviews (Kaggle), LAPD Crime Data, arXiv Papers