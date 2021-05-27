# keras_project

Un semplice utilizzo:
1. video_extraction.py : l'esecuzione di questo script estrae dai video contenuti in una cartella un numero di frame (a seconda del numero di frequenza impostato nel file).
2. csv_create.py : il file genera un csv con i valori 0 o 1 per ogni frame.
3. classification.py : lo script crea due cartelle 0 e 1 e ne posiziona i frame del train set nella cartella giusta a seconda del valore 0 o 1 (no fake e fake).
4. random.py : lo script crea due cartelle 0 e 1 e ne posiziona i frame del test set in maniera casuale
5. Training.ipynb : creazione dataset, modello e applicazione del modello sui dati. 
