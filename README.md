# 🔗 DataNexus

**Progetti di Sistemi Informativi Evoluti e Big Data** | A.A. 2025-2026

Una raccolta di quattro progetti che esplorano le principali tecnologie NoSQL e Big Data: dall'analisi di sentiment con MongoDB, al monitoraggio real-time con InfluxDB, ai grafi di conoscenza con Neo4j, fino all'elaborazione distribuita con MapReduce.

---

## 📁 Struttura del Repository

```
DataNexus/
├── homework1-mongodb/      # Sentiment Analysis su Amazon Reviews
├── homework2-influxdb/     # Analisi Crimini LAPD (Time Series)
├── homework3-neo4j/        # Grafo Articoli Scientifici arXiv
├── homework4-mapreduce/    # Analisi Pedaggi Autostradali
└── docs/                   # Documentazione e report PDF
```

---

## 🚀 Progetti

### 1️⃣ MongoDB — Sentiment Analysis
Analisi di recensioni Amazon Fine Food con sistema di raccomandazione.

**Tecnologie:** MongoDB, Python, VADER, TF-IDF  
**Features:**
- Collezioni separate per livello di score
- Sentiment analysis automatica
- Sistema di raccomandazione ibrido
- Rilevamento anomalie temporali

---

### 2️⃣ InfluxDB — Crime Data Analytics
Analisi serie temporali dei crimini registrati dal LAPD (2020-2025).

**Tecnologie:** InfluxDB, Python, Pandas, Matplotlib  
**Features:**
- Sistema di alert (warning/alarm) automatizzato
- Analisi stagionale della criminalità
- Clustering incrementale per pattern detection
- Dashboard con metriche real-time

---

### 3️⃣ Neo4j — Knowledge Graph
Grafo di pubblicazioni scientifiche AI da arXiv.

**Tecnologie:** Neo4j, Cypher, Python, BERTopic  
**Features:**
- Rete di co-authorship
- Topic modeling con similarità di Jaccard pesata
- Shortest path tra autori
- Visualizzazione grafi interattiva

---

### 4️⃣ MapReduce — Distributed Computing
Analisi pedaggi autostradali con paradigma MapReduce.

**Tecnologie:** PySpark, mrjob, Python  
**Features:**
- Confronto pedaggi 2015 vs 2025
- Implementazione con Combiner
- Benchmark mrjob vs PySpark

---

## 🛠️ Requisiti

```bash
# Python 3.10+
pip install pymongo influxdb-client neo4j pandas matplotlib plotly
pip install vaderSentiment scikit-learn bertopic sentence-transformers
pip install pyspark mrjob
```

---

## 📊 Dataset

| Progetto | Dataset | Fonte |
|----------|---------|-------|
| MongoDB | Amazon Fine Food Reviews | [Kaggle](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews) |
| InfluxDB | Crime Data 2020-Present | [Data.gov](https://catalog.data.gov/dataset/crime-data-from-2020-to-present) |
| Neo4j | arXiv AI Papers | Allegato |
| MapReduce | Pedaggi Autostradali | Generato |

---

## 👤 Autore

**Federico Sabbadini**  
Università degli Studi di Pavia  
Corso di Sistemi Informativi Evoluti e Big Data

---

## 📄 Licenza

Questo progetto è rilasciato sotto licenza MIT. Vedi [LICENSE](LICENSE) per dettagli.

---

<p align="center">
  <i>Built with ☕ and curiosity</i>
</p>
