# Classe energetica degli edifici di Milano

## Descrizione del progetto

Questo progetto ha l’obiettivo di costruire un modello di classificazione in grado di prevedere la classe energetica degli edifici del Comune di Milano a partire da informazioni strutturali, impiantistiche e territoriali.

Il dataset originale contiene dati relativi agli Attestati di Prestazione Energetica degli edifici. Per rendere il problema più semplice e adatto a una classificazione binaria, le classi energetiche sono state raggruppate in due macro-categorie:

- `1` = classe energetica buona: A4, A3, A2, A1, B, C
- `0` = classe energetica bassa: D, E, F, G

La colonna target del dataset pulito si chiama:

```python
CLASSE_BUONA