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
| `ZONA_CLIMATICA` | Zona climatica assegnata al comune secondo la normativa italiana. Nel dataset sono presenti soprattutto le classi `E` e `F`: `E` indica comuni con fabbisogno di riscaldamento medio-alto, mentre `F` indica comuni con fabbisogno di riscaldamento molto alto e senza limiti ordinari al periodo di accensione degli impianti termici. |
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
| `CI_TIPO_IMPIANTO_1` | Tipologia del principale impianto di climatizzazione invernale. Indica la tecnologia usata per produrre calore, ad esempio generatore a combustione, pompa di calore, teleriscaldamento, generatore a biomassa o generatore ad effetto Joule. |
| `CI_ANNO_INSTALLAZIONE_1` | Anno di installazione del primo impianto di climatizzazione invernale. |
| `CI_VETTORE_ENERGETICO_1` | Vettore energetico utilizzato dal principale impianto di climatizzazione invernale. Indica la fonte di energia che alimenta l’impianto, ad esempio gas naturale, energia elettrica, GPL, gasolio, biomasse, teleriscaldamento o solare termico. |
| `CI_POTENZA_NOMINALE_1` | Potenza nominale del primo impianto di climatizzazione invernale. |
| `CI_EFFICIENZA_MEDIA` | Efficienza media del sistema di climatizzazione invernale. |
| `CLASSE_BUONA` | Colonna target. Vale `1` per edifici con classe energetica buona e `0` per edifici con classe energetica bassa. |

## Relazione tra tipo di impianto e vettore energetico

Le colonne `CI_TIPO_IMPIANTO_1` e `CI_VETTORE_ENERGETICO_1` descrivono il principale impianto di climatizzazione invernale dell’edificio.

La colonna `CI_TIPO_IMPIANTO_1` indica la tecnologia utilizzata per produrre calore, ad esempio generatore a combustione, pompa di calore, teleriscaldamento, generatore a biomassa o generatore ad effetto Joule.

La colonna `CI_VETTORE_ENERGETICO_1` indica invece la fonte energetica che alimenta l’impianto, ad esempio gas naturale, energia elettrica, GPL, gasolio, biomasse, teleriscaldamento o solare termico.

Queste due informazioni sono complementari: il tipo di impianto descrive **come** viene prodotto il calore, mentre il vettore energetico descrive **con quale energia** viene prodotto.

Ad esempio, un `Generatore a combustione` può essere alimentato da gas naturale, GPL, gasolio o altri combustibili. Allo stesso modo, l’`Energia elettrica` può alimentare una `Pompa di calore`, generalmente più efficiente, oppure un `Generatore ad effetto Joule`, che indica riscaldamento elettrico diretto.

Per questo motivo entrambe le colonne sono utili per il modello di classificazione: insieme permettono di rappresentare meglio il comportamento energetico dell’edificio e possono contribuire alla previsione della classe energetica.

## File principale del progetto

Il file principale del progetto si chiama:

`verifica27.ipynb`

Si tratta di uno Jupyter Notebook utilizzato per svolgere due attività principali:

1. analisi esplorativa dei dati;
2. addestramento e valutazione di modelli di machine learning per prevedere il raggruppamento della classe energetica.

Nel notebook viene utilizzato il dataset pulito `cened_milano_pulito.csv`, che contiene solo le colonne selezionate come utili per la classificazione.

## Divisione del dataset

Per costruire e valutare correttamente i modelli di machine learning, il dataset è stato diviso in due parti:

- `80%` dei dati per il training set;
- `20%` dei dati per il test set.

Il training set viene utilizzato per addestrare il modello, mentre il test set viene utilizzato per valutare le prestazioni del modello su dati non visti durante l’addestramento.

Questa suddivisione permette di verificare se il modello è in grado di generalizzare, cioè se riesce a fare previsioni corrette anche su nuovi edifici non utilizzati nella fase di training.

## Analisi delle colonne stringa

Dopo la divisione del dataset in training e test set, il lavoro prosegue con lo studio delle colonne di tipo stringa, cioè delle variabili categoriche presenti nel dataset.

Questa fase è importante perché molti algoritmi di machine learning non possono utilizzare direttamente valori testuali. Per questo motivo, le colonne categoriche devono essere analizzate, pulite e trasformate in variabili numeriche tramite tecniche di encoding.

Le colonne stringa individuate verranno analizzate per capire:

- quali valori unici contengono;
- se sono presenti valori mancanti;
- se alcune categorie sono troppo rare;
- se le categorie hanno una relazione logica con la classe energetica;
- quale tecnica di encoding applicare prima dell’addestramento del modello.

## Come usare il progetto

Installare le librerie necessarie:

```bash
pip install -r requirements.txt