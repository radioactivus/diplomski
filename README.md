# Fine-tuning FinBERT modela za klasifikaciju sentimenta Ethereum vijesti

Projekat ispituje da li dodatna obuka finansijskog jezičkog modela FinBERT na vijestima povezanim sa Ethereumom poboljšava klasifikaciju tržišnog sentimenta.

Model klasifikuje vijesti u tri klase:

- `bullish` — pozitivan sentiment;
- `bearish` — negativan sentiment;
- `neutral` — neutralan sentiment.

## Struktura projekta

- `data/` — izvorni dataset, filtrirane vijesti i podijeljeni skupovi za obuku, validaciju i testiranje;
- `models/` — mjesto predviđeno za sačuvani fine-tuned model;
- `notebooks/` — notebook sa eksperimentom i evaluacijom modela;
- `scripts/` — pomoćne skripte za obradu podataka i izradu grafikona;

## Redoslijed skripti

Skripte se pokreću iz korijena ovog repozitorijuma, sljedećim redoslijedom:

1. `scripts/01_convert_to_csv.py`
2. `scripts/02_filter_ethereum_news.py`
3. `scripts/03_split_random.py`
4. `scripts/04_split_chronological.py`
5. `scripts/05_verify_splits.py`
6. `scripts/06_map_sentiment_labels.py`
7. `scripts/07_create_result_figures.py`

Skripte koriste relativne putanje, pa ih treba pokretati iz foldera `diplomski`.

## Preuzimanje modela

Dva najbolja modela su sacuvana i nalaze se na ovoj [`Google Cloud Storage lokaciji`](https://drive.google.com/file/d/1palVGtMGHHrUg7jdUY9K-uJG2CKGmFMz/view?usp=drive_link)

Nakon preuzimanja, zeljeni model treba smjestiti u folder `models/`.
