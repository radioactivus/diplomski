```md
## Analiza finansijskog sentimenta (Financial Sentiment Analysis — FSA)

### 1. Uvod i definicija

Analiza finansijskog sentimenta (FSA) predstavlja primjenu tehnika obrade prirodnog jezika (NLP)
za automatsko određivanje emocionalnog tona i subjektivnog stava izraženog u finansijskim tekstovima
kao na primjer vijestima, izvještajima kompanija, objavama na društvenim mrežama, transkriptima
konferencijskih poziva (earning calls), regulatornim i analitičarskim izvještajima. Cilj FSA nije samo
klasifikacija teksta kao pozitivnog, negativnog ili neutralnog, već i kvantifikacija intenziteta sentimenta
i njegovo povezivanje s mjerljivim tržišnim ishodima tipa kretanjem cijena akcija, volatilnošću,
obimom trgovanja i prihodima (Du, Xing, Mao & Cambria, 2024).
FSA se razlikuje od opšte analize sentimenta po nekoliko ključnih karakteristika. Prvo, finansijski jezik
je visoko specijalizovan: riječi poput "liability" (obaveza), "default" (neispunjenje), "exposure"
(izloženost) ili "short" (kratka pozicija) imaju specifična značenja koja se razlikuju od svakodnevne upotrebe.
Drugo, kontekst je presudan, na primjer rečenica "Kompanija je smanjila gubitke za 30%" sadrži negativnu riječ
("gubitke"), ali je poruka pozitivna. Treće, finansijski tekstovi često kombinuju kvantitativne podatke
(brojeve, procente, valute) s kvalitativnim opisima, što zahtijeva modele sposobne za integrisanu obradu oba
tipa informacija. Četvrto, vremenski faktor je kritičan — sentiment iz vijesti objavljene u 14:01 može biti
irelevantan u 14:15 ako je tržište već reagovalo (Du et al., 2024).
Du et al. (2024) u svom pregledu objavljenom u ACM Computing Surveys predlažu konceptualni okvir koji razlikuje
tri povezana, ali različita nivoa sentimenta u finansijskom kontekstu:

- **Tekstualni sentiment** — ono što tekst eksplicitno ili implicitno izražava (domen NLP-a)
- **Sentiment investitora** — subjektivni stavovi i očekivanja pojedinačnih ili institucionalnih investitora
                              (domen bihevioralne finansije)
- **Tržišni sentiment** — agregatno raspoloženje tržišta koje se manifestuje kroz cijene, obime i volatilnost
                              (domen kvantitativnih finansija)

FSA se primarno bavi prvim nivoom — ekstrakcijom sentimenta iz teksta — ali njegova vrijednost leži u sposobnosti
da informiše pa i predvidi druga dva nivoa. Upravo ta veza čini FSA jednom od najaktivnijih istraživačkih oblasti
na presijeku NLP-a i finansija.

---

### 2. Evolucija tehnika — od rječnika do velikih jezičkih modela

#### 2.1 Leksikonski pristup (2004–2014)
Prve sistematske metode FSA oslanjale su se na **ručno kreirane rječnike** (leksikone) koji pripisuju sentiment
pojedinačnim riječima ili frazama. Ključni doprinos u ovom periodu dali su Loughran i McDonald (2011) koji su
demonstrirali da opšti rječnici sentimenta (poput Harvard General Inquirer) daju pogrešne rezultate na
finansijskim tekstovima. Njihov rad, objavljen u The Journal of Finance, analizirao je preko 50.000 godišnjih
izvještaja (10-K filingova) i pokazao da gotovo tri četvrtine riječi klasifikovanih kao "negativne" u opštim
rječnicima zapravo nemaju negativno značenje u finansijskom kontekstu. Na osnovu toga, kreirali su
specijalizovani finansijski leksikon koji i danas služi kao baseline za evaluaciju naprednijih metoda.
Prednosti leksikonskog pristupa su transparentnost i jednostavnost implementacije.
Nedostaci su fundamentalni: nemogućnost razumijevanja konteksta, negacija ("nije loše" se tretira kao negativno
zbog riječi "loše"), sarkazma i složenih sintaktičkih struktura. Leksikoni tretiraju svaku riječ izolovano,
ignorišući odnose među riječima u rečenici.

#### 2.2 Mašinsko učenje (2011–2018)
Primjena klasičnih ML algoritama (Naive Bayes, SVM, Random Forest, Logistička regresija) donijela je značajno
poboljšanje jer su ovi modeli sposobni da uče kombinacije riječi i kontekstualne obrasce iz označenih podataka,
umjesto da se oslanjaju na unaprijed definisane liste. Representacija teksta u ovom periodu zasnivala se na
bag-of-words (BoW) i TF-IDF vektorizaciji, te na Word2Vec i GloVe embeddingima koji su omogućili hvatanje
semantičke sličnosti između riječi. Ključno ograničenje bio je nedostatak označenih podataka u finansijskom domenu.
Dataset Financial PhraseBank (Malo et al., 2014), koji sadrži 4.846 ručno označenih rečenica iz finansijskih
vijesti, postao je de facto standard za evaluaciju — ali je istovremeno ilustrovao koliko je teško doći do
kvalitetnih označenih podataka u ovom domenu. Za poređenje, opšti sentiment dataseti poput IMDB filmskih recenzija
sadrže preko 50.000 primjera.

#### 2.3 Duboko učenje (2015–2019)
Uvođenje dubokih neuronskih mreža — prvo rekurentnih (RNN, LSTM, GRU), a zatim konvolucionih (CNN) — omogućilo
je automatsko učenje hijerarhijskih reprezentacija teksta. LSTM mreže su posebno doprinijele jer su sposobne
da "pamte" kontekst kroz duže sekvence teksta, što je ključno za finansijske rečenice koje su često dugačke
i sintaktički složene. Attention mehanizam, uveden u kontekstu mašinskog prevođenja (Bahdanau et al., 2015),
dodatno je poboljšao performanse jer omogućava modelu da se "fokusira" na najrelevantnije dijelove teksta prilikom
klasifikacije. Na primjer,u rečenici "Uprkos padu prihoda u trećem kvartalu, kompanija je značajno poboljšala
operativne marže", attention mehanizam može naučiti da je "poboljšala operativne marže" relevantniji dio za
određivanje sentimenta od "padu prihoda".

#### 2.4 Prethodno trenirani jezički modeli — FinBERT era (2018–2023)
Ključni prelomni trenutak za FSA bio je nastanak prethodno treniranih jezičkih modela (pre-trained language models),
posebno BERT-a (Devlin et al., 2018). Paradigma "pred-treniraj, pa fino podesi" (*pre-train, then fine-tune*)
fundamentalno je promijenila pristup: umjesto treniranja modela od nule na malom finansijskom datasetu,
polazi se od modela koji već posjeduje bogato jezičko znanje stečeno na milijardama riječi opšteg teksta, a zatim
se fino podešava na relativno maloj količini finansijski označenih podataka. Araci (2019) je uveo **FinBERT** —
varijantu BERT-a dodatno pred-treniranu na korpusu od 46.143 Rojtersovih finansijskih vijesti (29 miliona riječi).
FinBERT postiže state-of-the-art rezultate, nadmašujući sve prethodne metode uključujući LSTM, ULMFit i ELMo.
Ključni nalazi Aracijevog rada su:
- Dodatno pred-treniranje na finansijskom korpusu mjerljivo poboljšava rezultate u poređenju s originalnim BERT-om
  time potvrđujući hipotezu da domensko prilagođavanje jezičkog modela donosi konkretne koristi
- FinBERT postiže superiorne rezultate čak i s manjim skupom za treniranje i finim podešavanjem samo dijela modela
  (ne svih 12 slojeva) — čime se drastično smanjuju računarski zahtjevi
- Tehnika postepenog odmrzavanja slojeva (gradual unfreezing) pomaže u sprečavanju katastrofalnog zaboravljanja,
  problema gdje model pri učenju novog zadatka "zaboravlja" prethodno naučeno znanje
Du et al. (2024) u svom pregledu potvrđuju da BERT-based modeli i dalje drže najjače rezultate za zadatak sentiment
klasifikacije na nivou rečenice. Njihova tabela performansi pokazuje da fino podešeni BERT modeli (poput onih koje
koriste Zhao et al. i Liu et al.) dosežu tacnost od 94–97% na standardnim benchmark datasetima, rezultat koji
nijedna prethodna tehnika nije mogla postići.

#### 2.5 Veliki jezički modeli — LLM era (2023–danas)
Pojava velikih jezičkih modela (GPT-3/4, LLaMA, BloombergGPT) otvorila je novu dimenziju FSA. Za razliku od
BERT-baziranih modela koji su specijalizovani isključivo za klasifikaciju, LLM-ovi mogu obavljati sentiment analizu
u zero-shot ili few-shot režimu, odnosno bez ikakvog finog podešavanja, samo na osnovu instrukcije u prirodnom jeziku
("Klasifikuj sentiment sljedeće finansijske vijesti kao pozitivan, negativan ili neutralan"). Međutim, rezultati
LLM-ova za čistu sentiment klasifikaciju su iznenađujuće neujednačeni. Du et al. (2024) pokazuju da BloombergGPT,
model treniran na 363 milijarde tokena Bloombergovih podataka (closedsource, uz cijenu od 2,67 miliona dolara)
postiže samo 51,07% accuracy na Financial PhraseBank datasetu, što je gotovo na nivou nasumičnog pogađanja.
Razlog leži u tome što LLM-ovi nisu optimizovani za zadatak klasifikacije, već prvenstveno za generisanje teksta.
S druge strane, fino podešeni LLM-ovi poput FinGPT-a (Yang, Liu & Wang, 2023) postižu konkurentne rezultate:
F1 od 87,62% na PhraseBank-u i 95,80% na FiQA datasetu. FinGPT je treniran na LLaMA-2 arhitekturi koristeći LoRA
(Low-Rank Adaptation) tehniku finog podešavanja za svega $65 — u poređenju s $2,67M za BloombergGPT.
Ključna prednost LLM-ova nad BERT-baziranim modelima nije u čistoj sentiment klasifikaciji (gdje BERT i dalje
pobjeđuje), već u širini primjene: LLM-ovi mogu istovremeno raditi sentiment analizu, sumarizaciju, odgovaranje na
pitanja, generisanje izvještaja i analizu finansijskih tabela — sve unutar jednog modela.

---

### 3. Primjene FSA u finansijskom sektoru

Du et al. (2024) identifikuju četiri primarne downstream primjene FSA:
**Predikcija cijena akcija i prinosa:** Najistražavanija primjena — korištenje sentimenta iz vijesti, tvitova ili
osjecaja kao dodatnog izvora informacija u modelima za predviđanje kretanja cijena. Istraživanja konzistentno
pokazuju da dodavanje sentiment signala poboljšava predikcione modele u poređenju s modelima zasnovanim isključivo
na istorijskim cijenama i volumenu.
**Predviđanje volatilnosti:** Sentiment iz vijesti i društvenih mreža koristi se za predvidjanje buduće
volatilnosti, s praktičnom primjenom u upravljanju rizikom, opcijskom ocjenjivanju i alokaciji portfolija.
**Analiza earning callova:** Automatska analiza sentimenta transkripata konferencijskih poziva između menadžmenta
kompanija i analitičara. Ton kojim menadžment opisuje rezultate u korelaciji je s budućim performansama akcija.
**Detekcija tržišnih anomalija i manipulacija:** FSA se koristi za identifikaciju neobičnih obrazaca sentimenta
koji mogu ukazivati na tržišnu manipulaciju, pump-and-dump šeme ili koordinisane dezinformacione kampanje, posebno
relevantno na tržištima kriptovaluta, sto moze posluziti kao alat regulatornim tijelima.

---

### 4. Zaključak i budući pravci primjene AI za FSA

FSA je prešla put od jednostavnog brojanja pozitivnih i negativnih riječi do sofisticiranih modela sposobnih za
kontekstualno razumijevanje finansijskog jezika. Evolucija od leksikona (Loughran & McDonald, 2011) preko
specijalizovanih BERT modela do velikih jezičkih modela (FinGPT, BloombergGPT) odražava širi razvoj NLP-a,
ali s jednom važnom specifičnošću: u finansijama, preciznost i pouzdanost imaju prednost nad fleksibilnošću.
Zato FinBERT i dalje drži poziciju za produkcijske pipeline-ove koji zahtijevaju brze, deterministične i
ponovljive rezultate, dok LLM-ovi preuzimaju ulogu u eksplorativnim analizama, sumarizaciji i zadacima koji
zahtijevaju šire razumijevanje konteksta. Budući pravci razvoja FSA uključuju: multimodalne modele sposobne za
istovremenu analizu teksta, tabela i grafova iz finansijskih izvještaja; modele prilagođene za vise jezika
real-time FSA sisteme sposobne za obradu hiljada vijesti u sekundi s minimalnim kasnjenjem te integraciju FSA
s objašnjivim AI (XAI) tehnikama koje omogućavaju razumijevanje zašto je model donio određenu sentiment procjenu,
zahtjev koji postaje sve relevantniji u kontekstu EU AI Acta i rastuće regulatorne pažnje prema AI sistemima
generalno (Du et al., 2024; Du et al., 2025).

---

### Reference

- Araci, D. (2019). FinBERT: Financial Sentiment Analysis with Pre-trained Language Models.
  [https://arxiv.org/abs/1908.10063](https://arxiv.org/pdf/1908.10063)
- Du, K., Xing, F., Mao, R. & Cambria, E. (2024). Financial Sentiment Analysis: Techniques and Applications.
  https://dl.acm.org/doi/full/10.1145/3649451#core-tabbed-abstracts
- Du, K., Zhao, Y., Mao, R., Xing, F. & Cambria, E. (2025). Natural Language Processing in Finance: A Survey.
  [*Information Fusion*, 115, 102755.](https://ww.sentic.net/nlp-in-finance.pdf)
- Loughran, T. & McDonald, B. (2011). When Is a Liability Not a Liability?
  https://scholar.google.com/citations?view_op=view_citation&hl=en&user=FnFYSIQAAAAJ&citation_for_view=FnFYSIQAAAAJ:blknAaTinKkC
- Malo, P. et al. (2014). Good Debt or Bad Debt: Detecting Semantic Orientations in Economic Texts.
  https://arxiv.org/pdf/1307.5336
- Yang, H., Liu, X. Y. & Wang, C. D. (2023). FinGPT: Open-Source Financial Large Language Models.
  https://arxiv.org/pdf/2306.06031
```
