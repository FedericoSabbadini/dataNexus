

# IMPLEMENTAZIONE MAPREDUCE CON PYSPARK
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, FloatType
import time
import json


def main():
    # INIZIALIZZAZIONE SPARKSESSION (SparkContext creato auto)
    #   master("local[*]") usa tutti i core disponibili in locale
    spark = SparkSession.builder         .appName("PedaggioMedio_MapReduce")         .master("local[*]")         .config("spark.driver.memory", "2g")         .config("spark.log.level", "ERROR")         .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR") #toglie log ridondanti

    start_time = time.time()

    # CARICAMENTO DEI DATI
    # Schema del dataset
    schema = StructType([
        StructField("IDVeicolo", StringType(), True),
        StructField("TipoVeicolo", StringType(), True),
        StructField("Tratta", StringType(), True),
        StructField("Pedaggio", FloatType(), True),
        StructField("DataTransito", StringType(), True),
        StructField("FasciaOraria", StringType(), True),
        StructField("Provincia", StringType(), True)
    ])

    df = spark.read.csv(
        "caselli_autostradali.csv",
        header=True,
        schema=schema,
        sep=";"
    )

    # conversione dataFrame in RDD
    rdd = df.rdd


    # ========================================
    # IMPLEMENTAZIONE MAPREDUCE CON RDD
    # ========================================

    def extract_year(date_str):
        """Estrae l'anno da una data in formato GG/MM/YYYY"""
        try:
            return int(date_str.split("/")[-1])
        except:
            return None


    # MAP function
    # map() trasforma in rdd con le colonne: (TipoVeicolo, Pedaggio, Anno)
    # filter() trasforma in rdd con le righe con Anno 2015 o 2025
    # map() trasforma in rdd con le colonne: (TipoVeicolo_Anno, (Pedaggio, 1))
    mapped_rdd = rdd         .map(lambda row: (row["TipoVeicolo"], row["Pedaggio"], extract_year(row["DataTransito"])))         .filter(lambda x: x[2] in [2015, 2025])         .map(lambda x: (f"{x[0]}_{x[2]}", (x[1], 1)))

    # REDUCE function
    # reduceByKey() trasforma in rdd aggregando per chiave (TipoVeicolo_Anno) e sommando i valori ([0]=pedaggio, [1]=conteggio)
    #     include la funzione di combiner
    # mapValues() trasforma in rdd con le colonne: (TipoVeicolo_Anno, (media, conteggio))
    #     la media è calcolata dividendo la somma dei pedaggi per il conteggio
    reduced_rdd = mapped_rdd         .reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]))         .mapValues(lambda x: {"media": round(x[0] / x[1], 2), "transiti": x[1]})


    # Raccolta e stampa risultati (formato simile a mrjob, per omogeneità con le sezioni seguenti)
    risultati = reduced_rdd.collect()
    for chiave, valore in sorted(risultati):
        print(f'"{chiave}"	{json.dumps(valore)}')

    elapsed_time = time.time() - start_time
    print(f"Tempo di esecuzione: {elapsed_time:.2f} secondi", file=__import__('sys').stderr)

    spark.stop()

if __name__ == "__main__":
    main()
