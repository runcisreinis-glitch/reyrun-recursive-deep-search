# REYRUN Recursive Deep Search: izpētes un eksperimentu ziņojums

Pilnās izpētes atbildes, autorētie secinājumi un to robežas. Dokumentācijas izdevums: 2026. gada 10. novembris. Programmas versija: 2.0.0-beta.3.

Ziņojumā ir visas gala atlases 30 atbildes, visas vēsturiskās kopas 30 atbildes un visas sešas stratēģiju salīdzinājuma izpētes atbildes. Gala atlase saglabā 12 agrākos gadījumus un pievieno 18 jaunus; abas kopas aptver 48 atšķirīgus pamatuzdevumus. Salīdzinājuma uzdevumi uzskaitīti atsevišķi.

Iekšējo vērtētāju pilnie auditi, norāžu momentuzņēmumi, izpildes demonstrācijas, atmiņas momentuzņēmumi, neapstrādātie žurnāli, vaicājumu izdrukas un iekšējās kvītis šajā izdevumā nav iekļautas. To būtiskie ziņotie secinājumi izklāstīti autorētā pārskatā. Skati [publikācijas tvērumu](PUBLICATION_SCOPE.md) un [izlaidumu manifestu](exclusion-manifest.json).

[GitHub repozitorijs](https://github.com/runcisreinis-glitch/reyrun-recursive-deep-search) · [Repozitorija ZIP](https://github.com/runcisreinis-glitch/reyrun-recursive-deep-search/archive/refs/heads/main.zip) · [Pirmkods](scripts/recursive_search.py) · [Atbalsti autoru](SUPPORT.md) · [Vairāk par Reini Facebook](https://www.facebook.com/reinis.runcis).

## Ko apliecina rezultāti

Gala atlasei ziņoti 156 vaicājumi. Septiņiem jaunajiem matemātikas gadījumiem ir pilns pierādījums vai atvasinājums un faktiski palaists aprēķins. Visi 18 jaunie pamatuzdevumi noslēdza reģistrētu mācību ciklu, un 15 vēlākie uzdevumi ielādēja agrākās mācības; šo darbu vadīja čats. Atsevišķajā trīs uzdevumu salīdzinājumā abas metodes izpildīja fiksētās atbilžu pārbaudes. Kandidāts veica 43 tīmekļa darbības pret 47, bet izmērītā precizitāte nepieauga un kandidāts netika ieviests.

Iekļauti visi četri pašreizējie izpildāmie skripti, to testi un aprēķinu programmas. Ziņotajā laidiena pārbaudē izpildīti 82 programmas testi. Ziņotais statiskais pirmkoda pārskats šajos četros skriptos neatrada tiešas HTTP/socket darbības, maksājumu izpildi, slēptu lejupielādētāju vai `eval`/`exec`; tā iekšējā kvīts nav iekļauta. `search_host.py` apzināti palaiž lietotāja konfigurēto ārējo komandu ar tās videi piešķirto piekļuvi. Atmiņas sablīvēšana pēc apstiprināta plāna var izņemt vecus pierādījumus. Šīs darbības apraksta iekļautais kods un protokoli. Pretvīrusu sertifikācija vai neatkarīgs ielaušanās tests nav apgalvots.

## Kā turpināt mācību ciklu

Pieslēgts [izpildes savienotājs](references/host-contract.md) veic sākuma un beigu soļus, nodod izpildītājam agrākās mācības un nepieņem nepabeigtu mācību ierakstu. Vajadzīga pastāvīga atmiņa un konfigurēts izpētes izpildītājs. Norādījumu uzstādīšana pati nerada nepārtrauktu fona pakalpojumu. Praktiska instalācijas pārbaude ir divi īsti uzdevumi, pārliecinoties, ka otrajā ielādēta pirmā pieredze.

Vēsturiskie secinājumi saglabāti kā izpētes pieraksti. Tulkošana un publikācijas redakcija nav jauns eksperiments. Avotu adreses paliek pilnajās atbildēs; sākotnējās vaicājumu izdrukas un privātie izpildes pierādījumi šajā izdevumā nav iekļauti. Pašreizējās publikācijas kontrolsummas ir [failu manifestā](file-manifest.json).

## Saturs

- [Pārbaudes un attīstības ziņojums](#release-report)
- [Gala atlase: visas 30 atbildes](#final30)
- [Vēsturiskā kopa: visas 30 atbildes](#historical30)
- [Visas sešas stratēģiju salīdzinājuma atbildes](#comparison)
- [Publicētie rezultāti un to robežas](#findings)
- [Ievada piemērs par kosmētiku](#cosmetics)
- [Ievada piemērs par spēļu tehnoloģijām](#gaming)
- [Ievada piemērs par aģenta arhitektūru](#architecture)


<a id="release-report"></a>

## Pārbaudes un attīstības ziņojums

**Laidiens 2.0.0-beta.3 · izpēte 2026. gada 9. novembrī.**

Gala pārbaudē ir 10 ikdienas jautājumi, 10 vidēji sarežģīti jautājumi dažādās nozarēs un 10 sarežģīti uzdevumi. Septiņos jaunajos sarežģītajos uzdevumos ir pilns matemātisks pierādījums vai atvasinājums un faktiski palaists aprēķins. Izlabotas divas reproducētas mācību atmiņas kļūmes; pārbaudītajam kodam izpildīti 82 testi. Atsevišķais jaunās meklēšanas stratēģijas izmēģinājums deva godīgu **no_gain** rezultātu: kandidāts nekļuva par jauno pamatmetodi.

[Pilnās 30 atbildes](validation/2026-11-09-beta3/30-examples.lv.md) · [Kompaktās mācības](references/observed-lessons.md).

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](PUBLICATION_SCOPE.md).

### 1. Kāpēc atlase tika pārveidota

Sākotnējie 30 pētījumi bija reāli veikti, taču neatkarīgais audits konstatēja, ka vidējā grupa bija pārāk koncentrēta uz IT un grūtajā grupā trūka izpildītu augstākās matemātikas uzdevumu. Gala atlasē saglabāti 12 piemērotie gadījumi un pievienoti 18 jauni. Sākotnējās atbildes saglabātas pilnībā ar norādītiem redakcionāliem labojumiem: [vēsturiskais izdevums](validation/2026-11-09/30-examples.lv.md) paliek pieejams. Kopā ir 48 atšķirīgi pamatuzdevumi; trīs salīdzinājuma uzdevumi uzskaitīti atsevišķi.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](PUBLICATION_SCOPE.md).

Gala atlases jautājumiem saglabāti **156 izpildīti vaicājumi**. Katram ir EN/DE/ZH/JA meklējumi. Vaicājums šajā valodā nav pierādījums, ka atrasts un izlasīts atbalstošs pirmavots šajā valodā. Piekļuves kļūdas, nenolasīti fragmenti un tikai kopsavilkumu lasījumi paliek norādīti. Nav apgalvots, ka šis kopums statistiski pierāda četru valodu priekšrocību pār vienu.

Jautājumi sagatavoti pārbaudei. Kur vajadzīgs precizējums, dotie nosacījumi ir marķēta simulācija, ne izdomāts sarunas dalībnieka apstiprinājums. Ikdienas gadījumi pārbauda arī nepilnīgu vai kļūdainu priekšstatu, ne tikai gludi formulētu ekspertu jautājumu.

| ID | Pārbaudītais jautājums | Vaicājumi |
| --- | --- | ---: |
| E01 | Grims pēc stundas pazūd | 6 |
| E02 | Kā izvēlēties bikses pēc auguma | 5 |
| E04 | Vai der jebkurš 65 W USB-C lādētājs | 6 |
| E05 | Ko nozīmē mazgāšanas zīmes | 4 |
| E07 | Atbrīvot telefonu un saglabāt fotogrāfijas | 4 |
| E08 | Vai 5 GHz nozīmē piecreiz ātrāku internetu | 4 |
| NE01 | Divi deci miltu: tilpums vai masa | 5 |
| NE02 | Vai istabai pietiks ar vienu krāsas spaini | 5 |
| NE03 | Kur paliek izvārītu rīsu kalorijas | 5 |
| NE04 | Baltas un miglainas glāzes | 5 |
| P02 | Spēles tulkošana, saglabājot vietturus | 5 |
| P04 | HDR video pārveidošana uz SDR | 4 |
| P05 | RAID1 un ģimenes fotogrāfiju rezerves kopijas | 4 |
| NP01 | Mēslojuma izmēģinājums uz saulainas palodzes | 5 |
| NP02 | Aizkaru audums un saraušanās | 6 |
| NP03 | Ūdens uzsildīšana un sajaukšana | 5 |
| NP04 | Ogle, jonapmaiņa un reversā osmoze | 7 |
| NP05 | Vai pieņemt lētāku papildu pasūtījumu | 6 |
| NP06 | Vēsturiska Rīgas adrese | 9 |
| NP07 | Putni un logu stikls | 6 |
| F03 | Aģents, kas pārbauda savus uzlabojumus | 6 |
| F08 | Atmiņas uzlabojuma cēloņsakarīga pārbaude | 4 |
| F09 | Ārējs maksājums pēc procesa avārijas | 4 |
| NF01 | Siltuma vienādojuma inversija | 5 |
| NF02 | Stohastisks process un diskrētā dispersija | 5 |
| NF03 | Nenormālas matricas īslaicīgais pieaugums | 5 |
| NF04 | Dualitāte bez galīga reizinātāja | 5 |
| NF05 | Masas koncentrēšanās un robežpāreja | 5 |
| NF06 | Strang shēma un oscilatora enerģija | 6 |
| NF07 | Piektās pakāpes polinoma Galuā grupa | 5 |

### 2. Ko nozīmē atbilžu pārbaude

Katram gadījumam saglabāta atbilde, avoti, apgalvojumu saites un sākotnējā faila SHA-256. Jaunajiem aprēķiniem saglabāts arī kods un tā izvade. Root neatkarīgi izlasīja visus septiņus jaunā autora matemātikas pierādījumus, pārbaudīja argumentu un saglabāto skaitlisko rezultātu saskaņu. Tas nav formāls pierādījumu asistenta sertifikāts. Iekšējais matemātikas pārskats šajā izdevumā nav publicēts.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](PUBLICATION_SCOPE.md).

Pamata izpēti katram piemēram veica viens aģents, pēc tam notika norādītā neatkarīgā pārskatīšana. Šis kopums neapliecina četrus neatkarīgus aģentus katra jautājuma formulēšanas un meklēšanas posmā; četru atsevišķu perspektīvu pieņemšanas audits faktiski izpildīts tālāk aprakstītajam stratēģijas salīdzinājumam.

Septiņām nozares atbildēm neatkarīgi pārbaudīta aprēķinu un secinājumu loģika. Papildu atsevišķs aģents pārbaudīja četras jaunās ikdienas atbildes un vēsturiskās adreses/loga gadījumus pret saglabātajiem pirmavotu fragmentiem; aprēķinus tas arī atkārtoja. Nav apgalvots, ka visi ārējie avoti katrā auditā no jauna atvērti tīmeklī. Iekšējais nozaru pārskats un sešu atbilžu audits šajā izdevumā nav publicēti.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](PUBLICATION_SCOPE.md).

Publiskajam izdevumam pielāgots matemātikas noformējums un citātu saites. NE02 izlabotas atstarpes; NP04 divdomīgais atvērums precizēts uz “Kasetne, kurā ir tikai aktīvā ogle...”. Sākotnējie pētniecības ieraksti glabājas atsevišķi. Redakcija, 2026. gada 10. novembris: publiskajās atbildēs veikti arī norādītie gramatikas, pieturzīmju, atstarpju un pieraksta labojumi, saglabājot izpētes nozīmi, nosacījumus un rezultātus. Pašreizējais failu manifests identificē rediģēto publikāciju.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](PUBLICATION_SCOPE.md).

### 3. Mācības starp meklēšanas reizēm

Visi 18 jaunie pamatuzdevumi noslēgti ar faktisku sākuma/beigu ierakstu. Trīs tematiskās sērijas sāka ar tukšu testa atmiņu; **15 turpmākie uzdevumi ielādēja agrāk saglabātas mācības**. To identifikatori un aģenta norāde par izmantošanu vai neattiecināmību ir cikla pierādījumā. Piemēram, daudzuma un mērvienības nošķiršana pārnesta no miltiem uz krāsu un sausiem/vārītiem rīsiem; glāžu materiāla gadījumā iepriekšējās skaitliskās mācības atzīmētas kā neattiecināmas.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](PUBLICATION_SCOPE.md).

Šos sākuma/beigu soļus vadīja čats. Četrpadsmit jaunajām nozares un matemātikas atbildēm papildus izpildīts stingrais failu/atsauču pārbaudītājs. Tas nav pierādījums, ka šīs 18 izpētes startēja automātisks fona pakalpojums. Iepriekš saglabātā divu darbu demonstrācija caur stingro savienotāju apliecina atsevišķu reālu savienotāja darbu un nākamā uzdevuma mācības ielādi.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](PUBLICATION_SCOPE.md).

Pastāvīgais cikls ir izpildāms: ielādēt saistītās mācības → veikt uzdevumu → saglabāt noderīgo, neveiksmes un neskaidro → izpētīt konkrētu uzlabojuma hipotēzi → salīdzināt ar esošo metodi → pieņemt tikai izpildītu kritēriju gadījumā. Mācību ielāde pati par sevi nepierāda katras nākamās atbildes kvalitātes pieaugumu. Šajā laidienā pārbaudītas abas atšķirīgās lietas: atmiņas darbība un atsevišķa kandidāta atlase.

### 4. Divi izmērīti programmas uzlabojumi

| Kļūme pirms labojuma | Ko mainīja | Faktiskā pārbaude |
| --- | --- | --- |
| Agrāka mācību kartīte varēja aizsegt vēlāk saglabātu pretrunīgu neveiksmi. | Novērojumiem un kartītēm tagad ir viena hronoloģiska 16 ierakstu atlase. | Nākamais sākuma ieraksts satur arī jaunāko neveiksmes tekstu. |
| Pie 5 MiB robežas pēc neveiksmīga ieraksta palicis nesaistīts pierādījuma objekts neļāva saglabāt pat atmiņas atbrīvošanas rezultātu. | No precīzi apstiprinātā atbrīvošanas plāna pirms atomiskās saglabāšanas dzēš tikai jau nesaistītos objektus; vēl lietotos pierādījumus saglabā līdz sekmīgai stāvokļa nomaiņai. | Pie 5 242 680 aizņemtiem baitiem un 200 brīviem baitiem atbrīvošana sekmīgi atstāja 4806 baitus. Atsevišķs ievadītas rakstīšanas kļūmes tests saglabāja agrāko stāvokli un tā pierādījumus. |

Iekšējos ierakstos ir rezultāti pirms un pēc labojuma, regresiju pārbaude, 82 testu kvīts un pilnais testu žurnāls. Tie ir skaidri marķēti sintētiski mehānisma testi. Tie nepārvērš programmas kļūmes labojumu par pierādītu meklēšanas precizitātes pieaugumu.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](PUBLICATION_SCOPE.md).

### 5. Atsevišķais meklēšanas paņēmiena salīdzinājums

Kandidāts pievienoja vienu paņēmienu: vispirms pārbaudīt visvājāk pamatoto nepieciešamo nosacījumu, kas var mainīt lēmumu. Ideja iegūta ar apgalvojuma/pierādījuma argumentācijas pārnesi; atsevišķa mērvienību tipēšanas ideja atlikta, lai nesajauktu divas izmaiņas vienā izmēģinājumā.

Pirms abu pušu izpildes fiksēti kritēriji un budžets, trīs uzdevumi un pareizības pārbaudes, esošā politika un kandidāts. Pamatprasme baseline pusē netika vājināta. Puses veica divi svaigi aģentu konteksti ar vienādu deklarēto modeļa konfigurāciju, uzdevumu secību un ierobežojumu: ne vairāk par 16 tīmekļa darbībām, 8 vaicājumiem, 12 lasījumiem un 12 minūtēm katram uzdevumam. Arī kļūdains pieprasījums skaitās darbība.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](PUBLICATION_SCOPE.md).

Uzdevumi pārbaudīja precīza Depth Anything kontrolpunkta izvades mērvienību, CLIP spēju vai nespēju radīt brīvu apraksta teikumu un DINOv2 izmantošanu lokālas bibliotēkas līdzības meklēšanai. Inferenci nepalaida un modeļu svarus nelejupielādēja: tika pētīta dokumentētā spēja un kods.

| Rādītājs | Esošā metode | Kandidāts |
| --- | ---: | ---: |
| Fiksētās faktu/izpildes godīguma pārbaudes | 9/9 | 9/9 |
| Nākamās darbības kategorija | 3/3 | 3/3 |
| Dokumentēts lietderīgs komponentes izmantojums | 3/3 | 3/3 |
| Pamatojuma un nākamā soļa lauki | 6/6 | 6/6 |
| Vaicājumi | 15 | 15 |
| Lasījumi, ieskaitot neveiksmīgos | 32 | 28 |
| Tīmekļa darbības kopā | 47 | 43 |
| Laiku summa no pirmā tīmekļa pieprasījuma līdz artefaktu pabeigšanai | 456,14 s | 495,50 s |

Trīs jaunu uzdevumu salīdzinājumā abi paņēmieni izpildīja visus iepriekš fiksētos atbilžu kritērijus. Kandidāts izmantoja 43 tīmekļa darbības pret esošās metodes 47, bet nesasniedza prasīto precizitātes pieaugumu; tas netika ieviests kā jaunā pamatmetode. Tas ir **no_gain**, ne apgalvojums, ka kandidāts ir sliktāks visos lietojumos. Četru darbību ietaupījums ir novērojums šajā vienā pilotā; kandidāta darbu laiku summa vienlaikus bija lielāka. Tabulas laiku auditors vienādi pārrēķināja no pirmā reālā pieprasījuma līdz artefaktu pabeigšanai. Autoru pašu atšķirīgi definētie 461,75 un 569,59 sekunžu rādītāji saglabāti atsevišķi; tie nav tiešs ātruma salīdzinājums. Kritērijus pēc rezultātu ieraudzīšanas nepārslēdza uz izmaksām. Automātiskā izvērtējuma rezultāts un visu sešu darbu reģistrs šajā izdevumā nav publicēti; pieejamas [pilnās atbildes](validation/2026-11-09-beta3/comparison/answers.lv.md).

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](PUBLICATION_SCOPE.md).

Četri dažādi, nevienas puses atbildes nerakstījuši aģenti sniedza optimistisko, skeptisko, konservatīvo un inovatīvo pārskatu. Tie nav četri viena aģenta izdomāti viedokļi. Klātbūtnes lauku pārbaude nav cilvēku lasāmības pētījums; “inovācijas” skaitlis šeit vērtē dokumentētu lietderīgu komponentes izmantojumu, ne vēsturisku jaunatklājumu.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](PUBLICATION_SCOPE.md).

Izmēģinājuma robežas: tikai trīs veidoti uzdevumi un viena atbilde katrai pusei; kopīga failu sistēma ar instrukciju robežu, ne OS izolācija; modeļa identitāte ir vides deklarācija. Dizainers sagatavoja arī sākotnējo pareizo atbilžu etalonu pēc kandidāta fiksēšanas; root to neatkarīgi pārbaudīja pirmavotos un fiksēja pirms izpildes. Puses slotu pieejamības dēļ sāka ar apmēram sešu minūšu nobīdi. Šīs robežas neļauj apgalvot statistisku vai universālu pārākumu.

Baseline pabeigšanas ievadē bija shēmas kļūda: mācības atsauču sarakstā iedoti četri faili atļauto trīs vietā. Kontrolieris saglabāja noraidījumu un atsevišķus labojumu ierakstus, samazinot tikai šo atsauču sarakstu. Visas četras novērojuma pierādījumu atsauces, atbildes, laiki un vaicājumi palika nemainīti. Tā nebija atbilžu atkārtošana vai slēpts otrais mēģinājums.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](PUBLICATION_SCOPE.md).

Pēc noraidījuma veikts vēl viens faktiskas ielādes pārbaudes cikls. Tas ielādēja saglabāto lēmumu un nemainīto pamatpolitiku; ar to nepieskaita vēl vienu jaunu tīmekļa pētījumu.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](PUBLICATION_SCOPE.md).

### 6. Kas paturēts, noraidīts un atlikts

| Statuss | Konkrētais saturs |
| --- | --- |
| Paturēts | Abi reproducēto kļūmju labojumi, avotu/atbilžu kontrolsummas, kompaktās mācības par mērvienībām, koncentrāciju, numuru/objektu identitāti un pierādījumu priekšnosacījumiem. |
| Noraidīts kā jauna pamatmetode | Priekšnosacījuma prioritizēšanas kandidāts: prasītais precizitātes ieguvums nav sasniegts. Tā rezultāti un atteikuma iemesls paliek pieejami. |
| Atlikts ar pārbaudāmu hipotēzi | Mācību atbilstības atlase, atsevišķs izmaksu mērķa izmēģinājums un valodu papildu ieguvuma novērtējums. Vajadzīgi jauni uzdevumi un iepriekš noteikts pieņemšanas kritērijs. |

Atmiņa ir ierobežota. Saspiests secinājums nevar bezgalīgi saglabāt visu izejas materiālu; neapstrādāto pierādījumu atmešana notiek tikai pēc dokumentēta plāna. Šī laidiena pilnie privātie izpētes pieraksti tiek saglabāti atsevišķi; publiski pieejamas pašu atbildes, aprēķini un kompaktā izcelsmes uzskaite, ne svešo lapu pilntekstu kopijas.

### 7. Labota vēsturiskā uzskaite un izplatīšanas robeža

Sākotnējā ziņojuma kopskaitā 147 bija iekļauti četri deklarēti E10 sākuma vaicājumi, kuru toreizējā pilnā izvade nav saglabājusies. Neatkarīgā pārbaude apstiprina 143 dažādus vaicājumus ar saglabātām sākotnējām kvītīm. Jau esošie E10 atkopšanas lasījumi ir sasaistīti ar avotiem; trūkstošās kvītis nav izdomātas. Jaunās gala atlases 156 skaits attiecas tikai uz tās 30 gadījumiem.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](PUBLICATION_SCOPE.md).

> Sākotnējā publikācijas piezīme, saglabāta vēsturei: Publiskā izplatīšanas lapa: https://reyrun-rekursive-deep-search.runcisreinis.chatgpt.site . Tajā ir lejupielāde, dokumentācija, šī pārbaude, visi piemēri, video un Facebook teksta sagatave. GitHub, Hugging Face, ModelScope un Gitee publiskie spoguļi šajā laidienā vēl nav izveidoti. Facebook ieraksts nav nosūtīts autora vietā.

Publikācijas stāvoklis 2026. gada 10. novembrī: publiskais [GitHub repozitorijs](https://github.com/runcisreinis-glitch/reyrun-recursive-deep-search) ir publicēts, un tā pirmais 111 failu izdevums ir pārbaudīts pret publikācijas manifestu. Ķīnas spoguļa publicēšana gaida konta pārbaudi: gan Gitee, gan ModelScope pieprasīja tālruņa piesaisti, un spogulis tajos vēl nav izveidots. Hugging Face spogulis nav izveidots. Facebook sagataves autora vietā nav publicētas.

Šī ir izpētes prasme un izpildāms mācību cikls pieslēdzamai aģenta videi. Pakotnes lejupielāde vai norādes ielīmēšana parastā čatā pati nepalaidīs diennakts procesu un negarantēs pastāvīgu atmiņu. Konkrētas instalācijas pieņemšanas pārbaude ir reāls pirmais darbs, otrais darbs un tajā ielādītā pirmā darba pieredze.


<a id="final30"></a>

## Gala atlase: visas 30 atbildes

Pārbaudes datums: **2026. gada 9. novembris**. Laidiens: **2.0.0-beta.3**.

> Redakcija, 2026. gada 10. novembris: publikācijai izlabota gramatika, pieturzīmes, atstarpes un nepilnīgs matemātiskais pieraksts. Saglabāti jautājumu skaitliskie dati un nosacījumi, pilnās atbildes, matemātiskie argumenti, izpētes rezultāti un avotu adreses. Sākotnējie izpētes ieraksti glabājas atsevišķi; pašreizējās publikācijas failus identificē failu manifests.

Šeit ir 10 ikdienas jautājumi parastā, reizēm neskaidrā valodā, 10 vidēji sarežģīti jautājumi dažādās nozarēs un 10 sarežģīti jautājumi. Septiņos sarežģītajos piemēros ir pilns matemātisks atvasinājums vai pierādījums un faktiski palaists kontrolaprēķins.

Jautājumi ir sagatavoti pārbaudei; tās nav 30 cilvēku intervijas. Skaidri dotie un simulētie nosacījumi nav apgalvojumi par Reiņa īsto mājokli, veselību, finansēm vai ierīcēm. Tīmekļa meklējumi, avotu lasīšana un norādītie aprēķini ir faktiski veikti. Neveikti fiziski izmēģinājumi paliek priekšlikumi.

Atlasē ir **12 saglabāti un 18 jauni piemēri**, kopā **156 vaicājumi**. Katrā piemērā meklēts angļu, vācu, ķīniešu un japāņu valodā. Tas nenozīmē, ka katrā valodā atrasts un izlasīts piemērots pirmavots. Avotu lasīšanas robežas un kļūmes saglabātas privātajā pierādījumu reģistrā; pilnie atbilžu teksti publicēti tālāk.

Sākotnējie 30 piemēri paliek atsevišķi vēsturē. Kopā ar 18 papildinājumiem izpētes krājumā ir 48 atšķirīgi pamatuzdevumi. Metodes salīdzinājuma trīs jaunie uzdevumi un atkārtotie izpildījumi šajā skaitā nav ieskaitīti.

Sākuma un beigu darbības šīs atlases izpētē vadītas manuāli. Jaunās vidējās un matemātikas grupas pierādījumu faili pārbaudīti arī ar atsevišķu stingro ierakstu pārbaudītāju. Tas nav apgalvojums, ka visas izpētes palaida patstāvīgs fona aģents.

[Pārbaudes kopsavilkums](validation/2026-11-09-beta3/release-report.lv.md) · [Sākotnējie 30 piemēri](validation/2026-11-09/30-examples.lv.md).

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](PUBLICATION_SCOPE.md).

### Saturs

#### 10 ikdienas jautājumi

- [E01 — Grims pēc stundas pazūd](#final30-e01)

- [E02 — Kā izvēlēties bikses pēc auguma](#final30-e02)

- [E04 — Vai der jebkurš 65 W USB-C lādētājs](#final30-e04)

- [E05 — Ko nozīmē mazgāšanas zīmes](#final30-e05)

- [E07 — Atbrīvot telefonu un saglabāt fotogrāfijas](#final30-e07)

- [E08 — Vai 5 GHz nozīmē piecreiz ātrāku internetu](#final30-e08)

- [NE01 — Divi deci miltu: tilpums vai masa](#final30-ne01)

- [NE02 — Vai istabai pietiks ar vienu krāsas spaini](#final30-ne02)

- [NE03 — Kur paliek izvārītu rīsu kalorijas](#final30-ne03)

- [NE04 — Baltas un miglainas glāzes](#final30-ne04)

#### 10 vidēji sarežģīti jautājumi dažādās nozarēs

- [P02 — Spēles tulkošana, saglabājot vietturus](#final30-p02)

- [P04 — HDR video pārveidošana uz SDR](#final30-p04)

- [P05 — RAID1 un ģimenes fotogrāfiju rezerves kopijas](#final30-p05)

- [NP01 — Mēslojuma izmēģinājums uz saulainas palodzes](#final30-np01)

- [NP02 — Aizkaru audums un saraušanās](#final30-np02)

- [NP03 — Ūdens uzsildīšana un sajaukšana](#final30-np03)

- [NP04 — Ogle, jonapmaiņa un reversā osmoze](#final30-np04)

- [NP05 — Vai pieņemt lētāku papildu pasūtījumu](#final30-np05)

- [NP06 — Vēsturiska Rīgas adrese](#final30-np06)

- [NP07 — Putni un logu stikls](#final30-np07)

#### 10 sarežģīti jautājumi

- [F03 — Aģents, kas pārbauda savus uzlabojumus](#final30-f03)

- [F08 — Atmiņas uzlabojuma cēloņsakarīga pārbaude](#final30-f08)

- [F09 — Ārējs maksājums pēc procesa avārijas](#final30-f09)

- [NF01 — Siltuma vienādojuma inversija](#final30-nf01)

- [NF02 — Stohastisks process un diskrētā dispersija](#final30-nf02)

- [NF03 — Nenormālas matricas īslaicīgais pieaugums](#final30-nf03)

- [NF04 — Dualitāte bez galīga reizinātāja](#final30-nf04)

- [NF05 — Masas koncentrēšanās un robežpāreja](#final30-nf05)

- [NF06 — Strang shēma un oscilatora enerģija](#final30-nf06)

- [NF07 — Piektās pakāpes polinoma Galuā grupa](#final30-nf07)

### 10 ikdienas jautājumi

<a id="final30-e01"></a>

#### E01 — Grims pēc stundas pazūd

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Man seja kaut kā spīd un kosmētika pēc stundas pazūd. Ko man nopirkt?

##### Nepieciešamais precizējums

Kāds ir ādas tips un vai ir kairinājums; kādu grimu lieto, un vai vispirms vajadzīga uzklāšanas metode? Kāds budžets un valsts?

##### SIMULĒTA atbilde pārbaudes uzdevumā

Pieaugušais; taukaina T zona, normāli vaigi, nav kairinājuma; ikdienas grims; vispirms uzklāšanas metode; 30 EUR Latvijā.

Šī ir uzdevuma devēja dota simulācija, nevis reāls lietotāja apstiprinājums.

##### Izpētītā atbilde

Sāktu ar plānākām grima kārtām un nelielu daudzumu matējoša pūdera T zonā. Visus 30 € uzreiz tērēt nevajag.

1. Uzklāj savu ierasto krēmu nelielā daudzumā un ļauj tam nosēsties. Pirms tonālā āda nedrīkst palikt izteikti slidena. Taukojošajai T zonai un normālajiem vaigiem vari pielāgot daudzumu atsevišķi. Šādu pieeju apraksta [KOSE](https://www.kose.co.jp/kose/make/make104.html).
2. Tonālo klāj plāni; papildu kārtu liec tikai vietās, kur vajag lielāku segumu. Tā ir [intervēto grima mākslinieku darba metode](https://www.allure.com/story/how-to-make-makeup-last-all-day), kuru ir vērts izmēģināt ar jau esošo tonālo.
3. Nedaudz caurspīdīga pūdera viegli piespied pierei, degunam un zodam. Vaigiem nevajag automātiski tikpat biezu kārtu. [Ražotāja norādes](https://www.essence.eu/de-de/make-up-tips/how-to-setting-powder) arī iesaka pūdera daudzumu pielāgot sejas zonām.
4. Kad parādās spīdums, vispirms viegli piespied salveti, neberzējot seju. Tikai pēc tam izlīdzini grimu un, ja vajag, pievieno pavisam maz pūdera. Tā grimu pielabo [CBC televīzijas grimētāji](https://www.hicbc.com/magazine/article/?id=metone-makecolumndo813-260829).

Ja pūdera nav, lētam izmēģinājumam der apsvērt [essence All About Matt, 8 g](https://www.drogas.lv/lv/kosmetika/sejai/kompaktpuderi-puderi/essence-all-about-matt-fixing-kompaktais-puderis-8g/p/BP_225741). Atvērtajā Drogas lapā norādīti 3,39 €; pirms pirkuma pārbaudi cenu un pieejamību. Turpat ir arī pircēju sūdzības par īsu matējuma noturību. Individuālo rezultātu uz tavas ādas no šīs informācijas paredzēt nevar.

Mans ierosinājums: vienu dienu pamēģini šo secību un pēc stundas apskati tieši T zonu. Ja grims joprojām pazūd, nākamajā solī vajadzēs pārbaudīt konkrēto krēma, saules aizsarglīdzekļa un tonālā kombināciju.


*Izpētes izcelsme: E01; 6 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `5449c7ead17b0ff512966b84a6d5d090392bbec8c7a4e179b0578a1ce863da2e`.*

<a id="final30-e02"></a>

#### E02 — Kā izvēlēties bikses pēc auguma

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Esmu 1,80 m. Kādas bikses man piestāvēs?

##### Nepieciešamais precizējums

Kādu siluetu un lietojumu vēlies, un vai meklē piegriezumu vai konkrētu izmēru? Vai ir zināms vidukļa apkārtmērs un iekšstaras garums?

##### SIMULĒTA atbilde pārbaudes uzdevumā

Ikdienai, patīk taisns siluets; vajadzīga pielaikošanas metode; viduklis un iekšstara nav izmērīti; konkrēts izmērs nav prasīts.

Šī ir uzdevuma devēja dota simulācija, nevis reāls lietotāja apstiprinājums.

##### Izpētītā atbilde

Sāktu ar taisnām ikdienas biksēm un salīdzinātu divus piegriezumus: parastu taisnu un nedaudz brīvāku augšstilbos. Tas ir mans pielaikošanas ierosinājums, kas atbilst tavai izvēlei. No 1,80 m auguma vien nevar noteikt vajadzīgo vidukli, staras garumu vai to, kurš siluets tev patiks. Ražotāji šos mērījumus vērtē atsevišķi. [Levi’s mērīšanas ceļvedis](https://www.levi.com/GB/en_GB/blog/article/how-to-measure-jeans)

Pielaikojot pārbaudi šādi:

- Aiztaisi jostasvietu un apsēdies. Tai jābūt ērtai arī sēdus; augšstilbus un stakli nedrīkst stipri vilkt.
- Apskaties no priekšpuses, sāniem un aizmugures. Novērtē, vai audums pie gurniem nav izteikti nostiepts vai sakrājies liekā maisā.
- Izmēģini ikdienā vajadzīgās kustības. Ja iespējams, arī pāris soļus. Japānas drēbnieku uzņēmuma [Dankan pielaikošanas norādes](https://dankan.co.jp/blogs/dankan-magazine/jeans-size-guide) uzsver komfortu kustībā, ne vien stāvot pie spoguļa.
- Garumu vērtē ar tiem apaviem, kurus valkāsi. Tīram taisnam siluetam es sākumā salīdzinātu staru, kas viegli pieskaras apavam, ar nedaudz īsāku variantu. Tā ir gaumes izvēle.

Mājās atrodi bikses, kuru garums jau patīk. Izklāj tās un izmēri iekšējo šuvi no stakles līdz apakšmalai. Jostasvietu mēri plakani un iegūto platumu reizini ar divi. Šo metodi apraksta [Levi’s](https://www.levi.com/GB/en_GB/blog/article/how-to-measure-jeans).

Salīdzinot izmēru tabulas, pārbaudi, vai tajās norādīti ķermeņa vai paša apģērba mērījumi. Tie nav automātiski vienādi, un pat viena burta izmērs var atšķirties starp piegriezumiem. [GU skaidrojums](https://faq-tw.gu-global.com/articles/zh_TW/Knowledge/000010565)


*Izpētes izcelsme: E02; 5 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `e55a96805a78342837a6362c5f1e50e447ff72416058cec2ab1535aa407446f5`.*

<a id="final30-e04"></a>

#### E04 — Vai der jebkurš 65 W USB-C lādētājs

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Vai jebkurš 65W USB-C lādētājs der manam portatīvajam?

##### Nepieciešamais precizējums

Kāds ir precīzs portatīvā modelis un uzlādes pieslēgvieta; vai vajag saderības pārbaudi vai konkrētu pirkumu?

##### SIMULĒTA atbilde pārbaudes uzdevumā

ThinkPad T14 Gen 4 AMD, USB-C PD; vajadzīgas saderības pārbaudes, nevis konkrēts pirkums.

Šī ir uzdevuma devēja dota simulācija, nevis reāls lietotāja apstiprinājums.

##### Izpētītā atbilde

Jebkurš 65 W lādētājs nederēs. Tavam **ThinkPad T14 Gen 4 AMD** jāpārbauda USB Power Delivery režīms, konkrētās pieslēgvietas jauda un kabelis. Lenovo šim modelim norāda gan 45 W, gan 65 W USB-C adapterus ar PD 3.0; 65 W ir arī ražotāja ātrās uzlādes nosacījums. [Lenovo specifikācija](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T14_Gen_4_AMD/ThinkPad_T14_Gen_4_AMD_Spec.PDF)

Pārbaudi marķējumu šādā secībā:

1. Meklē **USB PD / Power Delivery**, ne tikai “65 W” un USB-C spraudni.
2. Izvades tabulā meklē **20 V ⎓ 3,25 A** vai lielāku pieejamo strāvu pie 20 V, lai iegūtu visus 65 W. Aprēķins ir 20 × 3,25 = 65. Šādu izvadi norāda arī [Lenovo 65 W adaptera apraksts](https://m.lenovo.com.cn/wiki/product-1039806.html).
3. Pārliecinies, ka attiecīgais ports dod šo jaudu arī tavā lietošanas režīmā. Daudzportu lādētājam “65 W” var būt kopējā jauda. Piemēram, [Buffalo specifikācijā](https://www.buffalo.jp/product/detail/print/bsacpd6505c2bk.html) viena ierīce saņem līdz 65 W, bet divas ierīces dala 45 W un 20 W.
4. Ja kabelis ir atdalāms, arī tam jābūt paredzētam vismaz 65 W. Pie 20 V tam jāspēj pārvadīt vairāk par 3 A. Ar 60 W marķētu kabeli pilniem 65 W nepietiek; [USB-IF](https://usb.org/cable_connector) skaidro, ka kabeļu jaudas iespējas atšķiras un sertifikācijas marķējumā tās norāda atsevišķi.

Praktiskai pārbaudei vispirms pievieno tikai datoru un paskaties, vai nav paziņojuma par lēnu uzlādi un vai akumulatora līmenis darba laikā pieaug. [Microsoft](https://support.microsoft.com/de-de/windows/experience/power-battery/pc-is-charging-slowly-or-discharging-while-it-s-plugged-in) apraksta gadījumus, kad neatbilstošas barošanas dēļ dators lādējas lēni vai turpina izlādēties. Šī ir pārbaudes secība; konkrēts lādētājs ar tavu datoru šeit nav izmēģināts.


*Izpētes izcelsme: E04; 6 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `c8478d1e38f89ef7bbac47764f96225e5e7e498f7f25b301d23bc4db2cb6d6c5`.*

<a id="final30-e05"></a>

#### E05 — Ko nozīmē mazgāšanas zīmes

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Uz apģērba ir 30 grādi, pasvītrots spainītis un pārsvītrots trijstūris. Kā mazgāt?

##### Izpētītā atbilde

Izvēlies **saudzīgu mazgāšanas programmu līdz 30 °C un līdzekli bez balinātāja**. Ja zem spainīša ir viena svītra, zīmju nozīme ir šāda:

| Zīme | Ko tā nosaka |
|---|---|
| Spainītī “30” | Ūdens temperatūra nedrīkst pārsniegt 30 °C. |
| Viena svītra zem spainīša | Saudzīgāka mehāniskā apstrāde, mazāks veļas daudzums un saudzīgāka centrifugēšana. |
| Pārsvītrots trijstūris | Nedrīkst balināt, arī ar skābekļa balinātāju. |

Šīs nozīmes skaidro [GINETEX kopšanas simbolu apraksts](https://ginetex.de/pflegekennzeichnung/pflegesymbole/) un [Japānas Patērētāju lietu aģentūras tabula](https://www.caa.go.jp/policies/policy/representation/household_goods/guide/wash_02.html).

Praktiski savas veļasmašīnas instrukcijā izvēlies programmu, kas atbilst saudzīgai 30 °C mazgāšanai. Nepietiek tikai parastai intensīvai programmai samazināt temperatūru: svītra nosaka arī saudzīgāku veļas kustināšanu. GINETEX šim režīmam iesaka tvertni nepildīt vairāk par pusi un centrifugēt īsi vai necentrifugēt. Universālu apgriezienu skaitu no šīs etiķetes noteikt nevar. [GINETEX](https://ginetex.de/pflegekennzeichnung/pflegesymbole/)

Pārbaudi mazgāšanas un traipu tīrīšanas līdzekļa sastāvu vai norādes. Uzraksts “krāsainai veļai” var palīdzēt orientēties, bet būtiskā prasība ir balinātāja neesamība. Balināšanas aizliegums attiecas arī uz līdzekli, ko pievienotu atsevišķi traipa dēļ.

Ja zem spainīša ir **divas svītras**, vajadzīgs vēl saudzīgāks režīms. Savukārt žāvēšanu un gludināšanu nosaka citas zīmes; no šīm trim nevar secināt, vai apģērbu drīkst likt veļas žāvētājā.


*Izpētes izcelsme: E05; 4 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `d09651aa27257dad550470ee30cb329662c8253d1ec2a73280e26fbe1ece108c`.*

<a id="final30-e07"></a>

#### E07 — Atbrīvot telefonu un saglabāt fotogrāfijas

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Telefonā pietrūkst vietas. Vai Google Photos dzēšana atbrīvos telefonu, saglabājot bildes?

##### Nepieciešamais precizējums

Vai lieto Android vai iPhone, vai Google Photos dublēšana ir ieslēgta, un vai domā Free up space vai Delete?

##### SIMULĒTA atbilde pārbaudes uzdevumā

Android; Google Photos dublēšana ieslēgta; jāskaidro Free up space un Delete, neko faktiski nedzēst.

Šī ir uzdevuma devēja dota simulācija, nevis reāls lietotāja apstiprinājums.

##### Izpētītā atbilde

**Jā, izmantojot “Free up space on this device” un iepriekš pārbaudot dublēšanu.** Android lietotnē parastā dzēšana dara ko citu.

| Darbība | Kas notiek |
|---|---|
| **Free up space on this device** — atbrīvot vietu šajā ierīcē | No telefona izņem jau droši dublētās foto un video kopijas. Tās paliek Google Photos kontā. |
| **Delete / Move to trash** — dzēst / pārvietot uz atkritni | Dzēš attēlus no Google Photos un ierīces; dublēto attēlu dzēšana izplatās arī uz ierīcēm, kurās ieslēgta dublēšana. |

Šo atšķirību apraksta Google instrukcijas par [vietas atbrīvošanu ierīcē](https://support.google.com/photos/answer/6128843?co=GENIE.Platform%3DAndroid&hl=en) un [foto dzēšanu](https://support.google.com/photos/answer/6128858?co=GENIE.Platform%3DAndroid&hl=en).

**Es rīkotos šādi:**

1. Google Photos profilā pārbaudītu pareizo Google kontu un statusu **“Backup complete”**. Ieslēgta dublēšana vēl nenozīmē, ka tā ir pabeigta.
2. Dažiem svarīgiem attēliem atvērtu informāciju un pārbaudītu **“Backed up”**. Papildu pārbaudei atvērtu tos pašā kontā vietnē [photos.google.com](https://photos.google.com). Google apraksta [kopējā un atsevišķa foto dublēšanas statusa pārbaudi](https://support.google.com/photos/answer/6193313?co=GENIE.Platform%3DAndroid&hl=en).
3. Tikai pēc tam izvēlētos **“Free up space on this device”**. Pirms apstiprināšanas lietotne parāda atbrīvojamo apjomu.

Pēc vietējo kopiju izņemšanas bildes joprojām redzēsi Google Photos, pieslēdzoties kontam ar internetu. Taču tās vairs nebūs pieejamas telefona parastajā galerijā vai bezsaistē. Nesenie, mazāk nekā 30 dienas vecie faili var palikt ierīcē, tāpēc šī funkcija ne vienmēr iztukšo visas vietējās kopijas. To norāda [Google palīdzība](https://support.google.com/photos/answer/6128843?co=GENIE.Platform%3DAndroid&hl=en).

Te ir darbību skaidrojums; nekas telefonā nav dzēsts.


*Izpētes izcelsme: E07; 4 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `a87fa37d17041a24d4789ad062b1117241ac4be52b708b15389f582cb17b215d`.*

<a id="final30-e08"></a>

#### E08 — Vai 5 GHz nozīmē piecreiz ātrāku internetu

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Ko nozīmē rūtera 5 GHz? Vai internets būs piecreiz ātrāks?

##### Izpētītā atbilde

**5 GHz apzīmē Wi‑Fi radiofrekvenču joslu. Tas nesola piecreiz ātrāku internetu.** Gigaherci raksturo radioviļņa svārstību biežumu; datu pārraides ātrumu mēra, piemēram, megabitos sekundē jeb Mbit/s. “5 GHz” ir joslas nosaukums, kurā rūteris un telefons vai dators sazinās. [Intel skaidrojums](https://www.intel.com/content/www/us/en/products/docs/wireless/2-4-vs-5ghz.html).

Praksē izvēle parasti izskatās šādi:

| Josla | Kad tā var būt izdevīgāka |
|---|---|
| **5 GHz** | Tuvāk rūterim, kad vajag lielāku datu caurlaidību un ir labs signāls. Parasti iespējami platāki kanāli. |
| **2,4 GHz** | Tālāk no rūtera vai aiz vairākām sienām, ja 5 GHz savienojums kļūst vājš. Taču šajā joslā var būt vairāk traucējumu. |

Tās ir tendences, ne garantijas konkrētā dzīvoklī. [Buffalo](https://www.buffalo.jp/support/faq/detail/15959.html) norāda, ka 5 GHz ne vienmēr dod ātrāku vai stabilāku savienojumu. [TP-Link](https://media.tp-link.com.cn/document/html1714457949100.html) arī skaidro: signāla “svītriņu” skaits viens pats nepasaka ātrumu, jo nozīme ir traucējumiem un kanāla kvalitātei.

**Interneta ātrumu ierobežo visa ķēde:** pakalpojuma pieslēgums, rūteris, izmantotā ierīce un Wi‑Fi apstākļi. Tāpēc, piemēram, 100 Mbit/s pieslēgumu tikai pārslēgšanās uz 5 GHz nepārvērtīs par 500 Mbit/s pieslēgumu. Tas ir secinājums no šiem ierobežojumiem, ne mērījums tavā tīklā. [Intel](https://www.intel.com/content/www/us/en/products/docs/wireless/2-4-vs-5ghz.html).

**Es sāktu ar vienkāršu salīdzinājumu:** ja abas joslas pieejamas atsevišķi, ar to pašu ierīci tajā pašā vietā pārbaudītu abas vairākas reizes. Salīdzinātu arī video vai zvana stabilitāti. Labākā izvēle ir tā, kas labi strādā vietā, kur ierīci tiešām lieto.


*Izpētes izcelsme: E08; 4 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `6f96f040a16a7fe71cea977e04a72322a48b382a59dfcd2c97b10566eb8dd75e`.*

<a id="final30-ne01"></a>

#### NE01 — Divi deci miltu: tilpums vai masa

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Man tai cepumu receptei ir divi deci miltu. Nu tad uz svariem 200 un gatavs, vai tur kaut kas cits jādara?

*Pārbaudes nosacījumi:* Recepte saka 2 dl kviešu miltu; nav norādīts svars vai konkrēta miltu marka. Nepieciešamo precizējumu ieraksti kā testa rezultātu; neizdomā masas blīvumu.

##### Izpētītā atbilde

**Uz svariem automātiski 200 g neliec.** Receptes **2 dl ir 200 ml** — tas ir tilpums. Gramus iegūst, ja zināma attiecīgā daudzuma masa; miltiem tilpums un masa nav vienāds skaitlis. Vispārīgā sakarība ir masa = blīvums × tilpums. [NIST mērvienību skaidrojums](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-8).

Šai receptei izmanto mērtrauku ar 200 ml atzīmi un miltus nesaspied. Ja receptes autors piedāvā arī daudzumu gramos, visērtāk svērt pēc tā. Dr. Oetker skaidro, ka sausu produktu masa pie viena tilpuma var atšķirties; King Arthur parāda, ka rezultātu ietekmē arī miltu sablīvēšana. Tāpēc vienu internetā atrastu “grami vienā glāzē” skaitli nevajag pasniegt kā precīzu pārrēķinu tavai receptei. [Dr. Oetker](https://www.oetker.de/inspiration/tipps-tricks/t/mengenangaben-beim-backen-umrechnen), [King Arthur](https://www.kingarthurbaking.com/blog/2023/10/13/how-to-measure-flour).

Ja vēlies nākamreiz izmantot tikai svarus, vari vienreiz nosvērt tieši šai receptei nomērītos 200 ml un pierakstīt izmantoto miltu veidu un mērīšanas paņēmienu. Tas ir praktisks atkārtošanas paņēmiens; šajā pārbaudē milti fiziski nav svērti.

##### Ko pārbaudījām

Aprēķins: 2 × 100 = 200 ml. No šī vien masa gramos neizriet. Pārbaudei izdomāta miltu blīvuma vērtība nav izmantota. Papildu jautājums nav vajadzīgs, lai novērstu mērvienību sajaukumu; receptes autora gramus vajadzētu prasīt tikai tad, ja nepieciešams precīzs svars.

##### Inovācijas pārbaude

Apsvērti divi pārnesami paņēmieni: mērvienību pārbaude pirms pārrēķina un vienreizēja sava mērījuma saglabāšana atkārtošanai. Pirmais ļauj atklāt šajā jautājumā esošo kļūdaino vienādību. Otrajam būtu vajadzīgs īsts virtuves mērījums; tas paliek izmēģināms. Šie ir zināmu paņēmienu pielāgojumi, ne jauna fizikas teorija.


*Izpētes izcelsme: NE01; 5 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `a48ea1361fbe31664609f1f6c4294d0476059e8c11c4575fd35705bf5ecfc72a`.*

<a id="final30-ne02"></a>

#### NE02 — Vai istabai pietiks ar vienu krāsas spaini

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Istaba četri uz trīs. Vienu krāsas spaini paņemšu un visas sienas, pietiks tak?

*Pārbaudes nosacījumi:* Sākumā nosauc tikai būtiskos trūkstošos lielumus. Tad izmanto skaidri marķētu simulēto precizējumu: garums 4 m, platums 3 m, augstums 2,5 m, durvju+logu laukums 5 m², divas kārtas, uz izvēlētās krāsas norādīti 10 m²/L vienai kārtai; griestus nekrāso. Aprēķini teorētisko daudzumu, nodali reālo rezervi.

##### Izpētītā atbilde

**No “četri uz trīs” vien to nevar pateikt.** Cik augstas ir sienas, cik lielu laukumu aizņem logi un durvis, cik kārtu paredzēts un kas uz spaiņa rakstīts par litriem un m²/L? Vajadzīgs arī sienas stāvoklis, ja gribam novērtēt reālu patēriņu. Ražotāja kalkulators atsevišķi izmanto sienu kopējo platumu, augstumu un atvērumu laukumu. [Nippon Paint](https://www.nipponpaint.com.hk/en/calculator/).

##### Simulētais precizējums un aprēķins

Šie ir pārbaudes uzdevumā dotie skaitļi, ne pieņēmumi par lietotāja istabu: 4 × 3 m, augstums 2,5 m, durvis un logi kopā 5 m², divas kārtas, 10 m²/L katrai kārtai. Griestus nekrāso.

| Solis | Aprēķins | Rezultāts |
|---|---|---:|
| Sienu perimetrs | 2 × (4 + 3) | 14 m |
| Sienas pirms atvērumu atskaitīšanas | 14 × 2,5 | 35 m² |
| Krāsojamais laukums | 35 − 5 | 30 m² |
| Divu kārtu kopējais pārklājums | 30 × 2 | 60 m² |
| Krāsa pēc dotās segtspējas | 60 ÷ 10 | **6 L** |

Aprēķins atkārtots ar precīzu racionālu aritmētiku saglabātajā kodā. **5 L spainis šiem nosacījumiem ir par mazu; 6 L ir teorētiskais minimums bez rezerves.** Lai atbildētu par “vienu spaini”, joprojām jāzina tā tilpums.

Rezerve jānodala no šiem 6 L. Piemēram, **ja plānošanā izvēlas 10% rezervi**, iznāk 6,6 L; 10% šeit ir ilustrēts izvēles nosacījums, ne universāla ražotāja garantija. Reālo patēriņu ietekmē konkrētā krāsa un pamatne: Alpina savā lapā norāda vienas kārtas patēriņu gludai virsmai un lielāku patēriņu raupjai virsmai. [Alpina produkta dati](https://alpina-farben.de/produkt/alpina-wandfarbe/).

##### Ko no šī paņemt nākamajai reizei

Iepriekšējā miltu uzdevuma mācība te noderēja: vispirms nošķirt mērvienības. Grīdas m², sienu m², vienas kārtas m²/L un spaiņa litri ir dažādi lielumi. Par praktisku papildpārbaudi var kalpot neliels izmēģinājums uz zināma sienas laukuma, lai precizētu konkrētās virsmas patēriņu. Šajā sesijā siena nav krāsota; ieguvums no tāda izmēģinājuma nav izmērīts.


*Izpildītā aprēķina faili:* [calculation.json](validation/2026-11-09-beta3/calculations/NE02/calculation.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NE02/calculation.py)

*Izpētes izcelsme: NE02; 5 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `b058bcc12b6b055d14cf572f8d12c2df1109424360d63cee952279434a44cc80`.*

<a id="final30-ne03"></a>

#### NE03 — Kur paliek izvārītu rīsu kalorijas

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Rīsiem uz pakas trīssimt piecdesmit, aplikācijā simt divdesmit. Tie abi uz simtu gramu. Kur tās kalorijas pazūd kad es uzvāru?

*Pārbaudes nosacījumi:* Uzdevums ir par sausas un izvārītas masas salīdzinājumu, ne individuālu uztura ieteikumu. Pārbaudi abas iespējamās uzskaites bāzes. Aprēķina kontrolpiemērs: 100 g sausu rīsu ar 350 kcal pēc vārīšanas bez piedevām sver 280 g; pieņem, ka piemērā pārtikas enerģija nav aizlieta prom.

##### Izpētītā atbilde

**Vispirms pārbaudi, vai abi skaitļi attiecas uz vienādu produktu stāvokli: sausiem vai jau izvārītiem rīsiem.** Vārīšanās laikā rīsi uzņem ūdeni, tāpēc 100 g izvārītu rīsu satur mazāk sākotnējo sauso rīsu nekā 100 g nevārītu. Tas izskaidro lielu atšķirību kalorijās uz 100 g. [FAO par rīsu vārīšanu](https://www.fao.org/4/ac344e/ac344e.htm), [Reishunger skaidrojums saviem rīsiem](https://www.reishunger.de/wissen/article/112/kalorien-von-100-g-gekochtem-reis).

##### Pārbaudes uzdevumā dotais piemērs

Pieņemam tieši dotos nosacījumus: **100 g sausu rīsu satur 350 kcal, pēc vārīšanas ir 280 g un pārtikas enerģija nav aizlieta ar ūdeni vai papildināta ar piedevām.**

- Viss izvārītais daudzums: **350 kcal**.
- Katri 100 g: **350 ÷ 280 × 100 = 125 kcal**.
- 140 g porcija: **175 kcal**.

Aprēķins izpildīts arī saglabātajā Python kodā. **125 kcal ir šī piemēra rezultāts**, ne visu rīsu universāla tabulas vērtība. Ar konkrētās aplikācijas 120 kcal to nevar pielīdzināt bez ziņas, kurš rīsu veids un pagatavošanas stāvoklis tur izvēlēts. Piemēram, Japānas Lauksaimniecības ministrijas norādītajā parastajā pagatavošanas aprakstā masas pieaugums ir citāds; vienu gatavās masas koeficientu nevajag uzskatīt par nemainīgu visām receptēm. [MAFF](https://www.maff.go.jp/j/heya/kodomo_sodan/0103/01.html).

##### Kā uzskaitīt bez sajukuma

Ja sver sausos rīsus, izmanto ierakstu par sausiem rīsiem. Ja sver gatavu porciju, izvēlies atbilstošu gatavā ēdiena ierakstu vai aprēķini porcijas daļu no sava nosvērtā kopējā daudzuma. Eļļa, sviests un citas piedevas jāuzskaita atsevišķi.

Apgalvojums “vārīšanā nekas nekad nemainās” būtu pārāk plašs. FAO apraksta, ka, vārot liekā ūdenī un to nolejot, var aizskalot arī cieti un citas sastāvdaļas. Dotajā kontrolpiemērā šo zudumu nav pēc uzdevuma nosacījuma. [FAO par pagatavošanas zudumiem](https://www.fao.org/4/t0567e/T0567E0i.htm).

##### Paņēmiens, kas pārnesams tālāk

Pirmais paņēmiens ir nošķirt kopējo daudzumu no rādītāja “uz 100 g”; tas te pārbaudīts ar aprēķinu. Otrs — vienai pagatavošanas reizei saglabāt izmērītu sausās un gatavās masas attiecību. Otrais te ir priekšlikums, jo īsti rīsi nav vārīti vai svērti.


*Izpildītā aprēķina faili:* [calculation.json](validation/2026-11-09-beta3/calculations/NE03/calculation.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NE03/calculation.py)

*Izpētes izcelsme: NE03; 5 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `8d1e62bec67334265dfa32fa0241e748b46cfa9360404540c8e1110c815fc401`.*

<a id="final30-ne04"></a>

#### NE04 — Baltas un miglainas glāzes

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Glāzes pēc mašīnas baltas miglainas. Mazgāt vēlreiz vai mest ārā, viņa vispār kaut ko izmazgā?

*Pārbaudes nosacījumi:* Aparāta modelis un ūdens cietība nav zināmi. Atšķir mazgāšanas/nosēdumu problēmu un pastāvīgu stikla virsmas bojājumu. Piedāvā mazu saudzīgu atšķiršanas pārbaudi ar skaidru robežu; neizdomā diagnozi.

##### Izpētītā atbilde

**Vispirms pārbaudi vienu glāzi — uzreiz visas izmest nevajag.** Līdzīgs miglojums var rasties no noņemamiem nosēdumiem vai pašas stikla virsmas bojājuma. Ražotāji šos gadījumus nodala; atkārtota mazgāšana nevar atjaunot jau izēstu virsmu. [Bosch](https://www.bosch-home.com/de/bosch-erleben/magazin/haushaltstipps/kalk-glaeser-entfernen), [GE Appliances](https://products.geappliances.com/appliance/gea-support-search-content?contentId=21917).

Ja tā ir parasta, nedekorēta dzeramā glāze un tās kopšanas norādes to pieļauj, nelielu miglainu laukumu saudzīgi noslauki ar baltajā galda etiķī samitrinātu mīkstu drāniņu. Pēc tam rūpīgi noskalo un nosusini. Šādu lokālu noslaucīšanu minerālu pēdām apraksta Panasonic. [Panasonic norāde](https://jpn.faq.panasonic.com/app/answers/detail/a_id/100749/).

- **Ja laukums kļūst dzidrs**, vismaz šī miglojuma daļa bija noņemams nosēdums. Tad ir jēga pārbaudīt ūdens cietību, ierīces mīkstināšanas iestatījumu un līdzekļu dozēšanu pēc konkrētā modeļa instrukcijas.
- **Ja nekas nemainās**, virsmas bojājums ir viena iespēja. Viens mājas mēģinājums to vēl nepierāda; arī par visu glāžu stāvokli no tā nevar secināt.
- **Ja stikls ir vērtīgs, sens, apgleznots vai jau lobās**, šo sadzīves paņēmienu automātiski nepārnes uz to. V&A restauratori šādus priekšmetus aplūko atsevišķi un norāda, ka agresīva apstrāde var bojāt pašu virsmu. [V&A stikla kopšanas vadlīnijas](https://vanda-production-assets.s3.amazonaws.com/2019/04/03/14/23/08/658c998f-990b-4586-9a81-b9e7eb95f620/caring_for_glass.pdf).

Tālāk noderētu glāzes kopšanas marķējums, mašīnas modelis, izmantotais līdzeklis un ziņa, vai baltas pēdas ir arī uz citiem traukiem. Bez šīm ziņām “mašīna nemazgā” vai “visas glāzes sabojātas” būtu minējums. Bosch iesaka ierīces iestatījumus pieskaņot ūdens cietībai. [Ražotāja skaidrojums](https://www.bosch-home.com/de/bosch-erleben/magazin/haushaltstipps/kalk-glaeser-entfernen).

##### Kas šajā pārbaudē paveikts

Pārbaudīti avoti un izveidota nosacīta rīcības kārtība. Īstas glāzes, ūdens vai mašīna nav pārbaudīta.

Inovācijas daļā pārnests materiālu diagnostikas paņēmiens: vispirms atšķirt noņemamu virsmas slāni no pašas virsmas izmaiņas. Otrs apsvērtais paņēmiens ir mainīt vienu ierīces iestatījumu reizē un salīdzināt rezultātu uz vienas atsauces glāzes. Tas paliek praktiski izmēģināms, ievērojot konkrētā modeļa norādes. Restaurācijas avots palīdzēja noteikt, kur sadzīves paņēmiena pārnese jāpārtrauc.


*Izpētes izcelsme: NE04; 5 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `dfdeab62bd4a86a5588a0b76712c3cce1adf33b4934c1b41f469c9309f66fa99`.*

### 10 vidēji sarežģīti jautājumi dažādās nozarēs

<a id="final30-p02"></a>

#### P02 — Spēles tulkošana, saglabājot vietturus

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Gribu iztulkot viena spēlētāja spēli latviski, nezaudējot vietturus un tekstu kontekstu. Kādu brīvā koda darba kārtību izvēlēties?

TESTA SIMULĀCIJA: JSON virknes ar {player_name}, daudzskaitļa formām un dialogu ID; izpildāmu failu labošana neietilpst uzdevumā.

##### Izpētītā atbilde

Šim JSON piemēram izvēlētos Git kopā ar Weblate un pārbaudāmu importa/eksporta soli. Pieņēmums nāk no testa precizējuma: failā ir `{player_name}`, daudzskaitļa formas un dialogu ID. Konkrētās spēles faili nav apskatīti.

Weblate ir pašmitināms brīvā koda risinājums ar [GPL-3.0-or-later licenci](https://docs.weblate.org/en/latest/contributing/license.html). Taču pirms tulkošanas jānosaka JSON paveids: [vispārīgais JSON lasītājs](https://docs.weblate.org/en/latest/formats/json.html) pats neatbalsta daudzskaitļa grupas un konteksta laukus; [i18next JSON v4 lasītājs](https://docs.weblate.org/en/latest/formats/i18next.html) daudzskaitli atbalsta. Spēles shēma jāņem par pamatu, un i18next drīkst izvēlēties tikai tad, ja faili tam tiešām atbilst.

Darba kārtību veidotu šādi:

1. Saglabā oriģinālus un piesaisti katru tulkojumu stabilam dialoga ID. Tulkot drīkst teksta vērtības; ID, vietturu nosaukumus un JSON struktūru saglabā.
2. Katram dialogam pievieno runātāju, ainu, iepriekšējo/nākamo repliku un, kur vajag, ekrānattēlu. Šo papildu kontekstu glabā Weblate vai atsevišķā kartē pēc ID, ja spēles fails to neparedz. [Weblate konteksta iespējas](https://docs.weblate.org/ja/latest/user/translating.html).
3. Ieslēdz pārbaudi īstajai vietturu sintaksei. `python-brace-format` der, ja spēle lieto atbilstošu iekavu sintaksi; `strict-format` var liegt skaitļa viettura izlaišanu vienskaitļa formā. Citai sintaksei vajag citu pārbaudi. Automātiska atpazīšana nav garantija. [Pārbaudes](https://docs.weblate.org/en/latest/user/checks.html), [pārbaudes nosacījumi](https://docs.weblate.org/zh-cn/latest/user/checks.html).
4. Daudzskaitli salāgo ar spēles noteikumiem. CLDR latviešu kardinālajiem skaitļiem definē `zero`, `one` un `other`, arī daļskaitļu nosacījumus; spēle šīs kategorijas var attēlot savā shēmā. [CLDR tabula](https://www.unicode.org/cldr/charts/49/supplemental/language_plural_rules.html).

Vieglāka alternatīva vienam tulkotājam ir [Translate Toolkit `json2po/po2json`](https://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/json2po.html) ar PO redaktoru. Tas pievieno pārveides posmu, kura atgriezeniskums jāpārbauda; avota un tulkojuma revīzijām jāsakrīt. [Toolkit licences teksts](https://github.com/translate/translate/blob/master/COPYING) ir GNU GPL v3.

Sāktu ar 30 dažādām rindām. Vispirms importētu un eksportētu nemainītu tekstu, pēc tam salīdzinātu struktūru, ID un vietturus. Tulkojumā pārbaudītu arī diakritiku, teksta garumu un daudzskaitli pašā spēlē. Pieņemšanas nosacījums: neviena pazudusi atslēga vai neatļauti mainīts vietturis. Ja pārbaude neizdodas, lielo tulkojumu nesāktu.

Dokumentācija un Weblate vietturu pārbaudes klase ir apskatīta; instalēšana un spēles pārbaude nav veikta. Jauna tulkošanas platforma šobrīd nav pamatota. Precīzam importa rīkam vēl vajadzīgs spēles nosaukums un īsts JSON paraugs.


*Izpētes izcelsme: P02; 5 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `48a22fa21d508f6a59b79dc60397392063cff8ed5fa0d121cd423fa5cb725364`.*

<a id="final30-p04"></a>

#### P04 — HDR video pārveidošana uz SDR

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Gribu video HDR pārvērst SDR, lai krāsas nav pelēkas. Ko man jāzina pirms FFmpeg komandas?

TESTA SIMULĀCIJA: H.265, BT.2020/PQ, 10 biti; mērķis SDR Rec.709; lietotāja fails nav pieejams.

##### Izpētītā atbilde

Testa precizējumā dots H.265 video ar BT.2020/PQ un 10 bitiem, kura mērķis ir SDR Rec.709. Šādai ievadei vajag gan spilgtuma diapazona pārveidi, gan pareizu krāsu pārveidi. Vienkārši pārrakstīt faila atzīmi uz “BT.709” nepietiek: FFmpeg `setparams` maina īpašību atzīmes, nepārrēķinot pašu attēlu. [Filtru dokumentācija](https://www.ffmpeg.org/ffmpeg-filters.html#setparams).

Pirms gala komandas pārbaudītu:

- `color_primaries`, `color_transfer` un `color_space`: pamatkrāsu sistēmu, spilgtuma pārvades funkciju un matricu.
- `color_range`: vai ievade izmanto ierobežotu vai pilnu signāla diapazonu.
- Pikseļu formātu, bitu dziļumu un pieejamos HDR spilgtuma metadatus.
- FFmpeg versiju un pieejamos filtrus, kā arī ierīci, kurā SDR video jāatskaņo.

H.265 un 10 bitu norādes vien šos krāsu datus neaizstāj. Sākuma pārbaudei der šāda lasīšanas komanda:

```bash
ffprobe -v error -select_streams v:0 -show_streams -of json "input.mp4"
```

Tā izvada plūsmas informāciju; video netiek pārkodēts. [ffprobe dokumentācija](https://ffmpeg.org/ffprobe.html).

Parastā FFmpeg `tonemap` filtra gadījumā darbību secība ir: pareizi interpretēt PQ ievadi, pāriet uz lineāru gaismu ar peldošā komata datiem, pielāgot toņus SDR diapazonam, salāgot krāsas un izvadīt Rec.709. `zscale` palīdz veikt šīs krāsu un pārvades pārveides. Lineāras gaismas prasību skaidri norāda gan [pašreizējā dokumentācija](https://www.ffmpeg.org/ffmpeg-filters.html#tonemap), gan [filtra autora sākotnējā apspriede](https://ffmpeg.org/pipermail/ffmpeg-devel/2017-July/213824.html).

Izvēlēto toņu līkni vispirms izmēģinātu īsā fragmentā ar seju, tumšām vietām un spilgtām gaismām. SDR atskaņošanā pārbaudītu melno līmeni, gaismu detaļas un gala metadatus. Viena līkne, piemēram, Hable, nav automātiski piemērota katram materiālam.

Pelēkā attēla iespējamie cēloņi ir nepareiza PQ interpretācija, signāla diapazons vai atskaņotāja apstrāde. Bez video tie paliek pārbaudāmas hipotēzes. Nākamais solis ir `ffprobe` izdruka un īss paraugs; oriģinālu saglabā. Šajā piemērā video nav pārkodēts.


*Izpētes izcelsme: P04; 4 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `5749bc25a330d96888a7ba606477742be8dabbc6ce4712aeb4bd4dd0e57bcd93`.*

<a id="final30-p05"></a>

#### P05 — RAID1 un ģimenes fotogrāfiju rezerves kopijas

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Vai NAS ar RAID1 ir pietiekama ģimenes foto rezerves kopija?

##### Izpētītā atbilde

Ar RAID1 vien nepietiek, ja ģimenes foto atrodas tikai NAS. Tas vienlaikus glabā vienādus datus abos diskos un palīdz turpināt darbu viena diska kļūmes gadījumā. Dzēšana vai kaitīga pārrakstīšana var skart abus diskus. Arī visa NAS zudumam vajadzīga kopija ārpus šīs ierīces. To nošķir [Synology skaidrojums](https://blog.synology.com/de/was-ist-ein-backup/) un [Buffalo RAID apraksts](https://www.buffalo.jp/topics/trouble/detail/recovery_0005.html).

Ģimenes foto es veidotu šādu kārtību:

1. Foto oriģināli NAS vai datorā.
2. Regulāra kopija ar iepriekšējām versijām atsevišķā diskā; pēc kopēšanas disku atvieno.
3. Vēl viena kopija citā vietā, piemēram, šifrētā diskā pie tuvinieka. Mākonis ir iespējams, bet nav obligāts.

Tā ir mana praktiska rekomendācija, lai viena kļūme neskar visas kopijas. Bezsaistes šifrētas kopijas un regulāras atjaunošanas pārbaudes iesaka arī [CISA pamatnostādne](https://www.cisa.gov/sites/default/files/publications/CISA_MS-ISAC_Ransomware%20Guide_S508C_.pdf). Pats dokuments ir no 2020. gada; to nepiedāvāju kā jaunu 2026. gada pētījumu.

NAS momentuzņēmumi ir noderīgi iepriekšējā stāvokļa atgūšanai. Ja tie glabājas tikai tajā pašā ierīcē, tie neatrisina visas ierīces zudumu. Attālināta glabāšana šo situāciju maina: [QNAP dokumentācija](https://www.qnap.com/zh-tw/software/snapshots) apraksta momentuzņēmumu kopēšanu uz citu NAS un atjaunošanu tur.

Ja oriģināli saglabājas arī telefonā vai datorā, NAS jau var būt viena rezerves kopija. Jāpārbauda, vai sinhronizācija nepārnes dzēšanu uz otru vietu un vai saglabājas vecākas versijas.

Pirmais noderīgais tests: atjauno atsevišķā mapē dažus jaunus, vecus un iepriekš dzēstus attēlus. Atver tos un pārbaudi pilnu izšķirtspēju un vajadzīgos metadatus. Kopēšanas biežumu pieskaņo tam, cik nesenu foto zaudējums būtu pieņemams. Šo atjaunošanas testu es šeit neesmu izpildījis.


*Izpētes izcelsme: P05; 4 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `cf6c32af9cc0dca17d9ad2afc21227eae813854d9ad6de4a8f1038e9a0dce400`.*

<a id="final30-np01"></a>

#### NP01 — Mēslojuma izmēģinājums uz saulainas palodzes

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Man ir 12 vienādi bazilika stādi podiņos. Gribu salīdzināt divus mēslojumus; puse palodzes ir saulaināka. Kā 4 nedēļās veikt salīdzinājumu, lai nejauši nepierādītu tikai saules ietekmi?

*Pārbaudes nosacījumi:* Izstrādā izpildāmu izvietojumu, randomizāciju, mērījumu plānu un secinājumu robežas. Vairākas viena auga lapas nav neatkarīgi augi. Nepiešķir izmērītu rezultātu neizpildītam eksperimentam.

##### Izpētītā atbilde

Sakārto 12 stādus sešos pāros un katrā pārī nejauši piešķir vienam augam mēslojumu A, otram B. Trīs pārus novieto saulainākajā pusē, trīs mazāk saulainajā. Pārī abas vietas izvēlies iespējami līdzīgas. Katram mēslojumam tā būs seši augi, un katrā gaismas zonā pa trim. Tas ir randomizēts bloku plāns: bloks savāc līdzīgus apstākļus, bet mēslojumu salīdzina bloka iekšienē. [NIST skaidrojums](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm).

##### Izvietojums un piešķīrums

Numurē augus no 1 līdz 12 pirms mēslojuma piešķiršanas. Tabulas piešķīrumu izveidoju ar Python un fiksētu sēklu 20261109. Augšanas dati vēl nav iegūti. Katrā pārī kreisā un labā vieta ir divas blakus vietas vienādā attālumā no stikla. Ja gaisma mainās citā virzienā, pagriez pārus atbilstoši, lai vienā pārī būtu līdzīgākais apgaismojums.

| Pāris | Gaismas zona | Kreisā vieta: augs, mēslojums | Labā vieta: augs, mēslojums |
|---|---|---|---|
| 1 | Saulaināka | 6, B | 7, A |
| 2 | Saulaināka | 9, A | 11, B |
| 3 | Saulaināka | 2, B | 10, A |
| 4 | Mazāk saulaina | 4, A | 12, B |
| 5 | Mazāk saulaina | 5, B | 8, A |
| 6 | Mazāk saulaina | 1, A | 3, B |

Piešķīrumu saglabā visām četrām nedēļām. Alternatīvi katrā pārī vienreiz met monētu, kurš augs saņems A; otrs saņem B. Nepārkārto augus pēc tam, kad redzi, kurš aug labāk. Augus pāru starpā nepārvieto un neļauj vienam aizsegt otru.

##### Kas jāizdara un jāmēra

Pirms sākuma uzraksti salīdzināšanas noteikumu: katru līdzekli lietosi atbilstoši tā marķējuma devai un biežumam. Tādējādi salīdzināsi divas praktiskas mēslošanas programmas. Vienāds šķidruma tilpums viens pats nenozīmētu vienādu barības vielu devu. Podu izmēru, substrātu un kopšanas kārtību saglabā vienādus; mēslojuma šķīduma ūdeni ieskaiti kopējā laistījumā. Katram podam sava apakštase, lai iztecējušais šķīdums nesajauktu apstrādes.

Par galveno rādītāju šim vienkāršajam izmēģinājumam izvēlos stāda augstuma pieaugumu centimetros no 0. līdz 28. dienai. Tas mēra šo augšanas pazīmi; lielāks augstums pats par sevi vēl nenosaka lapu ražu vai garšu. Mēri no substrāta virsmas līdz viena un tā paša galvenā dzinuma galotnei, vienā diennakts laikā, pirms vai pēc laistīšanas pēc vienāda iepriekš izvēlēta noteikuma. Galotni šajā periodā nenoknieb.

0., 7., 14., 21. un 28. dienā katram augam pieraksti augstumu, lapu skaitu, bojājumus un pievieno foto ar lineālu. Pieraksti mēslojuma un ūdens devas, novirzes un aptuvenās tiešas saules stundas. Laisti pēc vienāda substrāta mitruma noteikuma, jo saulainākie podi var prasīt atšķirīgu ūdens daudzumu. Saglabā faktiski izlietoto daudzumu. Ja augs aiziet bojā, to reģistrē un neieliec jaunu augu vecā vietā kā turpinājumu.

12 augi reiz 5 mērīšanas dienas dod 60 augstuma ierakstus, taču eksperimentā ir 12 augi. Viena auga lapas un nedēļas nav jauni neatkarīgi mēslojuma atkārtojumi. Šeit uz podu atsevišķi piešķirto apstrādi pārnesu [NC3Rs eksperimentālās vienības principu](https://eda.nc3rs.org.uk/index.php/experimental-design-unit).

##### Kā salīdzināt

Katram augam aprēķini pieaugumu g = augstums 28. dienā − augstums sākumā. Katrā pārī aprēķini d = g(A) − g(B), un tad sešu pāru vidējo starpību: (d1 + d2 + d3 + d4 + d5 + d6)/6. Parādi arī visas sešas atsevišķās starpības un katras gaismas zonas trīs pārus. Pārbaudi, vai vidējo nosaka viens neparasts augs vai viena zona. Analīzē saglabā pārus; NIST bloku modelis salīdzinājumu veic, ņemot vērā bloku. Ja vajag formālu testu, ir tikai 2^6 = 64 iespējami A/B samainīšanas varianti pāros; izvēlēto statistiku un nulles hipotēzi nosaka pirms rezultātu apskatīšanas.

Četras nedēļas un seši augi katram mēslojumam dod nelielu salīdzinājumu šiem stādiem, šai palodzei un izvēlētajām devām. Vienāds rezultāts nepierādīs pilnīgu mēslojumu līdzvērtību. Bez nemēslotas grupas nevarēsi pateikt, vai abi mēslojumi pārspēj nemēslošanu. Japānas izmēģinājumu veicējs apraksta vietas apstākļu ievērošanu, atkārtojumus un atkārtotus izmēģinājumus; tas ir praktiskas organizācijas avots, ne pierādījums konkrētam bazilika mēslojumam. [Kimura, 2025](https://www.kankyo-kanri.co.jp/post/show?id=363).

##### Divas pārneses idejas

Rūpniecisko izmēģinājumu bloku princips jau ir izmantojams šajā plānā. Lētā pārbaude ir pirms sākuma pārliecināties, ka katrā pārī ir A un B un abas vietas saņem līdzīgu gaismu. Ja vienā pārī viena vieta ir pastāvīgā ēnā, vietas jāpārplāno pirms mēslošanas.

Otra iespēja ir akli nolasīt ar kodiem pārsauktus foto. [NC3Rs](https://eda.nc3rs.org.uk/experimental-design-blinding) apraksta apstrādes slēpšanu rezultātu vērtēšanas laikā. Šeit hipotēze ir, ka kodēšana mazinās vēlamā rezultāta ietekmi uz augstuma nolasījumu. Izmēģini to uz pieciem foto: atkārto nolasījumu nejaušā secībā, neapskatot A/B sarakstu. Ja foto nevar droši nolasīt līdz tava lineāla iedaļai, galvenajam mērījumam saglabā tiešu nolasījumu. Šīs idejas ieguvums šeit vēl nav izmērīts.


*Izpildītā aprēķina faili:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NP01/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NP01/calculation.py)

*Izpētes izcelsme: NP01; 5 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `2578c2c50eab70fef25501ea1989d4537ea515de93bd4ea59c511b6884b53bbf`.*

<a id="final30-np02"></a>

#### NP02 — Aizkaru audums un saraušanās

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Šuju divus kokvilnas aizkarus, katru gatavu 130 cm platu un 240 cm augstu. Malām kopā vajag 8 cm platumā, augšai un apakšai kopā 16 cm garumā. Audums 150 cm plats, garumā saraujas 5%, platumā 3%. Vai 5,2 m pietiks un kā pārbaudīt pirms griešanas?

*Pārbaudes nosacījumi:* Pieņem vienmērīgu norādīto saraušanos, bez raksta salāgošanas, bez brāķa un bez papildu rezerves. Izvērtē platumu un garumu atsevišķi; aprēķini teorētisko minimumu un izskaidro, kāpēc praksē vajadzīgs paša auduma paraugs.

##### Izpētītā atbilde

Pie dotās saraušanās 5,2 m nepietiek: teorētiskais minimums ir 5,389473684… m nesarauta auduma. 150 cm platums der. Ja audumu pārdod centimetros, matemātiski jānoapaļo uz augšu līdz 5,39 m; praktiska rezerve un parauga patēriņš šajā skaitlī nav ietverti.

##### Platumu un garumu rēķini atsevišķi

Gatavam aizkaram pieskaiti dotos atlokumus pirms saraušanās kompensācijas. Pēc iepriekšējās mazgāšanas jāvar izgriezt divus taisnstūrus, katru 138 × 256 cm.

| Lielums | Aprēķins | Rezultāts |
|---|---|---:|
| Viena paneļa platums pēc saraušanās, ar malām | 130 + 8 | 138 cm |
| Pieejamais auduma platums pēc saraušanās | 150 × 0,97 | 145,5 cm |
| Mazākais sākuma platums vienam panelim | 138 / 0,97 | 142,268041… cm |
| Viena paneļa garums pēc saraušanās, ar atlokiem | 240 + 16 | 256 cm |
| Viena paneļa sākuma garums | 256 / 0,95 | 269,473684… cm |
| Abu paneļu kopējais sākuma garums | 2 × 256 / 0,95 | 538,947368… cm |

Abi paneļi jāliek secīgi gar auduma rulli: divi 138 cm platumi blakus neietilpst 145,5 cm. Arī 256 cm garo malu pagriezt šķērsām nevar. Platuma atlikums pēc saraušanās ir 145,5 − 138 = 7,5 cm uz pilno platumu, nevis katrā malā. Aprēķini izmanto tieši uzdevuma izmērus un pieņēmumu par derīgu 150 cm sākuma platumu.

Saraušanās procentu rēķina no sākuma izmēra: pēc mazgāšanas paliek L × (1 − s). Tāpēc sākuma daudzumu iegūst, nepieciešamo gala izmēru dalot ar 0,95. Vienkārši pielikt 5% pie 5,12 m nepietiek: 5,12 × 1,05 = 5,376 m, kas pēc 5% saraušanās dod 5,1072 m. Garuma un platuma izmaiņu atsevišķu mērīšanu paredz arī [AATCC TM135-2025 publiskais tvēruma apraksts](https://members.aatcc.org/store/tm135/543/) un [BOKEN pārbaudes kārtība](https://www.boken.or.jp/find_tests/textile_general_performance/dimensional_change/1134/).

##### Kas notiktu ar 5,2 m

520 × 0,95 = 494 cm. Vajag 512 cm, tātad pēc mazgāšanas trūktu 18 cm. Sadalot audumu uz pusēm, katrs gabals būtu 247 cm, un pēc 16 cm atlokiem paliktu 231 cm augstums, par 9 cm īsāks nekā vajadzīgs. Pirms mazgāšanas nepieciešamā starpība ir 18,947368… cm.

5,4 m teorētiski derētu, jo pēc saraušanās paliktu 513 cm. Tas ir tikai 1 cm vairāk par abiem piegriežamajiem paneļiem kopā, tāpēc 5,4 m nevar saukt par lielu praktisku rezervi. Parauga izgriešanu no šī paša garuma vajadzētu ieskaitīt papildus.

##### Kā pārbaudīt savu audumu

Paņem tās pašas drānas gabalu, vēlams atsevišķu paraugu no tās pašas partijas, un atzīmē garenvirzienu. Mājās lietojamam kontrolparaugam vari izvēlēties, piemēram, ap 30 × 30 cm gabalu un iekšpusē trīs 20 cm attālumus katrā virzienā. Precīzi pieraksti reālos sākuma attālumus; mērīšanai izmanto iekšējos punktus, lai izirušas malas netraucētu. Šis ir vienkāršots mājas tests, ne sertificēta standarta pārbaude.

Mazgā un žāvē tā, kā vēlāk kopsi aizkarus, ievērojot auduma kopšanas norādes. Izžuvušu audumu izlīdzini bez stiepšanas un atkārtoti nomēri tos pašus attālumus. Katram virzienam saraušanās procentu aprēķins ir 100 × (pirms − pēc) / pirms. BOKEN apraksta tieši atzīmētu garuma un platuma salīdzinājumu; tās formulā negatīva izmēra pārmaiņa nozīmē saraušanos. [Metode](https://www.boken.or.jp/find_tests/textile_general_performance/dimensional_change/1134/).

Ja 20 cm atzīme gareniski kļūst par 19 cm, tas būtu 5%; ja šķērsām kļūst par 19,4 cm, tas būtu 3%. Tie ir hipotētiski kontrolpiemēri, ne tava auduma mērījumi. Ja pēc vēl viena tāda paša kopšanas cikla izmērs turpina mainīties, pārrēķini pēc jaunajiem datiem. Šūšanas darbnīcas SO pašu trikotāžas eksperiments apraksta izmaiņas vairākos ciklos; to nevar izmantot kā saraušanās procentu šiem kokvilnas aizkariem. [SO pieredzes apraksts](https://sewing-so.com/pages/水通し実験データ).

Pirms gala griešanas izmazgā un izžāvē visu audumu paredzētajā režīmā, pārbaudi lietderīgo platumu un faktisko garumu, tad atzīmē divus 138 × 256 cm paneļus. Ja testam nogriezts gabals no ruļļa, atskaiti to no pieejamā garuma. Stingri 5,2 m pietiktu tikai tad, ja faktiski izmērītā gareniskā saraušanās nepārsniegtu aptuveni 1,5385% un visi pārējie uzdevuma nosacījumi izpildītos. Dotais 5% pieņēmums šo iespēju izslēdz.

##### Divu mehānismu pārnese

Pirmā ideja ir detaļu ražošanā lietotā izmēra pirmskompensācija. [Apple Rubber inženiera aprakstā](https://www.applerubber.com/hot-topics-for-engineers/350/) sākuma izmēru iegūst ar gala izmērs / (1 − saraušanās). Formula der arī šim uzdevumam, taču gumijas saraušanās vērtības uz audumu nepārnes. Aprēķina atpakaļpārbaude jau izpildīta: 538,947368… × 0,95 = 512 cm.

Otra ideja ir izmantot nelielu ražošanas kontrolparaugu pirms visas sagataves griešanas. Tas var atklāt atšķirību starp solīto un reālo saraušanos. Te priekšrocība ir pārbaudāma, bet vēl nav izmērīta: paraugs jāizmazgā, un tad abās asīs jāapstiprina, ka paliek vajadzīgie izmēri. Kopējā auduma minimumā parauga patēriņš nav paslēpts.


*Izpildītā aprēķina faili:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NP02/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NP02/calculation.py)

*Izpētes izcelsme: NP02; 6 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `4c17373fee18434e2a383bc3b38f4411cc7ad64b87ae576a55040e687d80a629`.*

<a id="final30-np03"></a>

#### NP03 — Ūdens uzsildīšana un sajaukšana

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Cik elektrības teorētiski vajag 80 litru ūdens uzsildīšanai no 10 līdz 60 °C, ja visa procesa lietderība ir 90% un elektrība maksā 0,15 €/kWh? Cik 60 °C ūdens vajag 50 litriem 40 °C maisījuma ar 10 °C auksto ūdeni?

*Pārbaudes nosacījumi:* Izmanto ρ = 1 kg/L un c = 4,186 kJ/(kg·K). Salīdzini siltumu, elektrību un cenu; maisījumam pieņem siltuma zudumu neesamību un vienādu blīvumu. Neiekļauj nenorādītos ilgstošās glabāšanas zudumus vai tirgus cenu pieņēmumus.

##### Izpētītā atbilde

80 litru ūdens uzsildīšanai vajag 4,6511 kWh siltuma. Pie 90% procesa lietderības tas nozīmē 5,1679 kWh elektrības un 0,7752 € jeb, noapaļojot līdz centiem, 0,78 €. 50 litriem 40 °C maisījuma vajag 30 litrus 60 °C ūdens un 20 litrus 10 °C ūdens.

##### Siltums, elektrība un cena

Visi skaitļi attiecas uz dotajiem teorētiskā uzdevuma nosacījumiem: ρ = 1 kg/L, c = 4,186 kJ/(kg·K), visa uzsildīšanas procesa lietderība η = 0,90 un cena 0,15 €/kWh.

Ūdens masa ir 80 kg, temperatūras pieaugums 60 − 10 = 50 K. Izmanto Q = mcΔT; šo sakarību dod arī [KIT laboratorijas apraksts](https://labs.physik.kit.edu/prakt-nebenfach-manuals/Experiments/Spezifische_w%C3%A4rme_Wasser/).

Q = 80 × 4,186 × 50 = 16 744 kJ = 4,651111… kWh.

Pārrēķinā izmantots 1 kWh = 3600 kJ, ko norāda [NIST vienību tabula](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b9).

Lietderība ir lietderīgās izejas un ieguldītās enerģijas attiecība: η = Q/E. Šādi efektivitāti skaidro [ASV Enerģētikas departaments](https://www.energy.gov/cmei/femp/articles/take-five-what-energy-efficiency). Tāpēc:

E = Q/η = 4,651111…/0,90 = 5,167901… kWh.

Cena = 5,167901… × 0,15 = 0,775185… €.

| Daudzums | Rezultāts |
|---|---:|
| Ūdenim nodotais siltums | 4,6511 kWh |
| Ieguldītā elektroenerģija | 5,1679 kWh |
| Dotā procesa zudumi, E − Q | 0,5168 kWh |
| Maksa par šo elektroenerģiju | ap 0,78 € |

Zudumi ir 10% no ieguldītās elektrības. Elektrības daudzumu tāpēc nevar iegūt, siltumam vienkārši pieskaitot 10%. Skaitliskā atpakaļpārbaude: 5,167901… × 0,90 = 4,651111… kWh.

0,15 €/kWh ir uzdevumā dots tarifs. Papildu ilgstošas glabāšanas zudumi aprēķinā nav iekļauti; tie nav doti. Arī tvertnes sildīšanu nepieskaitu vēlreiz, jo uzdevums jau nosaka visa procesa lietderību. Reāla aparāta novērtējumā būtu precīzi jānosaka šīs lietderības robeža. [Nippon Heater tehniskais aprēķins](https://www.nippon-heater.co.jp/designmaterials/calculation/) ūdens, tvertnes un siltuma zudumu daļas uzskaita atsevišķi, ja tās aprēķina no sākuma.

##### 50 litri 40 °C ūdens

Apzīmē karstā ūdens tilpumu ar x litriem. Aukstā ūdens būs 50 − x litri. Pie vienāda blīvuma un siltumietilpības, bez siltuma zuduma, karstā ūdens atdotais siltums ir vienāds ar aukstā saņemto:

x × (60 − 40) = (50 − x) × (40 − 10).

20x = 1500 − 30x, tātad x = 30 L.

Izmantoju [KIT aprakstīto kalorimetrijas bilanci](https://labs.physik.kit.edu/prakt-klass-physik-manuals/P2/Spezifische_Waermekapazitaet/doc/Hinweise-Waermekapazitaet-Mischung/), šeit piemērotu divām viena veida ūdens masām. Kopīgie c un ρ saīsinās.

Pārbaude: 30 + 20 = 50 L un (30 × 60 + 20 × 10)/50 = 40 °C. Karstais ūdens atdod 30 × 4,186 × 20 = 2511,6 kJ; aukstais saņem 20 × 4,186 × 30 = 2511,6 kJ. Šim atsevišķajam sajaukšanas solim vēlreiz nepiemēro 90%, jo tā nosacījums ir sajaukšana bez zudumiem.

##### Divas pārneses idejas

No procesu efektivitātes uzskaites var pārņemt ieejas un izejas salīdzinājumu: izmērīt elektrību noteiktā uzsildīšanas intervālā un salīdzināt ar mcΔT. Hipotēze ir, ka tas palīdzētu pārbaudīt, vai reālais aparāts konkrētajā režīmā sasniedz pieņemtos 90%. Mazajam testam vajadzīgs atsevišķs elektrības uzskaites intervāls, zināms ūdens daudzums un sākuma/beigu temperatūra. Tvertnes siltumu un citus patērētājus nedrīkst nepamanīti ieskaitīt ūdens siltumā. Šeit fizisks tests nav veikts.

Otru mehānismu, divu krājumu sajaukšanu līdz mērķa īpašībai, var izmantot kā vienkāršu daudzumu kalkulatoru: karstā daļa = (T_mērķis − T_auksts)/(T_karsts − T_auksts). Šoreiz tā ir 30/50 = 0,60. Kods pārbaudīja gan tilpumu, gan siltuma bilanci; praktisks ieguvums un precizitāte konkrētā tvertnē vēl nav mērīti. Pārnesot šo formulu uz citām vielām, būtu jāpārbauda blīvums, siltumietilpība un sajaukšanās siltums, tāpēc ūdens vienkāršojumu universāli neizmanto.


*Izpildītā aprēķina faili:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NP03/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NP03/calculation.py)

*Izpētes izcelsme: NP03; 5 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `1f4870d93ee5f77de086383a64dc84ee59d1ce1896c6a8e853a5240edc673a78`.*

<a id="final30-np04"></a>

#### NP04 — Ogle, jonapmaiņa un reversā osmoze

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Krāna ūdens analīzē cietība 280 mg/L kā CaCO₃ un brīvais hlors 0,4 mg/L. Vai parasts aktīvās ogles krūzes filtrs noņems gan hloru, gan kaļķi? Kā atšķirt ogli, jonapmaiņu un reverso osmozi pēc faktiskas pārbaudes?

*Pārbaudes nosacījumi:* Nav dots konkrēts produkts. Salīdzini mehānismus, ko apliecina attiecīgie ražotāja/sertifikācijas ieraksti, un pirms/pēc mērījumu. Neapgalvo, ka ūdens analīze pati nosaka tā pilnu dzeramības drošumu.

##### Izpētītā atbilde

Kasetne, kurā ir tikai aktīvā ogle, var samazināt brīvo hloru; būtisku ūdens cietības samazinājumu no tās nevajag gaidīt. Ja krūze samazina arī kaļķošanos, pārbaudi, vai tajā papildus nav jonapmaiņas sveķu. Bez konkrētas kasetnes nosaukuma nevar noteikt samazinājuma procentu vai lietošanas ilgumu.

Ražotāja BRITA piemērs parāda atšķirību vienas produktu saimes iekšienē: tā apraksta ogles un jonapmaiņas kombināciju atsevišķi no tikai ogli izmantojoša elementa, kurš saglabā kalciju un magniju. Tas ir mehānisma piemērs, ne ieteikums pirkt šo zīmolu. [Ražotāja FAQ, sadaļas par filtru saturu](https://www.brita.at/faq/filter-filterkartuschen?sc=maxtra-pro).

##### Kā atšķiras trīs mehānismi

| Apstrāde | Ko tā dara šajā uzdevumā | Ko meklēt dokumentos un mērījumos |
|---|---|---|
| Aktīvā ogle | Brīvā hlora samazināšanā darbojas arī oksidēšanās un reducēšanās reakcijas; smaku izraisošu vielu samazināšanai izmanto adsorbciju. Izšķīdušo Ca/Mg mazināšanu no ogles vien neizsecina. | Konkrēts hlora samazināšanas apliecinājums; brīvā hlora tests pirms/pēc. Cietību mēra atsevišķi. |
| Jonapmaiņa | Mīkstināšanā sveķi Ca/Mg aizvieto ar citiem joniem. Nātrija vai kālija mīkstinātājs nav visu izšķīdušo sāļu izņemšana. Krūžu sveķu sastāvs un karbonātiskās cietības samazināšana var atšķirties. | Precīzs sveķu un sistēmas apraksts; kopējās cietības tests. Ja solīta tieši karbonātiskās cietības mazināšana, papildus jānosaka sārmainība. |
| Reversā osmoze | Spiediens virza ūdeni caur puscaurlaidīgu membrānu; sistēma samazina izšķīdušo vielu daudzumu. Daudzās sistēmās ir arī citi filtri. | Membrānas sistēmas dati un TDS samazināšanas apliecinājums; vadītspēja/TDS un cietība pirms/pēc. Par hlora samazināšanu spriež pēc visas sistēmas dokumentiem. |

Ogles ķīmisko darbību apraksta [Japānas ūdens filtru asociācija](https://www.jwpa.or.jp/qa01.htm). Jonapmaiņu un reverso osmozi skaidro [NSF standartu pārskats](https://www.nsf.org/consumer-resources/articles/standards-water-treatment-systems), bet sveķu resursa izsīkšanu un cietības testus apraksta [Hach](https://my.hach.com/parameters/hardness).

280 mg/L kā CaCO₃ ir cietības izteikšanas veids vienotā ekvivalentā. Tas nenozīmē, ka litrā peld 280 mg kaļķa daļiņu, ko pietiktu izsijāt. Hach nošķir cietību, ko pārsvarā veido kalcija un magnija joni, no sārmainības; abām ērtības labad var lietot mg/L kā CaCO₃. Ar vienu kopējās cietības skaitli karbonātisko daļu nenosaki. [Definīcijas](https://my.hach.com/parameters/hardness).

##### Ko apliecina sertifikācija

NSF/ANSI 42 ietver, piemēram, hlora un garšas/smakas samazināšanas prasības. NSF/ANSI 44 attiecas uz ar Na/K sāli reģenerējamiem katjonapmaiņas mīkstinātājiem; tas automātiski neapliecina jebkuras krūzes kasetni. NSF/ANSI 58 RO sistēmām paredz obligātu TDS samazināšanas pārbaudi, bet vairākas citu vielu prasības ir izvēles. Jāpārbauda tieši sava modeļa un kasetnes ieraksts, konkrētā viela, lietošanas nosacījumi un deklarētais resurss. [NSF pārskats](https://www.nsf.org/consumer-resources/articles/standards-water-treatment-systems), [NSF/ANSI 58 tvērums](https://www.nsf.org/knowledge-library/nsf-ansi-58-reverse-osmosis-drinking-water-treatment-systems).

NSF atvērtajā komponentu sarakstā ir arī ieraksts ar piezīmi “Conforms to the material requirements only”. Tādēļ sertifikācijas logo vai standarta numurs uz komponenta pats par sevi vēl neapliecina hlora vai cietības samazinājumu. Nolasītā saraksta iekšējais aktualitātes datums ir 2026. gada 1. septembris; tas izmantots piezīmes nozīmes demonstrācijai, ne šodienas konkrēta produkta statusa apstiprināšanai. [NSF ieraksts](https://info.nsf.org/Certified/DWTU/Listings.asp?Standard=042&TradeName=carbon&hdModlStd=ModlStd&submit3=Search).

##### Praktiska pārbaude

Vispirms atrodi kasetnes sastāvu un sagatavošanas instrukciju, uzstādi un izskalo to, kā noteikts. Vienā reizē paņem ieplūdes ūdeni un pēc filtrēšanas izplūdes ūdeni. Pieraksti datumu, temperatūru, filtrēto tilpumu un kasetnes iepriekš caurlaistos litrus.

Brīvo hloru mēri ar tieši brīvajam hloram paredzētu DPD testu, kura diapazons un izšķirtspēja der 0,4 mg/L un gaidāmajai zemākajai vērtībai. Ievēro komplekta nolasīšanas laiku; “kopējais hlors” ir cits rādītājs. Hach apraksta arī hloramīna radītu traucējumu DPD brīvā hlora mērījumam, tāpēc nestabilu krāsas maiņu nevajag pārvērst par pārliecinošu filtra rezultātu. [Hach tehniskie jautājumi](https://sea.hach.com/parameters/faq).

Cietībai izmanto kopējās cietības titrēšanas komplektu ar diapazonu, kas aptver 280 mg/L kā CaCO₃. EDTA pilienu titrēšana ir piemērotāka skaitliskam salīdzinājumam nekā rupjas krāsu joslas; Hach brīdina, ka teststrēmeles nav paredzētas precīzai cietības vērtībai. [Cietības mērīšana](https://my.hach.com/parameters/hardness).

RO gadījumā papildini ar vadītspējas vai TDS nolasījumu vienādos temperatūras un kalibrācijas apstākļos. Elektronisks TDS skaitlis var būt pārrēķins no vadītspējas: [Hach rokasgrāmata](https://cdn.hach.com/7FYZVWYB/at/v5p779fgxpgwkr28fxxk3/DOC3439780079_10ed.pdf) skaidri norāda pārrēķina koeficientu. Šāds skaitlis nav tiešs Ca/Mg vai hlora mērījums. Nātrija jonapmaiņā cietība var krist, saglabājoties citiem izšķīdušiem joniem. Ļoti zems TDS viens pats arī nepierāda, ka izmantota tieši RO: tehnoloģiju apstiprina dokumenti un iekārtas uzbūve.

Atkārto vismaz trīs pirms/pēc paraugu pārus. Hloram paturi arī nefiltrētu kontrolparaugu tikpat ilgi, cik prasīja filtrēšana, lai laika ietekmi nepierakstītu filtram. Tas ir ierosināts salīdzinājuma plāns. Atkārto to pie vēlākas kasetnes lietošanas stadijas, nepārsniedzot ražotāja maiņas noteikumus.

Samazinājums (%) = 100 × (pirms − pēc) / pirms. Hipotētiskā piemērā cietība 280 → 140 mg/L dotu 50%, bet hlors 0,4 → 0,04 mg/L dotu 90%. Šie pēcfiltra skaitļi nav izmērīti. Rezultātu zem noteikšanas robežas raksta, piemēram, “< testa noteikšanas robeža”, nevis pieņem par precīzu nulli.

##### Divas pārneses idejas un robeža

Pirmā ir laboratoriju pieeja ar dažādiem, savstarpēji papildinošiem mērījumiem: hlors, cietība, vadītspēja. Hipotēze ir, ka tā ļauj atklāt gadījumu, kad labāka garša tiek sajaukta ar mīkstināšanu. Tests ir iepriekš minētie paraugu pāri un kasetnes dokumentu salīdzinājums. Viena indikatora uzlabojumu nepārnes uz pārējiem.

Otra ir komponenta kalpošanas gaitas pārbaude: pieraksta caurlaistos litrus un atkārto tos pašus mērījumus. Jonapmaiņas sveķu izsīkšanu pēc cietības uzrauga arī Hach aprakstītajā rūpnieciskajā procesā. Mājas pārneses hipotēze ir savlaicīgi pamanīt efekta krišanos; bez sava filtra mērījumiem nomaiņas brīdi aprēķināt nevar.

Šīs divas sākotnējās analīzes vērtības un minētie pirms/pēc testi nenosaka ūdens pilnu dzeramības drošumu. Arī NSF uzsver, ka sertifikācija vienam standartam nenozīmē visu iespējamo piesārņotāju samazināšanu. [NSF](https://www.nsf.org/consumer-resources/articles/standards-water-treatment-systems).


*Izpildītā aprēķina faili:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NP04/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NP04/calculation.py)

*Izpētes izcelsme: NP04; 7 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `c70408c0cdcf78bf8954df8482a6bf273fd2f85f0b6af28262f2cd154496466d`.*

<a id="final30-np05"></a>

#### NP05 — Vai pieņemt lētāku papildu pasūtījumu

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Darbnīcā krūzi pārdod par 24 €, materiāli un iepakojums 9 €, samaksa par katru saražoto krūzi 6 €. Mēneša pastāvīgās izmaksas 360 €. Ir 120 krūžu jauda; pamatpasūtījums ir 40 krūzes. Papildu klients grib 30 par 18 €. Vai pieņemt un cik krūzes jāpārdod parastajā cenā, lai nosegtu izmaksas?

*Pārbaudes nosacījumi:* Šis ir hipotētisks uzdevums: nodokļi, komisijas un ārējās cenas jau izslēgtas; papildu pasūtījums neizspiež pamatpasūtījumu. Nošķir ieņēmumus, mainīgās izmaksas, seguma summu un peļņu; parādi arī nosacījumu, kurā secinājums mainītos.

##### Izpētītā atbilde

**Dotajos apstākļos papildu pasūtījumu ir izdevīgi pieņemt: tas dod 90 € papildu peļņas. Tikai parastajā cenā jāpārdod 40 krūzes, lai nosegtu mēneša izmaksas.** Ja garantēti pārdod arī visas 30 papildu pasūtījuma krūzes par 18 €, pietiek ar 30 krūzēm parastajā cenā; tad kopējais pārdotais daudzums ir 60.

Šis ir uzdevuma hipotētiskais aprēķins, nevis novērotas darbnīcas darbības rezultāts. Pieņemu, ka norādītās saražotās krūzes arī pārdod un ka 360 € pastāvīgās izmaksas dotajā jaudas robežā nemainās.

##### Aprēķins

Vienas krūzes mainīgās izmaksas ir **9 + 6 = 15 €**. Samaksu par katru saražoto krūzi ieskaitu arī papildu pasūtījumā: brīva jauda neatceļ gabaldarba samaksu. Pie parastās cenas krūze dod **24 − 15 = 9 €** izmaksu segšanai, pie īpašās cenas — **18 − 15 = 3 €**.

Seguma summa ir ieņēmumi mīnus mainīgās izmaksas. Peļņa rodas pēc pastāvīgo izmaksu atskaitīšanas. Šīs definīcijas un izmaksu segšanas formulu pārbaudīju [ACCA skaidrojumā par pārdošanas apjomu un izmaksām](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f5/technical-articles/CVP-analysis.html).

| Rādītājs | 40 krūzes par 24 € | Papildu 30 par 18 € | Abi pasūtījumi |
|---|---:|---:|---:|
| Ieņēmumi | 960 € | 540 € | 1500 € |
| Mainīgās izmaksas | 600 € | 450 € | 1050 € |
| Seguma summa | 360 € | 90 € | 450 € |
| Pastāvīgās izmaksas | 360 € | 0 € papildu | 360 € |
| Peļņa / peļņas pieaugums | 0 € | +90 € | 90 € |

Kopā jāizgatavo **70 krūzes**, tāpēc no 120 krūžu jaudas paliek **50 krūžu rezerve**. Lietotājs jau noteicis, ka papildu pasūtījums neizspiež pamatpasūtījumu. Pie brīvas jaudas pasūtījuma lēmumā salīdzina tā radītos papildu ieņēmumus ar papildu izmaksām; nemainīgās kopējās pastāvīgās izmaksas vēlreiz šim lēmumam nepieskaita. Šo loģiku apraksta [OpenStax nodaļa par īpašajiem pasūtījumiem](https://openstax.org/books/principles-managerial-accounting/pages/10-2-evaluate-and-determine-whether-to-accept-or-reject-a-special-order); līdzīgs brīvās jaudas piemērs ir [Niigatas universitātes mācību materiālā](https://www.nuis.ac.jp/pub/common/pdf/2020/or_kanrikaikei_2.pdf).

##### Cik pārdot, lai izmaksas būtu segtas?

**Bez papildu pasūtījuma:**


$$
Q=\frac{360}{24-9-6}=40.
$$


Pārbaude: 40 × 24 = 960 € ieņēmumu; 40 × 15 + 360 = 960 € izmaksu. Pie 39 krūzēm būtu 9 € zaudējumi, pie 41 — 9 € peļņa.

**Ar noteikti izpildītu papildu pasūtījumu:**


$$
9Q+30\times3-360=0,\qquad Q=30.
$$


Tādā gadījumā 30 parastās un 30 īpašās cenas krūzes dod 1260 € ieņēmumu, 900 € mainīgo izmaksu un 360 € seguma. Tas ir cits pārdošanas sastāvs. Dotais pamatpasūtījums jau ir 40 krūzes, tāpēc faktiskajā uzdevuma scenārijā rezultāts ir 90 € peļņa, nevis nulle.

##### Kad lēmums mainītos?

Turpmākie piemēri **maina sākotnējos nosacījumus**; tie nav papildu slēptās izmaksas, ko pieskaitu dotajam uzdevumam.

- Ja tieši šī pasūtījuma dēļ rastos papildu vienreizējas izmaksas (K), peļņas pieaugums būtu **90 − K**. Pie 90 € pasūtījums vairs nepalielinātu peļņu; virs 90 € to finansiāli nebūtu izdevīgi pieņemt.
- Ja jauda kļūtu pilna un pasūtījums izspiestu (q) parastās cenas krūzes, pie vienādām vienības izmaksām pieaugums būtu **90 − 9q**. Desmit izspiestas krūzes izdzēstu visu ieguvumu; 11 dotu −9 €, bet visu 30 aizstāšana — −180 €.

Alternatīvā pasūtījuma zaudētā seguma iekļaušanu pamato [ACCA materiāls par lēmumam nozīmīgām izmaksām](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f5/technical-articles/relevant-costs.html). Tajā esošo jau apmaksātu dīkstāves stundu piemēru šeit nepārnesu uz 6 € gabaldarba samaksu — tie ir atšķirīgi nosacījumi.

##### Divas pārneses idejas un to pārbaude

**1. Jaudas vērtība no matemātiskās optimizācijas.** Resursa ēnas cena raksturo, kā mērķa rezultātu maina papildu resursa vienība; šo jēdzienu pārbaudīju [SAS dokumentācijā](https://support.sas.com/documentation/cdl/en/ormpug/66107/HTML/default/ormpug_optmodel_sect102.htm). Hipotēze: pirms cenas noraidīšanas jānoskaidro, vai jauda ir saistoša un kāds pasūtījums tiktu zaudēts. Šeit atlikušās 50 vietas nozīmē, ka dotie pasūtījumi nekonkurē par jaudu. Izpildītais tests salīdzina nulles un 10, 11, 30 krūžu izspiešanu. Ideja ir lietderīga nosacījumu pārbaudei; šim divu pasūtījumu uzdevumam optimizācijas programma nav vajadzīga.

**2. Robežpārbaude no eksperimentu un programmatūras pārbaudes.** Hipotēze: lēmumu var padarīt pārbaudāmu, mainot vienu pieņēmumu un pārbaudot abas sliekšņa puses. Kodā izpildīti 39/40/41 un 29/30/31 krūžu gadījumi, kā arī 90 € papildu izmaksu robeža. Visi sakrīt ar tiešo ieņēmumu un izmaksu bilanci. Šis ir aprēķina tests, nevis pierādījums par īsta uzņēmuma pieprasījumu vai ražošanu.

Avoti nolasīti 2026. gada 9. novembrī. EN, DE, ZH un JA meklējumi saglabāti; ar praktisku darbnīcas novērojumu šie skaitļi nav salīdzināti. Aprēķins pārbaudīts ar izpildītu kodu un viena aģenta pārskatījumu; neatkarīgs ārējais vērtējums vēl nav veikts.


*Izpildītā aprēķina faili:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NP05/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NP05/calculation.py)

*Izpētes izcelsme: NP05; 6 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `88e58e88ef87ca52b9b6672580a69df6bdc096c92c28f85b4a8734af264c9d61`.*

<a id="final30-np06"></a>

#### NP06 — Vēsturiska Rīgas adrese

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Vecā Rīgas adresu grāmatā atradu ielas nosaukumu un mājas numuru. Vai varu to vienkārši pielīdzināt šodienas adresei? Izveido pārbaudes kārtību un demonstrē vienu īstu Rīgas ielas pārdēvēšanas piemēru ar avotiem.

*Pārbaudes nosacījumi:* Konkrēta privāta adrese nav dota. Neizdomā ēkas identitāti. Pārbaudi vēsturiskā nosaukuma periodu, numerācijas un ielas trases izmaiņu iespēju; izmanto LNB/arhīva/muzeja/pašvaldības pirmavotus. Svešvalodu meklējums var dot tukšu rezultātu; atzīmē to.

##### Izpētītā atbilde

**Veco ielas nosaukumu un mājas numuru nevar automātiski pārvērst šodienas adresē.** Vispirms jāatrod attiecīgā laika iela un tās posms, pēc tam jāpārbauda numura pēctecība un pati ēka. Vienāds numurs vai līdzīgs nosaukums dod meklēšanas pavedienu, nevis pierādītu atbilstību.

Konkrēts gads, nosaukums un privāta adrese nav doti, tādēļ ēku šeit neidentificēju. Zemāk ir izpildāma pārbaudes kārtība un dokumentēts pārdēvēšanas piemērs.

##### Pārbaudes kārtība

1. **Nofiksēt sākotnējo ierakstu.** Saglabāt adresu grāmatas nosaukumu, izdevuma gadu, lappusi un lapas attēlu. Pārrakstīt ielu, numuru, burtu vai korpusa apzīmējumu tieši kā oriģinālā. OCR tekstu salīdzināt ar attēlu; grāmatas izdošanas gadu nošķirt no tajā aprakstītā datu perioda. Reāls meklēšanas sākumpunkts ir [LNB 1846. gada Rīgas adresu grāmatas ieraksts](https://dom.lndb.lv/data/obj/419752.html). Šajā izpētē nolasīti tā metadati, nevis konkrēta nama ieraksts grāmatā.

2. **Izveidot datētu nosaukumu ķēdi.** Noskaidrot nosaukuma lietošanas periodu, vācu/krievu rakstības variantus un pārdēvēšanas dokumentu. [Rīgas vēstures un kuģniecības muzejs apraksta LNB un muzeja izdoto ielu nosaukumu rādītāju](https://www.rigamuz.lv/rvkm/izdevumi/rigas-ielu-laukumu-parku-un-tiltu-nosaukumu-raditajs-no-18-gs-lidz-musdienam/); bibliogrāfisks ieraksts vēl nenozīmē, ka ir pārbaudīta vajadzīgā grāmatas lappuse. Periodu nozīmi rāda [LNB Brīvības ielas autoritatīvais ieraksts](https://dati.lnb.lv/onto/nll_geo/lv/page/LNC10-000282215?clang=en): tajā Ādolfa Hitlera alejas nosaukumam dots 1942.–1944. gads, bet Ļeņina ielas nosaukumam — sākums 1950. gadā. Šos dažādu laiku variantus nedrīkst uztvert kā vienlaicīgas adreses.

3. **Pārbaudīt ielas posmu un trasi.** Tā laika kartē atrast krustojumus, kvartālu, ielas galus un orientierus. Salīdzināt ar mūsdienu karti: vai iela nav sadalīta, pagarināta, apvienota vai novirzīta? [LNB Karšu lasītavas apraksts](https://lnb.gov.lv/en/maps-reading-room/) norāda, ka tās karšu pārlūks ļauj salīdzināt vēsturiskos un mūsdienu datus. Šī iespēja ir pārbaudīta avota aprakstā; konkrēta zemesgabala kartes šeit nav savietotas.

4. **Atsevišķi pārbaudīt numerāciju.** Salīdzināt adresu grāmatas pirms un pēc pārmaiņas, meklēt pārnumurēšanas vai adresācijas lēmumu. Pārbaudīt ielas pusi, blakus numurus, stūra namu adreses, zemesgabalu sadalīšanu/apvienošanu un to, vai numurs attiecas uz namu vai citu uzskaites objektu. [GEO RĪGA datu apraksts](https://georiga.eu/en/atvertie-dati/rigas-ielas-un-adreses/) nošķir ēkas vai zemes vienības adresi no ielas nosaukuma un viduslīnijas; adreses var piešķirt, mainīt, precizēt vai likvidēt ar atsevišķu lēmumu. Tādēļ viena nosaukuma maiņa pati par sevi nepierāda numura saglabāšanos.

5. **Pierādīt fiziskā objekta pēctecību.** Vajadzības gadījumā izmantot būvlietu, inventarizācijas plānu, zemesgabala dokumentus, mājas grāmatu vai datētu fotogrāfiju. Salīdzināt novietojumu un ēkas pazīmes; ja nams nojaukts, atsevišķi norādīt vēsturisko vietu un šodien tur esošo objektu. [Latvijas Valsts arhīva 1432. fonda vēsturiskā izziņa](https://www.archiv.org.lv/apraksti/F/LV_LVA_F1432_VI.pdf) tieši apraksta arī nojaukto namu mājas grāmatas un nepilnīgus vai bojātus ierakstus. Nepilnīgs avots jāatzīmē, nevis jāaizpilda ar minējumu.

6. **Pierakstīt rezultātu ar pierādījuma pakāpi.** Praktiska tabula: “vecā adrese un gads → ielas posms → numerācijas avots → ēkas/zemesgabala avots → pašreizējā adrese → kas vēl nav zināms”. Ja trūkst numura vai ēkas saiknes, rezultāts paliek “ielas atbilstība atrasta; ēkas atbilstība nav pierādīta”.

##### Īsts piemērs: Maskavas ielas sadalījums 2024. gadā

Rīgas domes **2024. gada 21. februāra lēmums Nr. RD-24-3402-lē**, oficiāli publicēts **28. februārī**, nosaka šādas pārejas:

| Iela pirms šīs pārdēvēšanas | Posms vai objekts | Nosaukums pēc lēmuma |
|---|---|---|
| Maskavas iela | No 13. janvāra ielas līdz Lāčplēša ielai | Lastādijas iela |
| Maskavas iela | No Lāčplēša ielas līdz Rīgas robežai | Latgales iela |
| Toreizējā Latgales iela | Lēmuma 1. punktā identificētā atsevišķā iela | Jāņa Klīdzēja iela |

Avots ir [pats pašvaldības lēmums oficiālajā izdevumā](https://www.vestnesis.lv/op/2024/42.20), īpaši 1., 2.1., 2.2. un 4. punkts. Tas paredz arī adresācijas objektu adrešu maiņu.

**Perioda pārbaude:** 21. februāris ir lēmuma pieņemšanas datums, 28. februāris — oficiālās publikācijas datums. [Pašvaldības 2024. gada 1. marta paziņojums](https://www.riga.lv/lv/jaunums/jaunie-rigas-ielu-nosaukumi-ir-speka-izmainas-pilsetvide-tiks-veiktas-pakapeniski) apstiprina, ka jaunie nosaukumi tobrīd jau bija spēkā, bet zīmes un dažādi ārējie resursi mainījās pakāpeniski. Precīzu spēkā stāšanās dienu šeit neizsecinu tikai no pieņemšanas datuma. Ar šo dokumentu arī nepiedēvēju nosaukumam “Maskavas iela” nepārtrauktu lietojumu visā 19. un 20. gadsimtā: senākas adresu grāmatas gads jāpārbauda atsevišķi.

Piemērs rāda divas kļūdas, ko nepieļaut. Ne visa vecā Maskavas iela kļuva par Latgales ielu. Savukārt “Latgales iela” tieši pirms šīs pārdēvēšanas apzīmēja citu ielu nekā jaunais nosaukums bijušās Maskavas ielas posmam. **Neviena tabulas rinda nepierāda, ka kāds vecs mājas numurs ir saglabājies vai ka saglabājusies pati ēka.**

##### Divas pārneses idejas

**Identitātes saskaņošana no datu bāzēm.** Hipotēze: ielas nosaukumu glabāt kopā ar laiku un posmu, bet ēkas identitāti atsevišķi. Lētajā izpildītajā pārbaudē trīs lēmuma pārejas ievadītas kodā. “Maskavas iela” bez posma dod **divus kandidātus**; ar zināmu sākumposmu — vienu nosaukumu, taču ēkas identitāte joprojām paliek nenoteikta. Tas tieši novērš kļūdainu viena nosaukuma aizstāšanu visā datu kopā. Tests darbojas tikai šim 2024. gada lēmumam.

**Telpiska savietošana no kartogrāfijas.** Hipotēze: vēsturisku karti pārbaudīt pēc vairākiem skaidri identificētiem orientieriem un atlikt secinājumu, ja blakus kvartāli nesakrīt. LNB pakalpojuma apraksts apliecina vajadzīgā salīdzināšanas rīka esamību. Konkrētai adresei izmēģinājums vēl nav veikts, jo adrese nav dota; attālumu vai kļūdas metru precizitāti neizdomāju. Ar gatavo karšu pārlūku būtu jāsāk pirms atsevišķas ģeoreferencēšanas programmas veidošanas.

Izpētē izpildīti EN, DE, ZH un JA vaicājumi. ZH un JA rezultātos neatradu citējamu pirmavotu tieši šai Rīgas pārdēvēšanai; šis iztrūkums nav aizstāts ar tulkotu sekundāru tekstu. Avoti nolasīti 2026. gada 9. novembrī. Pārbaude ir viena aģenta veikta; konkrēta nama atrašana un neatkarīga ārējā pārskatīšana nav veikta.


*Izpildītā aprēķina faili:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NP06/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NP06/calculation.py)

*Izpētes izcelsme: NP06; 9 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `815e2ed72240d0b4127fba8c3ad37632ad6b1a9f62237d738f8719a7c501f58b`.*

<a id="final30-np07"></a>

#### NP07 — Putni un logu stikls

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Putni divreiz ieskrējuši lielā logā. Vai pietiek ar vienu plēsīga putna uzlīmi vidū? Salīdzini risinājumus pēc mehānisma, pierādījumiem un tā, kā es varu pārbaudīt izmaiņas.

*Pārbaudes nosacījumi:* Neiesaki iegādāties konkrētu zīmolu. Izskaidro virsmas novietojumu, raksta blīvuma nosacījumus un risinājumu atšķirību, nodalot laboratorijas/pētījuma rezultātu no garantijas konkrētam logam.

##### Izpētītā atbilde

**Ar vienu plēsīga putna uzlīmi loga vidū nepietiek.** Putns var izvairīties no uzlīmes un mēģināt lidot cauri brīvajam laukumam blakus tai. Praktiska izvēle ir blīvs, labi saskatāms raksts **uz ārējās stikla virsmas visā loga laukumā** vai visu bīstamo laukumu nosedzošs ārējs siets. Viena silueta nepietiekamību un raksta pamatnosacījumus skaidro [Kanādas vides dienesta norādījumi](https://www.canada.ca/en/environment-climate-change/services/avoiding-harm-migratory-birds/faq-bird-collisions-glass-windows.html).

##### Kā izvietot rakstu

Vienkāršam paša veidotam punktu vai līniju rakstam izmantoju šādus nosacījumus:

- Raksts atrodas **ārpusē**, uz tās virsmas, kur veidojas putnam redzamais atspīdums.
- Tas aptver visu bīstamo stiklojumu, arī malas un blakus esošās lielās rūtis.
- Starp marķējumiem nav spraugu, kas pārsniedz **5 cm horizontāli vai vertikāli**.
- Katrs elements ir vismaz **5 mm plats** un skaidri kontrastē ar fonu un atspoguļoto veģetāciju.
- Pēc uzstādīšanas pārbauda rakstu no ārpuses dažādos dienas laikos un leņķos.

Šī ir konkrētā [Kanādas dienesta vispārīgā vadlīnija](https://www.canada.ca/en/environment-climate-change/services/avoiding-harm-migratory-birds/faq-bird-collisions-glass-windows.html). [Šveices Putnu pētniecības stacija](https://www.vogelwarte.ch/de/ratgeber/vogelkollisionen-an-glas-vermeiden/) atsevišķiem līniju risinājumiem pieļauj citas atstarpes, piemēram, vismaz 5 mm platām vertikālām līnijām līdz 10 cm. Tas nenozīmē, ka jebkura reta uzlīmju kompozīcija ir līdzvērtīga. Šim nenomērītajam logam izvēlos vienkārši pārbaudāmo, blīvāko 5 × 5 cm pieeju; konkrēta pārbaudīta dizaina parametrus nedrīkst brīvi sajaukt ar cita dizaina parametriem.

**Tikai izvietojuma piemērs:** ja rūts būtu 1 × 1 m, varētu izvietot 20 × 20 jeb **400 punktus**, kuru diametrs ir 6 mm, centri atrodas ik pēc 5 cm, bet ārējās rindas centrs — 2,5 cm no malas. Starp punktu malām tad paliktu 4,4 cm. Kodā pārbaudīta šī ģeometrija. Tā nav tava loga izmēra aplēse un nav aizsardzības efektivitātes mērījums.

##### Risinājumu salīdzinājums

| Risinājums | Darbības mehānisms | Pierādījums un praktiskais nosacījums |
|---|---|---|
| Viens vanaga vai cita plēsēja siluets | Aizsedz tikai nelielu laukumu; brīvajās vietās saglabājas atspīdums vai šķietama caureja | Ar vienu vai divām uzlīmēm lielā rūtī nepietiek; forma pati par sevi neaizvieto blīvu pārklājumu |
| Blīvi ārēji punkti, līnijas vai rakstaina plēve | Padara šķietamo lidojuma ceļu vizuāli pārtrauktu un stiklu uztveramu kā šķērsli | Jāievēro virsma, blīvums, kontrasts un pilns pārklājums; dekoratīvas plēves nosaukums nepierāda efektu |
| Ārējs kukaiņu siets rāmī vai piemērots ārējs aizsegs | Redzams šķērslis; siets var arī fiziski atdalīt putnu no stikla | Jānosedz viss laukums. Jāpārbauda stiprinājums un atstarpe, lai siets darbotos kā barjera; nav prasības iegādāties konkrētu zīmolu |
| Aizvērts ārējs slēģis vai žalūzija | Aizsedz problemātisko stikla laukumu | Darbojas tikai aizvērtajā stāvoklī un ietekmē skatu/gaismu |
| Iekšēji aizkari vai iekšpusē pielīmēts raksts | Var mazināt caurredzamību, bet ārējais atspīdums var palikt priekšā rakstam | Papildu vai pagaidu pasākums; to nevar pieņemt par līdzvērtīgu ārējam marķējumam |
| UV risinājums | Maina konkrētu gaismas spektra daļu | Jāpārbauda konkrētais materiāls, uzstādīšana un pētījums; apzīmējums “UV” vien rezultātu negarantē |

Ārējos sietus un aizsegus kā alternatīvas min Kanādas dienests; Šveices stacija skaidro ārējās marķēšanas, kontrasta, blīvuma un pagaidu aizkaru risinājumus. Fiziskās barjeras skaidrojums tabulā ir mehānisma secinājums, nevis konkrēta šeit izmēģināta sieta rezultāts. [Avots par risinājumu nosacījumiem](https://www.vogelwarte.ch/de/ratgeber/vogelkollisionen-an-glas-vermeiden/).

##### Ko pētījumi ļauj secināt

[Swaddle un līdzautoru 2023. gada pētījuma nolasītajā kopsavilkumā](https://pubmed.ncbi.nlm.nih.gov/36751632/) salīdzinātas divas plēves uz stikla paketes iekšējās un ārējās virsmas. Tie bija kontrolēti zebras žubīšu lidojuma izmēģinājumi. Ārpusē vienai plēvei ieguvuma pierādījums bija pārliecinošāks, otrai — vājāks; iekšpusē nevienai netika konstatēta attiecīgā aizsardzības iedarbība. Tas ir izvairīšanās uzvedības rezultāts konkrētā izmēģinājumā, nevis noteikts garantēts sadursmju samazinājums šim logam.

Arī UV risinājumus nevajag salikt vienā kategorijā. [Japānas 2025. gada pētījuma kopsavilkums](https://www.jstage.jst.go.jp/article/jjo/74/2/74_243/_article/-char/ja) ziņo par lauka novērojumiem universitātes teritorijā un sadursmju mazinājumu vietās ar UV bloķējošu plēvi. Savukārt Šveices stacija brīdina par sliktiem rezultātiem pārbaudītajiem UV uzlīmju/plēvju produktiem. Atšķiras materiāli, gaismas iedarbība un pētījumu apstākļi. Japānas darbam nolasīts kopsavilkums, ne pilnā metodika, tādēļ no tā neizsecinu universālu materiāla izvēli vai uzstādīšanas specifikāciju. Praktiskajā ieteikumā dodu priekšroku skaidri redzamam ārējam rakstam.

##### Kā pārbaudīt izmaiņas pie sava loga

**Neatstāj logu neapstrādātu tikai jaunu sadursmju “kontroles perioda” savākšanai.** Divi jau notikuši triecieni pamato tūlītēju uzlabojumu.

Pirms pārmaiņas saglabā foto no ārpuses, pieraksti zināmo abu sadursmju datumu un to, vai vispār zināms novērošanas ilgums. Pēc uzstādīšanas nofotografē kopskatu un ar lineālu pārbaudi lielākās atstarpes. Viena redzama sprauga var būt svarīgāka par kopējo uzlīmju skaitu.

Pirmajā mēnesī veic vienādu īsu ikdienas pārbaudi: stikla pēdas, putns pie loga, dzirdēts trieciens vai kamerā redzams notikums. Pieraksti arī **“0 novērotu”** un atsevišķi **“nav pārbaudīts”**; vienu notikumu, ko redzēji un vēlāk atradi tā pēdu, neskaiti divreiz. Atzīmē laiku, gaismu, atspīdumu un marķējuma bojājumus. Turpini uzskaiti ilgāk un salīdzini pēc iespējas līdzīgus sezonas un novērošanas apstākļus.

Rādītājs var būt **novērotas sadursmes uz vienu loga dienu**, vienmēr blakus norādot pārbaudes biežumu. Diviem agrākiem notikumiem bez zināma perioda šādu sākuma rādītāju aprēķināt nevar. Retāka novērošana var palaist triecienus garām, tādēļ nulli pieraksta kā nulli *novērotu* notikumu. Ja sadursme atkārtojas, pārbaudi ārējo virsmu, spraugas, kontrastu un blakus rūtis; ar vienu jaunu uzlīmi problēmas vietā vien var nepietikt.

##### Divas pārneses idejas

**1. Fiziska barjera no inženierijas.** Hipotēze: ja ārēja raksta uztvere konkrētajā gaismā ir apšaubāma, pilns ārējs siets var dot citu aizsardzības mehānismu. Tā nav pārbaudīta šā loga efektivitāte. Lētais sākuma tests ir ārēja apskate: pilns pārklājums, stiprinājums un atstarpe no stikla. Šeit pieejams avotu pamatojums, bet fiziska uzstādīšana nav veikta.

**2. Notikumu uzskaite no uzticamības analīzes.** Hipotēze: ekspozīcijas un nenovēroto periodu uzskaite palīdz nepārvērst “nekas nav pamanīts” par garantiju. [NIST metode](https://www.itl.nist.gov/div898/handbook/apr/section4/apr451.htm) paredz nenoteiktību pat tad, ja testā nav neviena notikuma. Tikai matemātiskā ilustrācijā ar nemainīgu nejaušu notikumu intensitāti un pilnīgu atklāšanu nulle 30 loga dienās dod vienpusēju 95% intensitātes augšējo robežu ap **0,10 notikumiem dienā**, nevis nulli. Šis kodā pārrēķinātais piemērs nav tava loga riska aplēse: reāli mainās putnu aktivitāte, sezona un atklāšanas iespēja. Vienkārša uzskaites tabula šeit ir pamatotāka par sarežģītu prognozes modeli.

Avoti nolasīti 2026. gada 9. novembrī; EN, DE, ZH un JA vaicājumi saglabāti. PeerJ izdevēja pilnteksts, atrastais 2026. gada raksts un Taivānas praktiķu lapa atvēršanā atdeva 403 kļūdu; to nenolasītais saturs nav pierādījums šai atbildei. Šeit nav novērots konkrētais logs vai veikta neatkarīga ārējā rezultātu pārbaude.


*Izpildītā aprēķina faili:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NP07/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NP07/calculation.py)

*Izpētes izcelsme: NP07; 6 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `1fd8403f3e4af2c0475d1af15b9ca82c1944b428147cafcef4f8404d3b260d23`.*

### 10 sarežģīti jautājumi

<a id="final30-f03"></a>

#### F03 — Aģents, kas pārbauda savus uzlabojumus

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Kā izveidot aģenta procedūru, kura pati uzlabo meklēšanas skillu, bet neapmāna vērtētāju un nezaudē atgriešanos pie iepriekšējās versijas? Gatavie komponenti un iespējamā sintēze.

##### Izpētītā atbilde

##### Sāktu ar GEPA un atsevišķi aizsargātu vērtēšanu

Meklēšanas procedūru var uzlabot, salīdzinot nelielu skaitu skaidri nodalītu kandidātu. Aģents drīkst mainīt meklēšanas noteikumus un veidot kandidātus; neatkarīgs izpildītājs lemj, kuru versiju pieņemt. Ar norādījumu “neapmāni vērtētāju” nepietiek. Pētījumā RewardHackingAgents vērtētāja labošana un piekļuve slēptajām atbildēm bija atšķirīgi pārkāpumu ceļi, tādēļ jāaizsargā abi. Tas ir konkrētā pētījuma rezultāts, ne garantija pret visiem uzbrukumiem. [Primārais pētījums](https://arxiv.org/abs/2603.11337)

Gatavā sākuma bāze ir MIT licencētais GEPA: tas optimizē teksta kandidātus, izmantojot izpildes kļūdas un vērtēšanas atgriezenisko saiti. Dokumentēts arī adapteris savām sistēmām un izsaukumu budžets. DSPy integrācija der jau DSPy veidotai plūsmai; atsevišķam meklēšanas rīkam saprotamāks var būt tiešs GEPA adapteris. Dokumentācija ir pārbaudīta, bet šeit nav veikta GEPA instalācija vai mūsu meklētāja salīdzinājums. [Autoru repozitorijs](https://github.com/gepa-ai/gepa)

Izveidotu šādu pārbaudes kārtību.

1. Saglabāt pieņemto versiju, tās saturu, atkarības un kontrolsummas. Katrai izmaiņai izveidot atsevišķu kandidātu.
2. Mācību uzdevumus dot kandidāta veidotājam; galīgos pārbaudes uzdevumus un etalonatbildes turēt citā procesā un ārpus tā rakstīšanas/piekļuves tiesībām. Fiksēt modeli, rīkus, budžetu un kritiskās kļūdas pirms sacensības.
3. Salīdzināt pašreizējo pieņemto procedūru ar kandidātu uz tiem pašiem uzdevumiem. Vērtētājs pārrēķina rezultātus no reāliem avotiem un žurnāliem; kandidāta pašvērtējums nedod pieņemšanas punktus.
4. Pieņemt tikai pārbaudīto izmaiņu un saglabāt iepriekšējo versiju. Jaunā darbā pārbaudīt ielādētās versijas kontrolsummu; atgriešanās atjauno arī atbilstošo konfigurāciju. Git `revert` saglabā atcelšanu vēsturē, taču pats neatceļ ārējos blakusefektus. [Git dokumentācija](https://git-scm.com/docs/git-revert)

Divas izmēģināmas idejas papildina gatavo bāzi. Pirmā pārnes kļūdu atkārtošanās novēršanu uz aģenta atmiņu: glabājam īsu noraidīto kandidātu pierakstu. GEPA problēmas #379 autors apraksta lietotāja ziņotu gadījumu ar atkārtotiem neveiksmīgiem labojumiem un saistītu vēl atvērtu priekšlikumu; to nedrīkst saukt par jau ieviestu funkciju. Otrā izmanto reproducējamu laidienu principu: pieņemam tikai versijas pakotni, kurai neatkarīgs pārbaudītājs ir pārbaudījis rezultāta izcelsmi. [GEPA diskusija #379](https://github.com/gepa-ai/gepa/issues/379)

Lētais tests: divi kandidāti, iepriekš atdalīti uzdevumi un vienāds limits katrai pusei. Priekšrocības hipotēzi noraidām, ja ieguvums pazūd neatkarīgā pārrēķinā vai pieaug kritisko kļūdu skaits. Pat veiksmīgs salīdzinājums pamatotu tikai konkrēto izmaiņu pārbaudītajos uzdevumos. Arī detalizēta vērtētāja atgriezeniskā saite var palīdzēt pielāgot apiešanu, tādēļ slēpto pārbaudi netrenējam atkārtoti. [2026. gada autoru pētījums](https://www.microsoft.com/en-us/research/publication/reward-hacking-challenges-oversight-of-autonomous-research-agents/)


*Izpētes izcelsme: F03; 6 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `80c06468dc92c897f893f015e3c3d37f65b131e650477584d8a82202265ec0bf`.*

<a id="final30-f08"></a>

#### F08 — Atmiņas uzlabojuma cēloņsakarīga pārbaude

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Man vajag aģenta atmiņas izmaiņu cēloņsakarīgu novērtējumu. Kā atšķirt labāku atmiņu no vienkārši vairāk meklējumiem vai vieglākiem uzdevumiem?

##### Izpētītā atbilde

**Jāsalīdzina vecā un jaunā atmiņa uz tiem pašiem uzdevumiem, iepriekš nosakot meklēšanas iespējas.** Viena rezultātu tabula, kur jaunajai versijai ir vairāk rīku izsaukumu vai cita uzdevumu izlase, neizolē atmiņas ieguldījumu.

Gatava sākuma bāze ir LongMemEval: autoru repozitorijā ir 500 jautājumu kopums, sarunu vēstures, atbilžu vērtēšanas rīki un atmiņas darbībām paredzēti salīdzinājumi. Tas ļauj pārbaudīt informācijas atcerēšanos sarunās; mūsu aģenta pilnā darba kvalitāte vēl jāpārbauda ar paša uzdevumiem. [LongMemEval autoru repozitorijs](https://github.com/xiaowu0162/LongMemEval) Praktiskajā Redis autoru pētījumā atsevišķi salīdzināta neapstrādātu sarunu izgūšana, atmiņas izvilkumu izmantošana un abu apvienošana. Autori arī brīdina, ka citur publicētie rezultāti grafikā nav kontrolēta sacensība savā starpā. [Pirmavota eksperimenta apraksts](https://redis.github.io/redis-ai-research-public/longmemeval-agent-memory/)

Ierosinu pārbaudīt četras kombinācijas: **vecā/jaunā atmiņa × mazs/liels meklējumu skaits**. Pilns faktoru plāns ietver visas kombinācijas; tā pamatu apraksta [NIST](https://www.itl.nist.gov/div898/handbook/pri/section3/pri333.htm). Katrā meklējumu līmenī kontrolētajam eksperimentam izsaukumu skaits un ārējie pierādījumi ir fiksēti, ne tikai atļautais maksimums. Vienādi paliek modelis, uzvedne, tokenu limits un sākotnējā vēsture; mainās pārbaudāmais atmiņas mehānisms.

Uzdevumus bloķējam pēc grūtības un nejaušinām izpildes secību. Pirms katra mēģinājuma atjaunojam sākotnējo atmiņas stāvokli, lai viena versija nemācās no otras atbildes. Vērtētājs neredz versijas nosaukumu; atsauces atbildes, vērtēšanas noteikumi un slēptie uzdevumi aģentam nav labojami. Vērtējam faktu pareizību, atteikšanos minēt, kļūdu smagumu, lasīšanas un rakstīšanas izmaksas, kā arī pāru atšķirību nenoteiktību.

Atsevišķā izmēģinājumā ļaujam abām versijām pašām izvēlēties meklējumu skaitu vienāda kopējā budžeta ietvaros. Tas mēra **visas procedūras efektu**, ieskaitot spēju ietaupīt meklējumus. Pēc rezultātu saņemšanas vienkārši atlasīt tikai mēģinājumus ar vienādu izsaukumu skaitu būtu cita atlase un varētu sagrozīt secinājumu.

Sākumā pārbaudītu divus iespējamos uzlabojumus. Avota norādes pie katra atmiņas fakta var samazināt kļūdainu atcerēšanos; to lēti pārbaudīt uz jautājumiem ar savstarpēji pretrunīgiem datētiem faktiem. Reto detaļu saglabāšana līdzās kopsavilkumam var uzlabot precizitāti; to pārbaudīt ar detaļām, kuras kopsavilkuma bāze izmet. Abām versijām jābūt vienādam atmiņas izmēra limitam. Ja ieguvums pazūd pie fiksētiem pierādījumiem, nevaram to piedēvēt tikai labākai atmiņas reprezentācijai.

Šeit veikta izpēte četrās valodās. Aprakstītais eksperiments vēl jāizpilda, lai izmērītu kvalitātes atšķirības, laiku un izmaksas.


*Izpētes izcelsme: F08; 4 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `e9732308415621f3d5811a191efcb0a98c72105dece05d1e9647e43155058c78`.*

<a id="final30-f09"></a>

#### F09 — Ārējs maksājums pēc procesa avārijas

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Vai LLM aģentu sistēmā var visiem ārējiem maksājumiem garantēt tieši vienu izpildi, ja process avarē pēc pieprasījuma? Projektē praktisku risinājumu ar ierobežojumiem.

##### Izpētītā atbilde

**Visiem ārējiem maksājumiem universālu “tieši vienreiz” garantiju dot nevar.** Ja pakalpojums izpildījis pieprasījumu, bet atbilde pazūd, klienta lokālais stāvoklis var neatšķirties no situācijas, kur pieprasījums nav sasniedzis pakalpojumu. Akls atkārtojums var radīt otru maksājumu, savukārt neatkārtošana var atstāt maksājumu neizpildītu. AWS autoru apraksts tieši apskata šo neskaidrību un klienta piešķirtus unikālus pieprasījuma identifikatorus. [AWS Builders’ Library](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)

Praktiski var panākt vienu maksājuma efektu **konkrēta pakalpojuma idempotences līguma robežās**. Piemēram, Stripe API v1 saglabā pirmā pieprasījuma ar konkrēto atslēgu rezultātu tikai pēc galapunkta izpildes sākuma. Atkārtojot to pašu atslēgu, saņem saglabāto atbildi, arī kļūdu 500. Ja parametru pārbaude neizdodas vai rodas konflikts ar vienlaikus izpildē esošu pieprasījumu un galapunkta izpilde nesākas, idempotences rezultātu nesaglabā; šādu pieprasījumu var atkārtot. Atslēgas drīkst dzēst pēc vismaz 24 stundām; atkārtota jau dzēstas atslēgas izmantošana rada jaunu pieprasījumu. API v2 dokumentēta cita kļūmju apstrāde, tādēļ šos noteikumus nedrīkst vispārināt. [Stripe idempotence](https://docs.stripe.com/api/idempotent_requests)

Procedūru veidotu šādi:

1. Pirms sūtīšanas datubāzē vienā transakcijā saglabā maksājuma nodomu, nemainīgus parametrus, unikālu nodoma ID un nosūtāmo darbu. Vienam nodomam ir viena stabila pakalpojuma atslēga.
2. Atsevišķs izpildītājs nosūta darbu. Rindas atkārtojumi izmanto to pašu atslēgu un parametrus; aģents nevar pats pārvērst atkārtojumu jaunā nodomā.
3. Laika pārsniegumu atzīmē kā **iznākums nezināms**, saglabā pakalpojuma objekta ID, ja tas saņemts, un salīdzina stāvokli ar pakalpojuma datiem.
4. Ar parakstu pārbaudītus paziņojumus apstrādā idempotenti: reģistrē notikumu ID un nepaļaujas uz to pienākšanas secību. Stripe dokumentē gan dublikātus, gan secības negarantēšanu. [Paziņojumu dokumentācija](https://docs.stripe.com/webhooks)
5. Tuvojoties atslēgas derīguma robežai, neskaidru maksājumu vairs akli neatkārto. To noskaidro pēc pakalpojuma reģistra vai atstāj izmeklēšanai, saglabājot saistību ar sākotnējo nodomu.

Gatavie komponenti ir pakalpojuma SDK, transakciju datubāze un nosūtāmo darbu tabula. AWS dokumentētā *transactional outbox* pieeja sasaista lokālās izmaiņas un darba ierakstu, taču pati par sevi nepadara ārējo maksājumu atomāru ar mūsu datubāzi; dublētiem ziņojumiem joprojām vajag idempotentu saņēmēju. [AWS pieejas apraksts](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html)

Pārbaudītu divas hipotēzes: stabila nodoma atslēga novērš dublētu efektu pēc avārijas, un atsevišķa neskaidro iznākumu pārbaude samazina iestrēgušus darbus. Sākumā pietiktu ar viltotu maksājumu pakalpojumu, kurā izraisām avārijas pirms nosūtīšanas, pēc efekta un pirms atbildes saglabāšanas, kā arī dzēšam atslēgu un atkārtojam paziņojumus. Panākumu kritērijs ir ne vairāk kā viens efekts nodomam un pareizi uzrādīta nenoteiktība. Pabeigšana papildus atkarīga no pakalpojuma pieejamības un maksājuma pieņemšanas. Šeit nav izpildīts ne tests, ne maksājums; četru valodu izpēte devusi projektējumu, ne universālas garantijas pierādījumu.


*Izpētes izcelsme: F09; 4 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `75c719cea342922ccad16425e7db4c22898dcb6bc62dbe0bab8374b4f1b167ad`.*

<a id="final30-nf01"></a>

#### NF01 — Siltuma vienādojuma inversija

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Aplūko u_t=u_xx uz (0,π), u(0,t)=u(π,t)=0. No u(x,1) ar L² trokšņa līmeni δ=10^-6 grib atgūt u(x,0). Pierādi vai atspēko inversā operatora ierobežotību L², izmantojot normalizētas sinusu modas. Aprēķini lielāko veselo modu n, kuras sākuma koeficienta 1 signāls t=1 vēl pārsniedz δ. Piedāvā vienu regularizāciju un precīzi pasaki, ko tā negarantē.

*Pārbaudes nosacījumi:* Vajadzīgs pamatots pierādījums, formulas, izpildīts skaitlisks kontrolaprēķins un primārs matemātisks avots. Trokšņa robežu nepasniedz kā unikālu atgūšanas garantiju.

##### Izpētītā atbilde

Inversais operators nav ierobežots attiecībā pret L² normu. Lielākā vienības amplitūdas moda, kuras signāls laikā t=1 stingri pārsniedz 10⁻⁶, ir n=3.

##### Pierādījums

Izvēlamies $e_n(x)=\sqrt{2/\pi}\sin(nx)$. Tad $\|e_n\|_2=1$, $e_n''=-n^2e_n$, un tie veido ortonormētu bāzi $L^2(0,\pi)$. Doto robežnosacījumu un spektrālo reprezentāciju tieši aplūko Tautenhahn un Schröter raksta 1. nodaļa. [Avots](https://ems.press/content/serial-article-files/34869?nt=1).

Ja $f=u(\cdot,0)=\sum a_ne_n$, tad

$$
Sf=u(\cdot,1)=\sum_{n\ge1}e^{-n^2}a_ne_n.
$$

Visi reizinātāji ir pozitīvi, tādēļ precīziem datiem no operatora vērtību kopas risinājums ir vienīgs. Inversā operatora dabīgais definīcijas apgabals ir

$$
\mathcal R(S)=\{g=\sum g_ne_n:\sum e^{2n^2}|g_n|^2<\infty\}.
$$

Tajā $S^{-1}g=\sum e^{n^2}g_ne_n$. Tas nav uz visa $L^2$ definēts ierobežots operators.

Izvēlamies $g^{(n)}=Se_n=e^{-n^2}e_n$. Tad

$$
\|g^{(n)}\|_2=e^{-n^2}\to0,\qquad
\|S^{-1}g^{(n)}\|_2=1.
$$

Ierobežotība prasītu $1\le C e^{-n^2}$ ar vienu galīgu $C$ visiem $n$, kas nav iespējams. Līdzvērtīgi, $\|S^{-1}e_n\|_2=e^{n^2}\to\infty$. Neviena galīga operatora normas robeža šo secību neapmierina.

##### Trokšņa slieksnis

Koeficientam $a_n=1$ signāls ir $e^{-n^2}$. Nosacījums ir

$$
e^{-n^2}>\delta
\iff n^2<\log(10^6)
\iff n<3.71692218885.
$$

Tātad $n_{\max}=3$. Izpildītais aprēķins deva

$$
e^{-9}=1.23409804087\cdot10^{-4},\qquad
e^{-16}=1.12535174719\cdot10^{-7}.
$$

Normalizācijas dēļ arī katra trokšņa koeficienta modulis nepārsniedz $\delta$, ja kopējā $L^2$ trokšņa norma nepārsniedz $\delta$. Šis slieksnis attiecas uz dotu vienības amplitūdu; citu amplitūdu redzamība mainās.

##### Regularizācija un tās robeža

Var izmantot spektrālu nogriešanu:

$$
R_Ng^\delta=\sum_{n=1}^N e^{n^2}\langle g^\delta,e_n\rangle e_n .
$$

Tā ir ierobežota: $\|R_N\|=e^{N^2}$. Spektrālu filtru un regularizācijas kļūdas sadalījuma pamatojums dots minētajā rakstā, savukārt singulāro vērtību nogriešanu mērījumu inversijā aplūko Rust darbs. [NIST ieraksts](https://www.nist.gov/publications/truncating-singular-value-decomposition-ill-posed-problems-0).

No ortogonalitātes iegūstam

$$
\|R_Ng^\delta-f\|_2^2
\le e^{2N^2}\delta^2+\sum_{n>N}|a_n|^2.
$$

Pie $N=3$ saglabāto modu trokšņa kļūda nepārsniedz $0.00810308393$, bet augsto modu aste paliek nezināma. Pie $N=4$ šī trokšņa robeža jau ir $8.88611052$.

Regularizācija negarantē precīzu sākuma stāvokli, unikālu atgūšanu no trokšņainiem datiem vai vienmērīgi mazu kopējo kļūdu visiem $f\in L^2$. Tā nevar novērtēt atmesto asti no viena $\delta$ vien. Konkrētam fiksētam $f$, izvēloties $N(\delta)\to\infty$ un $\delta e^{N(\delta)^2}\to0$, seko konverģence, bet bez papildu gluduma nosacījuma nav dots konverģences ātrums. Pie $\delta=10^{-6}$ vērtība $N=3$ ir uzdevuma vienības signāla demonstrācija, ne universāli optimāla parametra izvēle.

##### Divu pārnesumu pārbaude

Attēlu izplūduma novēršanas singulāro vērtību nogriešana pārnesas uz šo uzdevumu tieši: abas metodes ierobežo dalīšanu ar maziem spektrālajiem reizinātājiem. Izpildītais 3. un 4. modas salīdzinājums apstiprina trokšņa pastiprinājuma cenu.

Atkārtotu mērījumu vidējošana šeit nedod garantētu ieguvumu, jo nav pieņemts neatkarīgs nejaušs troksnis. Kontrolpiemērā 100 reizes atkārtota kļūda $\delta e_4$ vidējošanā nemazinājās; inversijas kļūda palika 8.88611052. Tāpēc šo ideju bez trokšņa modeļa noraidām.

Nākamais lietderīgais tests: pie skaidri dotas Soboleva normas robežas salīdzināt trokšņa un astes robežas vairākām N vērtībām. Šāds papildu gluduma pieņēmums šajā uzdevumā nav dots, un tests nav veikts.


*Izpildītā aprēķina faili:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NF01/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NF01/calculation.py)

*Izpētes izcelsme: NF01; 5 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `ea6ba290bb2b250082c0c16969d3a8b410e3dbc3dcf5e4651a14510a7caa5bbe`.*

<a id="final30-nf02"></a>

#### NF02 — Stohastisks process un diskrētā dispersija

**Sākotnējais jautājums un nepieciešamie nosacījumi**

dX_t=-2X_tdt+3dW_t, X_0=1. Atvasini vidējo, dispersiju un stacionāro sadalījumu. Atvasini Euler–Maruyama stacionāro dispersiju un soļa stabilitātes nosacījumu; salīdzini h=0.25 ar nepārtraukto modeli un parādi, kas notiek pie h=1.2.

*Pārbaudes nosacījumi:* Vajadzīgs atvasinājums, izpildīts skaitlisks kontrolaprēķins un neatkarīgs primārais avots. Montekarlo rezultātu nedrīkst aizstāt ar teorētisku pierādījumu; ja simulē, saglabā seed un kodu.

##### Izpētītā atbilde

Dotā procesa robežsadalījums ir $N(0,9/4)$. Euler–Maruyama shēma pie $h=0.25$ ir stabila, taču tās stacionārā dispersija ir $3$, par $33\frac13\%$ lielāka. Pie $h=1.2$ vidējā vērtība svārstās ar augošu amplitūdu, bet dispersija aug eksponenciāli.

##### Precīzais risinājums

Reizinot vienādojumu ar $e^{2t}$ un izmantojot Itô reizinājuma formulu, iegūstam

$$
d(e^{2t}X_t)=3e^{2t}dW_t,\qquad
X_t=e^{-2t}+3\int_0^t e^{-2(t-s)}\,dW_s.
$$

Zemintegrāļa funkcija ir deterministiska un kvadrātiski integrējama. Itô integrālis ir centrēts Gausa mainīgais, un izometrija dod

$$
\mathbb E X_t=e^{-2t},\qquad
\operatorname{Var}(X_t)=9\int_0^t e^{-4(t-s)}ds
=\frac94(1-e^{-4t}).
$$

Tādēļ pie $t>0$

$$
X_t\sim N\left(e^{-2t},\frac94(1-e^{-4t})\right).
$$

Robeža ir $N(0,9/4)$. Ja arī $X_0\sim N(0,9/4)$, neatkarīgi no turpmākajiem Brauna pieaugumiem, šis sadalījums saglabājas visos laikos. Dotajam $X_0=1$ process sākumā nav stacionārs.

Šo Gausa stacionāro sadalījumu un atšķirību no Euler shēmas aplūko Higham un Kloeden pašu publicētais grāmatas fragments. [SIAM](https://www.siam.org/publications/siam-news/articles/numerics-for-stochastics/).

##### Euler–Maruyama atvasinājums

Ar neatkarīgiem $\xi_k\sim N(0,1)$,

$$
Y_{k+1}=(1-2h)Y_k+3\sqrt h\,\xi_k,\qquad Y_0=1.
$$

Apzīmējam $a=1-2h$. No neatkarības

$$
m_{k+1}=am_k,\quad v_{k+1}=a^2v_k+9h,\quad
m_k=a^k,\quad v_k=9h\sum_{j=0}^{k-1}a^{2j}.
$$

Galīga stacionāra dispersija pastāv tieši pie $|a|<1$, tātad

$$
0<h<1,\qquad
v_h=\frac{9h}{1-(1-2h)^2}=\frac{9}{4(1-h)}.
$$

Stacionārais sadalījums ir $N(0,v_h)$, jo stacionāru procesu var veidot kā kvadrātiski summējamu neatkarīgu Gausa inovāciju rindu. Divu risinājumu starpība ar tiem pašiem trokšņa pieaugumiem ir $a^k(Y_0-\widetilde Y_0)$, kas šajā intervālā izdziest.

Šeit stabilitāte nozīmē sākuma atšķirību izdzišanu un ierobežotu otro momentu; aditīvā trokšņa dēļ pats process uz nulli nekonverģē. Giles un līdzautoru oriģinālraksta 6.1. nodaļā formula dota trokšņa koeficientam $\sqrt2$; reizinot dispersiju ar $9/2$, tā sakrīt ar mūsu atvasinājumu. [Raksts](https://link.springer.com/article/10.1007/s11222-019-09890-0).

Ja $|a|\ge1$, stacionāra varbūtības sadalījuma nav. Tā raksturfunkcijai būtu jāapmierina

$$
|\varphi(t)|\le \exp\left[-\frac{9h\,t^2}{2}\sum_{j=0}^{k-1}a^{2j}\right]
$$

visiem k. Summa diverģē, tādēļ $\varphi(t)=0$ visiem $t\ne0$, pretrunā nepārtrauktībai pie nulles. Pie robežas $h=1$ ir $a=-1$ un $v_k=9k$; vienības modulis nedod stabilitāti.

##### Izpildīta skaitliska pārbaude

Pārbaude atkārtoja momentu rekursijas un salīdzināja tās ar galīgo ģeometrisko summu; Montekarlo simulācija netika izmantota.

| Modelis | Laiks | Vidējais | Dispersija |
|---|---:|---:|---:|
| Precīzs, $t=1$ | 1 | 0.1353352832 | 2.2087898125 |
| Euler, $h=0.25,\ k=4$ | 1 | 0.0625 | 2.98828125 |
| Precīzais robežsadalījums | $t\to\infty$ | 0 | 2.25 |
| Euler, $h=0.25$, robeža | $k\to\infty$ | 0 | 3 |
| Euler, $h=1.2,\ k=10$ | 12 | 28.9254654976 | 9401.4287353445 |
| Euler, $h=1.2,\ k=100$ | 120 | $4.10018609\cdot10^{14}$ | $1.89129667\cdot10^{30}$ |

Pie $h=1.2$, $a=-1.4$, tāpēc

$$
m_k=(-1.4)^k,\qquad
v_k=\frac{10.8}{0.96}(1.96^k-1).
$$

Nepārtrauktā modeļa dispersija tikmēr tuvojas 2.25.

##### Divi mehānismu pārnesumi

Digitāla lineāra filtra kovariances līdzsvara vienādojums $v=a^2v+q$ dod to pašu diskrēto dispersiju. Šo pārnesumu pārbaudījām ar momentu rekursiju līdz 100 soļiem; tas dod īsu, tieši pārbaudāmu stabilitātes testu.

Otrs pārnesums ir trokšņa stipruma saskaņošana ar vēlamo līdzsvara dispersiju. Aizstājot $9h$ ar $\frac94(1-a^2)$, var panākt pareizu stacionāro dispersiju stabilajā intervālā. Pie $h=0.25$ jaunā inovācijas dispersija ir 1.6875. Tomēr pirmās aiztures korelācija paliek 0.5, kamēr precīzajam procesam tā ir $e^{-0.5}=0.6065306597$. Šī korekcija izlabo līdzsvara dispersiju, bet neatveido precīzu laika dinamiku.

Šim lineārajam procesam pieejams precīzs solis

$$
X_{(k+1)h}=e^{-2h}X_{kh}
+\frac32\sqrt{1-e^{-4h}}\,\xi_k.
$$

Tas seko no jau atvasinātā Itô integrāļa un saglabā gan pārejas sadalījumu, gan stacionāro dispersiju jebkuram $h>0$. Šeit skaitliski pārbaudīti tā koeficienti, ne veikta nejaušu trajektoriju simulācija.

Nākamajā metodes salīdzinājumā jāpārbauda arī autokorelācija: vienāda stacionārā dispersija vien nenosaka pareizu laika dinamiku.


*Izpildītā aprēķina faili:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NF02/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NF02/calculation.py)

*Izpētes izcelsme: NF02; 5 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `4671d84891be30d7d6d4967f0cf4134d5126f897ca2c06e65743e9e0332b248e`.*

<a id="final30-nf03"></a>

#### NF03 — Nenormālas matricas īslaicīgais pieaugums

**Sākotnējais jautājums un nepieciešamie nosacījumi**

B=[[-1,20],[0,-1]]. Visas īpašvērtības ir negatīvas; vai no tā seko, ka ||exp(tB)||₂≤1 visiem t≥0? Atvasini matricas eksponenti, precīzo spektrālo normu un tās maksimuma laiku/vērtību. Nošķir asimptotisku stabilitāti un īslaicīgu pastiprinājumu.

*Pārbaudes nosacījumi:* Vajadzīgs pierādījums, izpildīts skaitlisks pārbaudījums un primārs avots par nenormālu operatoru pārejas uzvedību. Normas maksimumu nepaņem tikai no rupja skaitliska režģa.

##### Izpētītā atbilde

Dotajai matricai $\|\exp(tB)\|_2$ sākumā pieaug virs 1. Maksimālā norma ir aptuveni $7.3760289344$, un tā tiek sasniegta laikā $t_*=\sqrt{99}/10\approx0.9949874371$.

##### Matricas eksponente un precīzā norma

Rakstām $B=-I+N$, kur

$$
N=\begin{pmatrix}0&20\\0&0\end{pmatrix},\qquad N^2=0.
$$

Tā kā $I$ komutē ar $N$,

$$
E(t)=e^{tB}=e^{-t}(I+tN)
=e^{-t}\begin{pmatrix}1&20t\\0&1\end{pmatrix}.
$$

Abas B īpašvērtības ir $-1$, bet $BB^\top\ne B^\top B$, tātad matrica nav normāla.

Apzīmējam $a=20t\ge0$. Tad

$$
\begin{pmatrix}1&a\\0&1\end{pmatrix}^{\!\top}
\begin{pmatrix}1&a\\0&1\end{pmatrix}
=\begin{pmatrix}1&a\\a&a^2+1\end{pmatrix}
$$

ar raksturīgo polinomu

$$
\lambda^2-(a^2+2)\lambda+1.
$$

Lielākā īpašvērtība ir

$$
\lambda_+=\frac{a^2+2+a\sqrt{a^2+4}}2
=\left(\frac{\sqrt{a^2+4}+a}{2}\right)^2.
$$

Tādēļ

$$
F(t):=\|E(t)\|_2
=e^{-t}\left(\sqrt{1+100t^2}+10t\right).
$$

Šī formula der visiem $t\ge0$.

##### Globālais maksimums

Izmantojot $\log(\sqrt{1+y^2}+y)=\operatorname{arsinh}y$,

$$
\frac d{dt}\log F(t)
=-1+\frac{10}{\sqrt{1+100t^2}}.
$$

Atvasinājums ir pozitīvs pie $0\le t<t_*$, nulle pie $t_*$, negatīvs pie $t>t_*$, kur

$$
1+100t_*^2=100,\qquad t_*=\frac{\sqrt{99}}{10}.
$$

Tā kā $F(0)=1$ un $F(t)\to0$ pie $t\to\infty$, šis ir vienīgais globālais maksimums:

$$
\boxed{\max_{t\ge0}\|e^{tB}\|_2
=e^{-\sqrt{99}/10}(10+\sqrt{99})
=7.376028934374846\ldots}
$$


Skaitliskā pārbaude salīdzināja formulu ar tiešu singulāro vērtību aprēķinu septiņos laikos un maksimuma punktā. Pie $t=0.01$ norma jau ir 1.0939927522; pie $t=10$ tā ir 0.00908021295. Maksimumā SVD atrastais vienības sākumvektors aptuveni $(0.0500627751,\ 0.9987460731)$ sasniedz normu 7.3760289344. Maksimuma laiks iegūts analītiski, ne no režģa.

##### Ko tieši nozīmē stabilitāte

Visiem sākumvektoriem $z_0$,

$$
z(t)=e^{tB}z_0\longrightarrow0,
$$

jo $e^{-t}$ un $te^{-t}$ tiecas uz nulli. Tas ir asimptotiski stabils līdzsvars. Vienlaikus atsevišķi sākumvektori pirms izdzišanas ievērojami pieaug.

Šādu atšķirību starp īpašvērtību noteikto asimptotiku un nenormāla operatora īslaicīgu pastiprinājumu pēta Trefethen, Trefethen, Reddy un Driscoll oriģinālraksts. Mūsu konkrētais $7.376$ rezultāts ir iepriekš veiktais atvasinājums, ne no raksta pārņemts skaitlis. [Autora pieejamā kopija](https://people.maths.ox.ac.uk/trefethen/publication/PDF/1993_57.pdf).

Operatora normu katrā laikā maksimizējošais sākumvirziens var mainīties; normas līkne pati par sevi nav viena fiksēta sākumvektora trajektorija.

##### Divi pārbaudīti mehānismi

Enerģijas metodi no plūsmu stabilitātes var izmantot kā ātru lokālu pārbaudi:

$$
\frac d{dt}\|z\|_2^2=z^\top(B+B^\top)z,\qquad
\frac{B+B^\top}{2}=\begin{pmatrix}-1&10\\10&-1\end{pmatrix}.
$$

Simetriskās daļas īpašvērtības ir $9$ un $-11$. Pie $z_0=(1,1)/\sqrt2$ sākotnējais normas kvadrāta atvasinājums ir 18, tātad pieaugums tiešām iespējams. Šis tests nosaka sākotnējo pieaugumu, ne tā globālā maksimuma vērtību.

Otrs mehānisms ir vadības teorijas svērtā kvadrātiskā enerģija. Precīzi pārbaudījām

$$
P=\begin{pmatrix}1/2&5\\5&201/2\end{pmatrix}>0,\quad
\det P=101/4,\quad B^\top P+PB=-I.
$$

Tādēļ $V(z)=z^\top Pz$ apmierina $V'=-\|z\|_2^2<0$ nenulles trajektorijai. Svērtā norma dilst, bet šis apgalvojums nemaina jau aprēķināto Eiklīda normas pieaugumu. Hipotēzi, ka piemērotas enerģijas atrašana garantētu kontrakciju tieši uzdevumā dotajā 2-normā, noraidām.

Nākamais lietderīgais tests būtu novērtēt maksimālās pastiprināšanas jutību pret ārpusdiagonāles koeficientu un noapaļošanas kļūdām. Šeit pārbaudīts tieši koeficients 20.


*Izpildītā aprēķina faili:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NF03/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NF03/calculation.py)

*Izpētes izcelsme: NF03; 5 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `f28774c7a009d8b8162ade6f47f7831c5b86cecf29cb332d65b03d314140f1d4`.*

<a id="final30-nf04"></a>

#### NF04 — Dualitāte bez galīga reizinātāja

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Risini min_x x ar ierobežojumu x²≤0. Atvasini Lagranža duālo uzdevumu, primāro un duālo optimālo vērtību, sasniegšanu un KKT nosacījumus. Tad atkārto x²≤ε² pie ε>0 un analizē ε→0. Vai nulles dualitātes plaisa viena pati garantē galīgu optimālu reizinātāju?

*Pārbaudes nosacījumi:* Vajadzīgs formāls atvasinājums, izpildīts skaitlisks kontrolaprēķins vairākiem ε un avots. Neizmanto Slatera nosacījumu, ja tas nav izpildīts.

##### Izpētītā atbilde

Nulles dualitātes plaisa viena pati negarantē galīgu optimālu Lagranža reizinātāju. Dotajā uzdevumā primārais minimums ir sasniegts un ir 0, duālais supremums arī ir 0, bet neviena galīga $\lambda$ to nesasniedz.

##### Ierobežojums $x^2\le0$

Vienīgais pieļaujamais punkts ir $x^*=0$, tāpēc $p^*=0$. Lagranža funkcija ir

$$
L(x,\lambda)=x+\lambda x^2,\qquad \lambda\ge0.
$$

Pie $\lambda>0$, pabeidzot kvadrātu,

$$
L=\lambda\left(x+\frac1{2\lambda}\right)^2-\frac1{4\lambda},
\qquad g(\lambda)=\inf_xL=-\frac1{4\lambda}.
$$

Pie $\lambda=0$, $\inf_xx=-\infty$. Tātad duālais uzdevums ir

$$
\sup_{\lambda\ge0}g(\lambda)
=\sup_{\lambda>0}\left(-\frac1{4\lambda}\right)=0.
$$

Visām galīgām $\lambda>0$ ir $g(\lambda)<0$; vērtība 0 tiek tuvināta tikai, kad $\lambda\to\infty$. Tādēļ $p^*-d^*=0$, bet duālā optimizatora nav.

KKT nosacījumi būtu

$$
x^2\le0,\quad \lambda\ge0,\quad \lambda x^2=0,\quad
1+2\lambda x=0.
$$

Pie vienīgā pieļaujamā $x=0$ pēdējais nosacījums kļūst par $1=0$. Tātad galīga KKT pāra nav. Šeit KKT nepieciešamību nevar iegūt no Slatera nosacījuma, jo stingri pieļaujams punkts $x^2<0$ neeksistē.

Tieši šo pretpiemēru un tā duālo funkciju rāda Bertsekas MIT kursa oriģinālie lekcijas materiāli. [18. lekcija](https://ocw.mit.edu/courses/6-252j-nonlinear-programming-spring-2003/c7aa97e88ae57f07d03679055aa3502a_6252_slides18.pdf).

##### Ierobežojums $x^2\le\varepsilon^2,\ \varepsilon>0$

Pieļaujamā kopa ir $[-\varepsilon,\varepsilon]$, un

$$
x^*_\varepsilon=-\varepsilon,\qquad p^*_\varepsilon=-\varepsilon.
$$

Tagad

$$
L_\varepsilon(x,\lambda)=x+\lambda(x^2-\varepsilon^2),\qquad
g_\varepsilon(\lambda)=-\frac1{4\lambda}-\lambda\varepsilon^2
\quad(\lambda>0),
$$

bet $g_\varepsilon(0)=-\infty$. No

$$
g_\varepsilon'(\lambda)=\frac1{4\lambda^2}-\varepsilon^2=0,\qquad
g_\varepsilon''(\lambda)=-\frac1{2\lambda^3}<0
$$

iegūstam vienīgo duālo optimizatoru

$$
\lambda^*_\varepsilon=\frac1{2\varepsilon},\qquad
d^*_\varepsilon=g_\varepsilon(\lambda^*_\varepsilon)=-\varepsilon.
$$

Duālā funkcija pie abiem atvērtā apgabala galiem tiecas uz $-\infty$, tāpēc šis ir sasniegts globāls maksimums. Arī primārais minimums ir sasniegts.

Visi četri KKT nosacījumi ir izpildīti:

$$
x_\varepsilon^{*2}-\varepsilon^2=0,\quad
\lambda^*_\varepsilon>0,\quad
\lambda^*_\varepsilon(x_\varepsilon^{*2}-\varepsilon^2)=0,\quad
1+2\lambda^*_\varepsilon x^*_\varepsilon=0.
$$

Šoreiz $x=0$ ir stingri pieļaujams, jo $-\varepsilon^2<0$. Slatera nosacījums der pozitīvam $\varepsilon$; risinājumu turklāt jau iegūstam tiešā aprēķinā.

##### Robeža un precīzā aritmētika

Kad $\varepsilon\downarrow0$,

$$
x^*_\varepsilon\to0,\quad p^*_\varepsilon=d^*_\varepsilon\to0,
\quad \lambda^*_\varepsilon\to+\infty.
$$

Primāro punktu un optimālo vērtību robežas eksistē, bet galīga duālā optimizatora robežas nav.

| $\varepsilon$ | $x^*$ | $\lambda^*$ | $p^*=d^*$ |
|---:|---:|---:|---:|
| 1 | −1 | 1/2 | −1 |
| 1/10 | −1/10 | 5 | −1/10 |
| 1/100 | −1/100 | 50 | −1/100 |
| 1/1 000 000 | −1/1 000 000 | 500 000 | −1/1 000 000 |

Visas rindas un KKT atlikumi pārbaudīti ar precīziem racionāliem skaitļiem. Pie $\varepsilon=0$ un $\lambda=1,10,100,10^6$ duālās vērtības ir $-1/4,-1/40,-1/400,-1/4\,000\,000$: neviena nav nulle.

##### Divi pārnesumu testi

Ekonomiskās jutības jeb ēnu cenas interpretāciju pielietojam faktiskajam ierobežojuma labās puses parametram $b=\varepsilon^2$:

$$
p(b)=-\sqrt b,\qquad p'(b)=-\frac1{2\sqrt b}=-\lambda^*.
$$

Pie $b=0$ nav galīga labās puses slīpuma. Ja galīgs subgradients $s$ tur eksistētu, vajadzētu $-\sqrt b\ge sb$ visiem $b>0$, tātad $s\le-1/\sqrt b$ visiem maziem b, kas nav iespējams. Tas ģeometriski izskaidro reizinātāja nesasniedzamību. Atvasinājums pret pašu $\varepsilon$ ir −1; reizinātāja interpretācijā parametrus nedrīkst sajaukt.

Otrs tests izmanto bezdimensiju mērogošanu $x=\varepsilon y$. Pie $\varepsilon>0$ iegūstam $\min \varepsilon y$, $y^2\le1$, ar reizinātāju $\mu^*=\varepsilon/2$. Tas ir galīgs, tomēr sākotnējais reizinātājs ir

$$
\lambda^*=\mu^*/\varepsilon^2=1/(2\varepsilon).
$$

Precīzais aprēķins apstiprināja abas sakarības visām tabulas rindām. Pie $\varepsilon=0$ substitūcija vairs nav invertējama, tāpēc mērogošana neatrisina sākotnējās formulācijas deģenerāciju.

Nākamais tests ir pārbaudīt ekvivalentas pieļaujamās kopas formulāciju $x=0$ un atšķirt tās galīgo vienādības reizinātāju no sākotnējā $x^2\le0$ reizinātāja. Tas šajā aprēķinu partijā nav izpildīts.


*Izpildītā aprēķina faili:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NF04/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NF04/calculation.py)

*Izpētes izcelsme: NF04; 5 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `6a4a886a11fbc2830b79b0df53d94d265f43a12327cfd75bbfa6f090f9d3ca20`.*

<a id="final30-nf05"></a>

#### NF05 — Masas koncentrēšanās un robežpāreja

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Uz [0,1] ņem f_n(x)=n·1_(0,1/n)(x). Nosaki punktveida/gandrīz visur robežu, L¹ konverģenci un mēru f_n(x)dx vājo robežu. Pierādi atbildes un precīzi nosauc, kādēļ robežu nevar vienkārši ienest integrālī. Saisti ar vienmērīgu integrējamību.

*Pārbaudes nosacījumi:* Vajadzīgs pierādījums ar patvaļīgu nepārtrauktu testa funkciju un izpildīts skaitlisks kontrolpiemērs. Neapgalvo, ka šī secība pierāda visu skaitlisko integratoru kļūmi.

##### Izpētītā atbilde

$f_n\to0$ katrā punktā un gandrīz visur, bet $L^1$ konverģences nav. Mēri $\mu_n=f_n(x)\,dx$ uz slēgtā intervāla $[0,1]$ vāji konverģē uz Diraka mēru $\delta_0$.

##### Punktveida un $L^1$ uzvedība

Pie $x=0$ visiem n ir $f_n(0)=0$, jo indikatora intervāls ir atvērts. Fiksētam $x>0$, izvēloties $n>1/x$, arī ir $f_n(x)=0$. Robeža tādēļ ir nulle visos $[0,1]$ punktos.

Tomēr

$$
\int_0^1f_n(x)\,dx=n\frac1n=1,\qquad
\|f_n-0\|_1=1
$$

visiem n. Secība nekonverģē uz nulli $L^1$. Tā nekonverģē $L^1$ arī uz kādu citu funkciju: pie $m\ge n$

$$
\|f_m-f_n\|_1
=(m-n)\frac1m+n\left(\frac1n-\frac1m\right)
=2\left(1-\frac nm\right).
$$

Liekot $m=2n$, attālums ir 1, tātad secība nav Košī secība $L^1$.

##### Mēru vājā robeža

Ņemam patvaļīgu $\varphi\in C([0,1])$. Tad

$$
\int_{[0,1]}\varphi\,d\mu_n
=n\int_0^{1/n}\varphi(x)\,dx
=\int_0^1\varphi(y/n)\,dy.
$$

Ar nepārtrauktības moduli pie nulles

$$
\left|\int\varphi\,d\mu_n-\varphi(0)\right|
\le\sup_{0\le x\le1/n}|\varphi(x)-\varphi(0)|
\longrightarrow0.
$$

Tā kā $\int\varphi\,d\delta_0=\varphi(0)$, iegūstam $\mu_n\Rightarrow\delta_0$. Pierādījums attiecas uz katru nepārtrauktu testa funkciju, ne tikai uz dažiem momentiem.

Diraka mēram ir masa 1 punktā 0; to nevar uzrakstīt kā $L^1$ blīvumu pret Lebega mēru, jo šāda blīvuma integrālis pār vienpunktu kopu būtu 0. Tādēļ mēru vājā konverģence nav šīs blīvumu secības $L^1$ konverģence. Intervāls ir būtisks: uz $(0,1)$, testējot tikai ar kompakti atbalstītām nepārtrauktām funkcijām, iegūtu vago robežu 0, jo atbalsts ir prom no nulles.

Saikni ar vienības laukuma impulsiem rāda Rowell MIT signālapstrādes lekcija. Tās impulsa apzīmējumu šeit interpretējam kā mēra robežu, kuru iepriekš pierādījām; punktveida robeža joprojām ir nulle. [Lekcija](https://ocw.mit.edu/courses/2-161-signal-processing-continuous-and-discrete-fall-2008/a6d15b07b9720f44e4bc2e9da4d3a5a2_lecture_01.pdf).

##### Kāpēc integrāli un robežu samainīt nevar

Šeit

$$
\int\lim_nf_n=0,\qquad \lim_n\int f_n=1.
$$

Dominētās konverģences teorēmas priekšnosacījums nav izpildīts: neeksistē integrējama $g$, kas dominētu visus $f_n$ gandrīz visur. Pretējā gadījumā

$$
\int_0^{1/n}|g(x)|\,dx\ge1
$$

visiem n, lai gan integrējamas funkcijas integrāļa absolūtā nepārtrauktība prasa, lai šie integrāļi tiektos uz 0. Līdz ar to šāds integrējams dominētājs nevar eksistēt.

Trūkst arī vienmērīgas integrējamības. Katram galīgam $K>0$, izvēloties $n>K$,

$$
\int_{\{|f_n|>K\}}|f_n|\,dx=1.
$$

Tātad šo integrāļu supremums pēc n ir 1 visiem K un netiecas uz nulli. Līdzvērtīgi, kopās $A_n=(0,1/n)$ mērs tiecas uz 0, bet $\int_{A_n}f_n=1$.

Vienmērīgas integrējamības kritērijs un saikne ar $L^1$ konverģenci gandrīz visur konverģējošām secībām doti Ulmas universitātes lemmu 3.6 un 3.7 formulējumos un pierādījumos. Ķīnas pirmavota kursā definīcija 6.11 dod to pašu astes kritēriju. [Ulma](https://www.mathematik.uni-ulm.de/stochastik/lehre/ss05/wt/skript/node41.html), [Pekinas universitāte](https://math.pku.edu.cn/teachers/lidf/course/stochproc/stochprocnotes/html/_book/martingale.html).

Monotonās konverģences teorēma arī nav piemērojama: secība nav punktveidā monotoni augoša. Fatū lemma paliek spēkā un dod $0\le1$, ne vienādību.

##### Izpildītie kontrolaprēķini

| n | $\int f_n$ | $\int xf_n$ | $\int x^2f_n$ | $\int e^xf_n$ |
|---:|---:|---:|---:|---:|
| 10 | 1 | 1/20 | 1/300 | 1.0517091808 |
| 100 | 1 | 1/200 | 1/30000 | 1.0050167084 |
| 1000 | 1 | 1/2000 | 1/3000000 | 1.0005001667 |
| 1 000 000 | 1 | 1/2 000 000 | 1/3 000 000 000 000 | 1.0000005000 |

Formulas ir attiecīgi $1,\ 1/(2n),\ 1/(3n^2),\ n(e^{1/n}-1)$; pēdējai izmantots skaitliski stabils expm1 aprēķins. Tabula ilustrē robežu, bet patvaļīgas testa funkcijas pierādījumu neaizstāj.

##### Divi mehānismu pārnesumi

Signālapstrādes vienības impulsa ideja dod pareizo saglabājamās masas objektu. To apstiprina pilnais testa funkcijas pierādījums un aprēķinātie momenti. Hipotēzi, ka pati funkcija punktveidā kļūst par Diraka blīvumu, noraidām: Diraka mēram šāda blīvuma nav.

Otrs pārnesums ir koncentrācijas mēroga pielāgošana integrēšanā. Pie $n=1000$ parastā viduspunkta summa ar 100 vienādiem intervāliem deva 0, jo pirmais punkts 0.005 jau atrodas ārpus impulsa atbalsta $(0,0.001)$. Pēc mainīgā maiņas $x=y/n$ tie paši 100 viduspunkti dod masu 1; testam $e^x$ absolūtā kļūda bija $4.17\cdot10^{-12}$.

Tas ir konkrētas fiksēta režģa formulas piemērs. Tas nepierāda visu skaitlisko integratoru kļūmi. Nākamais tests būtu salīdzināt arī nezināma atbalsta adaptīvu integrēšanu ar skaidri noteiktu kļūdas budžetu; tas nav veikts.


*Izpildītā aprēķina faili:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NF05/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NF05/calculation.py)

*Izpētes izcelsme: NF05; 5 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `a523076932500c82b629e80bfe43112b67b2dcb748d03dda97373662a58b7ca8`.*

<a id="final30-nf06"></a>

#### NF06 — Strang shēma un oscilatora enerģija

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Harmoniskam oscilatoram ņem A=[[0,1],[0,0]],B=[[0,0],[-1,0]] un Strang soli M_h=exp(hA/2)exp(hB)exp(hA/2). Atvasini M_h, nosaki soļus, kuros tā pakāpes ir ierobežotas, atsevišķi izskatot h=2. Atrodi saglabātu pozitīvi definitu kvadrātisku formu stabilajā intervālā. Salīdzini ar eksplicīto Euler metodi.

*Pārbaudes nosacījumi:* h>0. Vajadzīgs algebraiskais pierādījums, izpildīts ilgāka soļu skaita eksperiments un primārais avots. Vienības modulis īpašvērtībām robežgadījumā pats par sevi nav pietiekams.

##### Izpētītā atbilde

**Matricas pakāpes ir ierobežotas tieši pie $0<h<2$.** Pie $h=2$ tās aug lineāri; pie $h>2$ — eksponenciāli. Stabilajā intervālā solis saglabā pozitīvi definitu formu

$$
E_h(x,v)=\tfrac12\bigl(x^2+(1-h^2/4)v^2\bigr).
$$

Eksplicītā Eilera metode šim nedempētajam oscilatoram ir nestabila pie katra fiksēta $h>0$.

##### Matrica un algebraiskais stabilitātes pierādījums

Tā kā $A^2=B^2=0$, abas eksponentes saīsinās pēc pirmās pakāpes. Reizinot uzdevumā norādītajā secībā,

$$
M_h=
\begin{pmatrix}1&h/2\\0&1\end{pmatrix}
\begin{pmatrix}1&0\\-h&1\end{pmatrix}
\begin{pmatrix}1&h/2\\0&1\end{pmatrix}
=
\begin{pmatrix}
1-h^2/2 & h-h^3/4\\
-h & 1-h^2/2
\end{pmatrix}.
$$

Apzīmēsim $a=1-h^2/2$, $c=1-h^2/4$. Tad $a^2+h^2c=1$, $\det M_h=1$ un

$$
\chi_{M_h}(\lambda)=\lambda^2-2a\lambda+1.
$$


Ja $0<h<2$, tad $c>0$, un

$$
P_h=\operatorname{diag}(1,c)>0,\qquad
M_h^\mathsf TP_hM_h=P_h.
$$

Identitāti iegūst, tieši sareizinot matricas un izmantojot $a^2+h^2c=1$; tā arī simboliski pārbaudīta saglabātajā kodā. Tāpēc $E_h(M_hz)=E_h(z)$, un visiem veseliem $k\ge0$

$$
c\|M_h^kz\|_2^2
 \le (M_h^kz)^\mathsf TP_h(M_h^kz)
 =z^\mathsf TP_hz
 \le\|z\|_2^2.
$$

Tātad

$$
\boxed{\|M_h^k\|_2\le(1-h^2/4)^{-1/2}\quad(k\ge0).}
$$

Robeža attiecas uz katru fiksētu $h<2$; konstante nav vienmērīga, tuvojoties $h=2$.

Vēl tiešāk: $D=P_h^{1/2}$ dod

$$
DM_hD^{-1}=
\begin{pmatrix}a&h\sqrt c\\-h\sqrt c&a\end{pmatrix},
$$

kas ir ortogonāla rotācijas matrica. Tās īpašvērtības ir $a\pm ih\sqrt c$, abas ar moduli 1. Mainīgā mēroga koordinātas izskaidro, kāpēc saglabājas elipse, kamēr parastā enerģija $H=(x^2+v^2)/2$ var svārstīties.

Struktūras saglabāšana un modificētas dinamikas analīze ir arī Hairer, Lubich un Wanner oriģinālās publikācijas temats. Šajā darbā no tās aktuāli nolasīts kopsavilkums; konkrētā matrica un precīzā forma iepriekš atvasināta patstāvīgi.

##### Robežgadījums $h=2$

Šeit

$$
M_2=\begin{pmatrix}-1&0\\-2&-1\end{pmatrix}=-I+N,
\qquad N=\begin{pmatrix}0&0\\-2&0\end{pmatrix},\quad N^2=0,\ N\ne0.
$$

Binoma formula dod

$$
\boxed{M_2^k=(-1)^k
\begin{pmatrix}1&0\\2k&1\end{pmatrix}.}
$$

Piemēram, $\|M_2^k(1,0)^\mathsf T\|_2=\sqrt{1+4k^2}\to\infty$, un precīzā operatora norma ir

$$
\|M_2^k\|_2=k+\sqrt{k^2+1}.
$$

Abas īpašvērtības ir $-1$, bet matrica nav diagonalizējama. Sākuma vektors $(0,1)^\mathsf T$ gan paliek ierobežots; tas nepadara visu matricu pakāpes ierobežotas. Pie šī soļa $P_h$ kļūst tikai pozitīvi pusdefinita. Neviena cita pozitīvi definita saglabāta forma nevar pastāvēt, jo tā dotu pretrunīgu ierobežotības pierādījumu.

Digitālo sistēmu analīzē analogs ir atkārtots neanulēts pols uz vienības riņķa: tas var radīt augošu locekli. ADI sākotnējā mācību materiāla 2.4. nodaļa šo izņēmumu skaidri izdala. Te pārbaudām autonomas matricas pakāpes, tādēļ nepielīdzinām šo kritēriju piespiestas sistēmas BIBO stabilitātei.

Ja $h>2$, tad $a<-1$, un īpašvērtības

$$
\lambda_\pm=a\pm h\sqrt{h^2/4-1}
$$

ir reālas, savstarpēji apgrieztas, un $\lambda_-<-1$. Atbilstošā īpašvektora trajektorija aug eksponenciāli. Kopā ar robežgadījumu tas pierāda apgalvojumu “tieši $0<h<2$”.

##### Eilera metode


$$
F_h=I+h(A+B)=
\begin{pmatrix}1&h\\-h&1\end{pmatrix},\qquad
F_h^\mathsf TF_h=(1+h^2)I.
$$

Tā kā $F_h/\sqrt{1+h^2}$ ir ortogonāla,

$$
\boxed{\|F_h^k\|_2=(1+h^2)^{k/2}},\qquad
H(F_h^kz)=(1+h^2)^kH(z).
$$

Tas pierāda neierobežotu augšanu visiem $h>0$ un katram nenulles sākuma vektoram. Pastewka autora kursa 14.–15. formula dod šo pašu enerģijas pieaugumu; kursā apskatītajam Verlet variantam pussoļu secība atšķiras, tādēļ tā enerģijas formu uz mūsu matricu nepārnesu.

##### Izpildītais ilgtermiņa eksperiments

Kods vispirms precīzi pārbaudīja matricu identitātes ar SymPy, pēc tam ar NumPy secīgi sareizināja soļa matricu. Stabilajiem soļiem veikti 10 000 reāli atkārtojumi, katrā skaitļojot operatora normu un invarianta defektu.

| $h$ | Soļi | Lielākā novērotā $\|M_h^k\|_2$ | Pierādītā robeža | Lielākais $\|(M_h^k)^\mathsf TP_hM_h^k-P_h\|_2$ |
|---:|---:|---:|---:|---:|
| 0.1 | 10 000 | 1.001252349 | 1.001252349 | $7.26\cdot10^{-14}$ |
| 1 | 10 000 | 1.132782219 | 1.154700538 | 0 |
| 1.9 | 10 000 | 3.202563052 | 3.202563076 | $1.44\cdot10^{-12}$ |
| 1.999 | 10 000 | 31.626730169 | 31.626730190 | $2.05\cdot10^{-12}$ |

Robežgadījumā 10 000 atkārtojumi deva tieši $\bigl(\begin{smallmatrix}1&0\\20000&1\end{smallmatrix}\bigr)$, bet norma ir aptuveni 20 000.00005. Pie $h=2.1$ pēc 1000 soļiem norma bija $5.972479742\cdot10^{273}$. Eilera metode pie $h=0.1$ pēc 10 000 soļiem deva $4.044537936\cdot10^{21}$, relatīvā atšķirība no slēgtās formulas bija $3.78\cdot10^{-15}$.

Skaitliskie dati apstiprina konkrēto realizāciju; apgalvojums par visiem soļu skaitiem balstās algebraiskajā pierādījumā. Saglabāšana arī nenozīmē precīzu fāzi: Stranga rotācijas leņķis ir $\theta=\arccos(1-h^2/2)$, bet precīzā risinājuma leņķis ir $h$. Pie $h=0.1$ pēc 10 000 soļiem uzkrātā leņķu starpība, neatņemot pilnos apgriezienus, ir $10000(\theta-h)=0.4171361154$ radiāni.

##### Divi pārbaudītie pārnesumi un nākamais tests

**H1 — uzkrātās enerģijas sertifikāts no pasīvu sistēmu analīzes.** Meklējām pozitīvu svaru matricu, kas diskretizēto soli padara par izometriju. Atrastā $P_h$, simboliskā identitāte un ilgtermiņa aprēķins hipotēzi atbalsta tieši $0<h<2$. Tā negarantē sākotnējās enerģijas precīzu saglabāšanu vai pareizu fāzi.

**H2 — digitāla rezonatora vienības riņķa nosacījuma pārnešana uz visu slēgto intervālu.** Pārbaudījām, vai īpašvērtību modulis 1 ļauj iekļaut $h=2$. Precīzā Žordāna formula un 10 000 soļu tests šo paplašinājumu noraida. Ārpus integrēšanas nozares lietotais vaicājums bija “lossless digital oscillator repeated pole unit circle stability Jordan block”.

Diagnoze: kritiskais punkts ir saglabātās formas pozitivitātes zudums pie robežas, turklāt stabilitāte un fāzes precizitāte ir dažādi kritēriji. Nākamais noderīgais tests ir pārbaudīt divu atšķirīgu, atsevišķi stabilu soļu periodisku maiņu: katram ir cita $P_h$, tādēļ kopēju ierobežotību automātiski secināt nevar. Šis nākamais tests šajā darbā nav izpildīts.

Meklēts EN/DE/ZH/JA; izpildīti 6 vaicājumi un 5 tīmekļa izsaukumi ar 7 atvērumu mēģinājumiem. Ženēvas un pilnteksta alternatīvu neveiksmīgās atbildes saglabātas. Izmantotas viena aģenta četras pārbaudes perspektīvas; tās nav neatkarīgas instances.

Primārie avoti: [Hairer, Lubich, Wanner (2003), kopsavilkums](https://www.cambridge.org/core/journals/acta-numerica/article/abs/geometric-numerical-integration-illustrated-by-the-stormerverlet-method/E55395D5DD7A4E0526D10EA74DA6C46B), [ADI, 2. nodaļa](https://www.adi.com/resource-library/dynamics-of-real-time-simulation-chapter-2/), [Pastewka, Euler-Integration](https://pastewka.github.io/Differentialgleichungen/lecture/chapter11.html).


*Izpildītā aprēķina faili:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NF06/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NF06/calculation.py)

*Izpētes izcelsme: NF06; 6 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `0482bf41d61c75dd8a560388ec7e5ef0eb4b087bcb653dafaf6ad414e6d350c2`.*

<a id="final30-nf07"></a>

#### NF07 — Piektās pakāpes polinoma Galuā grupa

**Sākotnējais jautājums un nepieciešamie nosacījumi**

Nosaki f(x)=x^5-x-1 Galuā grupu pār Q un vai saknes izsakāmas radikāļos. Izmanto precīzu faktorizāciju modulo 2 un modulo 3, norādot, kāpēc attiecīgie ciklu tipi nosaka grupu. Pārbaudi diskriminantu un katras izmantotās teorēmas priekšnosacījumus.

*Pārbaudes nosacījumi:* Vajadzīgs pilns arguments, izpildīta precīza polinomu aritmētika un primārie matemātikas avoti. CAS grupas nosaukums viens pats nav pierādījums.

##### Izpētītā atbilde

$$
\boxed{\operatorname{Gal}(x^5-x-1\,/\,\mathbb Q)\cong S_5.}
$$

**Neviena šī polinoma sakne nav izsakāma radikāļos pār $\mathbb Q$.** Pierādījums izmanto precīzu faktorizāciju modulo 2 un 3, teorēmu priekšnosacījumus un izpildītus aritmētikas sertifikātus.

##### Diskriminants un labie pirmskaitļi

Lai $f=x^5-x-1$, $g=f'=5x^4-1$. Polinoms ir monisks, tāpēc

$$
\operatorname{disc}(f)=(-1)^{5\cdot4/2}\operatorname{Res}(f,g)
=\operatorname{Res}(f,g).
$$

Izmantojot $f=(x/5)g-4x/5-1$, rezultanta simetriju un atlikuma formulu,

$$
\begin{aligned}
\operatorname{Res}(f,g)
&=\operatorname{Res}(g,f)\\
&=5^4\operatorname{Res}(g,-4x/5-1)\\
&=4^4g(-5/4)=5^5-4^4\\
&=\boxed{2869=19\cdot151}.
\end{aligned}
$$

Zīme ir pozitīva. Rezultanta formulas moniskam polinomam un tā atvasinājumam izklāstītas Milne 4.35.–4.36. apgalvojumā; šeit visi koeficienti ir precīzi racionāli skaitļi.

Tādēļ $f$ ir separabls. Turklāt $2869\equiv1\pmod2$ un $2869\equiv1\pmod3$, tātad abiem izvēlētajiem pirmskaitļiem redukcijās nav atkārtotu sakņu. Kods atsevišķi pārbaudīja arī $\gcd(\bar f,\bar f')=1$ abos laukos un aprēķināja diskriminantu kā precīzu $9\times9$ Silvestra matricas determinantu.

##### Precīzās faktorizācijas

###### Modulo 2


$$
\bar f=x^5+x+1=(x^2+x+1)(x^3+x^2+1)
\quad\text{laukā }\mathbb F_2[x].
$$

Abiem faktoriem vērtības punktos 0 un 1 ir 1. Otrās vai trešās pakāpes polinoms pār lauku ir reducējams tieši tad, ja tam ir sakne šajā laukā. Tātad abi faktori ir nesadalāmi; tie ir atšķirīgi un parādās vienreiz.

###### Modulo 3


$$
\bar f=x^5+2x+2.
$$

Vērtības punktos $0,1,2$ visas ir 2, tātad lineāru faktoru nav. Visi moniskie nesadalāmie kvadrātiskie polinomi pār $\mathbb F_3$ un dalīšanas atlikumi ir:

| Dalītājs | $f$ atlikums modulo dalītāju un 3 |
|---|---|
| $x^2+1$ | $-1$ |
| $x^2+x+2$ | $x-1$ |
| $x^2+2x+2$ | $x-1$ |

Saraksta pilnību pārbauda, pārskatot deviņus $x^2+bx+c$, $b,c\in\mathbb F_3$: tieši šiem trim nav saknes. Neviens nedala $f$.

Ja piektās pakāpes polinoms būtu reducējams, tā nesadalāmo faktoru sadalījumā būtu vismaz viens faktors ar pakāpi 1 vai 2; divas pakāpes, kuras abas ir vismaz 3, jau pārsniegtu 5. Tāpēc

$$
\boxed{x^5+2x+2\text{ ir nesadalāms pār }\mathbb F_3.}
$$


Tas ir arī precīzs pamatojums CAS izdrukātajai faktorizācijai, nevis paļaušanās uz CAS secinājumu. Papildu pārbaude izveidoja Bezū identitāti $\mathbb F_3[x]$:

$$
u f+v(x^9-x)=1,
$$

kur

$$
\begin{aligned}
u&=x^8+x^7+x^6+x^5-x^4-x^3-x^2-x-1,\\
v&=-x^4-x^3-x^2-x-1.
\end{aligned}
$$

Tā vēlreiz apliecina, ka nav faktoru, kuru pakāpe dala 2.

Tā kā $f\in\mathbb Z[x]$ ir monisks un primitīvs, Gausa lemma ļautu jebkuru netriviālu faktorizāciju pār $\mathbb Q$ pārrakstīt monisku veselu koeficientu faktoru reizinājumā. Redukcija modulo 3 saglabātu abu faktoru pozitīvās pakāpes, radot pretrunu. Tādēļ $f$ ir nesadalāms arī pār $\mathbb Q$. Mascot autora lekcijā šis konkrētais piemērs, diskriminants un abi modulārie sadalījumi apskatīti 22.–24. slaidā; šajā darbā to aritmētika izpildīta no jauna.

##### No ciklu tipiem līdz $S_5$

Lai $K$ ir $f$ sadalīšanās lauks pār $\mathbb Q$. Tas ir galīgs, normāls un separabls paplašinājums. Tā automorfismi uzticami permutē piecas atšķirīgās saknes, tāpēc $G=\operatorname{Gal}(K/\mathbb Q)\le S_5$. Nesadalāmība nozīmē arī tranzitivitāti.

Dedekinda ciklu tipu teorēma attiecas uz monisku veselu koeficientu polinomu un pirmskaitli, kas nedala diskriminantu. Redukcijas atšķirīgo nesadalāmo faktoru pakāpes tad dod kāda $G$ elementa disjunkto ciklu garumus. Visi šie priekšnosacījumi iepriekš pārbaudīti; netiek apgalvots, ka visa Galuā grupa būtu redukcijas cikliskā grupa.

Tātad modulo 2 sadalījums dod

$$
\sigma=(ab)(cde)\in G,
\qquad \tau=\sigma^3=(ab)\in G,
$$

bet modulo 3 nesadalāmība dod 5-ciklu $\gamma\in G$.

Atliek pierādīt, kāpēc šajā situācijā $\gamma$ un $\tau$ ģenerē $S_5$. Pārnumurēsim saknes ar $\mathbb Z/5\mathbb Z$, lai $\gamma(i)=i+1$. Pēc cikliskas pārnumurēšanas $\tau=(0,d)$, kur $d\ne0$. Tad

$$
\gamma^k\tau\gamma^{-k}=(k,k+d)\in G.
$$

Šīs transpozīcijas ir grafa šķautnes starp virsotnēm, kuru starpība ir $d$. Tā kā 5 ir pirmskaitlis, $d$ ir invertējams modulo 5 un grafs ir saistīts.

Saistīta grafa šķautņu transpozīcijas ģenerē visas transpozīcijas: gar vienkāršu ceļu $v_0,\ldots,v_m$, apzīmējot $t_j=(v_{j-1},v_j)$, iegūstam

$$
(v_0,v_m)=t_1\cdots t_{m-1}t_m t_{m-1}\cdots t_1.
$$

Visas permutācijas ir transpozīciju reizinājumi. Tādēļ $G$ satur $S_5$, un, tā kā $G\le S_5$, ir $G=S_5$. Ar transpozīcijām radītu tranzitīvu grupu arguments ir izklāstīts arī Conrad autora piezīmju pirmajā pierādījuma solī.

Šeit būtiski izmantots tieši pirmskaitlis 5. Apgalvojums “jebkurš $n$-cikls un jebkura transpozīcija ģenerē $S_n$” bez papildu nosacījumiem nav vispārīga teorēma.

##### Kāpēc nav izteiksmes radikāļos

Galuā atrisināmības teorēma raksturlielumā 0 saka: polinoms atrisināms radikāļos tieši tad, ja tā Galuā grupa ir atrisināma. Laukam $\mathbb Q$ raksturlielums ir 0, un mūsu polinoms ir separabls. Pieļauj arī kompleksus starprezultātus un vienības saknes; to aizliegums nav šā secinājuma pamats.

Grupa $S_5$ nav atrisināma. To šeit var pārbaudīt bez grupu klasifikācijas: $A_5$ konjugācijas klašu izmēri ir $1,15,20,12,12$. Tie atbilst identitātei, divām disjunktām transpozīcijām, 3-cikliem un abām 5-ciklu klasēm. Izmērus dod centralizatoru kārtas $60,4,3,5,5$; arī visi 60 elementi kodā precīzi pārskatīti.

Normālai apakšgrupai jābūt konjugācijas klašu apvienojumam, kurā ir identitāte, un pēc Lagranža teorēmas tās kārtai jādala 60. No iespējamām klašu izmēru summām tikai 1 un 60 dala 60. Tātad $A_5$ ir vienkārša. Tā nav abeliska, tāpēc tās komutatoru apakšgrupa ir netriviāla normāla apakšgrupa un sakrīt ar $A_5$. Atvasinātā virkne nesasniedz identitāti. Tā kā atrisināmas grupas apakšgrupa ir atrisināma, arī $S_5$ nav atrisināma.

Secinājums attiecas pat uz katru atsevišķo sakni. Ja viena sakne atrastos galīgā radikāļu paplašinājumā, šo paplašinājumu varētu iekļaut galīgā Galuā paplašinājumā ar atrisināmu grupu, pievienojot vajadzīgās vienības saknes un konjugātes. Normalitātes un $f$ nesadalāmības dēļ tajā atrastos visas $f$ saknes. Tad $G$ būtu atrisināmas grupas faktorgrupa — pretruna. Šī paplašinājuma konstrukcija ietilpst tikko minētās teorēmas pierādījumā.

##### Izpildītās pārbaudes un divas hipotēzes

Saglabātais kods izmanto precīzu polinomu un veselu skaitļu aritmētiku. Tas pārbaudīja faktoru reizinājumus, visas deviņas kvadrātiskās kandidatūras modulo 3, Bezū identitāti, diskriminantu ar diviem simboliskiem aprēķiniem un atsevišķu determinantu. Grupas nosaukuma noteikšanas funkcija netika izmantota.

**H1 — grafu saistītības sertifikāts grupas ģenerēšanai.** No šķautņu transpozīcijām iegūtais pierādījums aptver jebkuru transpozīcijas novietojumu pret 5-ciklu. Kods papildus pārbaudīja visus desmit novietojumus; katrs ģenerēja 120 elementus. Hipotēze šim uzdevumam apstiprināta. Ārpus Galuā teorijas meklētais vaicājums bija “connected graph edge transpositions generate symmetric group prime cycle”.

**H2 — diskriminanta kvadrātiskums kā pietiekams grupas identifikators.** Tā ir pārāk vāja pazīme. Nekvadrātisks diskriminants dod tikai $G\not\subseteq A_5$, nevis $G=S_5$. Kods konstruēja 20 afīnās permutācijas $x\mapsto ax+b$ uz $\mathbb F_5$, $a\ne0$. Šī īstā $S_5$ apakšgrupa ir tranzitīva, satur 5-ciklus un nepāra permutācijas, bet nesatur ciklu tipu $(2)(3)$. Precīzie tipu skaiti bija: identitāte 1, $(1)(2)(2)$ — 5, $(1)(4)$ — 10, $(5)$ — 4. Tādēļ hipotēze, ka nesadalāmība un nekvadrātiskums vien jau nosaka $S_5$, noraidīta. Šī afīnā grupa netiek piedēvēta dotajam polinomam.

Diagnoze: aritmētiski izšķirošais sertifikāts ir atšķirīgo 2. un 3. pakāpes faktoru pāris, no kura iegūst transpozīciju; tikai diskriminanta paritātes informācija to neaizstāj. Pieeja šim gadījumam nav jāmaina. Nākamais pārnesuma robežu tests būtu atkārtot cikla un transpozīcijas ģenerēšanu saliktā pakāpē, piemēram, 6, ar dažādiem šķautņu attālumiem. Šis nākamais tests šeit nav izpildīts, un vispārīgs uzlabojuma ieguvums nav apgalvots.

Meklēts EN/DE/ZH/JA; izpildīti 5 vaicājumi, 5 tīmekļa izsaukumi un 6 atvērumi. Iekšējā pārbaude veikta no četrām viena aģenta perspektīvām.

Primārie avoti: [Milne, Fields and Galois Theory](https://www.jmilne.org/math/CourseNotes/FT.pdf), [Mascot, Galois theory, 3. nodaļa](https://www.maths.tcd.ie/~mascotn/teaching/2021/MAU34101/3%20GalPoly.pdf), [Conrad, The Galois Group of $x^n-x-1$](https://kconrad.math.uconn.edu/blurbs/gradnumthy/galoisselmerpoly.pdf).


*Izpildītā aprēķina faili:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NF07/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NF07/calculation.py)

*Izpētes izcelsme: NF07; 5 vaicājumi; EN / DE / ZH / JA. Oriģinālās atbildes SHA-256: `c9f59189d47f357533fb3bb00c5bdb27dee4054ac671143a59284690f5f9242d`.*


<a id="historical30"></a>

## Vēsturiskā kopa: visas 30 atbildes

Pārbaudes datums: 2026. gada 9. novembris.

> Redakcija, 2026. gada 10. novembris: publikācijai veikti nelieli gramatikas un pieturzīmju labojumi. Datēta piezīme precizē vēsturisko vaicājumu uzskaiti. Saglabāti visi jautājumi, dotie skaitliskie dati un nosacījumi, pilnās atbildes, matemātiskie argumenti, izpētes rezultāti un avotu adreses. Sākotnējie izpētes ieraksti glabājas atsevišķi; pašreizējās publikācijas failus identificē failu manifests.

Šajā izdevumā ir 10 ikdienas, 10 praktiski tehniski un 10 pētniecības jautājumi. Jautājumus sagatavojām pārbaudei; tās nav intervijas ar 30 cilvēkiem. Nepieciešamie lietotāja precizējumi ir skaidri apzīmēti kā izdomāti testa scenārija dati. Tīmekļa meklējumi, avotu lasīšana, atbilžu rakstīšana un pieredzes saglabāšanas darbības tika faktiski izpildītas.

Trīs atsevišķi izpildītāji strādāja ar savām jautājumu grupām. Katrā jautājumā veikti meklējumi angļu, vācu, ķīniešu un japāņu valodā. Tas nenozīmē, ka katrā valodā atradās derīgs un pilnībā izlasāms avots. Avotu trūkumi un neatvērtās lapas saglabāti pārbaudes ierakstos.

Atbildes rāda prasmes lietojumu un tās praktiskās kļūdu pārbaudes. Šeit nav veikts kontrolēts salīdzinājums, kas pierādītu pārākumu pār visiem citiem meklētājiem vai MI. Pašreizējās cenas, programmu versijas un pakalpojumu iespējas pirms izmantošanas jāpārbauda no jauna.

### Ko izmainījām pēc pārbaudēm

Avotu atvēršanu tagad skaidri nošķir no vajadzīgās teksta vietas izlasīšanas. Meklējuma valodu reģistrē atsevišķi no avota satura valodas. Skaitliskus ieteikumus pārrēķina ar konkrētā uzdevuma datiem, arī tad, ja piemēru publicējis speciālists. Jaunu paziņojumu nošķir no neatkarīgas pārbaudes un atzīta rezultāta.

Izpildes savienotājam pievienota stingra pierādījumu ierakstu pārbaude. Tā atsaka pabeigtu izpildi, ja trūkst prasīto avotu, apgalvojumu, meklējumu vai redakcijas ierakstu. Šī pārbaude pārbauda failus un ierakstus; tā pati nepierāda teikumu patiesumu. Šie 30 piemēri izmantoja manuālo sākuma un beigu ciklu, savukārt jaunā savienotāja pārbaudes tika veiktas atsevišķi.

### Rezultāti

> Redakcijas precizējums, 2026. gada 10. novembris: zemāk saglabāta sākotnējā uzskaites rindkopa. Vēlākā pārbaude apstiprināja 143 atšķirīgus vaicājumus ar saglabātām sākotnējām kvītīm; sākotnējā kopskaitā 147 bija iekļauti arī četri deklarēti E10 vaicājumi, kuru pilnā sākotnējā izvade nebija saglabāta.

Faktiski izpildīti 147 vaicājumi: EN 50, DE 33, ZH 33, JA 31. Tie ietver 143 atšķirīgus vaicājumu tekstus un 4 atkārtojumus pēc pārtraukuma. E10 četru sākotnējo rīka izsaukumu pilnie rezultāti nebija saglabāti; atkopšanas laikā avoti tika atkārtoti nolasīti un jaunie izsaukumi saglabāti. Šis iztrūkums ir norādīts, ne aizvietots ar izdomātiem ierakstiem.

### Ikdienas jautājumi

#### E01

Man seja kaut kā spīd un kosmētika pēc stundas pazūd. Ko man nopirkt?

##### Nepieciešamais precizējums

Kāds ir ādas tips un vai ir kairinājums; kādu grimu lieto, un vai vispirms vajadzīga uzklāšanas metode? Kāds budžets un valsts?

##### SIMULĒTA atbilde pārbaudes uzdevumā

Pieaugušais; taukaina T zona, normāli vaigi, nav kairinājuma; ikdienas grims; vispirms uzklāšanas metode; 30 EUR Latvijā.

Šī ir uzdevuma devēja dota simulācija, nevis reāls lietotāja apstiprinājums.

Sāktu ar plānākām grima kārtām un nelielu daudzumu matējoša pūdera T zonā. Visus 30 € uzreiz tērēt nevajag.

1. Uzklāj savu ierasto krēmu nelielā daudzumā un ļauj tam nosēsties. Pirms tonālā āda nedrīkst palikt izteikti slidena. Taukojošajai T zonai un normālajiem vaigiem vari pielāgot daudzumu atsevišķi. Šādu pieeju apraksta [KOSE](https://www.kose.co.jp/kose/make/make104.html).
2. Tonālo klāj plāni; papildu kārtu liec tikai vietās, kur vajag lielāku segumu. Tā ir [intervēto grima mākslinieku darba metode](https://www.allure.com/story/how-to-make-makeup-last-all-day), kuru ir vērts izmēģināt ar jau esošo tonālo.
3. Nedaudz caurspīdīga pūdera viegli piespied pierei, degunam un zodam. Vaigiem nevajag automātiski tikpat biezu kārtu. [Ražotāja norādes](https://www.essence.eu/de-de/make-up-tips/how-to-setting-powder) arī iesaka pūdera daudzumu pielāgot sejas zonām.
4. Kad parādās spīdums, vispirms viegli piespied salveti, neberzējot seju. Tikai pēc tam izlīdzini grimu un, ja vajag, pievieno pavisam maz pūdera. Tā grimu pielabo [CBC televīzijas grimētāji](https://www.hicbc.com/magazine/article/?id=metone-makecolumndo813-260829).

Ja pūdera nav, lētam izmēģinājumam der apsvērt [essence All About Matt, 8 g](https://www.drogas.lv/lv/kosmetika/sejai/kompaktpuderi-puderi/essence-all-about-matt-fixing-kompaktais-puderis-8g/p/BP_225741). Atvērtajā Drogas lapā norādīti 3,39 €; pirms pirkuma pārbaudi cenu un pieejamību. Turpat ir arī pircēju sūdzības par īsu matējuma noturību. Individuālo rezultātu uz tavas ādas no šīs informācijas paredzēt nevar.

Mans ierosinājums: vienu dienu pamēģini šo secību un pēc stundas apskati tieši T zonu. Ja grims joprojām pazūd, nākamajā solī vajadzēs pārbaudīt konkrēto krēma, saules aizsarglīdzekļa un tonālā kombināciju.

#### E02

Esmu 1,80 m. Kādas bikses man piestāvēs?

##### Nepieciešamais precizējums

Kādu siluetu un lietojumu vēlies, un vai meklē piegriezumu vai konkrētu izmēru? Vai ir zināms vidukļa apkārtmērs un iekšstaras garums?

##### SIMULĒTA atbilde pārbaudes uzdevumā

Ikdienai, patīk taisns siluets; vajadzīga pielaikošanas metode; viduklis un iekšstara nav izmērīti; konkrēts izmērs nav prasīts.

Šī ir uzdevuma devēja dota simulācija, nevis reāls lietotāja apstiprinājums.

Sāktu ar taisnām ikdienas biksēm un salīdzinātu divus piegriezumus: parastu taisnu un nedaudz brīvāku augšstilbos. Tas ir mans pielaikošanas ierosinājums, kas atbilst tavai izvēlei. No 1,80 m auguma vien nevar noteikt vajadzīgo vidukli, staras garumu vai to, kurš siluets tev patiks. Ražotāji šos mērījumus vērtē atsevišķi. [Levi’s mērīšanas ceļvedis](https://www.levi.com/GB/en_GB/blog/article/how-to-measure-jeans)

Pielaikojot pārbaudi šādi:

- Aiztaisi jostasvietu un apsēdies. Tai jābūt ērtai arī sēdus; augšstilbus un stakli nedrīkst stipri vilkt.
- Apskaties no priekšpuses, sāniem un aizmugures. Novērtē, vai audums pie gurniem nav izteikti nostiepts vai sakrājies liekā maisā.
- Izmēģini ikdienā vajadzīgās kustības. Ja iespējams, arī pāris soļus. Japānas drēbnieku uzņēmuma [Dankan pielaikošanas norādes](https://dankan.co.jp/blogs/dankan-magazine/jeans-size-guide) uzsver komfortu kustībā, ne vien stāvot pie spoguļa.
- Garumu vērtē ar tiem apaviem, kurus valkāsi. Tīram taisnam siluetam es sākumā salīdzinātu staru, kas viegli pieskaras apavam, ar nedaudz īsāku variantu. Tā ir gaumes izvēle.

Mājās atrodi bikses, kuru garums jau patīk. Izklāj tās un izmēri iekšējo šuvi no stakles līdz apakšmalai. Jostasvietu mēri plakani un iegūto platumu reizini ar divi. Šo metodi apraksta [Levi’s](https://www.levi.com/GB/en_GB/blog/article/how-to-measure-jeans).

Salīdzinot izmēru tabulas, pārbaudi, vai tajās norādīti ķermeņa vai paša apģērba mērījumi. Tie nav automātiski vienādi, un pat viena burta izmērs var atšķirties starp piegriezumiem. [GU skaidrojums](https://faq-tw.gu-global.com/articles/zh_TW/Knowledge/000010565)

#### E03

Vai 0,999… tiešām ir 1? Izskaidro bez augstākās matemātikas.

Jā, parastajā decimālpierakstā **0,999… ir precīzi 1**. Daudzpunkte nozīmē, ka devītnieki turpinās bez gala. Arī [Harvey Mudd College matemātiķa skaidrojums](https://math.hmc.edu/funfacts/why-does-0-999-1/) uzsver, ka vienam skaitlim var būt divi dažādi pieraksti.

Vienkāršs piemērs ir trešdaļas:

- Dalot 1 ar 3, iegūst 0,333…; trijnieki nebeidzas.
- Trīs trešdaļas kopā ir 1.
- Pareizinot 0,333… ar 3, iegūst 0,999….

Tātad abos pierakstos ir viens un tas pats daudzums. Šo piemēru izmanto arī [Tokijas Universitātes nodarbībā skolēniem](https://www.ms.u-tokyo.ac.jp/video/open/2019jhschool-math/op2019-021.pdf).

Mulsumu rada tas, ka jebkurš **pabeigts** devītnieku pieraksts tiešām ir mazāks par 1:

| Pieraksts | Cik pietrūkst līdz 1 |
|---|---:|
| 0,9 | 0,1 |
| 0,99 | 0,01 |
| 0,999 | 0,001 |

Šie ir parasti atņemšanas aprēķini. Taču 0,999… nav pēdējā devītnieka, aiz kura varētu paslēpt vēl kādu atlikušu starpību. Lai cik mazu pozitīvu starpību iedomātos, pietiekami garš devītnieku pieraksts jau būtu tuvāk vieniniekam par to.

Bezgalīgais pieraksts apzīmē pašu skaitli, kuru šie arvien precīzākie pieraksti apraksta. Tas ir 1. Tas neprasa gaidīt, līdz kāds uzrakstīs visus devītniekus. Atšķirība starp galīgiem pierakstiem un to apzīmēto bezgalīgo decimāldaļu ir izskaidrota arī [Olivera Deizera matemātikas mācību tekstā](https://www.aleph1.info/?call=Puc&permalink=ema12_3_1_Z6).

#### E04

Vai jebkurš 65W USB-C lādētājs der manam portatīvajam?

##### Nepieciešamais precizējums

Kāds ir precīzs portatīvā modelis un uzlādes pieslēgvieta; vai vajag saderības pārbaudi vai konkrētu pirkumu?

##### SIMULĒTA atbilde pārbaudes uzdevumā

ThinkPad T14 Gen 4 AMD, USB-C PD; vajadzīgas saderības pārbaudes, nevis konkrēts pirkums.

Šī ir uzdevuma devēja dota simulācija, nevis reāls lietotāja apstiprinājums.

Jebkurš 65 W lādētājs nederēs. Tavam **ThinkPad T14 Gen 4 AMD** jāpārbauda USB Power Delivery režīms, konkrētās pieslēgvietas jauda un kabelis. Lenovo šim modelim norāda gan 45 W, gan 65 W USB-C adapterus ar PD 3.0; 65 W ir arī ražotāja ātrās uzlādes nosacījums. [Lenovo specifikācija](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T14_Gen_4_AMD/ThinkPad_T14_Gen_4_AMD_Spec.PDF)

Pārbaudi marķējumu šādā secībā:

1. Meklē **USB PD / Power Delivery**, ne tikai “65 W” un USB-C spraudni.
2. Izvades tabulā meklē **20 V ⎓ 3,25 A** vai lielāku pieejamo strāvu pie 20 V, lai iegūtu visus 65 W. Aprēķins ir 20 × 3,25 = 65. Šādu izvadi norāda arī [Lenovo 65 W adaptera apraksts](https://m.lenovo.com.cn/wiki/product-1039806.html).
3. Pārliecinies, ka attiecīgais ports dod šo jaudu arī tavā lietošanas režīmā. Daudzportu lādētājam “65 W” var būt kopējā jauda. Piemēram, [Buffalo specifikācijā](https://www.buffalo.jp/product/detail/print/bsacpd6505c2bk.html) viena ierīce saņem līdz 65 W, bet divas ierīces dala 45 W un 20 W.
4. Ja kabelis ir atdalāms, arī tam jābūt paredzētam vismaz 65 W. Pie 20 V tam jāspēj pārvadīt vairāk par 3 A. Ar 60 W marķētu kabeli pilniem 65 W nepietiek; [USB-IF](https://usb.org/cable_connector) skaidro, ka kabeļu jaudas iespējas atšķiras un sertifikācijas marķējumā tās norāda atsevišķi.

Praktiskai pārbaudei vispirms pievieno tikai datoru un paskaties, vai nav paziņojuma par lēnu uzlādi un vai akumulatora līmenis darba laikā pieaug. [Microsoft](https://support.microsoft.com/de-de/windows/experience/power-battery/pc-is-charging-slowly-or-discharging-while-it-s-plugged-in) apraksta gadījumus, kad neatbilstošas barošanas dēļ dators lādējas lēni vai turpina izlādēties. Šī ir pārbaudes secība; konkrēts lādētājs ar tavu datoru šeit nav izmēģināts.

#### E05

Uz apģērba ir 30 grādi, pasvītrots spainītis un pārsvītrots trijstūris. Kā mazgāt?

Izvēlies **saudzīgu mazgāšanas programmu līdz 30 °C un līdzekli bez balinātāja**. Ja zem spainīša ir viena svītra, zīmju nozīme ir šāda:

| Zīme | Ko tā nosaka |
|---|---|
| Spainītī “30” | Ūdens temperatūra nedrīkst pārsniegt 30 °C. |
| Viena svītra zem spainīša | Saudzīgāka mehāniskā apstrāde, mazāks veļas daudzums un saudzīgāka centrifugēšana. |
| Pārsvītrots trijstūris | Nedrīkst balināt, arī ar skābekļa balinātāju. |

Šīs nozīmes skaidro [GINETEX kopšanas simbolu apraksts](https://ginetex.de/pflegekennzeichnung/pflegesymbole/) un [Japānas Patērētāju lietu aģentūras tabula](https://www.caa.go.jp/policies/policy/representation/household_goods/guide/wash_02.html).

Praktiski savas veļasmašīnas instrukcijā izvēlies programmu, kas atbilst saudzīgai 30 °C mazgāšanai. Nepietiek tikai parastai intensīvai programmai samazināt temperatūru: svītra nosaka arī saudzīgāku veļas kustināšanu. GINETEX šim režīmam iesaka tvertni nepildīt vairāk par pusi un centrifugēt īsi vai necentrifugēt. Universālu apgriezienu skaitu no šīs etiķetes noteikt nevar. [GINETEX](https://ginetex.de/pflegekennzeichnung/pflegesymbole/)

Pārbaudi mazgāšanas un traipu tīrīšanas līdzekļa sastāvu vai norādes. Uzraksts “krāsainai veļai” var palīdzēt orientēties, bet būtiskā prasība ir balinātāja neesamība. Balināšanas aizliegums attiecas arī uz līdzekli, ko pievienotu atsevišķi traipa dēļ.

Ja zem spainīša ir **divas svītras**, vajadzīgs vēl saudzīgāks režīms. Savukārt žāvēšanu un gludināšanu nosaka citas zīmes; no šīm trim nevar secināt, vai apģērbu drīkst likt veļas žāvētājā.

#### E06

Man ir 3000x2000 pikseļu foto. Vai no tā sanāks labs A4 izdrukas attēls?

**Jā, no 3000 × 2000 pikseļu foto var sanākt laba A4 izdruka**, ja pats foto ir pietiekami ass. Tas ir vērtējums pēc izšķirtspējas; bez attēla apskates nevaru novērtēt izplūdumu, troksni vai pārāk stipras saspiešanas pēdas. Adobe norāda, ka fotogrāfijai tintes printerī bieži pietiek ar vismaz 220 pikseļiem collā. [Adobe skaidrojums](https://helpx.adobe.com/photoshop/desktop/crop-resize-transform/resize-adjust-resolution/printer-resolution.html)

Tava foto malu attiecība ir 3:2, savukārt [A4 ir 297 × 210 mm](https://www.adobe.com/uk/creativecloud/design/discover/a4-format.html). Tāpēc ainavas novietojumā ir divi varianti:

| Izvietojums | Rezultāts pēc aprēķina |
|---|---|
| Ievietot visu foto bez apgriešanas | Attēls 297 × 198 mm, aptuveni 257 ppi; augšā un apakšā kopā paliek 12 mm. |
| Aizpildīt visu A4, saglabājot proporcijas | Aptuveni 242 ppi; jānogriež mazliet no foto kreisās un labās malas. |

Aprēķini pieņem pilnu norādīto papīra laukumu, bez papildu apgriešanas printera bezmalu režīmā. Pamatformula ir pikseļu skaits dalīts ar izdrukas izmēru collās. [Adobe par izmēra un izšķirtspējas attiecību](https://helpx.adobe.com/photoshop/desktop/crop-resize-transform/resize-adjust-resolution/image-size-resolution-and-resampling.html)

A4 pie 300 ppi orientieris ir aptuveni **3508 × 2480 pikseļi**, kā rāda arī [Canon tabula](https://ij.manual.canon/ij/webmanual/ProfessionalPrintLayout/All/1.0/SC/DPPG/dppg_f-02.html). Tavs attēls šo skaitu nesasniedz, tomēr tas automātiski nepadara izdruku sliktu.

Es sāktu ar visu kadru un nelielām baltām malām, īpaši ja objekti ir tuvu foto malām. Ja rezultāts ir svarīgs, izdrukā nelielu detaļas paraugu tajā pašā mērogā, kādā tas būs uz A4. Vienkārši nomainot failā skaitli “72” uz “300 ppi” bez pikseļu pārrēķina, jaunas detaļas nerodas.

#### E07

Telefonā pietrūkst vietas. Vai Google Photos dzēšana atbrīvos telefonu, saglabājot bildes?

##### Nepieciešamais precizējums

Vai lieto Android vai iPhone, vai Google Photos dublēšana ir ieslēgta, un vai domā Free up space vai Delete?

##### SIMULĒTA atbilde pārbaudes uzdevumā

Android; Google Photos dublēšana ieslēgta; jāskaidro Free up space un Delete, neko faktiski nedzēst.

Šī ir uzdevuma devēja dota simulācija, nevis reāls lietotāja apstiprinājums.

**Jā, izmantojot “Free up space on this device” un iepriekš pārbaudot dublēšanu.** Android lietotnē parastā dzēšana dara ko citu.

| Darbība | Kas notiek |
|---|---|
| **Free up space on this device** — atbrīvot vietu šajā ierīcē | No telefona izņem jau droši dublētās foto un video kopijas. Tās paliek Google Photos kontā. |
| **Delete / Move to trash** — dzēst / pārvietot uz atkritni | Dzēš attēlus no Google Photos un ierīces; dublēto attēlu dzēšana izplatās arī uz ierīcēm, kurās ieslēgta dublēšana. |

Šo atšķirību apraksta Google instrukcijas par [vietas atbrīvošanu ierīcē](https://support.google.com/photos/answer/6128843?co=GENIE.Platform%3DAndroid&hl=en) un [foto dzēšanu](https://support.google.com/photos/answer/6128858?co=GENIE.Platform%3DAndroid&hl=en).

**Es rīkotos šādi:**

1. Google Photos profilā pārbaudītu pareizo Google kontu un statusu **“Backup complete”**. Ieslēgta dublēšana vēl nenozīmē, ka tā ir pabeigta.
2. Dažiem svarīgiem attēliem atvērtu informāciju un pārbaudītu **“Backed up”**. Papildu pārbaudei atvērtu tos pašā kontā vietnē [photos.google.com](https://photos.google.com). Google apraksta [kopējā un atsevišķa foto dublēšanas statusa pārbaudi](https://support.google.com/photos/answer/6193313?co=GENIE.Platform%3DAndroid&hl=en).
3. Tikai pēc tam izvēlētos **“Free up space on this device”**. Pirms apstiprināšanas lietotne parāda atbrīvojamo apjomu.

Pēc vietējo kopiju izņemšanas bildes joprojām redzēsi Google Photos, pieslēdzoties kontam ar internetu. Taču tās vairs nebūs pieejamas telefona parastajā galerijā vai bezsaistē. Nesenie, mazāk nekā 30 dienas vecie faili var palikt ierīcē, tāpēc šī funkcija ne vienmēr iztukšo visas vietējās kopijas. To norāda [Google palīdzība](https://support.google.com/photos/answer/6128843?co=GENIE.Platform%3DAndroid&hl=en).

Te ir darbību skaidrojums; nekas telefonā nav dzēsts.

#### E08

Ko nozīmē rūtera 5 GHz? Vai internets būs piecreiz ātrāks?

**5 GHz apzīmē Wi‑Fi radiofrekvenču joslu. Tas nesola piecreiz ātrāku internetu.** Gigaherci raksturo radioviļņa svārstību biežumu; datu pārraides ātrumu mēra, piemēram, megabitos sekundē jeb Mbit/s. “5 GHz” ir joslas nosaukums, kurā rūteris un telefons vai dators sazinās. [Intel skaidrojums](https://www.intel.com/content/www/us/en/products/docs/wireless/2-4-vs-5ghz.html).

Praksē izvēle parasti izskatās šādi:

| Josla | Kad tā var būt izdevīgāka |
|---|---|
| **5 GHz** | Tuvāk rūterim, kad vajag lielāku datu caurlaidību un ir labs signāls. Parasti iespējami platāki kanāli. |
| **2,4 GHz** | Tālāk no rūtera vai aiz vairākām sienām, ja 5 GHz savienojums kļūst vājš. Taču šajā joslā var būt vairāk traucējumu. |

Tās ir tendences, ne garantijas konkrētā dzīvoklī. [Buffalo](https://www.buffalo.jp/support/faq/detail/15959.html) norāda, ka 5 GHz ne vienmēr dod ātrāku vai stabilāku savienojumu. [TP-Link](https://media.tp-link.com.cn/document/html1714457949100.html) arī skaidro: signāla “svītriņu” skaits viens pats nepasaka ātrumu, jo nozīme ir traucējumiem un kanāla kvalitātei.

**Interneta ātrumu ierobežo visa ķēde:** pakalpojuma pieslēgums, rūteris, izmantotā ierīce un Wi‑Fi apstākļi. Tāpēc, piemēram, 100 Mbit/s pieslēgumu tikai pārslēgšanās uz 5 GHz nepārvērtīs par 500 Mbit/s pieslēgumu. Tas ir secinājums no šiem ierobežojumiem, ne mērījums tavā tīklā. [Intel](https://www.intel.com/content/www/us/en/products/docs/wireless/2-4-vs-5ghz.html).

**Es sāktu ar vienkāršu salīdzinājumu:** ja abas joslas pieejamas atsevišķi, ar to pašu ierīci tajā pašā vietā pārbaudītu abas vairākas reizes. Salīdzinātu arī video vai zvana stabilitāti. Labākā izvēle ir tā, kas labi strādā vietā, kur ierīci tiešām lieto.

#### E09

PDF ir bildes ar tekstu. Gribu kopēt latviešu tekstu, nemaksājot un nesūtot dokumentu svešam servisam. Ko izmantot?

**Es sāktu ar [NAPS2](https://www.naps2.com/).** Tā ir bezmaksas atvērtā koda programma Windows, macOS un Linux datoriem. Tai var importēt esošu PDF un ar OCR jeb teksta atpazīšanu pievienot kopējamu teksta slāni.

**Darbības:**

1. Lejupielādē NAPS2 no projekta vietnes un importē PDF.
2. Nospied **OCR**; Mac datorā tas ir **Tools → OCR**. Lejupielādē latviešu valodas datus un izvēlies **Latvian**. NAPS2 izmanto Tesseract valodu failus; latviešu valodas kods ir **lav**. To pamato [NAPS2 dokumentācija](https://www.naps2.com/doc/org-use) un [Tesseract valodu saraksts](https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html).
3. Atzīmē **“Make PDFs searchable using OCR”** un saglabā rezultātu kā jaunu PDF, saglabājot arī oriģinālu.
4. Atver jauno PDF lasītājā, iezīmē tekstu un kopē to. Pašā NAPS2 atsevišķa OCR teksta eksporta uz TXT nav; šim mērķim projekta instrukcija iesaka kopēt no saglabātā PDF. [OCR instrukcija](https://www.naps2.com/doc/ocr).

Programmas un valodu failu sākotnējai lejupielādei vajag internetu, bet dokumenta atpazīšanu var veikt lokāli. Projekta autors to izskaidro [atbalsta diskusijā](https://sourceforge.net/p/naps2/discussion/general/thread/df4f787b95/), un [izvietošanas dokumentācija](https://www.naps2.com/doc/org-use) apraksta arī darbu datorā bez interneta. Dokumentu nosūtīšana ir atsevišķās **Email PDF** funkcijas darbība; [privātuma politika](https://www.naps2.com/privacy-policy) šo integrāciju apraksta atsevišķi.

Tavam mērķim saglabā failu vietējā mapē, kas netiek sinhronizēta ar mākoņpakalpojumu, un e-pasta nosūtīšanu neizmanto. Pēc programmas un valodas datu lejupielādes vari apstrādi veikt arī ar atvienotu internetu.

**Vispirms izmēģini vienu lapu:** salīdzini garumzīmes, mīkstinājumus, skaitļus un teksta secību ar oriģinālu. Ja rezultāts vājš, izmēģini OCR režīmu **Best**; dokumentācija to piedāvā kā lēnāku variantu, kas dažkārt atpazīst labāk. Konkrētais PDF šajā pārbaudē nav apstrādāts.

#### E10

Vai ledusskapī ielikts silts ēdiens sabojās ledusskapi? Kā saprātīgi rīkoties ar mazu zupas katliņu mājās?

**Neliels daudzums silta ēdiena pats par sevi parasti ledusskapi nesabojā.** FDA savā mājsaimniecību ceļvedī tieši skaidro, ka karsta ēdiena ievietošana ledusskapī nekaitē ierīcei, un iesaka ēdienu sadalīt mazākos traukos, lai tas atdziest ātrāk. [FDA norādes](https://www.fda.gov/food/buy-store-serve-safe-food/refrigerator-thermometers-cold-facts-about-food-safety).

Tomēr lielāks karstuma daudzums liek ledusskapim vairāk dzesēt un var sasildīt blakus noliktos produktus. [Liebherr](https://www.liebherr.com/de-ch/gefrier-kuehlschraenke/freshmag/frische-ideen/warme-speisen-in-den-kuehlschrank-7712798) tāpēc iesaka mazākas porcijas un iepriekšēju atdzesēšanu, piemēram, aukstā ūdens peldē.

**Ar mazu zupas katliņu es rīkotos šādi:**

1. Ja zupa vēl ļoti karsta, katliņu uz brīdi ieliktu aukstā ūdenī un ar tīru karoti apmaisītu. Ūdenim nevajag iekļūt zupā. Vēl viena iespēja — pārliet zupu mazākos, seklos pārtikas traukos.
2. Traukus pārsegtu un drīz ievietotu ledusskapī, arī ja zupa vēl ir nedaudz silta. Atstātu ap tiem vietu gaisa cirkulācijai.
3. Pārbaudītu, ka ledusskapis uztur ap **4 °C**. Ja tā temperatūra nav zināma, to var pārbaudīt ar ledusskapja termometru.

Sadalīšanu seklos traukos un ātru ievietošanu ledusskapī iesaka gan [Honkongas Pārtikas drošības centrs](https://www.cfs.gov.hk/sc_chi/consumer_zone/safefood_all/five_keys_apply_leftovers.html), gan [Japānas Lauksaimniecības ministrija](https://www.maff.go.jp/j/syouan/seisaku/foodpoisoning/frige.html); pēdējā arī iesaka aptuveni 4 °C un nepārpildīt plauktus.

**Zupu nevajag stundām atstāt uz galda, gaidot pilnīgu atdzišanu.** Mājas apstākļiem FDA iesaka ēdienu ievietot ledusskapī divu stundu laikā pēc gatavošanas; karstumā virs aptuveni 32 °C — stundas laikā. Tās ir maksimālās gaidīšanas robežas, ne mērķis nogaidīt tik ilgi. Praktiskā izvēle ir atdzesēt strauji un ielikt agrāk. [FDA](https://www.fda.gov/food/buy-store-serve-safe-food/refrigerator-thermometers-cold-facts-about-food-safety).

### Praktiski tehniski jautājumi

#### P01

Spēlē redzu runas par ESP, aimbot un kernel anti-cheat. Ko tie dara, kā atšķiras spēles modi no čītiem, un kur par šo jēdzīgi lasīt? Man nevajag čītu vai apiešanas instrukcijas.

ESP atklāj spēlē slēptu informāciju, aimbot automatizē tēmēšanu, bet kernel anti-cheat ir daļa no aizsardzības pret neatļautu iejaukšanos. Tie dara dažādus darbus.

| Jēdziens | Ko tas nozīmē praksē |
|---|---|
| ESP | Parāda, piemēram, citu spēlētāju atrašanās vietas arī tad, kad tās nebūtu jāredz. PUBG komanda apraksta šo datu attēlošanu ar tekstu vai grafiku. |
| Aimbot | Programma palīdz automātiski virzīt tēmēšanu uz mērķi. Riot aprakstītais pixelbot ir piemērs, kas analizē attēlu un veic ievades darbības. |
| Kernel anti-cheat | Aizsardzības draiveris darbojas operētājsistēmas kodolā ar augstām privilēģijām. Papildus tam var darboties spēles klients un servera pārbaudes. |

Šīs atšķirības apraksta [PUBG izstrādātāji](https://pubg.com/en/news/6957), [Riot inženieri](https://www.riotgames.com/en/news/vanguard-on-demand) un [Activision dokumentācija](https://support.activision.com/cn/zh/articles/ricochet-overview).

Mods ir spēles pārveidojums vai papildinājums. Izstrādātājs var atbalstīt jaunas kartes, priekšmetus un citas izmaiņas, kā to paredz [Steam Workshop](https://partner.steamgames.com/doc/features/workshop). Atļautību nosaka konkrētās spēles noteikumi un izmantotā funkcija. Piemēram, Riot par neatļautu priekšrocību uzskata slēptas informācijas atklāšanu un darbību veikšanu spēlētāja vietā. Nosaukums “mods” pats par sevi atļauju nedod. [Riot politika](https://support.riotgames.com/en-us/riot/events/third-party-applications).

Lai saprastu tehnisko pusi, sāktu ar [Paula Chamberlaina Fog of War aprakstu](https://www.riotgames.com/en/news/demolishing-wallhacks-valorants-fog-war). VALORANT pretkrāpšanās izstrādātājs skaidro, kā serveris var nesūtīt klientam slēpto pretinieku atrašanās vietas, un apraksta savus testus. [PUBG Anti-ESP vēstule](https://pubg.com/en/news/6957) parāda arī praktisko sarežģījumu: atkārtojumiem un nāves kamerai vajag informāciju, kuru aktīvam spēlētājam nedrīkst atklāt. Šie ir pašu izstrādātāju ziņojumi; šeit spēles aizsardzība nav testēta.

Darbības režīmu pārbaudītu katrai sistēmai atsevišķi. [Vanguard pašreizējā dokumentācija](https://support.riotgames.com/de-de/riot/performance/what-is-vanguard) jau apraksta Pre-Check iespēju ieslēgt to pēc pieprasījuma, ja dators izpilda attiecīgās drošības prasības. Visu kodola aizsardzību raksturot kā “vienmēr ieslēgtu” būtu neprecīzi.

Pirms konkrēta moda lietošanas nākamais solis ir pārbaudīt šīs spēles modifikāciju politiku un to, vai noteikumi atšķiras viena un vairāku spēlētāju režīmam.

#### P02

Gribu iztulkot viena spēlētāja spēli latviski, nezaudējot vietturus un tekstu kontekstu. Kādu brīvā koda darba kārtību izvēlēties?

TESTA SIMULĀCIJA: JSON virknes ar {player_name}, daudzskaitļa formām un dialogu ID; izpildāmu failu labošana neietilpst uzdevumā.

Šim JSON piemēram izvēlētos Git kopā ar Weblate un pārbaudāmu importa/eksporta soli. Pieņēmums nāk no testa precizējuma: failā ir `{player_name}`, daudzskaitļa formas un dialogu ID. Konkrētās spēles faili nav apskatīti.

Weblate ir pašmitināms brīvā koda risinājums ar [GPL-3.0-or-later licenci](https://docs.weblate.org/en/latest/contributing/license.html). Taču pirms tulkošanas jānosaka JSON paveids: [vispārīgais JSON lasītājs](https://docs.weblate.org/en/latest/formats/json.html) pats neatbalsta daudzskaitļa grupas un konteksta laukus; [i18next JSON v4 lasītājs](https://docs.weblate.org/en/latest/formats/i18next.html) daudzskaitli atbalsta. Spēles shēma jāņem par pamatu, un i18next drīkst izvēlēties tikai tad, ja faili tam tiešām atbilst.

Darba kārtību veidotu šādi:

1. Saglabā oriģinālus un piesaisti katru tulkojumu stabilam dialoga ID. Tulkot drīkst teksta vērtības; ID, vietturu nosaukumus un JSON struktūru saglabā.
2. Katram dialogam pievieno runātāju, ainu, iepriekšējo/nākamo repliku un, kur vajag, ekrānattēlu. Šo papildu kontekstu glabā Weblate vai atsevišķā kartē pēc ID, ja spēles fails to neparedz. [Weblate konteksta iespējas](https://docs.weblate.org/ja/latest/user/translating.html).
3. Ieslēdz pārbaudi īstajai vietturu sintaksei. `python-brace-format` der, ja spēle lieto atbilstošu iekavu sintaksi; `strict-format` var liegt skaitļa viettura izlaišanu vienskaitļa formā. Citai sintaksei vajag citu pārbaudi. Automātiska atpazīšana nav garantija. [Pārbaudes](https://docs.weblate.org/en/latest/user/checks.html), [pārbaudes nosacījumi](https://docs.weblate.org/zh-cn/latest/user/checks.html).
4. Daudzskaitli salāgo ar spēles noteikumiem. CLDR latviešu kardinālajiem skaitļiem definē `zero`, `one` un `other`, arī daļskaitļu nosacījumus; spēle šīs kategorijas var attēlot savā shēmā. [CLDR tabula](https://www.unicode.org/cldr/charts/49/supplemental/language_plural_rules.html).

Vieglāka alternatīva vienam tulkotājam ir [Translate Toolkit `json2po/po2json`](https://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/json2po.html) ar PO redaktoru. Tas pievieno pārveides posmu, kura atgriezeniskums jāpārbauda; avota un tulkojuma revīzijām jāsakrīt. [Toolkit licences teksts](https://github.com/translate/translate/blob/master/COPYING) ir GNU GPL v3.

Sāktu ar 30 dažādām rindām. Vispirms importētu un eksportētu nemainītu tekstu, pēc tam salīdzinātu struktūru, ID un vietturus. Tulkojumā pārbaudītu arī diakritiku, teksta garumu un daudzskaitli pašā spēlē. Pieņemšanas nosacījums: neviena pazudusi atslēga vai neatļauti mainīts vietturis. Ja pārbaude neizdodas, lielo tulkojumu nesāktu.

Dokumentācija un Weblate vietturu pārbaudes klase ir apskatīta; instalēšana un spēles pārbaude nav veikta. Jauna tulkošanas platforma šobrīd nav pamatota. Precīzam importa rīkam vēl vajadzīgs spēles nosaukums un īsts JSON paraugs.

#### P03

Vai 12 GB VRAM pietiek lokālam 27B valodas modelim? Ko tieši skaitīt?

TESTA SIMULĀCIJA: nomināli 4 bitu svari, konteksts 8192, viens lietotājs; nav ātrdarbības garantijas.

Ar dotajiem testa pieņēmumiem 12 GB VRAM nepietiek, lai visus 27B modeļa 4 bitu svarus un darba atmiņu turētu videokartē. Lokāla izpilde ar daļēju pārcelšanu uz datora RAM tomēr ir iespējama atbilstošā programmā.

Pirmais aprēķins ir vienkāršs:

`27 000 000 000 × 4 / 8 = 13 500 000 000 baitu`

Tas ir 13,5 GB jeb aptuveni 12,57 GiB tikai ideāli sapakotiem svariem, jau vairāk par 12 GiB. Reālā kvantizācija var pievienot mēroga koeficientus un citus datus. Piemēram, [GGML Q4_0 blokā](https://github.com/ggml-org/llama.cpp/blob/master/ggml/src/ggml-common.h) četru bitu vērtībām blakus glabājas mēroga koeficients.

Jāskaita visas šīs daļas:

- Faktiskais svaru apjoms un to sadalījums starp GPU un RAM.
- KV kešatmiņa izvēlētajam 8192 tokenu kontekstam un vienam lietotājam.
- Pagaidu aprēķinu buferi un izpildes programmas atmiņa.
- VRAM, kuru jau izmanto darbvirsma un citas programmas.

KV apjomu nevar noteikt tikai pēc “27B”: vajag konkrēto arhitektūru un keša datu tipu. Arī dažādām uzmanības shēmām un keša stratēģijām patēriņš atšķiras. [Transformers dokumentācija](https://huggingface.co/docs/transformers/en/kv_cache).

[llama.cpp](https://github.com/ggml-org/llama.cpp) atbalsta CPU un GPU kopīgu izpildi, bet tā [parametri](https://github.com/ggml-org/llama.cpp/blob/master/tools/completion/README.md) atsevišķi kontrolē GPU slāņus, KV izvietojumu un keša tipu. RAM jābūt pietiekami daudz, un ātrums jāpārbauda uz konkrētās aparatūras. Modelis, kurš ielādējas, vēl nav pārbaudīts pie pilna konteksta.

Labs pretpiemērs ir [llama.cpp lietotāja ziņojums](https://github.com/ggml-org/llama.cpp/discussions/26736): citā, lielā DeepSeek konfigurācijā KV pārcelšana uz RAM neatrisināja aprēķinu bufera VRAM trūkumu. Tā ir viena lietotāja pieredze, ne šā 27B modeļa mērījums.

Nākamajam solim vajag precīzu modeļa failu, kvantizācijas nosaukumu, RAM apjomu un brīvo VRAM. Tad pārbauda starta žurnāla svaru, KV un aprēķinu buferus un veic pilna konteksta izmēģinājumu. Ja prasība ir visu turēt GPU, izvēlētos mazāku modeli vai lielāku VRAM; zemāku bitu kvantizāciju pieņemtu tikai pēc kvalitātes pārbaudes. Šeit modelis nav palaists.

#### P04

Gribu video HDR pārvērst SDR, lai krāsas nav pelēkas. Ko man jāzina pirms FFmpeg komandas?

TESTA SIMULĀCIJA: H.265, BT.2020/PQ, 10 biti; mērķis SDR Rec.709; lietotāja fails nav pieejams.

Testa precizējumā dots H.265 video ar BT.2020/PQ un 10 bitiem, kura mērķis ir SDR Rec.709. Šādai ievadei vajag gan spilgtuma diapazona pārveidi, gan pareizu krāsu pārveidi. Vienkārši pārrakstīt faila atzīmi uz “BT.709” nepietiek: FFmpeg `setparams` maina īpašību atzīmes, nepārrēķinot pašu attēlu. [Filtru dokumentācija](https://www.ffmpeg.org/ffmpeg-filters.html#setparams).

Pirms gala komandas pārbaudītu:

- `color_primaries`, `color_transfer` un `color_space`: pamatkrāsu sistēmu, spilgtuma pārvades funkciju un matricu.
- `color_range`: vai ievade izmanto ierobežotu vai pilnu signāla diapazonu.
- Pikseļu formātu, bitu dziļumu un pieejamos HDR spilgtuma metadatus.
- FFmpeg versiju un pieejamos filtrus, kā arī ierīci, kurā SDR video jāatskaņo.

H.265 un 10 bitu norādes vien šos krāsu datus neaizstāj. Sākuma pārbaudei der šāda lasīšanas komanda:

```bash
ffprobe -v error -select_streams v:0 -show_streams -of json "input.mp4"
```

Tā izvada plūsmas informāciju; video netiek pārkodēts. [ffprobe dokumentācija](https://ffmpeg.org/ffprobe.html).

Parastā FFmpeg `tonemap` filtra gadījumā darbību secība ir: pareizi interpretēt PQ ievadi, pāriet uz lineāru gaismu ar peldošā komata datiem, pielāgot toņus SDR diapazonam, salāgot krāsas un izvadīt Rec.709. `zscale` palīdz veikt šīs krāsu un pārvades pārveides. Lineāras gaismas prasību skaidri norāda gan [pašreizējā dokumentācija](https://www.ffmpeg.org/ffmpeg-filters.html#tonemap), gan [filtra autora sākotnējā apspriede](https://ffmpeg.org/pipermail/ffmpeg-devel/2017-July/213824.html).

Izvēlēto toņu līkni vispirms izmēģinātu īsā fragmentā ar seju, tumšām vietām un spilgtām gaismām. SDR atskaņošanā pārbaudītu melno līmeni, gaismu detaļas un gala metadatus. Viena līkne, piemēram, Hable, nav automātiski piemērota katram materiālam.

Pelēkā attēla iespējamie cēloņi ir nepareiza PQ interpretācija, signāla diapazons vai atskaņotāja apstrāde. Bez video tie paliek pārbaudāmas hipotēzes. Nākamais solis ir `ffprobe` izdruka un īss paraugs; oriģinālu saglabā. Šajā piemērā video nav pārkodēts.

#### P05

Vai NAS ar RAID1 ir pietiekama ģimenes foto rezerves kopija?

Ar RAID1 vien nepietiek, ja ģimenes foto atrodas tikai NAS. Tas vienlaikus glabā vienādus datus abos diskos un palīdz turpināt darbu viena diska kļūmes gadījumā. Dzēšana vai kaitīga pārrakstīšana var skart abus diskus. Arī visa NAS zudumam vajadzīga kopija ārpus šīs ierīces. To nošķir [Synology skaidrojums](https://blog.synology.com/de/was-ist-ein-backup/) un [Buffalo RAID apraksts](https://www.buffalo.jp/topics/trouble/detail/recovery_0005.html).

Ģimenes foto es veidotu šādu kārtību:

1. Foto oriģināli NAS vai datorā.
2. Regulāra kopija ar iepriekšējām versijām atsevišķā diskā; pēc kopēšanas disku atvieno.
3. Vēl viena kopija citā vietā, piemēram, šifrētā diskā pie tuvinieka. Mākonis ir iespējams, bet nav obligāts.

Tā ir mana praktiska rekomendācija, lai viena kļūme neskar visas kopijas. Bezsaistes šifrētas kopijas un regulāras atjaunošanas pārbaudes iesaka arī [CISA pamatnostādne](https://www.cisa.gov/sites/default/files/publications/CISA_MS-ISAC_Ransomware%20Guide_S508C_.pdf). Pats dokuments ir no 2020. gada; to nepiedāvāju kā jaunu 2026. gada pētījumu.

NAS momentuzņēmumi ir noderīgi iepriekšējā stāvokļa atgūšanai. Ja tie glabājas tikai tajā pašā ierīcē, tie neatrisina visas ierīces zudumu. Attālināta glabāšana šo situāciju maina: [QNAP dokumentācija](https://www.qnap.com/zh-tw/software/snapshots) apraksta momentuzņēmumu kopēšanu uz citu NAS un atjaunošanu tur.

Ja oriģināli saglabājas arī telefonā vai datorā, NAS jau var būt viena rezerves kopija. Jāpārbauda, vai sinhronizācija nepārnes dzēšanu uz otru vietu un vai saglabājas vecākas versijas.

Pirmais noderīgais tests: atjauno atsevišķā mapē dažus jaunus, vecus un iepriekš dzēstus attēlus. Atver tos un pārbaudi pilnu izšķirtspēju un vajadzīgos metadatus. Kopēšanas biežumu pieskaņo tam, cik nesenu foto zaudējums būtu pieņemams. Šo atjaunošanas testu es šeit neesmu izpildījis.

#### P06

Ja es iedodu AI GitHub saiti uz skillu, vai tas to jau ir uzinstalējis uz visiem laikiem?

Nē. Iedota saite pati par sevi nepierāda, ka prasme ir uzstādīta. Aģents var tikai izlasīt tās tekstu šīs sarunas vajadzībām. Uzstādīšanai vajadzīgi saglabāti faili vai reģistrēta pakotne, kā arī veids, kā konkrētā aģenta programma to atrod un izmanto. [OpenAI prasmes dokumentācija](https://developers.openai.com/api/docs/guides/tools-skills) šos soļus apraksta atsevišķi.

Prasme parasti ir mape ar `SKILL.md` un vajadzīgajiem papildu failiem. OpenAI vietējā izpildē lieto failu ceļus; viesotajā izpildē prasmi pievieno attiecīgajai videi. Viesotā konteinera saturs tiek atmests, kad konteiners beidzas vai tiek dzēsts. Tātad “šobrīd pieejama” vēl nenozīmē “pieejama visās nākamajās sarunās”. [Izpildes veidi un dzīves cikls](https://developers.openai.com/api/docs/guides/tools-skills)

Piemēram, [OpenAI CLI prasmes instalēšanas apraksts](https://developers.openai.com/api/reference/cli) Codex gadījumā nošķir `.agents/skills/` konkrētam projektam un `~/.agents/skills/` lietotāja projektiem. Tas paredz instalētāju vai visas prasmes mapes kopēšanu un pārbaudi jaunā aģenta sesijā. Šie ceļi ir konkrētā rīka piemērs; citā programmā kārtība var atšķirties.

Citā aģenta vidē kārtība atšķiras. [Letta Code autoru instrukcija](https://github.com/letta-ai/letta-code#installing-external-skills) paredz `letta skills install` ar GitHub adresi, lai ievietotu prasmi konkrēta aģenta atmiņā. Ar `letta skills list --agent <agent-id>` pārbauda tā prasmju sarakstu. Arī šajā piemērā saites nolasīšana un prasmes instalēšana ir atsevišķas darbības.

Pārliecinošai uzstādīšanas atskaitei es gribētu redzēt:

- saglabāto vietu un aptverto vidi vai lietotāju;
- konkrēto versiju vai Git izmaiņu identifikatoru;
- apliecinājumu, ka aģents prasmi atrod;
- vajadzīgo rīku un savienojumu pārbaudi;
- jaunas sesijas piemēru, kur prasme tiešām nolasīta un izmantota.

Šo pārbaudi iesaku es. Atsevišķu prasmes, savienojuma un ieslēgšanas soļu nepieciešamību labi parāda arī [Docs MCP instrukcija](https://developers.openai.com/learn/docs-mcp).

“Uz visiem laikiem” nevar secināt arī no veiksmīgas instalācijas: saglabātajiem failiem jāpaliek pieejamiem un nākamajai videi tie jāielādē. Šajā piemērā jaunu prasmi neinstalēju un tās pieejamību citās sesijās neesmu pārbaudījis.

#### P07

Kas 2026. gadā ir praktiski lietojams aģenta ilgtermiņa atmiņai lokāli, bez obligāta mākoņa? Salīdzini vairākus gatavus risinājumus.

Es sāktu ar trim risinājumiem zemāk. Tie ir gatavi projekti, bet piedāvā atšķirīgu integrācijas apjomu. Pārbaude veikta 2026. gada 9. novembrī: lasīju repozitoriju konfigurācijas, autoru piemēru kodu un dokumentāciju. Instalācijas un atmiņas kvalitātes testus neveicu. Tabulā ir nolasītās `main` zara pakotņu versijas, nevis solījums, ka visi avoti piesaistīti vienam nemainīgam Git revīzijas identifikatoram.

| Risinājums | Pārbaudītā versija un licence | Kam to izvēlētos |
|---|---|---|
| Mem0 OSS bibliotēka | [2.2.1](https://github.com/mem0ai/mem0/blob/main/pyproject.toml), [Apache 2.0](https://raw.githubusercontent.com/mem0ai/mem0/main/LICENSE) | Atmiņas pievienošanai jau esošam aģentam. |
| Letta Code | [0.34.45](https://github.com/letta-ai/letta-code/blob/main/package.json), [Apache 2.0](https://github.com/letta-ai/letta-code/blob/main/LICENSE), ar zīmola materiālu izņēmumu | Ja vajag pašu aģenta vidi ar saglabājamu stāvokli un atmiņu. |
| Graphiti | [0.31.2](https://github.com/getzep/graphiti/blob/main/pyproject.toml), [Apache 2.0](https://github.com/getzep/graphiti/blob/main/LICENSE) | Ja svarīgas attiecības starp faktiem un to izmaiņas laikā. |

**Mem0:** autoru [lokālais piemērs](https://github.com/mem0ai/mem0/blob/main/docs/cookbooks/companions/local-companion-ollama.mdx) izmanto vietējo Qdrant un Ollama gan valodas modelim, gan teksta iegulumiem. Nolasīju arī [Ollama iegulumu klienta kodu](https://github.com/mem0ai/mem0/blob/main/mem0/embeddings/ollama.py). Tomēr [gatavā servera aprakstā](https://github.com/mem0ai/mem0/blob/main/docs/open-source/setup.mdx) noklusējuma pakotnei uzskaitīti ierobežoti mākoņpakalpojumu piegādātāji. Tāpēc pilnīgi lokālam sākumam izvēlētos bibliotēkas dokumentēto konfigurāciju; servera attēlam vajadzīga atsevišķa pārbaude vai pielāgošana.

**Letta:** [vecais repozitorijs](https://github.com/letta-ai/letta) norāda uz aktuālo `letta-code`. [Pašmitināšanas dokumentācija](https://github.com/letta-ai/letta-docs-md/blob/main/self-hosting/index.md) paredz vietējo režīmu bez Letta konta: sarunas, atmiņa un cits aģenta stāvoklis paliek datorā. Modeļa izvēle ir atsevišķa: pilnīgi lokālai darbībai jāpieslēdz, piemēram, vietējais Ollama. [Noklusējums ir Letta Cloud](https://github.com/letta-ai/letta-code), tāpēc vajadzīgais režīms jāizvēlas apzināti.

**Graphiti:** [autoru README](https://github.com/getzep/graphiti) satur Ollama konfigurācijas kodu valodas modelim, iegulumiem un pārrindošanai. Papildus jānodrošina grafu datubāze un integrācija ar aģentu. Tas ir grafu veidošanas ietvars; autori arī norāda, ka maziem vietējiem modeļiem strukturētā JSON izvada uzticamība var būt nepietiekama.

Mana izvēle būtu Mem0 esošam aģentam, Letta jaunai aģenta videi, Graphiti konkrētai vajadzībai pēc faktu vēstures. Pirms ilgākas lietošanas pārbaudītu saglabāšanu pēc restarta, pretrunīga fakta labojumu, atsauci uz avotu, dzēšanu un lietotāju atdalīšanu. Pēc modeļu lejupielādes pārbaudītu arī darbību bez ārējā tīkla. Šis ir ieteikts pieņemšanas tests; tīkla neatkarību un kvalitāti uz tava datora šeit neesmu pierādījis.

#### P08

Man USB-C monitors nedod attēlu no datora, kaut ports der. Kāpēc?

Tas, ka spraudnis der, vēl neapstiprina video pārvadi. Datora USB-C ports var nodrošināt datus un barošanu, bet neatbalstīt monitoram vajadzīgo attēla signālu. Parastam DP Alt Mode savienojumam šī funkcija jāpārbauda konkrētā porta un monitora dokumentācijā. [VESA](https://www.displayport.org/faq/) norāda, ka DP logo var palīdzēt, tomēr izšķiroša ir ierīces specifikācija.

Es pārbaudītu šādā secībā:

1. **Precīzais ports.** Atrodi datora un monitora modeļus un rokasgrāmatā pārbaudi izvēlēto USB-C ligzdu. Viena datora dažādie porti var pildīt atšķirīgas funkcijas. Pieņēmumu par DP atbalstu no ligzdas formas vien izdarīt nevar.
2. **Kabelis un barošana.** Izmēģini monitora komplektā esošo vai jau pārbaudītu video pārraidei paredzētu kabeli. Ja monitoram paredzēta atsevišķa barošana, pievieno to. [ASUS japāņu instrukcija](https://www.asus.com/jp/support/faq/1048768/) iesaka pārbaudīt arī abus pieslēguma galus.
3. **Monitora ievade.** Izvēlies atbilstošo USB-C ievadi monitora izvēlnē un pārliecinies, ka dators ir pamodināts. [ASUS diagnostikas apraksts](https://www.asus.com/de/support/faq/1012723/) aptver šos soļus un cita kabeļa vai datora pārbaudi.
4. **Tiešais savienojums.** Uz pārbaudes laiku izņem doku vai pāreju no ķēdes. Ja tieši strādā, tālāk pārbaudi doka iespējas, barošanu un savienojumus. To iesaka arī [ASUS USB-C atbalsts](https://www.asus.com/us/support/faq/1042417/).
5. **Pa vienam maini komponentus.** Izmēģini citu zināmu derīgu kabeli un citu video izvadi atbalstošu datoru. Ja monitors tiek atpazīts, bet attēla nav, izmēģini tā atbalstītu zemāku izšķirtspējas vai atsvaidzes režīmu.

Atsevišķi pārbaudi, vai tas ir DisplayLink monitors: [šim tipam vajag atbilstošu draiveri](https://www.asus.com/jp/support/faq/1048768/). To nedrīkst automātiski sajaukt ar DP Alt Mode savienojumu.

Bez modeļiem un savienojuma ķēdes konkrētais vainīgais paliek hipotēze. Nākamajam solim pietiek ar datora un monitora modeļiem, izmantoto portu, kabeļa vai doka modeli un operētājsistēmu. Pašu aparatūru šeit neesmu pārbaudījis.

#### P09

Kā mainīt datora DNS un vai tas obligāti padarīs spēles ping mazāku?

DNS nomaiņa negarantē mazāku spēles ping. DNS atrod nosaukumam atbilstošu adresi; ātrāka šīs adreses atrašana pati par sevi nesamazina pakešu ceļošanas laiku jau esošā savienojumā ar to pašu spēles serveri. Tas ir secinājums no abu procesu atšķirības. [Google tehniskais skaidrojums](https://developers.google.com/speed/public-dns/docs/performance) atsevišķi apskata DNS vaicājumu aizturi un ģeogrāfiski atšķirīgu serveru adrešu izvēli.

Iespējams netiešs efekts: cits DNS var atdot cita servera adresi. Vai konkrētā spēle tā izvēlas serveri un vai tas palīdz, bez mērījuma nevar pateikt.

Operētājsistēma nav nosaukta, tāpēc konkrētais piemērs ir **Windows 11**:

1. Pieraksti pašreizējos DNS iestatījumus un to, vai tie ir automātiski.
2. Atver **Iestatījumi → Tīkls un internets → izmantotais Ethernet vai Wi-Fi adapteris**.
3. Pie **DNS serveru piešķiršanas** izvēlies **Rediģēt → Manuāli**.
4. IPv4 DNS laukos ievadi izvēlētā pakalpojuma adreses. Piemēram, Cloudflare parastajam DNS tās ir `1.1.1.1` un `1.0.0.1`. Ja konfigurē arī IPv6 DNS, attiecīgās adreses ir `2606:4700:4700::1111` un `2606:4700:4700::1001`.
5. Saglabā. Maini tieši DNS laukus; datora IP adrese un vārteja šim nolūkam nav jāaizstāj.

Šis ir [Cloudflare dokumentētais iestatīšanas piemērs](https://developers.cloudflare.com/1.1.1.1/setup/windows/), nevis apgalvojums, ka tas tavā tīklā būs ātrākais DNS. Lai atsauktu izmaiņu, atjauno pierakstītās adreses vai iepriekš lietoto automātisko režīmu. [Microsoft apraksta automātisko DNS saņemšanu ar DHCP](https://support.microsoft.com/de-de/windows/experience/connectivity-networking/essential-network-settings-and-tasks-in-windows).

Es vērtētu DNS atbildes laiku un spēles ping atsevišķi. Pirms un pēc maiņas veic vairākus mērījumus pret to pašu spēles serveri pie līdzīgas tīkla slodzes; skaties arī aiztures svārstības un pakešu zudumus. Ja mainījusies servera IP adrese, to pieraksti. Tas ir mans ieteiktais salīdzinājums; šeit iestatījumus nemainīju un veiktspēju nemērīju. Citai sistēmai precīzais izvēļņu ceļš jāpielāgo tās nosaukumam un versijai.

#### P10

Vēlos meklēt kodu arī nepabeigtos PR un arhīvos. Kā atšķirt noderīgu komponentu no projekta, kuru uzturēt maksās vairāk nekā gatavu alternatīvu?

Sāktu ar vienu vajadzīgo funkciju: kāda ievade, kāds rezultāts un ar kuru gatavo alternatīvu to salīdzināt. Tad var novērtēt komponenta pienesumu, neuzņemoties visu atrasto projektu.

GitHub parastā **Code Search meklē noklusējuma zaros**. Tāpēc nepievienota PR kodu nevar paļāvīgi atrast tikai ar vispārīgu koda meklējumu. [GitHub dokumentācija](https://docs.github.com/en/search-github/github-code-search/using-github-code-search) šo robežu norāda tieši.

Šādi sāktu meklēšanu; tie ir piemēri, kuros jāaizstāj `OWNER/REPO` un `TERM`:

| Kur meklēt | Vaicājuma piemērs |
|---|---|
| Nepievienotie PR, arī aizvērtie | `repo:OWNER/REPO is:pr is:unmerged TERM` |
| PR melnraksti | `repo:OWNER/REPO is:pr draft:true TERM` |
| PR arhivētos repozitorijos | `is:pr archived:true TERM` |
| Arhivēto repozitoriju kods | `TERM is:archived` |
| Forku kods | `TERM is:fork` |

[PR meklēšanas](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests) un [Code Search sintakse](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax) atšķiras. Īpaši nejauc `archived:true` PR meklēšanā ar `is:archived` koda meklēšanā.

Atrasto PR lasītu kopā ar apspriedi, pārskatītāju iebildumiem un testiem. Pēc tam atsevišķā darba kopijā var pārbaudīt tā izmaiņu zaru ar [`gh pr checkout`](https://docs.github.com/de/pull-requests/how-tos/review-pull-requests/checking-out-pull-requests-locally). Arhīvam fiksētu konkrētu izmaiņu identifikatoru: [GitHub skaidro](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives), ka zaru un tagu norādes var pārvietoties.

Mana atlases pārbaude būtu šāda:

- **Robeža:** vai funkciju var lietot un nomainīt atsevišķi?
- **Atļautā lietošana:** vai konkrētajiem failiem un atkarībām ir saprotami licences nosacījumi? Publisks repozitorijs pats par sevi nav brīva licence; to skaidro [GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).
- **Pārbaudāmība:** vai neliels piemērs dod vajadzīgo rezultātu un parāda kļūmju uzvedību?
- **Uzturēšana:** kurš labos kļūdas, pielāgos atkarības un pārcels izmaiņas pēc atjauninājumiem?
- **Ieguvums:** ko šis komponents izdara izmērāmi labāk par gatavo alternatīvu?

Izmaksu aplēsē ieskaitītu pielāgošanu, testus, turpmākos labojumus un atkarību atjaunināšanu vienā un tajā pašā periodā abiem variantiem. Ja vajadzīga plaša vecā projekta atdzīvināšana, bet konkrētais ieguvums paliek neskaidrs, izvēlētos gatavo alternatīvu. Tā ir mana lēmuma metode; šeit konkrēta PR izpildi, integrāciju vai ietaupījumu neesmu pārbaudījis.

### Pētniecības jautājumi

#### F01

Vai jau ir vispārpieņemts pierādījums Navjē–Stoksa eksistences un gluduma tūkstošgades problēmai? Ja nav, ko mūsu AI pētniecības projekts var reāli pārbaudīt, neizliekoties, ka esam to atrisinājuši?

### Paziņots atrisinājums, turpinās izvērtēšana

2026. gada 9. novembrī nebūtu precīzi vienkārši atkārtot, ka šī problēma joprojām nav atrisināta. OpenAI 8. septembrī publicēja apgalvotu atrisinājumu un Lean formalizāciju. Clay institūts 11. septembrī rakstīja, ka problēma šķietami ir atrisināta, bet savā aktuālajā sarakstā to ievieto sadaļā “Active problems”. Pārbaudītie primārie avoti tādēļ pamato formulējumu “paziņots atrisinājums, turpinās izvērtēšana”; tie paši par sevi neapliecina vispārpieņemtu, galīgi nostiprinātu atzinumu. [Clay paziņojums](https://www.claymath.org/news/navier-stokes-announcement/) · [Clay saraksts](https://www.claymath.org/millennium-problems/)

Jāpārbauda tieši tā problēmas versija, uz kuru attiecas rezultāts. Publicētais darbs apgalvo singularitātes izveidošanos ar gludu ārēju spēku, kas atbilst Clay formulējuma C un D alternatīvām. Tas neapgalvo, ka šādi atrisināts arī vispārīgais gadījums bez ārēja spēka. To var pārbaudīt, salīdzinot darba apgalvojumu ar Feffermana oficiālo formulējumu, kur A un B prasa nulles ārējo spēku. [Autoru paziņojums](https://openai.com/index/navier-stokes-solution/) · [Oficiālais uzdevums](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf)

Mūsu projekts var sākt ar publicētā darba pārbaudi un pēc tās izmēģināt divas palīdzrīku idejas.

1. Atkārtot publicētā sertifikāta pārbaudi. Gatavā bāze ir autoru Apache-2.0 repozitorijs ar Lean, Mathlib un Lake; dokumentācijā dotas būvēšanas komandas. Atsevišķa Comparator pārbaude izmanto salīdzināmu uzdevuma formalizāciju. Jāsaglabā konkrētā revīzija, atkarības, pilns izpildes žurnāls un pārbaudītā teorēma. Šajā izpētē dokumentācija ir izlasīta; būvēšana nav izpildīta. [Repozitorijs](https://github.com/openai/NavierStokesAndEuler) · [Comparator instrukcija](https://raw.githubusercontent.com/openai/NavierStokesAndEuler/main/ComparatorChallenges/README.md)
2. Veidot mazu hipotēzi par pierādījuma pārbaudes palīdzrīku: sasaistīt katru dabiskās valodas nosacījumu ar formālo definīciju un ziņot par neatbilstībām. Otrs eksperiments būtu skaitlisko simulāciju pārnest uz rigorozu kļūdu robežu pārbaudi konkrētam datu un laika intervālam. Ar skaitlisku singularitātes iespaidu vien nepietiek: oficiālais apraksts pats uzsver skaitliskās nestabilitātes problēmu. [Oficiālais uzdevums](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf)

Lētais sākuma tests būtu viena precīzi nosaukta lemma vai viena Comparator pārbaude ar iepriekš ierobežotu CPU laiku. Veiksme nozīmētu atgūstamu pārbaudes rezultātu un skaidru hipotēžu sarakstu. Ja mainīts uzdevuma formulējums vai pietrūkst formāla pamatojuma, rezultāts paliek nepilnīgs. Datora laika, enerģijas un ieviešanas izmaksas vēl jāizmēra šajā vidē.

#### F02

Vai no viena augstas izšķirtspējas video var viennozīmīgi atgūt visu 3D ainu un fotoreālistiski parādīt neredzētās virsmas?

### Pilnīgu viennozīmīgu atgūšanu garantēt nevar

Augsta izšķirtspēja palīdz saskatīt redzamās detaļas. Skati aiz priekšmetiem no lielāka pikseļu skaita nerodas. Ja video nekad neparāda kādu virsmu un tā neietekmē redzamos atspulgus vai ēnas, vairākas atšķirīgas šīs virsmas versijas var dot to pašu ierakstu. Šādu atšķirību ierakstā nav ar ko noteikt. Rekonstrukcijas pētījumos tieši izdalīta nenoteiktība nepietiekami novērotās vietās, kustīgu objektu radītas kļūdas un kameras pozīcijas neprecizitātes. [Autoru pētījums](https://aaltoml.github.io/uncertainty-nerf-gs/)

Viens video tomēr var saturēt daudz derīgu skatpunktu. Statiskai ainai ar kameras pārvietošanos, pietiekamu pārklājumu un saskatāmu faktūru es sāktu ar COLMAP. Tā autori iesaka atšķirīgus kameras novietojumus, ne tikai rotāciju uz vietas, un brīdina par spīdumiem un bezfaktūras virsmām. Tādēļ kameras trajektorija un ainas īpašības ir jāvērtē kopā ar pikseļu skaitu. [COLMAP pamācība](https://colmap.github.io/tutorial.html)

| Gatavā bāze | Ko pārbaudīt |
|---|---|
| COLMAP | Kameru pozīcijas un ģeometriju no savstarpēji pārklājošiem kadriem; projekta pamatkods ir ar BSD licenci. |
| MASt3R | Apmācīta attēlu atbilstību un 3D novērtēšanas pieeja kā atsevišķs salīdzinājums; kodam ir CC BY-NC-SA 4.0, svaru lietojumam arī datu kopu noteikumi. |

Šajā izpētē izlasīta dokumentācija; šie rīki nav uzstādīti vai izpildīti. MASt3R nav jāpasniedz kā neierobežoti komerciāli izmantojams brīvā koda aizvietotājs. [COLMAP](https://github.com/colmap/colmap) · [MASt3R licences un uzstādīšana](https://github.com/naver/mast3r)

Fotoreālistisks attēls no jauna skatpunkta var būt ticama sintēze. Lai sauktu to par konkrētās vietas atjaunojumu, vajag salīdzinājumu ar neatkarīgi uzņemtu attēlu vai citu mērījumu. Oriģināla neredzētā aizmugure var būt citāda.

Ierosinu divas pārbaudāmas sintēzes hipotēzes. Pirmajā parastajai rekonstrukcijai pievienojam redzamības masku un vairākus neatkarīgus modeļa novērtējumus, lai atzīmētu nepamatotās vietas. Otrajā šo nenoteiktību izmantojam nākamā filmēšanas skatpunkta izvēlei. Autoru darbā apskatītas ansambļu un papildu skatpunkta pieejas, bet mūsu apvienojuma priekšrocība vēl jāmēra. [Nenoteiktības avoti un metodes](https://aaltoml.github.io/uncertainty-nerf-gs/)

Sākuma pārbaudei izvēlamies vienu statisku objektu, ierobežotu kadru kopu un atsevišķi paslēptus pārbaudes skatus. Salīdzinām parasto bāzi, masku un papildu filmējumu pie vienāda skaitļošanas limita. Noraidām hipotēzi, ja tā nemazina kļūdaini pārliecinošus atjaunojumus vai pasliktina izmērīto ģeometriju. GPU laiku, atmiņu un darbu pie adaptera uzskaitām faktiskajā izmēģinājumā.

#### F03

Kā izveidot aģenta procedūru, kura pati uzlabo meklēšanas skillu, bet neapmāna vērtētāju un nezaudē atgriešanos pie iepriekšējās versijas? Gatavie komponenti un iespējamā sintēze.

### Sāktu ar GEPA un atsevišķi aizsargātu vērtēšanu

Meklēšanas procedūru var uzlabot, salīdzinot nelielu skaitu skaidri nodalītu kandidātu. Aģents drīkst mainīt meklēšanas noteikumus un veidot kandidātus; neatkarīgs izpildītājs lemj, kuru versiju pieņemt. Ar norādījumu “neapmāni vērtētāju” nepietiek. Pētījumā RewardHackingAgents vērtētāja labošana un piekļuve slēptajām atbildēm bija atšķirīgi pārkāpumu ceļi, tādēļ jāaizsargā abi. Tas ir konkrētā pētījuma rezultāts, ne garantija pret visiem uzbrukumiem. [Primārais pētījums](https://arxiv.org/abs/2603.11337)

Gatavā sākuma bāze ir MIT licencētais GEPA: tas optimizē teksta kandidātus, izmantojot izpildes kļūdas un vērtēšanas atgriezenisko saiti. Dokumentēts arī adapteris savām sistēmām un izsaukumu budžets. DSPy integrācija der jau DSPy veidotai plūsmai; atsevišķam meklēšanas rīkam saprotamāks var būt tiešs GEPA adapteris. Dokumentācija ir pārbaudīta, bet šeit nav veikta GEPA instalācija vai mūsu meklētāja salīdzinājums. [Autoru repozitorijs](https://github.com/gepa-ai/gepa)

Izveidotu šādu pārbaudes kārtību.

1. Saglabāt pieņemto versiju, tās saturu, atkarības un kontrolsummas. Katrai izmaiņai izveidot atsevišķu kandidātu.
2. Mācību uzdevumus dot kandidāta veidotājam; galīgos pārbaudes uzdevumus un etalonatbildes turēt citā procesā un ārpus tā rakstīšanas/piekļuves tiesībām. Fiksēt modeli, rīkus, budžetu un kritiskās kļūdas pirms sacensības.
3. Salīdzināt pašreizējo pieņemto procedūru ar kandidātu uz tiem pašiem uzdevumiem. Vērtētājs pārrēķina rezultātus no reāliem avotiem un žurnāliem; kandidāta pašvērtējums nedod pieņemšanas punktus.
4. Pieņemt tikai pārbaudīto izmaiņu un saglabāt iepriekšējo versiju. Jaunā darbā pārbaudīt ielādētās versijas kontrolsummu; atgriešanās atjauno arī atbilstošo konfigurāciju. Git `revert` saglabā atcelšanu vēsturē, taču pats neatceļ ārējos blakusefektus. [Git dokumentācija](https://git-scm.com/docs/git-revert)

Divas izmēģināmas idejas papildina gatavo bāzi. Pirmā pārnes kļūdu atkārtošanās novēršanu uz aģenta atmiņu: glabājam īsu noraidīto kandidātu pierakstu. GEPA problēmas #379 autors apraksta lietotāja ziņotu gadījumu ar atkārtotiem neveiksmīgiem labojumiem un saistītu vēl atvērtu priekšlikumu; to nedrīkst saukt par jau ieviestu funkciju. Otrā izmanto reproducējamu laidienu principu: pieņemam tikai versijas pakotni, kurai neatkarīgs pārbaudītājs ir pārbaudījis rezultāta izcelsmi. [GEPA diskusija #379](https://github.com/gepa-ai/gepa/issues/379)

Lētais tests: divi kandidāti, iepriekš atdalīti uzdevumi un vienāds limits katrai pusei. Priekšrocības hipotēzi noraidām, ja ieguvums pazūd neatkarīgā pārrēķinā vai pieaug kritisko kļūdu skaits. Pat veiksmīgs salīdzinājums pamatotu tikai konkrēto izmaiņu pārbaudītajos uzdevumos. Arī detalizēta vērtētāja atgriezeniskā saite var palīdzēt pielāgot apiešanu, tādēļ slēpto pārbaudi netrenējam atkārtoti. [2026. gada autoru pētījums](https://www.microsoft.com/en-us/research/publication/reward-hacking-challenges-oversight-of-autonomous-research-agents/)

#### F04

Vai aģents var bezgalīgu pieredzi bez zudumiem glabāt 5 MiB atmiņā? Kādu godīgu alternatīvu var uzbūvēt?

### 5 MiB var glabāt atlasītu pieredzi, ne visu patvaļīgu vēsturi

Bezgalīgu, patvaļīgu pieredzi bez zudumiem ievietot 5 MiB atmiņā nevar. To var redzēt, saskaitot atmiņas stāvokļus: 5 × 1024 × 1024 × 8 = 41 943 040 biti. Fiksētam šāda izmēra stāvoklim ir galīgs iespējamo konfigurāciju skaits. Garāku patvaļīgu vēsturu ir vairāk, tādēļ dažādām vēsturēm jānonāk vienā stāvoklī; no tā vairs nevar viennozīmīgi atjaunot abas. Tas ir skaitīšanas arguments, kas pazīstams kā baložu būru princips. [Universitātes pierādījuma izklāsts](https://www.informatik.hu-berlin.de/~koessler/Proseminar/Proseminar2015/JacobsSchubfach.pdf)

Īpaši regulāru virkni, piemēram, “vienmēr nulle”, var aprakstīt īsi. Šāds piemērs nemaina garantiju patvaļīgiem datiem. Arī kopsavilkums, modeļa svari vai kontrolsumma nesaglabā visas izdzēstās detaļas: atjaunošanai vajadzīgajai informācijai jāatrodas kaut kur. Informācijas teorija saista iespējamo bezzudumu saspiešanu ar avota paredzamību. [CMU mācību materiāls](https://www.cs.cmu.edu/~15322/book/ch15/03.html)

Praktiskajā atmiņā iepriekš nosakām, ko saglabājam un ko drīkstam zaudēt. 5 MiB kopējā robežā ieskaitām ne tikai mācību kartītes, bet arī indeksus, versijas, atteikto kandidātu pierakstus un saglabājamos pierādījumus. Vienai kartītei glabājam situāciju, izmēģināto paņēmienu, rezultātu, ierobežojumu un avota norādi. Pretrunīgus novērojumus nesapludinām par vienu pārliecinošu noteikumu.

Gatavā plašākas atmiņas bāze ir Letta: dokumentācijā aprakstīti atmiņas bloki kontekstā un vēsture datubāzē ārpus konteksta. Tas palīdz organizēt lielu vēsturi, bet dokumentētā pieeja nav pierādījums visas sistēmas 5 MiB robežai. Ja izmantojam ārēju arhīvu, tā apjoms un glabāšanas ilgums jāuzrāda atsevišķi. [Letta autoru dokumentācija](https://docs.letta.com/v1-sdk/concepts/stateful-agents)

Mūsu ierobežotajai vajadzībai izmēģinātu divas hipotēzes. Pirmā: kartītes atlasīt pēc atkārtoti izmērītas lietderības konkrētiem uzdevumiem, salīdzinot ar vienkāršu jaunāko kartīšu saglabāšanu. Otrā: atsevišķi rezervēt nelielu vietu neveiksmēm un pretrunām, lai veiksmju kopsavilkumi tās neizspiestu. Abu ideju vērtību nosaka atbildes uz jaunajiem uzdevumiem. Saspiestā teksta apjoms to neparāda.

Lētais tests ir iepriekš sagatavota vēsture, kas pārsniedz limitu, un slēpti jautājumi par tās dažādām daļām. Mērām pareizu atcerēšanos, izdomātus apgalvojumus un diskā faktiski aizņemtos baitus. Atmiņas samazināšana saglabā dzēšanas sarakstu; ja obligātie ieraksti vairs neietilpst, rakstīšana apstājas. Pārbūves pagaidu faili un darba RAM jāuzskaita atsevišķi. Šajā izpētē šāds atmiņas kvalitātes eksperiments nav izpildīts.

#### F05

Kā empīriski noskaidrot, vai vācu, ķīniešu un japāņu meklēšana dod vairāk nekā tikai angļu meklēšana pie vienāda laika budžeta?

### Jāsalīdzina vienādi uzdevumi vienādā laikā

Četru valodu priekšrocību šajā projektā vēl neesam izmērījuši. To noskaidrotu iepriekš fiksētā salīdzinājumā pa uzdevumu pāriem: katru uzdevumu izpilda gan angļu vaicājumu procedūra, gan EN/DE/ZH/JA procedūra. Modelis, rīki un kopējais laika limits ir vienādi; daudzvalodu puse savā laikā apmaksā arī terminoloģijas izvēli, tulkošanu un papildu avotu lasīšanu. Viena un tā paša uzdevuma izmantošana abām pusēm samazina uzdevumu grūtības radīto sajaukumu. Šāda bloķēšana atbilst NIST eksperimentu projektēšanas principam. [NIST](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm)

Vispirms precīzi definējam, ko mainām. Es sākumā mainītu tikai vaicājumu valodas: abām pusēm atļautu lasīt jebkurā valodā atrastus avotus. Citādi vienlaikus mainītos gan meklēšana, gan piekļuve informācijai. Angļu puse drīkst izmantot visu savu budžetu papildu angļu vaicājumiem; daudzvalodu puse nesaņem papildu izsaukumus bez uzskaites.

Uzdevumus pirms rezultātu redzēšanas sadalām pa tēmām un pēc iespējamās vietējo avotu nozīmes. Abu variantu secību nejaušinām. Izmantojam atsevišķus kontekstus un atmiņas kopijas, lai otrā puse neieraudzītu pirmās atradumus. Dzīvajā tīmeklī saglabājam rezultātu un atvērto lapu kvītis, jo indekss un lapas mainās.

Galvenais mērījums būtu pārbaudītu, uzdevuma atrisināšanai nepieciešamu apgalvojumu pareizība. Atsevišķi vērtējam lietderību, neatbalstītus apgalvojumus, atrasto pretpierādījumu un izmaksas. Tulkojumi un pārpublicējumi skaitās viens sākotnējais pierādījums. Vērtētāji saņem atbildes latviski bez procedūras nosaukuma; strīdīgos apgalvojumus pārbauda avotā.

Gatavo MIRACL kopu var izmantot, lai atsevišķi pārbaudītu informācijas atrašanu: tajā ir cilvēku anotēta atbilstība daudzās valodās. Taču MIRACL uzdevums ir meklēt tās pašas valodas korpusā; tas pats par sevi neatbild uz jautājumu par četru valodu tīmekļa izpēti un gala atbilžu kvalitāti. Tāpēc gatavo kopu papildinātu ar atsevišķu mūsu reālo uzdevumu pārbaudi. [MIRACL autoru publikācija](https://transacl.org/index.php/tacl/article/view/4805)

Iespējamās hipotēzes ir divas: vietējie termini atrod agrāk neatrastu primāro avotu; papildu valodas pārsvarā atrod dublikātus un iztērē laiku. Pēc galvenās pārbaudes valodas var pievienot pa vienai, saglabājot to pašu kopējo limitu. Pirms darba nosakām minimāli vērtīgu ieguvumu un analizējam pāru starpības ar nenoteiktības intervālu, uzdevumu uzskatot par vienību. Neliels pilots palīdz aprēķināt vajadzīgo izlasi. Ja intervāls ietver arī praktiski nevērtīgu rezultātu, secinājums paliek nenoteikts; priekšrocības novērtējumu nevar aizstāt ar vaicājumu skaitu.

#### F06

Vai dekompilators var precīzi atjaunot oriģinālo pirmkodu no optimizēta binārā faila? Kā šodien salīdzināt gatavus brīvā koda risinājumus ar pašu sintēzi?

### Oriģinālo pirmkodu vispārīgā gadījumā atgūt nevar

Dekompilators var izveidot saprotamu programmas darbības aprakstu, bet optimizēts binārais fails parasti nenosaka vienu vienīgu sākotnējo tekstu. GCC dokumentē mirušā koda dzēšanu, ekvivalentu fragmentu apvienošanu un funkciju pārveidojumus. Ja atšķirīgās avota daļas kompilators izdzēsis, binārajā failā vairs nav informācijas, kura versija tur bija. Arī pētnieki tieši apraksta kompilācijā zūdošu tipu, struktūru un izmēru informāciju. [GCC](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html) · [Primārais dekompilācijas pētījums](https://www.s3.eurecom.fr/docs/asiaccs22_mantovani.pdf)

Vispirms jāizvēlas sasniedzamais rezultāts: identisks sākotnējais teksts, pārkompilējams kods, ekvivalenta uzvedība vai analītiķim vieglāk saprotams rezultāts. Tie ir dažādi panākumu kritēriji. No ārēja avota atrasts īstais pirmkods var atrisināt pirmo uzdevumu konkrētam failam, taču tā jau ir papildu informācija.

Par salīdzināšanas bāzi izvēlētos Ghidra un RetDec.

| Rīks | Pamatota izvēles robeža |
|---|---|
| Ghidra | Apache-2.0 projekts ar dekompilāciju, skriptiem un automatizētu darbu; piemērots kā galvenā pielāgojamā bāze. |
| RetDec | LLVM balstīts dekompilators ar C izvadi; repozitorijā norādīts ierobežotas uzturēšanas režīms un vairāki licenču komponenti. |

Rīku dokumentācija ir izlasīta, bet instalācija un mūsu datu tests nav izpildīti. RetDec ierobežota uzturēšana ir konkrēts praktisks pretarguments jaunai ilgtermiņa integrācijai, ne pierādījums sliktākai dekompilācijai katrā failā. [Ghidra autori](https://github.com/NationalSecurityAgency/ghidra) · [RetDec autori](https://github.com/avast/retdec)

Lētā salīdzinājumā izmantotu mūsu pašu nelielas programmas ar zināmu pirmkodu un skaidru licenci. Tās kompilētu ar fiksētām kompilatora versijām un dažādiem optimizācijas līmeņiem, atsevišķi ar atkļūdošanas informāciju un bez tās. Publicētu neveiksmes, patērēto CPU laiku un manuālos labojumus. Teksta līdzību nedrīkst pārdēvēt par uzvedības ekvivalenci; pēdējo pārbauda ar neatkarīgiem ievadiem un, ierobežotos fragmentos, formāli formulētiem nosacījumiem.

Pašu risinājumam pārbaudītu divas iespējas. Pirmā: Ghidra izvadi pārstrukturējošs modelis uzlabo lasāmību, bet katrs labojums iziet neatkarīgu uzvedības pārbaudi. Otrā: simbolus, virknes un izsaukumus izmanto kandidātu atrašanai atļautā pirmkodu korpusā. Kandidātu sakritība vēl nav izcelsmes pierādījums; jāpārbauda versija un būvēšanas apstākļi.

Sākumā pietiek ar vienu šauru funkciju saimi un fiksētu laika limitu. Būvēšanu turpinātu tikai tad, ja sintēze pārspēj pielāgotu gatavo bāzi iepriekš izvēlētajā mērķī un neievieš uzvedības kļūdas. Mūsu sistēmas priekšrocībai vēl vajadzīgs šāds salīdzinājums.

#### F07

Vai vienādi modeļa svaru faili un seed garantē identisku atbildi uz citām videokartēm? Ko fiksēt reproducējamībai?

**Nē, ar svaru failiem un vienādu seed nepietiek.** NVIDIA cuBLAS atkārtojamības solījums attiecas uz konkrētu rīku versiju, vienādu GPU arhitektūru un vienādu SM skaitu, turklāt ar dokumentētiem nosacījumiem par plūsmām un algoritmiem. Tas nav solījums par patvaļīgām videokartēm. [NVIDIA dokumentācija](https://docs.nvidia.com/cuda/cublas/index.html#results-reproducibility)

Arī pašreizējā vLLM dokumentācija norāda, ka reproducējamība pēc noklusējuma netiek garantēta. Bezsaistes režīmā var izvēlēties determinētu plānošanu vai no pieprasījumu grupējuma neatkarīgu izpildi; tiešsaistē dokumentēts otrais risinājums. Pat ar šiem iestatījumiem garantijas robeža ir tā pati aparatūra un vLLM versija. Seed nosaka nejaušo skaitļu ģeneratoru stāvokli, nevis visu aprēķinu vidi. [vLLM uzturētāju skaidrojums](https://docs.vllm.ai/en/latest/usage/reproducibility/)

Vispirms nosakām, ko tieši gribam atkārtot: starprezultātu bitus, tokenu virkni vai atbilžu kvalitāti. Tie ir atšķirīgi kritēriji. Ļoti tuvu kandidāttokenu gadījumā arī maza skaitliska atšķirība var mainīt izvēli; turpmākā ģenerēšana tad turpinās no citas virknes. Tas ir mehānisma skaidrojums, ne mūsu aparatūrā izmērīts rezultāts.

Reproducējamības paketē ierosinu saglabāt:

- svaru, tokenizatora, modeļa konfigurācijas un precīzās ievades kontrolsummas, sarunas veidni, dekodēšanas parametrus un RNG stāvokļus;
- programmas revīziju, atkarību un konteinera versijas, draiveri, CUDA, bibliotēkas, skaitļu formātu, kvantēšanu un izvēlētos aprēķinu kodolus;
- GPU modeli, ierīču skaitu un izvietojumu, paralēlisma iestatījumus, pieprasījumu grupējumu, plānotāju un kešatmiņas režīmu;
- ārējo rīku atbildes un izgūtos dokumentus, ja modelis tos izmanto, kā arī iegūtos tokenus, kļūdas un laikus.

Gatavā bāze ir dokumentēts, fiksētas versijas vLLM reproducējamības režīms. Paši pievienotu vides apraksta ģeneratoru un salīdzinātāju, kas atrod pirmo tokenu vai skaitlisko novirzi. **Pirmā hipotēze:** fiksēta plānošana samazina atšķirības starp atkārtojumiem vienā datorā. **Otrā:** precīzāks skaitļu formāts un saskaņoti kodoli samazina novirzes starp divām GPU konfigurācijām. Neviena hipotēze nesola vispārēju bitu identitāti.

Sākuma pārbaudei pietiktu ar iepriekš izvēlētu uzvedņu kopumu: atkārtojumiem A/A un tad A/B, mainot tikai aparatūru. Reģistrēt tokenu sakritību, pirmo novirzi un faktiskās izmaksas. Ja atšķiras jau A/A, pirms starpiekārtu salīdzinājuma jāsalabo bāze. Šeit GPU testi nav veikti; izpildīti vaicājumi četrās valodās, secinājumu balsta izlasītā ražotāja un uzturētāju dokumentācija.

#### F08

Man vajag aģenta atmiņas izmaiņu cēloņsakarīgu novērtējumu. Kā atšķirt labāku atmiņu no vienkārši vairāk meklējumiem vai vieglākiem uzdevumiem?

**Jāsalīdzina vecā un jaunā atmiņa uz tiem pašiem uzdevumiem, iepriekš nosakot meklēšanas iespējas.** Viena rezultātu tabula, kur jaunajai versijai ir vairāk rīku izsaukumu vai cita uzdevumu izlase, neizolē atmiņas ieguldījumu.

Gatava sākuma bāze ir LongMemEval: autoru repozitorijā ir 500 jautājumu kopums, sarunu vēstures, atbilžu vērtēšanas rīki un atmiņas darbībām paredzēti salīdzinājumi. Tas ļauj pārbaudīt informācijas atcerēšanos sarunās; mūsu aģenta pilnā darba kvalitāte vēl jāpārbauda ar paša uzdevumiem. [LongMemEval autoru repozitorijs](https://github.com/xiaowu0162/LongMemEval) Praktiskajā Redis autoru pētījumā atsevišķi salīdzināta neapstrādātu sarunu izgūšana, atmiņas izvilkumu izmantošana un abu apvienošana. Autori arī brīdina, ka citur publicētie rezultāti grafikā nav kontrolēta sacensība savā starpā. [Pirmavota eksperimenta apraksts](https://redis.github.io/redis-ai-research-public/longmemeval-agent-memory/)

Ierosinu pārbaudīt četras kombinācijas: **vecā/jaunā atmiņa × mazs/liels meklējumu skaits**. Pilns faktoru plāns ietver visas kombinācijas; tā pamatu apraksta [NIST](https://www.itl.nist.gov/div898/handbook/pri/section3/pri333.htm). Katrā meklējumu līmenī kontrolētajam eksperimentam izsaukumu skaits un ārējie pierādījumi ir fiksēti, ne tikai atļautais maksimums. Vienādi paliek modelis, uzvedne, tokenu limits un sākotnējā vēsture; mainās pārbaudāmais atmiņas mehānisms.

Uzdevumus bloķējam pēc grūtības un nejaušinām izpildes secību. Pirms katra mēģinājuma atjaunojam sākotnējo atmiņas stāvokli, lai viena versija nemācās no otras atbildes. Vērtētājs neredz versijas nosaukumu; atsauces atbildes, vērtēšanas noteikumi un slēptie uzdevumi aģentam nav labojami. Vērtējam faktu pareizību, atteikšanos minēt, kļūdu smagumu, lasīšanas un rakstīšanas izmaksas, kā arī pāru atšķirību nenoteiktību.

Atsevišķā izmēģinājumā ļaujam abām versijām pašām izvēlēties meklējumu skaitu vienāda kopējā budžeta ietvaros. Tas mēra **visas procedūras efektu**, ieskaitot spēju ietaupīt meklējumus. Pēc rezultātu saņemšanas vienkārši atlasīt tikai mēģinājumus ar vienādu izsaukumu skaitu būtu cita atlase un varētu sagrozīt secinājumu.

Sākumā pārbaudītu divus iespējamos uzlabojumus. Avota norādes pie katra atmiņas fakta var samazināt kļūdainu atcerēšanos; to lēti pārbaudīt uz jautājumiem ar savstarpēji pretrunīgiem datētiem faktiem. Reto detaļu saglabāšana līdzās kopsavilkumam var uzlabot precizitāti; to pārbaudīt ar detaļām, kuras kopsavilkuma bāze izmet. Abām versijām jābūt vienādam atmiņas izmēra limitam. Ja ieguvums pazūd pie fiksētiem pierādījumiem, nevaram to piedēvēt tikai labākai atmiņas reprezentācijai.

Šeit veikta izpēte četrās valodās. Aprakstītais eksperiments vēl jāizpilda, lai izmērītu kvalitātes atšķirības, laiku un izmaksas.

#### F09

Vai LLM aģentu sistēmā var visiem ārējiem maksājumiem garantēt tieši vienu izpildi, ja process avarē pēc pieprasījuma? Projektē praktisku risinājumu ar ierobežojumiem.

**Visiem ārējiem maksājumiem universālu “tieši vienreiz” garantiju dot nevar.** Ja pakalpojums izpildījis pieprasījumu, bet atbilde pazūd, klienta lokālais stāvoklis var neatšķirties no situācijas, kur pieprasījums nav sasniedzis pakalpojumu. Akls atkārtojums var radīt otru maksājumu, savukārt neatkārtošana var atstāt maksājumu neizpildītu. AWS autoru apraksts tieši apskata šo neskaidrību un klienta piešķirtus unikālus pieprasījuma identifikatorus. [AWS Builders’ Library](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)

Praktiski var panākt vienu maksājuma efektu **konkrēta pakalpojuma idempotences līguma robežās**. Piemēram, Stripe API v1 saglabā pirmā pieprasījuma ar konkrēto atslēgu rezultātu tikai pēc galapunkta izpildes sākuma. Atkārtojot to pašu atslēgu, saņem saglabāto atbildi, arī kļūdu 500. Ja parametru pārbaude neizdodas vai rodas konflikts ar vienlaikus izpildē esošu pieprasījumu un galapunkta izpilde nesākas, idempotences rezultātu nesaglabā; šādu pieprasījumu var atkārtot. Atslēgas drīkst dzēst pēc vismaz 24 stundām; atkārtota jau dzēstas atslēgas izmantošana rada jaunu pieprasījumu. API v2 dokumentēta cita kļūmju apstrāde, tādēļ šos noteikumus nedrīkst vispārināt. [Stripe idempotence](https://docs.stripe.com/api/idempotent_requests)

Procedūru veidotu šādi:

1. Pirms sūtīšanas datubāzē vienā transakcijā saglabā maksājuma nodomu, nemainīgus parametrus, unikālu nodoma ID un nosūtāmo darbu. Vienam nodomam ir viena stabila pakalpojuma atslēga.
2. Atsevišķs izpildītājs nosūta darbu. Rindas atkārtojumi izmanto to pašu atslēgu un parametrus; aģents nevar pats pārvērst atkārtojumu jaunā nodomā.
3. Laika pārsniegumu atzīmē kā **iznākums nezināms**, saglabā pakalpojuma objekta ID, ja tas saņemts, un salīdzina stāvokli ar pakalpojuma datiem.
4. Ar parakstu pārbaudītus paziņojumus apstrādā idempotenti: reģistrē notikumu ID un nepaļaujas uz to pienākšanas secību. Stripe dokumentē gan dublikātus, gan secības negarantēšanu. [Paziņojumu dokumentācija](https://docs.stripe.com/webhooks)
5. Tuvojoties atslēgas derīguma robežai, neskaidru maksājumu vairs akli neatkārto. To noskaidro pēc pakalpojuma reģistra vai atstāj izmeklēšanai, saglabājot saistību ar sākotnējo nodomu.

Gatavie komponenti ir pakalpojuma SDK, transakciju datubāze un nosūtāmo darbu tabula. AWS dokumentētā *transactional outbox* pieeja sasaista lokālās izmaiņas un darba ierakstu, taču pati par sevi nepadara ārējo maksājumu atomāru ar mūsu datubāzi; dublētiem ziņojumiem joprojām vajag idempotentu saņēmēju. [AWS pieejas apraksts](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html)

Pārbaudītu divas hipotēzes: stabila nodoma atslēga novērš dublētu efektu pēc avārijas, un atsevišķa neskaidro iznākumu pārbaude samazina iestrēgušus darbus. Sākumā pietiktu ar viltotu maksājumu pakalpojumu, kurā izraisām avārijas pirms nosūtīšanas, pēc efekta un pirms atbildes saglabāšanas, kā arī dzēšam atslēgu un atkārtojam paziņojumus. Panākumu kritērijs ir ne vairāk kā viens efekts nodomam un pareizi uzrādīta nenoteiktība. Pabeigšana papildus atkarīga no pakalpojuma pieejamības un maksājuma pieņemšanas. Šeit nav izpildīts ne tests, ne maksājums; četru valodu izpēte devusi projektējumu, ne universālas garantijas pierādījumu.

#### F10

Kā pārbaudīt pašuzlabojošu attēlu rekonstrukcijas programmu, lai augstāks PSNR nepaslēptu sliktāku fotogrāfisko kvalitāti un izdomātas detaļas?

**Augstāks PSNR vēl nepierāda labāku fotogrāfisko kvalitāti vai pareizas detaļas.** Blau un Michaeli pētījums apraksta robežu starp vidējo izkropļojumu un uztveres kvalitāti. Tas nenozīmē, ka katrs PSNR pieaugums automātiski pasliktina katru attēlu. Savukārt Cohen un līdzautori analizē, kā ticama izskata ģenerēta restaurācija var pievienot detaļas, kuru oriģinālā nav. [Uztveres un izkropļojuma pētījums](https://arxiv.org/abs/1711.06077); [izdomāto detaļu pētījums](https://arxiv.org/abs/2405.16475)

Vērtējumu sadalītu trīs daļās.

**Atbilstība novērojumam.** Uz attēliem ar zināmu etalonu rēķināt PSNR un strukturālo līdzību, iepriekš fiksējot krāsu telpu, apgriešanu, izšķirtspēju un izlīdzināšanu. Saglabāt arī rezultātu pa ainām un kļūdu kartes; vidējais skaitlis var paslēpt vienu ļoti sliktu gadījumu.

**Fotogrāfiskā kvalitāte.** Gatavs papildinājums ir autoru LPIPS realizācija: tā salīdzina attēlus pēc uztverei pielāgotām pazīmēm. Dokumentācija nosaka arī ievades mērogu un tīkla variantus, kuri salīdzinājumā jāsaglabā vienādi. Autoru novērtēšanā izmantota cilvēku izvēle starp diviem variantiem pret etalonu. [LPIPS kods un novērtēšanas apraksts](https://github.com/richzhang/PerceptualSimilarity). Mūsu testā cilvēki akli salīdzinātu sajauktus kandidātu pārus gan pilnā attēlā, gan nozīmīgos fragmentos. LPIPS un cilvēku patika paši par sevi neapstiprina, ka attēls rāda sākotnējās detaļas.

**Detaļu pareizība.** Atsevišķi pārbaudīt uzrakstus, objektu skaitu, sejas pazīmes, ģeometriju un faktūras pret zināmo etalonu vai atliktiem papildu skatpunktiem. Ja pieejams tikai viens bojāts attēls, pilnīgi pazudušās detaļas var būt ticamas, taču to pareizību no tā paša attēla neapstiprināsim. Šādas vietas rezultātā jāatzīmē kā neskaidras.

Gatavā bāze ir pašreizējā rekonstrukcijas programma un fiksēts vērtēšanas komplekts; izšķirtspējas palielināšanai pievienotu vienkāršu interpolāciju. Pašuzlabojošais aģents maina programmu tikai izstrādes kopumā. Slēptajā pārbaudē atdala ainas, nevis blakus kadrus no vienas ainas; etalonus, vērtētāju un pieņemšanas sliekšņus kandidāts nevar labot. Iepriekšējā versija paliek atjaunojama.

**Pirmā hipotēze:** vairāku kritēriju pieņemšana ar aizliegumu ieviest smagas detaļu kļūdas dos noderīgākas versijas nekā PSNR optimizācija vien. **Otrā:** nelielu ievades perturbāciju un vairāku rekonstrukciju salīdzinājums palīdzēs atklāt nestabilas izdomātas detaļas. Stabilitāte pati par sevi vēl nepierāda pareizību.

Hipotēžu sākuma pārbaudei izvēlētos nelielu, iepriekš fiksētu ainu kopumu ar smalkiem uzrakstiem, sejām un atkārtotām faktūrām un divus kandidātus ar vienādu resursu limitu. Ja PSNR uzvarētājs pasliktina aklo kvalitātes vērtējumu vai ievieš kritisku neatbilstību, to nepieņem. Faktisko laiku un izmaksas reģistrē testā. Šeit veikta četru valodu izpēte un avotu lasīšana; rekonstrukcijas, LPIPS aprēķini un cilvēku eksperiments nav izpildīti.

### Kā lietot prasmi savā vidē

Iedod aģentam visu prasmes mapi vai publicētā projekta saiti. Palūdz izlasīt SKILL.md, ievērot četru valodu izpētes kārtību un precīzi nosaukt, kas ir aktivizēts. Vienas sarunas norādījumu ievērošana, pastāvīga instalācija un pieslēgta pieredzes atmiņa ir atsevišķi pārbaudāmi soļi.

Ja vide atbalsta failus un programmu izpildi, pieslēdz sākuma un beigu darbības un pārbaudi otro uzdevumu: vai tas saņēma pirmā uzdevuma mācību? Jaunus paņēmienus pieņem tikai pēc iepriekš noteikta salīdzinājuma un neatkarīgām pārbaudēm. Tas dod kontrolējamu attīstības ceļu, ne garantiju, ka katrs nākamais jautājums būs vieglāks vai atbilde vienmēr labāka.

<a id="support-the-author"></a>

### Atbalsti autoru

Atbalsta sadaļa atjaunināta 2026. gada 10. novembrī pēc autora aktuālajām norādēm. Šeit izmantots autora apstiprinātais latviešu teksts. Eksperimentu saturam veikti tikai ievadā norādītie redakcionālie labojumi. Šī sadaļa aizstāj agrāko atbalsta formulējumu un tīklu nosaukumus.

Mani sauc Reinis Runcis. Esmu paralizēts un dzīvoju viens. Ikdienā cīnos, lai turpinātu radīt, un ar šo darbu dalos bez maksas. Ceru ar savu piemēru iedvesmot arī cilvēkus, kuriem šķiet, ka viņu situācijā nav izejas.

Ja šis projekts tev noder vai vēlies palīdzēt man turpināt iesākto, būšu pateicīgs par brīvprātīgu ziedojumu. Tavs atbalsts palīdz man ikdienā un darbā pie šādiem rīkiem.

Swedbank · Saņēmējs: **REINIS RUNCIS**  
IBAN: **`LV82HABA0551011504293`**

- [Stripe (EUR)](https://buy.stripe.com/dRm7sNfD2bOZckRb9A6g802)
- [Stripe (USD)](https://donate.stripe.com/cNifZj4Yog5fckR5Pg6g800)
- [PayPal](https://paypal.me/ReinisRuncisSupport)

**USDT · BSC / BEP-20**

`0x32834068Fa4fEe29fA10e2020e68Fb23d5fC1d21`

**USDT · Solana / SPL**

`Hy6hKMwMDgXFdaD3N5J1CNMs2LwiE22QdrQnEYoX3fZh`

[Vairāk par mani Facebook](https://www.facebook.com/reinis.runcis)

Atbalsts ir brīvprātīgs un nav prasmes izmantošanas nosacījums.


<a id="comparison"></a>

## Visas sešas stratēģiju salīdzinājuma atbildes

Visu sešu izpētes atbilžu pilnais saturs ir saglabāts no pārskatītā latviešu izdevuma. Redakcija, 2026. gada 10. novembris: vienā teikumā izlabots lietvārda locījums; rezultāti, strukturētie lauki un avotu adreses nav mainīti. Pirmavotu adreses paliek tekstā un katras atbildes strukturētajā avotu sarakstā. Strukturētie lauki ir pašu autorēto atbilžu sastāvdaļa; atsevišķas vērtētāju izvades, testu veidnes un izpildes ieraksti nav iekļauti.

Pieejamas arī [atbildes angliski](validation/2026-11-09-beta3/comparison/answers.en.md) un [publicētie salīdzinājuma rezultāti](PUBLISHED_FINDINGS.lv.md). Izdevums nepievieno jaunu izpētes izmēģinājumu. Pierādījumu robežas norādītas [publikācijas tvērumā](PUBLICATION_SCOPE.md).

### baseline / IT01-depth-output

**Nē, šī kontrolpunkta izvadam nav pamatoti pievienot mērvienību `m`.** `depth-anything/Depth-Anything-V2-Small-hf` kartītē norādīts relatīvais dziļums, un arī autoru repozitorijs pamatmodeļus pieskaita relatīvā dziļuma novērtēšanai. Kartītes vispārīgais teikums par relatīvo un absolūto dziļumu neapstiprina, ka tieši šis kontrolpunkts izvada metrus. [Modeļa kartīte](https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf), [autoru repozitorijs](https://github.com/DepthAnything/Depth-Anything-V2).

Projekta autors precizē, ka modelis prognozē apgriezto dziļumu: mazāka prognozes vērtība atbilst tālākam punktam. Tādēļ komponenti var paturēt attēla apgabalu relatīvā tuvuma secībai. Šī secība pati nedod fizisku attālumu metros. [Autora skaidrojums](https://github.com/DepthAnything/Depth-Anything-V2/issues/174).

Nākamais solis ir izvēlēties atsevišķu metriskajam dziļumam pielāgotu kontrolpunktu, piemēram, telpām `Depth-Anything-V2-Metric-Indoor-Small-hf`. Tas jau ir autora pielāgots modelis; pašam jauna apmācība nav jāveic, taču dotā uzdevuma kodu nozīmē tā ir `replace_core` izvēle. Pirms paļauties uz tā attālumiem, jāpārbauda kļūda saviem attēliem pret izmērītiem attālumiem. [Metriskā modeļa kartīte](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf). Lietotājs projekta diskusijā apraksta nepareizu mērogu punktu mākoņa veidošanā; tas ir konkrētas pieredzes ziņojums, ne universāls kļūdas mērījums. [Pieredzes ziņojums](https://github.com/DepthAnything/Depth-Anything-V2/issues/152).

Šeit pārbaudīti avoti un konfigurācija. Inferenci neizpildīju, pakotnes neinstalēju un svarus nelejupielādēju.

### evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": false,
    "native_output_kind": "relative_depth",
    "action": "replace_core",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "depth_ordering"
  },
  "explanation": "Depth-Anything-V2-Small-hf ir relatīvā dziļuma kontrolpunkts. Tā izvade raksturo attēla punktu relatīvo tuvumu, un tai uzdevumā dotajos apstākļos nav pamatota metru mēroga. Projekta autors precizē, ka tā ir apgrieztā dziļuma prognoze. Metru atzīmes pievienošana izvadi nepārvērš metriskā attālumā.",
  "next_step": "Saglabāt šo modeli tuvāku un tālāku attēla apgabalu secībai. Attālumam metros izvēlēties autoru atsevišķi metriskajam dziļumam pielāgotu kontrolpunktu, piemēram, telpām Depth-Anything-V2-Metric-Indoor-Small-hf; pirms lietošanas pārbaudīt tā kļūdu saviem attēliem pret izmērītiem attālumiem. Šeit veikta tikai avotu pārbaude.",
  "sources": [
    "https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf",
    "https://github.com/DepthAnything/Depth-Anything-V2",
    "https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf/blob/main/config.json",
    "https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf",
    "https://github.com/DepthAnything/Depth-Anything-V2/blob/main/metric_depth/README.md",
    "https://github.com/DepthAnything/Depth-Anything-V2/issues/174"
  ]
}
```



### baseline / IT02-clip-generation

**Nē, oficiālais CLIP `ViT-B/32` ar norādīto piemēru brīvu apraksta teikumu neģenerē.** `encode_image` un `encode_text` atgriež pazīmju vektorus. Izsaukums ar attēlu un tekstiem dod to savstarpējās līdzības vērtības; piemērā teksti ir ievadīti iepriekš, un rezultāts ir šo kandidātu vērtējums. [Dokumentētais piemērs un API](https://github.com/openai/CLIP).

Tas redzams arī `clip/model.py`: teksta kodētājs izveido vektoru, bet `forward` normalizē abu veidu vektorus un atgriež līdzības matricas. Šajā izpildes ceļā nav jauna teikuma tokenu ģenerēšanas posma. Prasītajam brīvajam aprakstam būtu vajadzīga cita vai papildu apmācīta komponente ar teksta dekoderi, tātad dotajā kodu sistēmā `replace_core`. [Modeļa kods](https://github.com/openai/CLIP/blob/main/clip/model.py).

Bibliotēkai var paturēt meklēšanu pēc līdzības. Nākamais izveidojamais posms: saglabāt katra attēla normalizētu `encode_image` vektoru kopā ar faila ceļu, teksta vaicājumu kodēt ar `encode_text` un sarindot attēlus pēc kosinusa līdzības. Tas balstās dokumentētajā vektoru salīdzināšanas mehānismā. [API un normalizēšanas piemērs](https://github.com/openai/CLIP). Rezultātu atbilstība jāpārbauda uz savas bibliotēkas; sākotnējā modeļa kartīte norāda, ka citas valodas ārpus angļu valodas nav mērķtiecīgi apmācītas vai novērtētas. [Modeļa kartīte](https://github.com/openai/CLIP/blob/main/model-card.md).

Šeit izlasīta dokumentācija un attiecīgais kods. Modelis nav palaists, pakotnes nav instalētas un svari nav lejupielādēti.

### evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": false,
    "native_output_kind": "embeddings",
    "action": "replace_core",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "similarity_retrieval"
  },
  "explanation": "Oficiālais CLIP ViT-B/32 kodē ievadītu attēlu un tekstu vektoros. Tā forward atgriež attēlu un ievadīto tekstu līdzības vērtības, bet piemērs aprēķina varbūtības iepriekš norādītiem tekstiem. Šajā modelī un piemērā nav attēla apraksta brīvas ģenerēšanas dekodera. Tādēļ pie dotajiem nosacījumiem pilnu jaunu apraksta teikumu tas nerada.",
  "next_step": "Attēlu bibliotēkai saglabāt katra faila normalizētu encode_image vektoru un faila ceļu; teksta vaicājumu kodēt ar encode_text un sarindot attēlus pēc vektoru kosinusa līdzības. Brīva apraksta teikumam būtu jāizvēlas cita vai papildu apmācīta komponente ar teksta ģenerēšanas dekoderi, tātad jāmaina sākotnējais ierobežojums. Šeit modelis nav izpildīts.",
  "sources": [
    "https://github.com/openai/CLIP",
    "https://github.com/openai/CLIP/blob/main/clip/model.py",
    "https://github.com/openai/CLIP/blob/main/model-card.md",
    "https://github.com/openai/CLIP/blob/main/LICENSE",
    "https://github.com/openai/CLIP/blob/main/requirements.txt"
  ]
}
```



### baseline / IT03-dinov2-retrieval

**Jā, DINOv2 `ViT-S/14` dod izmantojamu attēla reprezentāciju šādai meklēšanai bez jaunas pamatmodeļa apmācības.** Autoru modeļa kartīte tieši min attēlu meklēšanu ar tuvākajiem kaimiņiem; ViT-S vektoram ir 384 elementi. Klašu etiķetes attēlu vektoru savstarpējai sarindošanai nav vajadzīgas. [Modeļa kartīte](https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md).

Avotos ir modeļa kods, svaru saites un `dinov2_vits14` ielādes piemērs. `forward_features` dod globālo `x_norm_clstoken` un lokālās attēla daļu pazīmes; parastais `forward` atgriež globālo reprezentāciju caur `Identity` galvu. [Repozitorijs](https://github.com/facebookresearch/dinov2), [modeļa kods](https://github.com/facebookresearch/dinov2/blob/main/dinov2/models/vision_transformer.py).

Lai iegūtu savas mapes meklētāju, vēl jāizveido šāda apstrāde:

1. Sagatavot lokālu koda un jau lejupielādēto svaru ielādi. Pamatmodeļa ielādes kods pieņem arī svaru ceļu. [Ielādes kods](https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/backbones.py).
2. Visus attēlus apstrādāt vienādi, iegūt globālos vektorus, atsevišķi veikt L2 normalizēšanu un saglabāt vektorus ar failu ceļiem.
3. Iesniegtajam attēlam aprēķināt tādu pašu vektoru, sarindot bibliotēku pēc kosinusa līdzības un atgriezt izvēlēto tuvāko rezultātu skaitu.
4. Pievienot attēla iesniegšanu un rezultātu attēlošanu, pēc tam pārbaudīt atbilstību savos piemēros. Šie ir lietotnes apstrādes posmi ap dokumentēto tuvāko kaimiņu mehānismu. [Modeļa lietojumi](https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md).

Tādēļ izvēle ir `adapt_output`. Rezultātu kvalitāte savā mapē vēl jāpārbauda: projekta lietotājs ziņoja par meklēšanas pasliktināšanos, attēlu apgriežot; tas ir konkrēts pieredzes ziņojums. [Diskusija](https://github.com/facebookresearch/dinov2/issues/103). Šeit inferenci neizpildīju, pakotnes neinstalēju un svarus nelejupielādēju.

### evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": true,
    "native_output_kind": "embeddings",
    "action": "adapt_output",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "similarity_retrieval"
  },
  "explanation": "DINOv2 ViT-S/14 dod 384 elementu attēla reprezentāciju, un autoru modeļa kartīte dokumentē attēlu meklēšanu ar tuvākajiem kaimiņiem bez jaunas pamatmodeļa pielāgošanas. Kodā pieejams globālais x_norm_clstoken un patch pazīmes. Publicētais pamatmodelis ir izmantojama komponente; savai mapei vēl vajag indeksēšanu, līdzības sarindošanu un attēla iesniegšanas saskarni. Šiem posmiem jauns apmācīts pamatmodelis nav nepieciešams.",
  "next_step": "Sagatavot lokālu repozitorija un svaru ielādi. Ar vienādu priekšapstrādi iegūt katra bibliotēkas attēla 384 elementu globālo vektoru, atsevišķi L2 normalizēt to un saglabāt kopā ar faila ceļu. Iesniegtajam attēlam iegūt tādu pašu vektoru, aprēķināt kosinusa līdzību, atlasīt top-k failus un parādīt tos saskarnē. Pirms plašākas lietošanas pārbaudīt atbilstību savas mapes attēlu piemēros, tostarp rotētos attēlos. Šeit izpilde nav veikta.",
  "sources": [
    "https://github.com/facebookresearch/dinov2",
    "https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md",
    "https://github.com/facebookresearch/dinov2/blob/main/dinov2/models/vision_transformer.py",
    "https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/backbones.py"
  ]
}
```



### candidate / IT01-depth-output

### Slēdziens

Mērvienību **m** šā kontrolpunkta izvadam pievienot nedrīkst. `depth-anything/Depth-Anything-V2-Small-hf` dod relatīvu dziļuma karti. Modeļa kartīte to marķē kā relatīvu, un autoru repozitorijs tieši šo Transformers piemēru saista ar relatīvajiem pamata modeļiem. Kartītes plašais teksts par absolūtā dziļuma rezultātiem neapstiprina metru skalu šim kontrolpunktam. 

Komponenti var paturēt attēla apgabalu relatīvam **tuvāk/tālāk kārtojumam**. Adapteris var mainīt kartes izmēru, to attēlot vai nolasīt izvēlēta apgabala vērtības. No šīm darbībām neiegūst trūkstošo fizisko mērogu; arī autors skalas pielāgošanai prasa patiesas metriskas dziļuma vērtības. Tas ir secinājums par dotajiem nosacījumiem, kuros šādu etalonu nav. 

Ja vajadzīgs metriskas dziļuma kartes novērtējums bez paša veiktas apmācības, nākamais solis ir izvēlēties autoru jau publicēto metrisko Small kontrolpunktu: Hypersim telpām vai Virtual KITTI 2 ārtelpām. To piemērs norāda izvadi metros. Tā ir kontrolpunkta maiņa (`replace_core`); precizitāte konkrētajai ainai vēl jāpārbauda. 

Šeit pārbaudīta dokumentācija, konfigurācija un izvades galvas kods. Modelis nav palaists, svari nav lejupielādēti, instalācija nav veikta.

### evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": false,
    "native_output_kind": "relative_depth",
    "action": "replace_core",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "depth_ordering"
  },
  "explanation": "Tieši depth-anything/Depth-Anything-V2-Small-hf dod relatīvu dziļuma karti bez pamatotas metru skalas. Kartītes plašais teksts par absolūtu dziļumu attiecas uz modeļu saimi; autoru repozitorijs nodala relatīvos pamata kontrolpunktus no īpaši pielāgotajiem metriskajiem modeļiem. Interpolācija vai normalizēšana metrisku mērogu nepievieno.",
  "next_step": "Šo kontrolpunktu paturēt relatīvam tuvāk/tālāk kārtojumam. Ja vajadzīgs metriskas dziļuma kartes novērtējums bez paša veiktas apmācības, aizstāt to ar autoru publicēto metrisko Small kontrolpunktu: Hypersim telpām vai Virtual KITTI 2 ārtelpām, un pārbaudīt kļūdu savas ainas apstākļos. Tas maina kontrolpunktu; ar sākotnēji fiksēto Small-hf prasīto funkciju izpildīt nevar.",
  "sources": [
    "https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf",
    "https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf/blob/main/config.json",
    "https://huggingface.co/docs/transformers/model_doc/depth_anything",
    "https://github.com/DepthAnything/Depth-Anything-V2",
    "https://github.com/DepthAnything/Depth-Anything-V2/blob/main/metric_depth/README.md",
    "https://github.com/huggingface/transformers/blob/v5.22.2/src/transformers/models/depth_anything/modeling_depth_anything.py",
    "https://github.com/DepthAnything/Depth-Anything-V2/issues/200",
    "https://github.com/LiheYoung/Depth-Anything/issues/226"
  ]
}
```



### candidate / IT02-clip-generation

### Slēdziens

**Nē.** Oficiālais CLIP `ViT-B/32` ar publicēto piemēru brīvas formas attēla apraksta teikumu nerada. `encode_image` un `encode_text` atgriež pazīmju vektorus, bet `model(image, text)` atgriež attēla un iepriekš ievadīto tekstu līdzības rezultātus. Arī koda `forward` funkcija beidzas ar šiem līdzības tensoriem. Izvades saime ir `embeddings`. 

Ar adapteri var atlasīt piemērotāko jau uzrakstīto teikumu no kandidātu bankas. Tas joprojām izvēlas kādu no dotajiem tekstiem. Ja nepieciešams jauns brīvi veidots apraksts, jāizmanto attēla aprakstu modelis ar apmācītu teksta ģeneratoru vai jāpievieno šāda komponente. Pēc uzdevuma definīcijas tā ir `replace_core` darbība un prasa mainīt sākotnējo ierobežojumu. 

Attēlu bibliotēkai CLIP ir paturams **līdzības meklēšanai**. Nākamais praktiskais solis: ar `encode_image` saglabāt attēlu vektorus kopā ar failu ceļiem, ar `encode_text` kodēt angļu vaicājumu un sakārtot attēlus pēc normalizēto vektoru līdzības. Tas ir adapteris ap esošo modeli, kam nav vajadzīga jauna pamatmodeļa apmācība. Šī ir dokumentēto funkciju izmantošanas rekomendācija; savas kolekcijas rezultāti vēl jāpārbauda. Angļu vaicājums ievēro sākotnējās modeļa kartītes valodas robežu. 

Šeit nolasīta dokumentācija un kods. Modelis nav palaists, nekas nav instalēts un modeļa svari nav lejupielādēti.

### evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": false,
    "native_output_kind": "embeddings",
    "action": "replace_core",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "similarity_retrieval"
  },
  "explanation": "Oficiālais CLIP ViT-B/32 kodē attēlu un jau ievadītu tekstu pazīmju vektoros. model(image, text) atgriež līdzības logits, un piemērs izvēlas starp iepriekš dotām teksta iespējām. encode_text nav teikumu ģenerēšanas dekoderis; brīvas formas jaunu attēla aprakstu šis modelis un piemērs nerada.",
  "next_step": "Brīvas formas aprakstiem vajadzīgs attēla aprakstu modelis ar apmācītu teksta ģeneratoru vai šādas komponentes pievienošana, tātad jāmaina sākotnējais ierobežojums. CLIP paturēt bibliotēkas meklēšanai: ar encode_image izveidot un saglabāt attēlu vektorus kopā ar failu ceļiem, ar encode_text kodēt angļu vaicājumu un sarindot attēlus pēc normalizēto vektoru līdzības. Šim meklēšanas adapterim nav jāapmāca jauns pamatmodelis; rezultātu kvalitāte jāpārbauda savā kolekcijā.",
  "sources": [
    "https://github.com/openai/CLIP",
    "https://github.com/openai/CLIP/blob/main/clip/model.py",
    "https://github.com/openai/CLIP/blob/main/model-card.md",
    "https://github.com/openai/CLIP/blob/main/LICENSE"
  ]
}
```



### candidate / IT03-dinov2-retrieval

### Slēdziens

**Jā.** Publicētais DINOv2 `ViT-S/14` dod šim nolūkam izmantojamu attēla reprezentāciju. Modeļa kartīte norāda 384 dimensiju vektorus un tieši min attēlu meklēšanu ar tuvākajiem kaimiņiem bez papildu pamatmodeļa apmācības. Klašu etiķetes šādam vaicājuma un kolekcijas vektoru salīdzinājumam nav vajadzīgas. 

Gatavi ir modeļa svari un pazīmju iegūšanas kods: `forward_features` atgriež `x_norm_clstoken` un attēla fragmentu pazīmes. Vienkāršai visas bildes meklēšanai sāktu ar CLS vektoru. Gala darbībai jāizveido adapteris, tāpēc izvēle ir **`adapt_output`**. Pamatmodelis nav jāmaina. 

Adaptera nākamie soļi:

1. Vienādi priekšapstrādāt mapes attēlus un vaicājuma attēlu, iegūt CLS vektorus un L2 normalizēt tos.
2. Saglabāt kolekcijas vektorus kopā ar attēlu failu ceļiem.
3. Salīdzināt vaicājuma vektoru ar kolekciju pēc kosinusa līdzības un atgriezt `top-k` rezultātus.
4. Pievienot attēla izvēles un sarindoto rezultātu saskarni.

Šie ir ieteiktie datu apstrādes soļi ap dokumentēto reprezentāciju. Kvalitāte konkrētajā kolekcijā vēl jāpārbauda; modeļa iegūšana pati par sevi nav gatava failu bibliotēkas programma. 

Lokālajam variantam iepriekš jāsagatavo repozitorija kods, atkarības un svaru fails. Pašreizējā `dinov2_vits14` funkcija pieņem `weights` ar vietējā faila ceļu; šis ceļš kodā ir paredzēts ielādei. Modeļa kartīte un apskatītā koda galvene norāda Apache-2.0 licenci. 

Šeit pārbaudīti avoti un kods. Modelis nav palaists, svari nav lejupielādēti un darbība bez tīkla nav praktiski izmēģināta.

### evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": true,
    "native_output_kind": "embeddings",
    "action": "adapt_output",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "similarity_retrieval"
  },
  "explanation": "Publicētais DINOv2 ViT-S/14 dod attēla pazīmju reprezentāciju; modeļa kartīte nosauc 384 dimensiju izvadi un tieši paredz image retrieval ar nearest neighbors bez fine-tuning. forward_features atgriež x_norm_clstoken un patch pazīmes. Klašu etiķetes vai jauna pamatmodeļa apmācība šim meklēšanas ceļam nav vajadzīga, bet publicētais backbone pats nav gatava lietotāja mapes meklēšanas saskarne.",
  "next_step": "Izveidot lokālu adapteri: sagatavot repo kodu, atkarības un ViT-S/14 svaru failu; dinov2_vits14 ielādēt ar weights norādi uz vietējo failu. Vienādi priekšapstrādāt kolekciju un vaicājumu, izvilkt x_norm_clstoken, L2 normalizēt vektorus, saglabāt tos ar failu ceļiem, aprēķināt kosinusa līdzību un atgriezt top-k attēlus. Pievienot attēla izvēles un rezultātu saskarni; kvalitāti pārbaudīt uz savas kolekcijas. Pamatmodelis nav jāmaina.",
  "sources": [
    "https://github.com/facebookresearch/dinov2",
    "https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md",
    "https://github.com/facebookresearch/dinov2/blob/main/dinov2/models/vision_transformer.py",
    "https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/backbones.py",
    "https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/utils.py"
  ]
}
```


<a id="findings"></a>

## Publicētie rezultāti un to robežas

Gala izpētes kopā ir 10 ikdienas jautājumi, 10 vidēji sarežģīti jautājumi dažādās nozarēs un 10 sarežģīti jautājumi. Tajā saglabāti 12 agrākie gadījumi un pievienoti 18 jauni; kopā ar vēsturisko atlasi tie veido 48 atšķirīgus pamatuzdevumus. Septiņos jaunajos sarežģītajos gadījumos ir pilns matemātisks pierādījums vai atvasinājums un faktiski palaists aprēķins. Abas 30 gadījumu kopas ir pilnībā pieejamas angļu un latviešu valodā.

Atsevišķais meklēšanas stratēģijas izmēģinājums **nepierādīja precizitātes uzlabojumu**. Kandidāts netika pieņemts par jauno pamatmetodi, un saglabātais lēmums ir `no_gain`.

### Trīs uzdevumu salīdzinājums

Kandidāts vispirms pārbaudīja visvājāk pamatoto nepieciešamo nosacījumu, kas var mainīt lēmumu. Uzdevumi bija par konkrēta Depth Anything kontrolpunkta izvades mērvienībām, CLIP spēju radīt jaunu apraksta teikumu un DINOv2 izmantošanu attēlu līdzības meklēšanai. Visas sešas izpētes atbildes ar publiskajām avotu saitēm saglabātas [angliski](validation/2026-11-09-beta3/comparison/answers.en.md) un [latviski](validation/2026-11-09-beta3/comparison/answers.lv.md).

| Ziņotais rādītājs | Esošā metode | Kandidāts |
|---|---:|---:|
| Faktu un izpildes godīguma pārbaudes | 9/9 | 9/9 |
| Nākamās darbības kategorija | 3/3 | 3/3 |
| Dokumentēts lietderīgs komponentes izmantojums | 3/3 | 3/3 |
| Pamatojuma un nākamā soļa lauki | 6/6 | 6/6 |
| Meklēšanas vaicājumi | 15 | 15 |
| Lasījumi, ieskaitot neveiksmīgos | 32 | 28 |
| Tīmekļa darbības kopā | 47 | 43 |
| Laiku summa no pirmā tīmekļa pieprasījuma līdz rezultātu failu pabeigšanai | 456,14 sekundes | 495,50 sekundes |

Precizitātes pieaugums šajās pārbaudēs bija nulle. Četru tīmekļa darbību ietaupījums neizpildīja iepriekš fiksēto precizitātes pieauguma prasību, un kandidāta kopējais laiks bija lielāks. Pēc rezultātu iegūšanas pieņemšanas mērķis netika mainīts. Agrāk norādītie, citādi definētie 461,75 un 569,59 sekunžu rādītāji nav tieši salīdzināms ātruma mērījums.

Tas bija izmēģinājums ar trim sagatavotiem uzdevumiem un vienu atbildi katrai pusei. Abi konteksti izmantoja kopīgu failu sistēmu ar norāžu robežu; operētājsistēmas līmeņa izolācijas nebija. Modeļa identitāti deklarēja izpildvide. Uzdevumu veidotājs sagatavoja arī sākotnējās etalonatbildes pēc kandidāta fiksēšanas; pirms izmēģinājuma tās pārbaudīja pirmavotos. Abas puses sāka ar apmēram sešu minūšu nobīdi. Šie nosacījumi nepamato statistiska vai universāla pārākuma apgalvojumu. Salīdzinājumā modeļu inference netika palaista un modeļu svari netika lejupielādēti.

### Izpētes tvērums un labojumi

Gala 30 gadījumiem ziņoti 156 izpildīti vaicājumi. Katram gadījumam meklēts angliski, vāciski, ķīniski un japāniski. Vaicājums kādā valodā nepierāda, ka šajā valodā atrasts un izlasīts secinājumu atbalstošs pirmavots. Piekļuves kļūmes un ierobežoti avotu lasījumi atbildēs paliek norādīti.

Sākotnējās atlases vidējā grupa bija pārāk koncentrēta uz IT, bet sarežģītajā grupā trūka pabeigtu augstākās matemātikas uzdevumu. Jaunā atlase novērš šos trūkumus, saglabājot agrākās atbildes. Vēsturiskajā kopskaitā 147 bija iekļauti četri deklarēti E10 vaicājumi, kuru pilnā sākotnējā izvade nav saglabājusies. Pamatotais vēsturiskais skaits ir 143 dažādi vaicājumi ar saglabātām kvītīm; trūkstošās kvītis nav izgatavotas no jauna un uzdotas par sākotnējiem pierādījumiem.

Jautājumi veidoti pārbaudei, un simulētie precizējumi ir marķēti. Katram piemēram galveno izpēti veica viens aģents, pēc tam notika ziņotās pārskatīšanas. Šis kopums neapliecina četru neatkarīgu aģentu meklēšanu katrā gadījumā. Matemātiskie argumenti izlasīti un salīdzināti ar saglabātajiem aprēķiniem; formāla pierādījumu asistenta sertifikācija nav apgalvota. [Laidiena ziņojumā](validation/2026-11-09-beta3/release-report.lv.md) saglabāti rezultāti un to nosacījumi.

### Kas uzlabots programmā

Ziņotajā laidiena pārbaudē izpildīti 82 programmas testi. Izlabotas divas reproducētas kļūmes: agrāka mācību kartīte varēja aizsegt jaunāku pretrunīgu novērojumu, savukārt nesaistīts pierādījumu objekts pie atmiņas robežas varēja neļaut saglabāt atmiņas atbrīvošanas rezultātu. Pašreizējais pirmkods, testi, aprēķinu programmas un to izvades ir iekļautas, lai lasītāji tās varētu pārbaudīt un palaist. Programmas mehānisma testi nepierāda augstāku meklēšanas precizitāti.

Visi 18 jaunie pamatuzdevumi noslēdza reģistrētu mācību ciklu, un 15 vēlākie uzdevumi ielādēja agrākās mācības. Šīs darbības vadīja čats. Pieredzes ielāde nepierāda, ka katra nākamā atbilde kļūst labāka vai ka darbojas patstāvīgs fona pakalpojums. Atsevišķā divu uzdevumu izpildes demonstrācija šeit aprakstīta tikai ar tās ziņoto rezultātu: nākamais uzdevums ielādēja saglabātu mācību. Tās iekšējie izpildes ieraksti nav iekļauti.

Noderīgie labojumi un kompaktās mācības saglabātas. Priekšnosacījuma prioritizēšanas kandidāts netika ieviests. Mācību atbilstība, izmēģinājums ar izmaksu mērķi un vairāku meklēšanas valodu papildu ieguvums paliek hipotēzes, kurām vajadzīgi jauni uzdevumi un iepriekš fiksēti pieņemšanas kritēriji.

### Kas ir publicēts

Šis ir autorēts rezultātu pārskats. Pilnas vērtētāju izvades, norāžu momentuzņēmumi, izpildes ieraksti, atmiņas momentuzņēmumi, neapstrādātie žurnāli, rīku vaicājumu izdrukas un iekšējās kvītis nav iekļautas ne kā atsevišķi faili, ne kā kopijas kopējā eksperimentu ziņojumā. Šie izlaidumi ierobežo iespēju neatkarīgi rekonstruēt sākotnējo izpildes vadību. Pilnās izpētes atbildes, matemātiskie argumenti, aprēķinu kods, ziņotais negatīvais rezultāts un norādītās robežas paliek pieejamas.

Lasāms [publikācijas tvērums](PUBLICATION_SCOPE.md), [izpētes un eksperimentu ziņojums angliski](EXPERIMENTS.md) un [ziņojums latviski](EXPERIMENTS.lv.md). [Failu manifests](file-manifest.json) norāda šā izdevuma precīzos failus. Publikācija nesniedz pretvīrusu sertifikātu, vispārēju izpētes kvalitātes garantiju vai apgalvojumu par pastāvīgi strādājošu uzlabošanās pakalpojumu.


<a id="cosmetics"></a>

## Ievada piemērs par kosmētiku

> Nu man tā seja spīd, bet tas tonis kaut kā saiet rievās... Gribu smuki, lai nav tā maska, nezinu, ko pirkt?

Izklausās, ka gribas vienmērīgāku sejas toni, mazāk spīduma un plānu klājumu, kurā āda joprojām izskatās dabiski. **Es sāktu ar esošā tonālā plānāku uzklāšanu, pirms pirkt jaunu.** No šī apraksta vēl nevaru pateikt, vai galvenais klupšanas akmens ir pats produkts, tā daudzums vai tas, kas uzklāts zem tā.

#### Vispirms izmēģini šo

Nākamreiz pārbaudei paņem aptuveni pusi ierastā tonālā daudzuma. Klāj tikai tur, kur gribas izlīdzināt toni, un papildu sedzošo kārtiņu pievieno konkrētam laukumiņam. Vietās, kur produkts sakrājas rieviņās, atstāj īpaši plānu kārtu. Mazāk produkta un plānas kārtas iesaka arī L’Oréal grima speciālisti; tā ir lietošanas metode, ne garantija katrai sejai. [Avots](https://www.loreal-paris.de/tipps-und-trends/make-up/welches-make-up-bei-falten-tipps)

Kad parādās spīdums, viegli piespied tīru papīra salveti vai matējošo lapiņu. Neberzē. Tikai pēc tam, ja vajag, uzliec mazliet pūdera uz spīdīgās vietas. Šādu secību apraksta Shiseido grima konsultante; arī Amerikas Dermatoloģijas akadēmija iesaka lieko taukainumu nosusināt ar vieglu piespiešanu. [Shiseido](https://corp.shiseido.com/slqm/jp/information/information_251203.html) · [AAD](https://www.aad.org/public/everyday-care/skin-care-basics/dry/oily-skin)

#### Ja tomēr jāpērk — trīs saprotami varianti

- **Esošais tonālais un matējošās lapiņas.** Izvēlētos, ja tonis un klājums sākumā patīk, bet vēlāk seja spīd. Pluss: nav jāpērk vēl viena tonālā pudelīte. Mīnuss: lapiņas pašas neatrisina produkta sakrāšanos rieviņās, un dienas gaitā tās var vajadzēt atkārtoti. [AAD](https://www.aad.org/public/everyday-care/skin-care-basics/dry/oily-skin)
- **Viegli tonējošs līdzeklis jeb “skin tint”.** Izvēlētos, ja galvenais ir mazināt maskas iespaidu un pietiek ar daļēju segumu. Piemērs ir **Maybelline Super Stay Skin Tint**: ražotājs norāda vieglu līdz vidēju segumu. Kompromiss — tas arī sola mirdzumu, tāpēc būtu mazāk loģisks pirmais mēģinājums, ja tieši spīdums traucē visvairāk. [Ražotāja apraksts](https://www.maybelline.de/alle-produkte/gesichts-make-up/foundation/super-stay-24h-skin-tint)
- **Viegli vai vidēji sedzošs matēts tonālais.** Izvēlētos, ja gribas gan izlīdzināt toni, gan mazināt spīdumu. Piemērs ir **Maybelline Fit Me Matte + Poreless**, ko ražotājs raksturo šādi. Kompromiss — matēts finišs var izcelt sausākas vietas un rieviņas; vairāk produkta to ne vienmēr izlabos. [Produkta apraksts](https://www.maybelline.de/alle-produkte/gesichts-make-up/foundation/fit-me-matte-poreless-makeup) · [L’Oréal lietošanas padomi](https://www.loreal-paris.de/tipps-und-trends/make-up/welches-make-up-bei-falten-tipps)

Abi nosaukumi ir kategoriju piemēri pēc ražotāju aprakstiem, ne salīdzinošā testā noteikti uzvarētāji. Konkrēto toni vēl nevaru piemeklēt. Pirms pilnas pudelītes pirkšanas noderētu paraudziņš, ja tas pieejams.

**Kurš tonālais tev pašlaik ir — vari atsūtīt nosaukumu vai iepakojuma foto?**


<a id="gaming"></a>

## Ievada piemērs par spēļu tehnoloģijām

**Wallhack un aimbot apraksta iegūto priekšrocību; DMA apraksta piekļuves mehānismu.** Vienā sistēmā šīs lietas var būt apvienotas. Tāpēc uzraksts “DMA aimbot” vēl neko nepasaka par kvalitāti, drošumu vai to, vai demonstrācija vispār ir īsta.

### Trīs atšķirīgas lietas

**Wallhack un plašākais ESP** izmanto informāciju, kuru spēle spēlētājam parasti neparāda: pretinieka atrašanās vietu, kontūru vai citus datus. Tā var būt atmiņā pieejamas informācijas attēlošana atsevišķā slānī vai izmaiņas attēlošanā. Būtiska robeža: ja serveris klientam slēpto pozīciju vispār nenosūta, atmiņas lasīšana to neuzburs. Riot apraksta tieši šādu *Fog of War* pieeju; praksē jāņem vērā arī redzamības maiņa un aizture. [Riot tehniskais skaidrojums](https://www.riotgames.com/en/news/demolishing-wallhacks-valorants-fog-war)

**Aimbot** automatizē mērķēšanas darbību. Vieni varianti izmanto spēles datus, citi analizē redzamos ekrāna pikseļus ar datorredzi un pēc tiem koriģē vadību. “AI” var nozīmēt reālu atpazīšanas modeli, bet var būt arī reklāmas uzlīme. Ekrāna analīze pati neredz cauri sienai; tā arī neatceļ iespēju analizēt rezultātā radušos spēlētāja uzvedību. Pētījums *GAN-Aimbots* aplūko gan šīs pieejas, gan uzvedības atdarināšanu; tā eksperimenta iznākums nav garantija visām spēlēm. [Pētījums, 2022](https://arxiv.org/html/2205.07060v1)

**DMA — Direct Memory Access** ir aparatūras tiešā piekļuve atmiņai, ko normāli izmanto arī derīgas ierīces. Negodīgā sistēmā to mēģina izmantot spēles datu iegūšanai. Tā nav “neredzamības karte”: IOMMU ierobežo, kurām atmiņas zonām ierīce drīkst piekļūt. Rezultāts atkarīgs no aparatūras, programmaparatūras un aizsardzības darbības. Microsoft dokumentācija skaidri nošķir Windows aizsardzību pēc sistēmas ielādes no aizsardzības sāknēšanas laikā. [Microsoft](https://learn.microsoft.com/de-de/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt)

### Kas to izstrādā un ko dara anticheat?

Lietderīgi nošķirt autoru, pielāgotāju, pārdevēju un pētnieku. Autors izprot spēles datu plūsmu; citam darbs ir grafika, ievades automatizācija vai draiveri. Pārdevējs var tirgot cita darbu. Savukārt pētnieki līdzīgus mehānismus pēta, lai pārbaudītu aizsardzību. Tās ir dažādas lomas: tehnisks video nepierāda ne autorību, ne uzticamību.

Anticheat parasti veido vairākus slāņus: spēles un sistēmas integritātes pārbaudes, piekļuves uzraudzību, servera noteikumu pārbaudes un uzvedības analīzi. Kodola draiveris dod citu redzamību nekā parasta programma, tomēr nav visu problēmu atrisinājums. Arhitektūras atšķiras: Epic aprakstītajā EAC Linux v2 paredzēts izmantot platformas aizsardzību un eBPF bez sava anticheat kodola moduļa. [Epic arhitektūra](https://onlineservices.epicgames.com/news/introducing-easy-anti-cheat-linux-v2?lang=ja)

**Servera autoritāte** nozīmē, ka serveris pieņem galīgo lēmumu par spēles stāvokli. Taču arī serverim jāizvērtē klienta pieprasījumi; centrālais serveris pats par sevi nenovērš liekas informācijas nosūtīšanu vai automatizētu mērķēšanu. [Unreal tīkla modelis](https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-overview-for-unreal-engine)

**Pašziņota izstrādātāju pieredze:** Inferna Studio raksta, ka pašu anticheat kļūdaini bloķējis izstrādātāja kontu. Tas ir konkrēts autora stāsts, ne neatkarīgi pārbaudīts tests vai kļūdainu banu biežuma mērījums. Tas palīdz saprast, kādēļ aizdomīgs signāls un pierādīta krāpšanās nav sinonīmi. [Pieredzes apraksts](https://infernastudio.com/articles/our-anti-cheat-banned-a-player-it-was-us)

### Kur mācīties un kam neticēt?

Tehniskiem jautājumiem noder [Reverse Engineering Stack Exchange](https://reverseengineering.stackexchange.com/tour), Ghidra projekta diskusijas un spēļu dzinēju izstrādātāju dokumentācija. **Ghidra** palīdz pētīt kompilētu kodu; **debuggeri**, piemēram, WinDbg, ļauj apskatīt savas programmas izpildi, atmiņu un reģistrus. Tie ir vispārīgi izpētes rīki. [Ghidra](https://github.com/NationalSecurityAgency/ghidra) · [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/)

Vērtējot apgalvojumu, prasītu trīs lietas:

- **Ko tieši demonstrē?** Versija, vide, ievade, pilns rezultāts un zināmie ierobežojumi ir vērtīgāki par atlasītu uzvaru montāžu.
- **Vai apgalvojums ir pārbaudāms?** “Nekad nenosakāms”, “strādā visur” un “AI, tāpēc drošs” nav tehniski pierādījumi.
- **Vai avoti sakrīt?** Repozitorija vēsture, autora skaidrojums un atkārtojama demonstrācija palīdz pārbaudīt izcelsmi. Atsauksmju skaits vai prasība izslēgt aizsardzību paši par sevi uzticamību neapliecina.

**Labs nākamais solis:** savā Unity vai Unreal bezsaistes ainā izveidot divus tēlus un sienu, ieslēgt izstrādātāja diagnostikas attēlojumu un salīdzināt “dati pastāv” ar “objekts ir redzams”. Pēc tam savā lokālā klienta/servera piemērā pārbaudīt, kuri dati tiek nosūtīti. Tā kļūst saprotama problēmas sakne un aizsardzības jēga.


<a id="architecture"></a>

## Ievada piemērs par aģenta arhitektūru

Pārbaudīts 2026. gada 9. novembrī. Šis ir reālas izpētes rezultāts un pārbaudāms arhitektūras priekšlikums; ārējie projekti šajā piemērā nav instalēti vai izmērīti.

### Jautājums

“Kā uzbūvēt lokālu MI aģentu, kas nemaina modeļa svarus, saglabā mazu pieredzes bibliotēku un uzlabo gan savas darbības, gan paņēmienu, ar kuru izvēlas, ko no pieredzes mācīties?”

### Atbilde

**Es sāktu ar gatavu atmiņas un prasmju pamatu un izmēģinātu vienu papildinājumu: pārbaudīt, vai konkrētā atmiņa patiešām uzlabo nākamo lēmumu.** Atmiņā ierakstīts padoms vēl nepierāda, ka modelis to saprata vai izmantoja pareizajā situācijā.

Šis ir perspektīvs virziens, taču nebūtu pamatoti teikt, ka neviens to nav realizējis. MemEvolve jau pēta gan aģenta pieredzes, gan pašas atmiņas arhitektūras attīstīšanu. EvolveLab sadala to četrās maināmās darbībās: pieredzes pārveidošana, glabāšana, atrašana un pārvaldība. Tas dod konkrētu pētniecības pamatu mūsu iecerei. [Pētījums](https://proceedings.mlr.press/v306/zhang26fa.html)

#### Ko var izmantot jau tagad

| Pamats | Kāpēc tas ir interesants | Kas jāpārbauda pirms izvēles |
|---|---|---|
| **ReMe** | Failos glabāta, atlasāma atmiņa; dokumentācijā aprakstīta arī Hermes integrācija. Sākotnējai teksta meklēšanai nav obligāts atsevišķs iegultņu modelis. | Konkrētā Hermes versija, automatizācijas modeļa izmaksas un vai izvēlētajā konfigurācijā izdodas mūsu atmiņas robeža. |
| **Memento-Skills** | Gatavs projekts, kura darba kārtībā ietilpst prasmju izvēle, izpilde, kļūdu izvērtēšana un prasmju pārrakstīšana, saglabājot pamatmodeli nemainīgu. | Cik labi šis cikls darbojas ar mūsu modeli un uzdevumiem; projekta demonstrācijas neatbild uz to mūsu vietā. |
| **MemEvolve / EvolveLab** | Vistiešākais pamats eksperimentiem, kuros mainās arī pieredzes atlasīšanas un pārvaldības metode. | Pētniecības koda integrācija, konkrētais modulis un tā atkarības; tas nav šeit pārbaudīts ikdienas aģents. |

[ReMe pirmavots](https://reme.agentscope.io/zh/overview) · [Memento-Skills autoru apraksts](https://www.memento.run/research/skills/) · [MemEvolve kods](https://github.com/bingreeky/MemEvolve)

Šo projektu repozitoriji norāda Apache-2.0 licenci; pārņemot atsevišķus failus, atkarību, modeļu un datu tiesības jāpārbauda atsevišķi. Šajā izvērtējumā izlasīta dokumentācija un repozitoriju apraksti, ne reproducēti to rezultāti.

#### Kādu papildinājumu būtu vērts izmēģināt

Mans priekšlikums ir **īsu pieredzes kartīšu bibliotēka ar piemērošanas nosacījumiem un pārbaudītu atlases kārtību**. Tā nav pretenzija uz pasaulē pirmu arhitektūru. Mūsu pārbaudāmais mērķis būtu mazāk atkārtotu kļūdu pie ierobežota glabāšanas un meklēšanas budžeta.

Kartīte saturētu situāciju, darbību, iznākumu, pierādījuma adresi un nosacījumu, kad padoms neder. Piemēram: “Ja meklētāja fragments un projekta fails atšķiras, pārbaudi konkrēto pašreizējo failu. No dokumentācijas vien nesecini, ka funkcija uz tava datora darbojas.”

Pirms darba aģents saņemtu tikai attiecīgās kartītes. Pēc darba tas saglabātu vienu būtisku mācību vai pamatotu secinājumu, ka jauna mācība nav iegūta. Atsevišķā pārbaudē salīdzinātu trīs variantus: bez kartītēm, ar pašreizējo atlasi un ar jauno atlasi. Tā var nošķirt bibliotēkas ieguvumu no paša modeļa spējas jau tāpat atrisināt jautājumu.

Šādas pārbaudes vajadzību pastiprina pētījums “Large Language Model Agents Are Not Always Faithful Self-Evolvers”: tā autori novēroja, ka modeļi mēdz ignorēt vai nepareizi interpretēt saīsinātu pieredzi. Tas nepierāda, ka īsa atmiņa neder; tas liek pārbaudīt, vai saīsinājumā saglabājies lēmumam vajadzīgais. [Pētījums](https://arxiv.org/abs/2601.22436)

Arī praktiska pieredze dod konkrētu norādi: amtr autors pēc 24 konteksta saīsināšanas paaudzēm apraksta problēmu, ka darba hipotēze pārtop šķietami apstiprinātā secinājumā. Viņa pielāgojums — kopā saglabāt pārbaudīto un vēl nepārbaudīto. Tas ir autora paša novērojums, ne vispārējas efektivitātes pierādījums. [Autora pieredze un saite uz kodu](https://zenn.dev/naoto256/articles/amtr-working-memory)

#### Kad sintēze būtu izdevīgāka par gatavo

Vispirms salīdzinātu ar ReMe vai Memento-Skills konfigurāciju, kurai dots tāds pats modelis, rīki, atmiņas budžets un pielāgošanas darbs. Ja mūsu prasību var izpildīt ar nelielu gatavā projekta iestatījumu, izvēlētos to.

Piedāvāju sākuma pārbaudi ar 24 iepriekš neizmantotiem uzdevumiem, kuros ir arī nepiemērotas un novecojušas mācības. Pirms rezultātu redzēšanas noteiktu, piemēram, šādu mērķi: vismaz par 20% mazāk atkārtotu kļūdu, neviena jauna kritiska kļūda un nepieaugošs meklēšanas darbību skaits. Atsevišķs lasītājs pārbaudītu, vai ieteikums, pamatojums un nākamā darbība ir saprotami. **20% ir piedāvāts lēmuma slieksnis, ne sasniegts rezultāts.** Mazais tests palīdzētu izlemt par turpināšanu, ne pierādītu universālu pārākumu.

Plānošanas aplēse: 12–24 darba stundas nelielam savienotājam, 16–32 stundas uzdevumu un vērtēšanas sagatavošanai, 12–24 stundas kļūdu labošanai un atkārtojamai demonstrācijai — kopā 40–80 stundas, aptuveni 1–2 nedēļas vienam izstrādātājam ar gatavu vidi. Trīs varianti reiz 24 uzdevumi ir 72 aģenta uzdevumu izpildes, ne 72 atsevišķi modeļa pieprasījumi. Faktiskais modeļa izsaukumu skaits un ilgums vispirms jāmēra mazā izmēģinājumā.

Elektrību aprēķinātu kā izmērīto visa datora vidējo jaudu kW reiz aktīvās stundas; cenu — pēc konkrētā tarifa vai faktiski izmantotā pakalpojuma. Šīs vērtības šeit nav izmērītas. Regulārai uzturēšanai sākotnēji rezervētu 2–4 stundas nedēļā, līdz kļūst zināms atkarību un kļūdu biežums.

**Lēmums: ir pamats ierobežotam salīdzinošam eksperimentam. Vēl nav pamata solīt, ka mūsu sintēze pārspēs gatavos risinājumus vai ka tā jau darbojas autonomi.**
