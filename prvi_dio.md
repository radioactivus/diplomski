# DIO I: SISTEMATIZACIJA UMJETNE INTELIGENCIJE

## Table of Contents

1. [Uvod](#1-uvod)
2. [Historijski razvoj umjetne inteligencije](#2-historijski-razvoj-umjetne-inteligencije)
3. [Taksonomija umjetne inteligencije](#3-taksonomija-umjetne-inteligencije)
4. [Generativna umjetna inteligencija — poseban osvrt](#4-generativna-umjetna-inteligencija-poseban-osvrt)
5. [Obrada prirodnog jezika (NLP)](#5-obrada-prirodnog-jezika-nlp)
6. [Robotska automatizacija procesa (RPA)](#6-robotska-automatizacija-procesa-rpa)
7. [Kompjuterski vid (Computer Vision)](#7-kompjuterski-vid-computer-vision)
8. [Sistemi za podršku odlučivanju i prediktivna analitika](#8-sistemi-za-podršku-odlučivanju-i-prediktivna-analitika)
9. [Etička pitanja i objašnjivi AI (XAI)](#9-etička-pitanja-i-objašnjivi-ai-xai)
10. [Paradoks produktivnosti i trenutno stanje](#10-paradoks-produktivnosti-i-trenutno-stanje)
11. [Zaključak prvog dijela](#11-zaključak-prvog-dijela)
12. [Reference](#reference)



## 1. Uvod

Umjetna inteligencija (AI — Artificial Intelligence) predstavlja jednu od najznačajnijih tehnoloških paradigmi savremenog doba. Od svojih konceptualnih početaka sredinom 20. vijeka, AI je prošao kroz periode intenzivnog optimizma, razočarenja (tzv. "AI zime"), te eksponencijalnog rasta koji danas oblikuje gotovo svaki segment privrede i društva. Procjenjuje se da će globalna potrošnja na AI tehnologije dostići 97 milijardi dolara do 2027. godine, uz složenu godišnju stopu rasta (CAGR) od 29,6%, čime finansijski sektor postaje najbrže rastuća industrija u pogledu AI investicija (Kearns, 2023; La Croce, 2023).

Međutim, unatoč enormnim ulaganjima, istraživanja pokazuju značajan jaz između percepcije i mjerljivog uticaja AI na produktivnost. Izvještaj Opagio (2026) navodi da je u 2025. godini globalno utrošeno 2,6 biliona dolara na AI, dok 90% firmi izvještava o nultom mjerljivom uticaju — fenomen koji podsjeća na Solowljev paradoks produktivnosti iz 1987. godine vezan za kompjutersku revoluciju. Samo 29% rukovodilaca može kvantificirati povrat na investiciju u AI (Opagio, 2026). Istovremeno, McKinsey procjenjuje potencijalni godišnji ekonomski uticaj AI na 2,6–4,4 biliona dolara, ali napominje da samo 1% organizacija smatra svoju AI implementaciju "zrelom".

Ovo poglavlje ima za cilj sistematizovati oblast umjetne inteligencije kroz višedimenzionalnu taksonomiju — klasifikujući AI prema sposobnostima, funkcionalnosti, tehnikama, namjeni i načinu implementacije. Cilj je pružiti strukturirani okvir koji će čitaocu omogućiti razumijevanje raznovrsnosti AI sistema prije nego što se u drugom dijelu rada fokusiramo na specifične primjene u finansijskom sektoru.

Rad se primarno oslanja na taksonomiju koju je predložio Dutta (2025) u radu "Taxonomy of Artificial Intelligence", te na dodatne izvore uključujući Vuković, Dekpo-Adza i Matović (2025), Russell i Norvig (2021), te Goodfellow, Bengio i Courville (2016).

## 2. Historijski razvoj umjetne inteligencije

### 2.1 Začeci: Od Turinga do Dartmoutha (1936–1956)

Teorijske osnove AI postavio je Alan Turing 1936. godine konceptom Turingove mašine — apstraktnog matematičkog modela koji je definisao granice izračunljivosti. Godine 1950. Turing je objavio seminalni rad "Computing Machinery and Intelligence" u kojem je formulisao pitanje "Mogu li mašine misliti?" i predložio tzv. Turingov test (igru imitacije) kao kriterij za procjenu inteligencije mašina (Turing, 1950).

Termin "Artificial Intelligence" formalno je skovan na Dartmouth konferenciji 1956. godine, koju su organizovali John McCarthy, Marvin Minsky, Nathaniel Rochester i Claude Shannon. Ova konferencija se smatra osnivačkim događajem discipline AI, i na njoj je postavljena ambiciozna premisa: "svaki aspekt učenja ili bilo koja druga osobina inteligencije može u principu biti toliko precizno opisana da se može napraviti mašina koja je simulira" (McCarthy et al., 1955).

### 2.2 Rani entuzijazam i simbolički AI (1956–1974)

Period nakon Dartmoutha obilježen je velikim optimizmom. Istraživači su razvijali programe za dokazivanje teorema (Logic Theorist, 1956), rješavanje problema opšte namjene (General Problem Solver, 1957), te rane sisteme za obradu prirodnog jezika (ELIZA, 1966). Dominantan pristup bio je simbolički AI — zasnovan na formalnoj logici, pravilima i manipulaciji simbolima. Minsky i Papert su u ovom periodu postigli značajne rezultate u oblasti perceptrona, ali su istovremeno u svojoj knjizi Perceptrons (1969) ukazali na fundamentalna ograničenja jednoslojnih neuronskih mreža, čime su usporili istraživanja u tom pravcu na gotovo dva desetljeća.

### 2.3 Prva AI zima (1974–1980)

Nerealistična očekivanja iz prethodnog perioda dovela su do razočarenja. Lighthill izvještaj (1973) za britansku vladu zaključio je da AI nije ispunio obećanja, što je rezultiralo drastičnim smanjenjem finansiranja. Simbolički pristup pokazao se neefikasnim za složene probleme realnog svijeta — sistemi su bili krhki, nesposobni za generalizaciju, i zahtijevali su enormne količine ručno kodiranog znanja.

### 2.4 Ekspertni sistemi i drugi talas (1980–1987)

Osamdesetih godina AI je doživio renesansu kroz ekspertne sisteme — programe koji su kodificirali znanje stručnjaka iz uskih domena u formi IF-THEN pravila. Sistem MYCIN (medicinska dijagnostika), R1/XCON (konfiguracija računara za DEC), i DENDRAL (hemijska analiza) demonstrirali su komercijalnu vrijednost AI. Japanski projekt "Peta generacija" (1982) pokrenuo je globalnu trku u AI istraživanjima. Industrija ekspertnih sistema dostigla je tržišnu vrijednost od preko milijardu dolara sredinom 1980-ih.

### 2.5 Druga AI zima (1987–1993)

Kolaps tržišta specijalizovanih LISP mašina i ograničenja ekspertnih sistema (skupo održavanje, nemogućnost učenja, krhkost pri promjenama u domeni) doveli su do druge AI zime. Mnoge kompanije koje su se oslanjale na AI tehnologije bankrotirale su, a termin "umjetna inteligencija" postao je gotovo tabu u poslovnom svijetu.

### 2.6 Statistički pristup i mašinsko učenje (1993–2011)

Devedesete godine donijele su fundamentalni zaokret: od simboličkog pristupa ka statističkim metodama i mašinskom učenju. Ključni momenti uključuju:

- 1997 — IBM-ov Deep Blue poražava svjetskog šampiona u šahu Garija Kasparova
- 1998 — Yann LeCun razvija konvolucione neuronske mreže (CNN) za prepoznavanje rukopisa
- 2006 — Geoffrey Hinton demonstrira efikasan trening dubokih neuronskih mreža (deep belief networks), čime efektivno pokreće revoluciju dubinskog učenja
- 2011 — IBM Watson pobjeđuje ljudske šampione u kvizu Jeopardy!

Ovaj period karakteriše pomak od ručno kodiranih pravila ka algoritmima koji uče iz podataka, uz rastuću dostupnost digitalnih podataka i povećanje računarske moći.

### 2.7 Dubinsko učenje i moderna era (2012–danas)

Moderna era AI počinje 2012. godine kada je AlexNet — duboka konvoluciona neuronska mreža — ostvarila dramatičnu pobjedu na ImageNet takmičenju u klasifikaciji slika, smanjivši stopu greške za gotovo 50% u odnosu na prethodne metode (Krizhevsky, Sutskever & Hinton, 2012). Od tog trenutka, dubinsko učenje postaje dominantna paradigma.

Ključni događaji koji su uslijedili:

- 2014 — Generativne suparničke mreže (GAN) — Ian Goodfellow
- 2016 — AlphaGo poražava svjetskog šampiona u igri Go
- 2017 — Transformer arhitektura ("Attention Is All You Need", Vaswani et al.) — revolucionarna arhitektura koja postaje osnov za moderne jezičke modele
- 2018 — BERT (Google) — bidirekcioni transformer za razumijevanje jezika
- 2020 — GPT-3 (OpenAI) — 175 milijardi parametara, demonstrira sposobnost generisanja teksta na nivou blizu ljudskog
- 2022 — ChatGPT demokratizuje pristup AI za široku javnost; DALL-E 2 i Stable Diffusion za generisanje slika
- 2023 — GPT-4, multimodalni modeli, eksplozija generativnog AI
- 2024–2025 — Era AI agenata, specijalizovani industrijski modeli, DeepSeek, Anthropic Claude, otvoreni modeli (LLaMA, Mistral)

Ova era je definisana eksponencijalnim rastom skale modela, količine podataka za trening, i računarskih resursa — fenomenom koji se često opisuje tzv. "zakonima skaliranja" (scaling laws).

## 3. Taksonomija umjetne inteligencije

Sistematizacija AI sistema zahtijeva višedimenzionalni pristup, s obzirom na raznovrsnost tehnika, primjena i sposobnosti koje ovi sistemi demonstriraju. Dutta (2025) predlaže sveobuhvatnu taksonomiju koja klasifikuje AI duž pet ključnih dimenzija: prema sposobnostima, prema funkcionalnosti, prema tehnikama, prema namjeni i prema načinu implementacije.

### 3.1 Klasifikacija prema sposobnostima (Capability)

Ova klasifikacija odražava stepen opštosti i autonomije AI sistema i predstavlja najšire prihvaćenu podjelu u akademskoj literaturi.

### 3.1.1 Uska umjetna inteligencija (ANI — Artificial Narrow Intelligence)

ANI, poznata i kao "slaba AI", predstavlja sisteme dizajnirane za obavljanje jednog specifičnog zadatka ili uskog skupa povezanih zadataka. Svi današnji operativni AI sistemi spadaju u ovu kategoriju, bez obzira na njihovu impresivnu performansu u datoj domeni.

Karakteristike:

- Specijalizacija za definisani zadatak
- Nemogućnost transfera znanja izvan domene treninga
- Visoka performansa unutar uskog opsega, ali potpuna nesposobnost izvan njega
- Odsustvo svijesti, razumijevanja ili generalne inteligencije

Primjeri:

- Sistemi za prepoznavanje govora (Siri, Alexa, Google Assistant)
- Preporuke sadržaja (Netflix, Spotify, YouTube algoritmi)
- Spam filteri za email
- Autonomna navigacija vozila (u specifičnim uvjetima)
- AlphaGo, AlphaFold (predviđanje strukture proteina)
- ChatGPT, GPT-4, Claude (generisanje teksta — uprkos impresivnim sposobnostima, i dalje ANI)

Važno je naglasiti da čak i najnapredniji veliki jezički modeli (LLM) poput GPT-4 ili Claude-a spadaju u ANI kategoriju. Iako demonstriraju zapanjujuću fleksibilnost u radu s jezikom, oni nemaju istinsko razumijevanje, svijest o sebi, niti sposobnost autonomnog postavljanja ciljeva izvan svog dizajna.

### 3.1.2 Opšta umjetna inteligencija (AGI — Artificial General Intelligence)

AGI, ili "jaka AI", odnosi se na hipotetski sistem koji bi posjedovao kognitivne sposobnosti na nivou ljudske inteligencije — sposobnost učenja, razumijevanja, zaključivanja i primjene znanja u bilo kojoj domeni, uključujući i one s kojima se ranije nije susretao.

Karakteristike:

- Sposobnost transfera znanja između domena
- Apstraktno rezonovanje i planiranje
- Razumijevanje konteksta i kauzalnosti
- Adaptacija na potpuno nove situacije bez ponovnog treniranja
- Potencijalno: samosvijest i autonomno postavljanje ciljeva

AGI ostaje teorijski koncept i predmet intenzivne debate u naučnoj zajednici. Procjene o vremenu do realizacije AGI variraju dramatično — od optimističnih prognoza od 5–10 godina (npr. Sam Altman, CEO OpenAI) do skeptičnih stavova da AGI možda nikada neće biti ostvaren u formi kako ga danas zamišljamo (npr. Gary Marcus). Ključni izazovi uključuju: problem utemeljenja (grounding), zdravorazumsko zaključivanje, kontinuirano učenje bez katastrofalnog zaboravljanja, te fundamentalna pitanja o prirodi inteligencije i svijesti.

### 3.1.3 Superinteligencija (ASI — Artificial Super Intelligence)

ASI predstavlja hipotetski sistem koji bi nadmašio ljudsku inteligenciju u svim domenama — od naučnog istraživanja i kreativnog stvaralaštva do socijalne inteligencije i strateškog planiranja. Koncept je popularizovao Nick Bostrom u knjizi Superintelligence: Paths, Dangers, Strategies (2014).

Potencijalne karakteristike:

- Superiornija analitička, kreativna i socijalna inteligencija od bilo kojeg čovjeka
- Sposobnost samo-unapređenja (recursive self-improvement)
- Mogućnost rješavanja problema koji su za ljude fundamentalno nerazrješivi

ASI ostaje u domeni spekulativne teorije i filozofije, ali postavlja kritična etička i egzistencijalna pitanja. Koncept "eksplozije inteligencije" (intelligence explosion), koji je prvi opisao matematičar I.J. Good 1965. godine, sugeriše da bi dovoljno inteligentna mašina mogla dizajnirati još inteligentnije mašine, pokrećući lanac samo-unapređenja s nepredvidivim ishodima.

---

## 3.2 Klasifikacija prema funkcionalnosti

Ova dimenzija, zasnovana na radu Arend Hintzea (2016), klasifikuje AI sisteme prema sofisticiranosti njihove interne reprezentacije svijeta i sposobnosti korištenja memorije.

### 3.2.1 Reaktivne mašine (Reactive Machines)

Najjednostavniji tip AI sistema koji reaguje isključivo na trenutni ulaz, bez ikakve memorije ili modela svijeta. Ovi sistemi ne mogu koristiti prošla iskustva za informisanje budućih odluka.

- Primjer: IBM Deep Blue — evaluira šahovske pozicije u realnom vremenu, ali ne "pamti" prethodne partije i ne uči iz iskustva
- Karakteristika: deterministički odgovor na dati ulaz; nema koncepta prošlosti ili budućnosti

### 3.2.2 Mašine s ograničenom memorijom (Limited Memory)

Sistemi koji mogu privremeno pohranjivati i koristiti prošla iskustva za informisanje trenutnih odluka. Većina modernih AI sistema, uključujući duboke neuronske mreže, spada u ovu kategoriju.

- Primjeri: Autonomna vozila (koriste podatke sa senzora iz nedavne prošlosti za predikciju kretanja), ChatGPT (održava kontekst unutar konverzacije), sistemi za preporuku
- Karakteristika: privremena, ograničena memorija koja ne postaje permanentni dio modela učenja

### 3.2.3 Teorija uma (Theory of Mind)

Hipotetski AI sistemi sposobni za razumijevanje mentalnih stanja drugih agenata — njihovih uvjerenja, namjera, emocija i znanja. U kognitivnoj psihologiji, "teorija uma" je sposobnost pripisivanja mentalnih stanja drugima, koja se kod djece razvija oko četvrte godine.

- Status: Aktivno istraživačko područje; rani eksperimenti s LLM-ovima pokazuju rudimentarne aspekte ovog kapaciteta (npr. sposobnost razumijevanja sarkazma, perspektive drugog govornika), ali pravi Theory of Mind AI ne postoji
- Značaj: Ključan za razvoj AI sistema koji mogu istinski surađivati s ljudima u kompleksnim socijalnim kontekstima

### 3.2.4 Samosvjesni AI (Self-Aware AI)

Čisto teorijski koncept AI sistema koji posjeduje svijest o sebi, subjektivna iskustva i razumijevanje vlastitog postojanja. Ovaj tip AI je u domeni filozofske spekulacije i povezan je s "teškim problemom svijesti" (hard problem of consciousness) — pitanjem koje nije riješeno ni za biološke sisteme.

## 3.3 Klasifikacija prema tehnikama

Ova dimenzija klasifikuje AI prema metodološkom pristupu koji sistem koristi za postizanje inteligentnog ponašanja. Predstavlja najrelevantniju klasifikaciju za praktičnu primjenu i razumijevanje tehničkih mogućnosti i ograničenja pojedinih AI sistema.

### 3.3.1 Simbolički AI (Rule-based / Knowledge-driven AI)

Simbolički AI, poznat i kao "Good Old-Fashioned AI" (GOFAI), zasniva se na eksplicitnoj reprezentaciji znanja kroz simbole, pravila i logičke strukture. Sistemi manipulišu simbolima prema formalno definisanim pravilima.

Ključne tehnike:

- Ekspertni sistemi (baze znanja + inferencijalni mehanizmi)
- Logičko programiranje (Prolog)
- Ontologije i semantičke mreže
- Pretraživanje stabla odlučivanja

Prednosti: Transparentnost i objašnjivost odluka; moguća formalna verifikacija; efikasnost s malim količinama podataka u strukturisanim domenama.

Ograničenja: Zahtijeva ručno kodiranje znanja; krhkost pri promjenama; nesposobnost za rad s nestrukturiranim podacima; eksponencijalni rast kompleksnosti ("prokletstvo dimenzionalnosti").

Relevantnost danas: I danas se koristi u regulatornim sistemima (compliance), medicinskoj dijagnostici (klinički vodiči), i kao komponenta hibridnih AI sistema (neurosimbolički AI).

### 3.3.2 Mašinsko učenje (Machine Learning — ML)

Mašinsko učenje predstavlja granu AI u kojoj sistemi uče iz podataka bez eksplicitnog programiranja pravila. Umjesto da programer definiše pravila, algoritam sam otkriva obrasce u podacima (Mitchell, 1997; Russell & Norvig, 2021).

ML se dalje dijeli prema paradigmi učenja:

a) Nadgledano učenje (Supervised Learning)

Model uči iz označenih podataka — parova ulaz-izlaz — i generalizuje na nove, neviđene ulaze.

Algoritmi: Linearna/logistička regresija, stabla odlučivanja, Random Forest, Support Vector Machines (SVM), k-Nearest Neighbors (k-NN), Naive Bayes, Gradient Boosting (XGBoost, LightGBM)

Primjene: Klasifikacija (spam detekcija, kreditni scoring, dijagnoza bolesti), regresija (predviđanje cijena, prognoza potražnje)

Zahtjev: Velike količine kvalitetno označenih podataka

b) Nenadgledano učenje (Unsupervised Learning)

Model otkriva skrivene strukture u podacima bez unaprijed definisanih oznaka.

Algoritmi: K-means klasterovanje, hijerarhijsko klasterovanje, DBSCAN, analiza glavnih komponenti (PCA), t-SNE, autoencoderi

Primjene: Segmentacija korisnika, detekcija anomalija (fraud detection), redukcija dimenzionalnosti, otkrivanje tema u tekstu

Prednost: Ne zahtijeva označene podatke, što je značajna prednost s obzirom na to da je označavanje podataka skupo i vremenski zahtjevno

c) Učenje s potkrepljenjem (Reinforcement Learning — RL)

Agent uči kroz interakciju s okruženjem — primajući nagrade ili kazne za svoje akcije, s ciljem maksimiziranja kumulativne nagrade tokom vremena.

Ključni koncepti: Agent, okruženje, stanje, akcija, nagrada, politika (policy), Q-funkcija

Algoritmi: Q-Learning, Deep Q-Networks (DQN), Policy Gradient, Proximal Policy Optimization (PPO), Actor-Critic metode

Primjene: Igre (AlphaGo, Atari), robotika, upravljanje resursima, optimizacija portfolija u finansijama, autonomna vožnja

Izazovi: Sporo učenje, potreba za mnogo interakcija, problem balansa eksploatacije i eksploracij

d) Polu-nadgledano učenje (Semi-supervised Learning)

Kombinuje malu količinu označenih podataka s velikom količinom neoznačenih, što je praktično relevantno jer je u realnom svijetu označavanje podataka skupo.

e) Samo-nadgledano učenje (Self-supervised Learning)

Model generiše vlastite nadzorne signale iz neoznačenih podataka — npr. predviđanje maskiranog dijela teksta (BERT) ili sljedećeg tokena (GPT). Ova paradigma je osnov treniranja modernih velikih jezičkih modela i predstavlja jedno od najznačajnijih metodoloških pomaka u posljednjoj deceniji.

### 3.3.3 Dubinsko učenje (Deep Learning — DL)

Dubinsko učenje je podskup mašinskog učenja zasnovan na dubokim neuronskim mrežama — mrežama s velikim brojem slojeva (layers) koji omogućavaju učenje hijerarhijskih reprezentacija podataka. Svaki sloj transformiše podatke na sve apstraktnijem nivou (Goodfellow, Bengio & Courville, 2016).

Ključne arhitekture:

| Arhitektura | Opis | Primarna primjena |
|---|---|---|
| Feedforward NN (FNN) | Osnovne mreže s prolazom informacije naprijed | Klasifikacija, regresija |
| Konvolucione mreže (CNN) | Specijalizovane za prostorno strukturirane podatke; koriste konvolucione filtere | Prepoznavanje slika, video analiza, medicinska dijagnostika |
| Rekurentne mreže (RNN) | Obrađuju sekvencijalne podatke; imaju "memoriju" prethodnih ulaza | Obrada teksta, vremenski nizovi |
| LSTM / GRU | Napredne RNN varijante koje rješavaju problem nestajućih gradijenata | Prepoznavanje govora, mašinsko prevođenje, predviđanje cijena akcija |
| Transformer | Arhitektura zasnovana na mehanizmu pažnje (attention); paralelna obrada | NLP, generativni AI, multimodalni modeli |
| GAN (Generative Adversarial Networks) | Dvije mreže (generator i diskriminator) u kompetitivnom treningu | Generisanje slika, video, augmentacija podataka |
| Autoencoder / VAE | Mreže za učenje kompresovanih reprezentacija | Redukcija dimenzionalnosti, detekcija anomalija, generisanje podataka |
| Difuzioni modeli | Generativni modeli zasnovani na postepenom dodavanju i uklanjanju šuma | Generisanje slika (DALL-E, Stable Diffusion, Midjourney) |
| Graph Neural Networks (GNN) | Mreže za rad s grafovskim strukturama | Socijalne mreže, molekularna hemija, mreže transakcija |

Dubinsko učenje u praksi — zahtjevi i izazovi:

- Zahtijeva velike količine podataka za trening
- Računarski izuzetno intenzivno (GPU/TPU klasteri)
- Problem "crne kutije" — odluke su teško objašnjive
- Sklonost pristranosti (bias) prisutnoj u podacima za trening
- Katastrofalno zaboravljanje pri učenju novih zadataka

### 3.3.4 Evolutivni algoritmi

Inspirisani biološkom evolucijom, ovi algoritmi koriste mehanizme selekcije, mutacije i rekombinacije za optimizaciju rješenja.

Tipovi: Genetski algoritmi (GA), genetsko programiranje, evolucione strategije, diferencijalna evolucija

Primjene: Optimizacija dizajna, rasporeda, hiperparametara neuronskih mreža, razvoj strategija trgovanja

Prednost: Efikasni za probleme s velikim, diskontinuiranim prostorima pretraživanja

### 3.3.5 Hibridni pristup (Neurosimbolički AI)

Sve značajniji pravac koji kombinuje snagu neuronskih mreža (učenje iz podataka, rad s nestrukturiranim ulazima) sa transparentnošću simboličkog AI (logičko zaključivanje, objašnjivost). Smatra se jednim od najperspektivnijih puteva ka robusnijim i pouzdanijim AI sistemima.

Primjeri: Sistemi koji koriste LLM za razumijevanje upita i simbolički solver za egzaktan odgovor; neurosimbolički pristupi u medicinskoj dijagnostici

Značaj za finansije: Posebno relevantan u regulisanim industrijama gdje je objašnjivost odluka zakonski zahtjev

### 3.4 Klasifikacija prema namjeni (Purpose)

### 3.4.1 Asistivni AI (Augmentivni)

Sistemi dizajnirani da pojačaju ljudske sposobnosti — pomažu ljudima da rade brže, preciznije ili da donose bolje odluke, ali konačnu odluku i dalje donosi čovjek.

Primjeri: Alati za pomoć u pisanju (Grammarly, GitHub Copilot), sistemi za podršku odlučivanju u medicini, dashboard-i za vizualizaciju analitike

Filozofija: Čovjek u petlji (human-in-the-loop); AI kao alat, ne zamjena

Istraživanje Dell'Acqua, Mollick i Kellogg et al. (2023), provedeno na 700+ BCG konsultanata, pokazalo je da korištenje AI alata kao asistivne tehnologije dovodi do +40% poboljšanja performansi za zadatke unutar AI-jeve "granice sposobnosti" (capability frontier), ali −19% za zadatke izvan nje — demonstrirajući kritičnu važnost razumijevanja granica asistivnog AI.

### 3.4.2 Autonomni AI

Sistemi sposobni za nezavisno djelovanje bez kontinuirane ljudske supervizije — samostalno percipiraju okruženje, donose odluke i izvršavaju akcije.

Primjeri: Autonomna vozila (Level 4–5), autonomni dronovi, algoritamsko trgovanje bez ljudske intervencije, autonomni robotski sistemi u logistici

Izazovi: Sigurnost, odgovornost u slučaju grešaka, etička pitanja, regulatorna kompleksnost, povjerenje korisnika

Razlika između asistivnog i autonomnog AI nije binarna već predstavlja spektar autonomije — od potpuno ljudski kontrolisanih sistema, preko sistema s različitim stupnjevima ljudskog nadzora, do potpuno autonomnih sistema

### 3.5 Klasifikacija prema načinu implementacije (Deployment)

### 3.5.1 Cloud AI

AI sistemi koji se izvršavaju na udaljenim serverima u cloud infrastrukturi (AWS, Azure, Google Cloud). Korisnici pristupaju putem API-ja ili web interfejsa.

Prednosti: Pristup enormnim računarskim resursima bez kapitalnih ulaganja; skalabilnost; pristup najnovijim modelima

Nedostaci: Zavisnost od internet konekcije; pitanja privatnosti podataka; latencija; tekući operativni troškovi

Primjeri: OpenAI API (GPT-4), Google Cloud AI, Amazon SageMaker

### 3.5.2 Edge AI

AI obrada koja se vrši lokalno na uređaju (smartphone, IoT senzor, kamera, automobil), bez slanja podataka u cloud.

Prednosti: Niska latencija (kritično za autonomna vozila, industrijsku automatizaciju); rad bez internet konekcije; privatnost podataka (podaci ne napuštaju uređaj)

Nedostaci: Ograničeni računarski resursi; potreba za optimizacijom modela (kvantizacija, pruning, destilacija znanja)

Primjeri: Face ID na iPhone-u, pametne kamere za nadzor, prediktivno održavanje u tvornicama

### 3.5.3 Ugrađeni AI (Embedded AI)

AI integrisan direktno u hardver i firmver uređaja — dizajniran za specifičnu namjenu s minimalnim resursima.

Primjeri: AI čipovi u automobilima (NVIDIA Drive), pametni termostati, medicinski uređaji za monitoring

Razlika od Edge AI: Dok Edge AI može pokretati opšte modele lokalno, Embedded AI je tipično specijalizovan za jedan zadatak i duboko integrisan u hardversku platformu


## Napomena
Ovaj fajl je generisan kao *sigurna kopija* u slučaju da postoje razlike u postojećem `dio_1_sistematizacija_AI.md`. Nastavak (poglavlja 3.2 do 11) će se dodati identično kao u `.txt` u sljedećim iteracijama.
## 4. Generativna umjetna inteligencija — poseban osvrt

S obzirom na transformativni uticaj generativnog AI-ja na savremeno društvo i ekonomiju, ovo poglavlje pruža detaljniji pregled ove kategorije AI sistema.

### 4.1 Definicija i principi

Generativni AI obuhvata sisteme sposobne za kreiranje novog sadržaja — teksta, slika, zvuka, videa, programskog koda, 3D modela — koji nije prost kopija podataka za trening, već nova kreacija bazirana na naučenim obrascima. Za razliku od diskriminativnih modela (koji klasificiraju ili predviđaju), generativni modeli uče distribuciju podataka i mogu generisati nove uzorke iz te distribucije.

### 4.2 Transformer arhitektura — temelj modernog generativnog AI

Transformer, uveden u radu "Attention Is All You Need" (Vaswani et al., 2017), revolucionirao je oblast obrade prirodnog jezika i postao osnov za gotovo sve moderne generativne modele. Ključne inovacije:

- Mehanizam samo-pažnje (Self-Attention): Omogućava modelu da istovremeno "obrati pažnju" na sve dijelove ulazne sekvence, umjesto sekvencijalne obrade kao kod RNN. Ovo omogućava hvatanje dugoročnih zavisnosti i masivnu paralelizaciju treninga.
- Poziciono kodiranje (Positional Encoding): Budući da transformer nema inherentan koncept redoslijeda, poziciono kodiranje dodaje informaciju o poziciji svakog tokena u sekvenci.
- Encoder-Decoder struktura: Originalni transformer koristi encoder (za razumijevanje ulaza) i decoder (za generisanje izlaza). Moderni modeli koriste varijante: samo-decoder (GPT serija), samo-encoder (BERT), ili encoder-decoder (T5, BART).

### 4.3 Veliki jezički modeli (LLM — Large Language Models)

LLM-ovi su transformer modeli trenirani na enormnim korpusima teksta (stotine milijardi do biliona tokena) s ciljem predviđanja sljedećeg tokena u sekvenci. Ova naizgled jednostavna zadaća — predviđanje sljedećeg tokena — rezultira emergentnim sposobnostima koje se pojavljuju s rastom skale modela.

Ključni modeli i njihove karakteristike:

| Model | Organizacija | Parametri | Ključna inovacija |
|---|---|---|---|
| GPT-3 (2020) | OpenAI | 175B | Demonstracija few-shot učenja |
| PaLM (2022) | Google | 540B | Poboljšano zaključivanje |
| GPT-4 (2023) | OpenAI | ~1.8T (proc.) | Multimodalnost (tekst + slika) |
| LLaMA 2/3 (2023–24) | Meta | 7B–405B | Otvoreni modeli visoke kvalitete |
| Claude 3/3.5 (2024) | Anthropic | N/A | Fokus na sigurnost i duge kontekste |
| Gemini (2024) | Google | N/A | Nativna multimodalnost |
| DeepSeek-V2/V3 (2024–25) | DeepSeek | 236B MoE | Efikasna MoE arhitektura, otvoreni |
| Mistral/Mixtral (2024) | Mistral AI | 7B–141B | Evropski otvoreni modeli |

Emergentne sposobnosti: S rastom skale, LLM-ovi demonstriraju sposobnosti koje nisu eksplicitno trenirane — lančano zaključivanje (chain-of-thought reasoning), programiranje, matematičko rezonovanje, translacija, sumiranje — fenomen koji ostaje predmet aktivne naučne debate.

RLHF (Reinforcement Learning from Human Feedback): Tehnika usklađivanja (alignment) koja koristi ljudske evaluatore za fino podešavanje modela, čineći ih korisnijim, bezbjednijim i usklađenijim s ljudskim preferencijama. Ovo je ključna inovacija koja je omogućila tranziciju od istraživačkih modela do proizvoda poput ChatGPT.

### 4.4 Generativni modeli izvan teksta

- Generisanje slika: DALL-E (OpenAI), Midjourney, Stable Diffusion — zasnovani na difuzionim modelima
- Generisanje videa: Sora (OpenAI), Runway Gen-3, Kling — rani stadij ali brz napredak
- Generisanje zvuka/muzike: MusicLM (Google), Suno, Udio
- Generisanje koda: GitHub Copilot, Cursor, Codex — AI koji piše programski kod na osnovu opisa u prirodnom jeziku
- Multimodalni modeli: GPT-4o, Gemini — sposobni za obradu i generisanje više tipova medija istovremeno
## 5. Obrada prirodnog jezika (NLP — Natural Language Processing)

NLP zaslužuje poseban osvrt kao jedna od najzrelijih i najšire primijenjenih oblasti AI, s direktnom relevantnošću za finansijski sektor.

### 5.1 Definicija i historija

NLP je grana AI koja se bavi interakcijom između računara i ljudskog jezika — omogućavajući mašinama da čitaju, razumiju, interpretiraju i generišu tekst na prirodnom jeziku. Razvoj NLP-a prošao je kroz tri velike faze:

- Rulesbased era (1950–1990): Ručno kodirana gramatička pravila i rječnici
- Statistička era (1990–2013): Statistički modeli jezika, n-grami, skriveni Markovljevi modeli (HMM), TF-IDF
- Era dubokog učenja (2013–danas): Word embeddings (Word2Vec, GloVe), RNN/LSTM, i konačno transformeri

### 5.2 Ključni NLP zadaci

| Zadatak | Opis | Primjena u praksi |
|---|---|---|
| Analiza sentimenta | Određivanje emocionalnog tona teksta (pozitivan/negativan/neutralan) | Analiza tržišnog raspoloženja, praćenje reputacije brenda |
| Named Entity Recognition (NER) | Identifikacija entiteta (osobe, organizacije, lokacije, datumi) | Ekstrakcija informacija iz dokumenata, compliance |
| Mašinsko prevođenje | Automatski prijevod između jezika | Google Translate, DeepL |
| Sumarizacija teksta | Sažimanje dugih dokumenata u ključne tačke | Sažeci vijesti, pravnih dokumenata |
| Odgovaranje na pitanja (QA) | Sistem odgovara na pitanja na osnovu datog teksta/znanja | Chatbotovi, virtuelni asistenti |
| Klasifikacija teksta | Kategorizacija dokumenata u predefinisane klase | Routing emailova, klasifikacija dokumenata |
| Ekstrakcija relacija | Identifikovanje odnosa između entiteta u tekstu | Konstrukcija grafova znanja |

### 5.3 NLP u kontekstu finansija (uvod za Dio II)

Du, Zhao, Mao, Xing i Cambria (2025) u svom pregledu "Natural Language Processing in Finance" identificiraju 10 ključnih NLP primjena u finansijama: analiza sentimenta, finansijsko predviđanje, upravljanje portfolijem, Q&A/chatbotovi, upravljanje rizikom, regulatorna usklađenost, ESG i održive finansije, objašnjiva AI, te digitalna imovina. Ova tematika će biti detaljno obrađena u Dijelu II rada.

## 6. Robotska automatizacija procesa (RPA)

### 6.1 Definicija

RPA (Robotic Process Automation) obuhvata softverske "robote" koji automatizuju repetitivne, pravilima vođene poslovne procese — unos podataka, kopiranje između sistema, generisanje izvještaja, obradu faktura. RPA ne koristi fizičke robote već softverske agente koji simuliraju ljudsku interakciju s korisničkim interfejsima.

### 6.2 RPA vs. "inteligentna automatizacija"

RPA u svojoj osnovnoj formi nije "inteligentna" — izvršava unaprijed definirane sekvence koraka. Međutim, inteligentna automatizacija (IPA) kombinuje RPA s AI komponentama:

| Nivo | Tehnologija | Sposobnost |
|---|---|---|
| Nivo 1: Bazični RPA | Skriptovani botovi | Automatizacija strukturiranih, ponovljivih zadataka |
| Nivo 2: RPA + OCR/NLP | Optičko prepoznavanje + jezička obrada | Obrada nestrukturiranih dokumenata |
| Nivo 3: Kognitivna automatizacija | ML + RPA | Učenje iz obrazaca, adaptacija |
| Nivo 4: Autonomna automatizacija | AI agenti | Samostalno donošenje odluka i orkestracija procesa |

Bunduchi et al. (2025) pokazuju da RPA transformiše rad u tri faze: konvergentna (neposredni dobici u efikasnosti), difuziona (širenje na nove procese), i divergentna (redizajn radnih mjesta i organizacione strukture). Istraživanje ukazuje na to da inicijalni efekti — redukcija grešaka i ubrzanje izvršenja zadataka — vremenom evoluiraju u fundamentalnu rekonfiguraciju uloga u organizaciji.

## 7. Kompjuterski vid (Computer Vision)

### 7.1 Definicija

Kompjuterski vid je oblast AI koja omogućava mašinama da interpretiraju i razumiju vizualne informacije iz digitalnih slika, videa i drugih vizualnih ulaza. Cilj je emulacija ljudskog vizualnog sistema — od prepoznavanja objekata do razumijevanja kompleksnih scena.

### 7.2 Ključne tehnike i zadaci

- Klasifikacija slika: Identifikacija šta slika prikazuje (npr. mačka vs. pas)
- Detekcija objekata: Lociranje i identifikacija višestrukih objekata na slici (YOLO, SSD, Faster R-CNN)
- Semantička segmentacija: Klasifikacija svakog piksela slike
- Optičko prepoznavanje znakova (OCR): Pretvaranje slika teksta u mašinski čitljiv tekst
- Procjena poze: Detekcija položaja ljudskog tijela
- Generisanje opisa slika: AI generiše tekstualni opis vizualnog sadržaja

### 7.3 Primjene

Ettalibi et al. (2024) i Barua et al. (2025) dokumentuju primjenu kompjuterskog vida u industrijskoj proizvodnji — kontrola kvaliteta u realnom vremenu, prediktivno održavanje, i AI upravljanje proizvodnim rasporedom — s mjerljivim smanjenjem zastoja i poboljšanjem prinosa. Kompjuterski vid se takođe široko koristi u medicini (dijagnostika na osnovu medicinskih slika), sigurnosti (sistemi za nadzor), poljoprivredi (monitoring usjeva dronovima), i maloprodaji (Amazon Go trgovine bez kasa).

## 8. Sistemi za podršku odlučivanju i prediktivna analitika

### 8.1 Prediktivna analitika

Prediktivna analitika koristi statističke modele, mašinsko učenje i rudarenje podataka za predviđanje budućih ishoda na osnovu historijskih podataka. Adesina et al. (2024) dokumentuju da prediktivni AI poboljšava profitabilnost, efikasnost i tržišni udio kroz primjene u kreditnom scoringu, detekciji prevara, predviđanju ishoda pacijenata i prognoziranju potražnje.

### 8.2 AI agenti

Najnoviji trend u AI industriji su AI agenti — autonomni ili polu-autonomni sistemi koji mogu planirati, koristiti alate, izvršavati višekoračne zadatke i donositi odluke s minimalnom ljudskom intervencijom. Za razliku od standardnih chatbot interakcija (pitanje-odgovor), AI agenti mogu:
- Dekomponovati kompleksne ciljeve u podkorake
- Koristiti externe alate (pretraživanje weba, izvršavanje koda, pristup bazama podataka)
- Iterativno poboljšavati svoje odgovore
- Sarađivati s drugim agentima (multi-agent sistemi)

Ova tehnologija je u ranom stadiju ali se brzo razvija, s primjenama u korisničkoj podršci, softverskom inženjerstvu, istraživanju i analizi podataka.

## 9. Etička pitanja i objašnjivi AI (XAI)

### 9.1 Pristranost i pravednost (Bias & Fairness)

AI sistemi mogu perpetuirati i pojačati društvene pristranosti prisutne u podacima za trening. Dokumentovani primjeri uključuju:
- Pristrasan AI za zapošljavanje koji diskriminira ženske kandidate (Amazon, 2018)
- Rasna pristranost u algoritmima za procjenu recidivizma (COMPAS sistem)
- Neravnomjerna tačnost sistema za prepoznavanje lica za različite etničke grupe
- Pristranost u kreditnom scoringu koji sistematski nepovoljno tretira određene demografske grupe

### 9.2 Objašnjivi AI (Explainable AI — XAI)

XAI je grana AI koja se fokusira na razvoj metoda za razumijevanje i interpretaciju odluka AI sistema. Chen et al. (2023) naglašavaju rastuću važnost XAI u finansijama, posebno u regulisanim industrijama gdje je objašnjivost odluka zakonski zahtjev.

Ključne XAI tehnike:
- LIME (Local Interpretable Model-agnostic Explanations) — lokalno objašnjenje individualnih predikcija
- SHAP (SHapley Additive exPlanations) — baziran na kooperativnoj teoriji igara, pripisuje doprinos svake varijable
- Attention vizualizacija — prikaz na koje dijelove ulaza model "obraća pažnju"
- Kontrafaktička objašnjenja — "Šta bi trebalo biti drugačije da bi odluka bila suprotna?"

### 9.3 Privatnost i sigurnost

- Privatnost podataka: GDPR, CCPA i drugi regulatorni okviri postavljaju stroge zahtjeve za obradu ličnih podataka
- Adversarial napadi: Ciljano manipulisani ulazi koji "varaju" AI sisteme
- Deepfakes: Generativni AI za kreiranje lažnih videa, slika i audio zapisa — s implikacijama za dezinformacije i prevare
- Model inversion: Napadi koji mogu rekonstruisati podatke za trening iz modela

### 9.4 Regulatorni okvir

- EU AI Act (2024): Prva sveobuhvatna regulativa AI na svijetu; klasifikuje AI sisteme prema riziku (neprihvatljiv, visok, ograničen, minimalan) i postavlja zahtjeve proporcionalne razini rizika
- Executive Order on AI (SAD, 2023): Fokus na sigurnost, privatnost i pravednost
- Globalna fragmentacija: Različiti pristupi regulaciji — EU favorizuje striktnu regulativu, SAD decentraliziraniji pristup, Kina kontrolu baziranu na sadržaju

## 10. Paradoks produktivnosti i trenutno stanje

### 10.1 Solow-ov paradoks u AI kontekstu

Robert Solow je 1987. godine primijetio: "Kompjutersku eru možete vidjeti svuda osim u statistikama produktivnosti." Gotovo četiri decenije kasnije, sličan paradoks se ponavlja s AI.

Ključni nalazi:
- Baslandze et al. (2026), Atlanta Fed: Istraživanje ~750 rukovodilaca pokazuje da su percipirani dobici produktivnosti veći od mjerljivih — klasičan paradoks produktivnosti
- Opagio (2026): 2,6 biliona dolara utrošeno globalno u 2025., ali 90% firmi izvještava o nultom mjerljivom uticaju
- Goldman Sachs (2024): Rani usvojitelji bilježe ~25% povećanja produktivnosti, ali samo ~5% firmi koristi AI u produkciji; očekuje se uticaj na BDP od 2027.
- McKinsey: Potencijal 2,6–4,4 biliona dolara godišnjeg ekonomskog uticaja, ali samo 1% organizacija smatra svoju implementaciju "zrelom"

### 10.2 Objašnjenja paradoksa

- Vremenski pomak: Historijski, opšte-namjenske tehnologije (elektricitet, kompjuteri) zahtijevaju decenije za punu realizaciju produktivnih efekata — potrebne su komplementarne inovacije u organizaciji, procesima i vještinama
- Problem mjerenja: Tradicionalne metrike produktivnosti (output/sat) možda ne hvataju kvalitativna poboljšanja koja AI donosi
- Faza eksperimentiranja: Većina organizacija je još u fazi pilotiranja; samo mali procenat ima AI u skali u produkcijskim sistemima
- J-kriva efekat: Kratkoročni pad produktivnosti usljed učenja i reorganizacije, prije dugoročnog rasta
- Nejednaka distribucija: Koristi su koncentrisane u malom broju firmi i sektora; agregatne statistike to ne reflektuju

### 10.3 Gdje je uticaj mjerljiv

Brynjolfsson, Li i Raymond (2025) sa Stanforda dokumentuju mjerljive efekte generativnog AI u korisničkom servisu: +14% stope rješavanja i −25% vremena obrade, s tim da su najveći dobici kod manje iskusnih radnika. Dell'Acqua, Mollick et al. (2023) na uzorku BCG konsultanata bilježe +40% performansi za zadatke unutar granica AI sposobnosti. Ovi nalazi sugerišu da je uticaj AI realan, ali neravnomjerno distribuiran i zavisan od konteksta primjene.

## 11. Zaključak prvog dijela

Ovaj dio rada predstavio je sistematizovani pregled umjetne inteligencije kroz višedimenzionalnu taksonomiju, obuhvatajući klasifikacije prema sposobnostima (ANI → AGI → ASI), funkcionalnosti (reaktivne mašine → samosvjesni AI), tehnikama (simbolički AI, mašinsko učenje, dubinsko učenje, evolutivni algoritmi, hibridni pristupi), namjeni (asistivni vs. autonomni), te načinu implementacije (cloud, edge, embedded).

Ključni zaključci prvog dijela:

- Svi operativni AI sistemi danas su uska AI (ANI) — čak i najimpresivniji LLM-ovi. AGI i ASI ostaju teorijski koncepti.
- Transformer arhitektura je fundamentalna inovacija koja je omogućila savremenu eksploziju generativnog AI, od velikih jezičkih modela do generisanja slika i videa.
- Mašinsko učenje, a posebno dubinsko učenje, dominiraju praktičnim primjenama, dok se simbolički pristup zadržava u regulisanim industrijama i hibridnim sistemima.
- Paradoks produktivnosti — enormna ulaganja uz ograničene mjerljive efekte — ostaje centralni izazov, ali historijski obrasci sugerišu da je to pitanje vremena, komplementarnih inovacija i organizacijske adaptacije.
- Etička pitanja — pristranost, objašnjivost, privatnost, regulacija — su postala integralni dio AI diskursa, s EU AI Actom kao prvim sveobuhvatnim regulatornim okvirom.

Ova sistematizacija pruža neophodan konceptualni okvir za drugi dio rada, u kojem ćemo detaljno analizirati kako se svaki od ovih tipova AI primjenjuje u finansijskom sektoru — od algoritamskog trgovanja i kreditnog scoringa do robo-savjetnika i regulatorne usklađenosti.

Reference

Adesina, O. et al. (2024). Leveraging Predictive Analytics for Strategic Decision-Making: Enhancing Business Performance Through Data-Driven Insights. World Journal of Advanced Research and Reviews.
Barua, S. et al. (2025). Leveraging AI for Smart Production Management in Industry 4.0. Scientific Reports (Nature).
Baslandze, S. et al. (2026). Artificial Intelligence, Productivity, and the Workforce: Evidence from Corporate Executives. Atlanta Fed Working Paper.
Bostrom, N. (2014). Superintelligence: Paths, Dangers, Strategies. Oxford University Press.
Brynjolfsson, E., Li, D., & Raymond, L. (2025). Generative AI at Work. Stanford Digital Economy Lab.
Bunduchi, R. et al. (2025). The Progressive Transformation of Work with RPA. European Journal of Information Systems.
Chen, X. et al. (2023). Explainable AI in Finance: A Bibliometric Review. (Various publishers).
Dell'Acqua, F., Mollick, E., Kellogg, K. et al. (2023). Navigating the Jagged Technological Frontier. Harvard/Wharton/MIT.
Du, K., Zhao, Y., Mao, J., Xing, F., & Cambria, E. (2025). Natural Language Processing in Finance: A Survey. Information Fusion (Elsevier).
Dutta, A. (2025). Taxonomy of Artificial Intelligence. ResearchGate Preprint. DOI: 10.13140/RG.2.2.32410.09926.
Ettalibi, A. et al. (2024). AI and Computer Vision-based Real-time Quality Control. Procedia Computer Science (ScienceDirect).
Goldman Sachs (2024). AI Is Showing Very Positive Signs of Boosting GDP. Goldman Sachs Insights.
Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.
Hintze, A. (2016). Understanding the Four Types of AI. The Conversation.
Krizhevsky, A., Sutskever, I., & Hinton, G. (2012). ImageNet Classification with Deep Convolutional Neural Networks. NeurIPS.
McCarthy, J., Minsky, M., Rochester, N., & Shannon, C. (1955). A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence.
McKinsey & Company. How Generative AI Is Reshaping Global Productivity and the Future of Work.
Mitchell, T. (1997). Machine Learning. McGraw-Hill.
Minsky, M. & Papert, S. (1969). Perceptrons. MIT Press.
Opagio (2026). The AI Productivity Paradox.
Russell, S. & Norvig, P. (2021). Artificial Intelligence: A Modern Approach. 4th Edition. Pearson.
Solow, R. (1987). "We'd better watch out." New York Times Book Review.
Turing, A. (1950). Computing Machinery and Intelligence. Mind, 59(236), 433–460.
Vaswani, A. et al. (2017). Attention Is All You Need. NeurIPS.
Vuković, D. B., Dekpo-Adza, S., & Matović, S. (2025). AI Integration in Financial Services: A Systematic Review of Trends and Regulatory Challenges. Humanities and Social Sciences Communications (Nature), 12, 562.
