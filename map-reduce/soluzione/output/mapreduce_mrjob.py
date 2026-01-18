# STRUTTURA DI UN JOB MRJOB:
# La classe eredita da MRJob e definisce le fasi del processing:
from mrjob.job import MRJob

class PedaggioMedioMRJob(MRJob):
    """Calcola pedaggio medio per (TipoVeicolo, Anno) con Combiner."""

    def mapper(self, _, line): #  Riceve una riga del CSV alla volta
        if line.startswith("IDVeicolo"): 
            return
        try:
            parts = line.strip().split(";") # Estrae i campi (split sul delimitatore ';')
            tipo, pedaggio = parts[1], float(parts[3])
            anno = int(parts[4].split("/")[-1])
            if anno in [2015, 2025]:
                yield f"{tipo}_{anno}", {"sum": pedaggio, "count": 1} # media NON è associativa, quindi passiamo sum e count
                #  * chiave = "TipoVeicolo_Anno" (es. "Auto_2015")
                #  * valore = {"sum": pedaggio, "count": 1}
        except:
            pass


    def combiner(self, key, values):
        # Aggrega localmente somma e conteggio (media non associativa)
        s, c = 0, 0
        for v in values:
            s += v["sum"]
            c += v["count"]
        yield key, {"sum": s, "count": c}


    def reducer(self, key, values):
        s, c = 0, 0
        for v in values:
            s += v["sum"]
            c += v["count"]
        yield key, {"media": round(s/c, 2), "transiti": c} # Calcola la media finale: sum(pedaggi) / count(transiti)

if __name__ == "__main__":
    PedaggioMedioMRJob.run()
