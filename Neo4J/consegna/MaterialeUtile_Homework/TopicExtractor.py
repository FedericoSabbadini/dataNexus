#!/usr/bin/env python
# coding: utf-8

# In[42]:


# -------------------------------------------------------------------------
# 1) Import librerie
# -------------------------------------------------------------------------
# pip install bertopic (Python 3.10 required)
import pandas as pd
import numpy as np
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

print("✔ Import librerie completata!")

# -------------------------------------------------------------------------
# 2) Caricamento dataset
# -------------------------------------------------------------------------
df = pd.read_csv("arxiv_papers.csv")   # deve contenere almeno: abstract, url
abstracts = df["abstract"].fillna("").tolist()

print("✔ Caricamento dataset completato!")

# -------------------------------------------------------------------------
# 3) Modello di embedding
# -------------------------------------------------------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

print("✔ Modello di embedding configurato!")

# -------------------------------------------------------------------------
# 4) Topic modeling
# -------------------------------------------------------------------------
topic_model = BERTopic(
    embedding_model=model,
    calculate_probabilities=True
)

# topics_main = topic assegnato
# probs_full = matrice completa delle probabilità di assegnamento dei topic agli abstract
topics_main, probs_full = topic_model.fit_transform(abstracts)

print("✔ Main topic assegnati!")

# -------------------------------------------------------------------------
# 5) Top-k topic per ogni URL
# -------------------------------------------------------------------------
top_k = 3  # modifica a piacere (es. 5)

top_topics = []
top_probs = []

for row in probs_full:
    row = np.array(row)  # assicurati che sia un array 1D
    idx = np.argsort(row)[::-1][:top_k]
    vals = row[idx]
    top_topics.append(idx.tolist())
    top_probs.append(vals.tolist())

print("✔ Top-k topic completata!")

# -------------------------------------------------------------------------
# 6) Ricavo le label testuali dei topic
# -------------------------------------------------------------------------

topic_info = topic_model.get_topic_info()  # contiene colonne: Topic, Count, Name
topic_label_map = dict(zip(topic_info["Topic"].tolist(), topic_info["Name"].tolist()))

# Etichette per i top-k topic
top_topic_labels = [
    [topic_label_map.get(t, "Outlier") for t in topic_list]
    for topic_list in top_topics
]

# Etichette del topic principale
topic_main_labels = [topic_label_map.get(t, "Outlier") for t in topics_main]

print("✔ Estrazione label testuali completata!")

# -------------------------------------------------------------------------
# 7) Creazione DataFrame finale
# -------------------------------------------------------------------------
df_topics = pd.DataFrame({
    "url": df["url"],
    "topic_main": topics_main,
    "topic_main_probability": [probs_full[i][topics_main[i]] for i in range(len(topics_main))],
    "topic_main_label": topic_main_labels,
    "top_topics": top_topics,
    "top_probabilities": top_probs,
    "top_topic_labels": top_topic_labels
})

print("✔ Creazione DataFrame finale completata!")

# -------------------------------------------------------------------------
# 8) Salvataggio su CSV
# -------------------------------------------------------------------------
df_topics.to_csv("papers_with_topics.csv", index=False)

print("✔ Estrazione topic completata!")
print("File salvato: papers_with_topics.csv")

# -------------------------------------------------------------------------
# 9) Salvataggio DEFINIZIONI TOPIC
# -------------------------------------------------------------------------
topic_info = topic_model.get_topic_info()  # contiene topic_id + parole chiave

topic_info.to_csv("topic_definitions.csv", index=False)

print("✔ File salvato: topic_definitions.csv")


# In[ ]:




