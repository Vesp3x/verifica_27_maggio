# Classe energetica degli edifici di Milano

## Descrizione del progetto

Questo progetto ha l’obiettivo di costruire un modello di classificazione in grado di prevedere la classe energetica degli edifici del Comune di Milano a partire da informazioni strutturali, impiantistiche e territoriali.

Il dataset originale contiene dati relativi agli Attestati di Prestazione Energetica degli edifici. Per rendere il problema più semplice e adatto a una classificazione binaria, le classi energetiche sono state raggruppate in due macro-categorie:

- `1` = classe energetica buona: A4, A3, A2, A1, B, C
- `0` = classe energetica bassa: D, E, F, G

La colonna target del dataset pulito si chiama `CLASSE_BUONA`.

## Obiettivo

L’obiettivo del modello è prevedere se un edificio appartiene a una classe energetica buona oppure bassa.

## Dataset

Il dataset utilizzato deriva dal database CENED relativo alla certificazione energetica degli edifici nel Comune di Milano.

Dal file originale sono state selezionate solo le colonne considerate utili per la predizione della classe energetica. Sono state escluse le colonne identificative, amministrative o troppo direttamente collegate al calcolo della classe energetica, per evitare che il modello riceva informazioni equivalenti alla risposta.

Il file pulito utilizzato nel progetto è:

`cened_milano_pulito.csv`

## Colonne del dataset

| Colonna | Descrizione |
|---|---|
| `RESIDENZIALE` | Indica se l’edificio o l’unità immobiliare ha destinazione d’uso residenziale. |
| `NON_RESIDENZIALE` | Indica se l’edificio o l’unità immobiliare ha destinazione d’uso non residenziale. |
| `CLASSIFICAZIONE_DPR` | Classificazione dell’edificio secondo le categorie previste dalla normativa DPR di riferimento. |
| `INTERO_EDIFICIO` | Indica se la certificazione riguarda l’intero edificio. |
| `UNITA_IMMOBILIARE` | Indica se la certificazione riguarda una singola unità immobiliare. |
| `NUMERO_UNITA_IMMOBILIARI` | Numero di unità immobiliari considerate nella certificazione. |
| `NUOVA_COSTRUZIONE` | Indica se l’edificio è una nuova costruzione. |
| `RISTRUTTURAZIONE_IMPORTANTE` | Indica se l’edificio è stato oggetto di una ristrutturazione importante. |
| `RIQUALIFICAZIONE_ENERGETICA` | Indica se l’edificio è stato oggetto di interventi di riqualificazione energetica. |
| `COMUNE` | Comune in cui si trova l’edificio. |
| `ZONA_CLIMATICA` | Zona climatica assegnata al comune secondo la normativa italiana. |
| `ANNO_COSTRUZIONE` | Anno di costruzione dell’edificio. |
| `SUPERF_UTILE_RISCALDATA` | Superficie utile riscaldata dell’edificio o dell’unità immobiliare. |
| `VOLUME_LORDO_RISCALDATO` | Volume lordo riscaldato dell’edificio o dell’unità immobiliare. |
| `SUPERFICIE_DISPERDENTE` | Superficie dell’involucro edilizio attraverso cui avvengono dispersioni termiche. |
| `RAPPORTO_SV` | Rapporto tra superficie disperdente e volume. Indica la compattezza dell’edificio. |
| `CLIMATIZZAZIONE_INVERNALE` | Indica la presenza del servizio di climatizzazione invernale, cioè riscaldamento. |
| `CLIMATIZZAZIONE_ESTIVA` | Indica la presenza del servizio di climatizzazione estiva, cioè raffrescamento. |
| `VENTILAZIONE_MECCANICA` | Indica la presenza di un sistema di ventilazione meccanica. |
| `PROD_ACQUA_CALDA_SANITARIA` | Indica la presenza di produzione di acqua calda sanitaria. |
| `VETTORE_ENERGETICO` | Fonte energetica principale utilizzata dall’edificio o dagli impianti. |
| `CI_TIPO_IMPIANTO_1` | Tipologia del primo impianto di climatizzazione invernale. |
| `CI_ANNO_INSTALLAZIONE_1` | Anno di installazione del primo impianto di climatizzazione invernale. |
| `CI_VETTORE_ENERGETICO_1` | Vettore energetico utilizzato dal primo impianto di climatizzazione invernale. |
| `CI_POTENZA_NOMINALE_1` | Potenza nominale del primo impianto di climatizzazione invernale. |
| `CI_EFFICIENZA_MEDIA` | Efficienza media del sistema di climatizzazione invernale. |
| `CLASSE_BUONA` | Colonna target. Vale `1` per edifici con classe energetica buona e `0` per edifici con classe energetica bassa. |

## Come usare il progetto

Installare le librerie necessarie:

```bash
pip install -r requirements.txt