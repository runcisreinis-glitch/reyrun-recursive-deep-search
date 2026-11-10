# REYRUN Recursive Deep Search — pārbaudes un attīstības ziņojums

**Laidiens 2.0.0-beta.3 · izpēte 2026. gada 9. novembrī.**

Gala pārbaudē ir 10 ikdienas jautājumi, 10 vidēji sarežģīti jautājumi dažādās nozarēs un 10 sarežģīti uzdevumi. Septiņos jaunajos sarežģītajos uzdevumos ir pilns matemātisks pierādījums vai atvasinājums un faktiski palaists aprēķins. Izlabotas divas reproducētas mācību atmiņas kļūmes; pārbaudītajam kodam izpildīti 82 testi. Atsevišķais jaunās meklēšanas stratēģijas izmēģinājums deva godīgu **no_gain** rezultātu: kandidāts nekļuva par jauno pamatmetodi.

[Pilnās 30 atbildes](30-examples.lv.md) · [Kompaktās mācības](../../references/observed-lessons.md).

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](../../PUBLICATION_SCOPE.md).

## 1. Kāpēc atlase tika pārveidota

Sākotnējie 30 pētījumi bija reāli veikti, taču neatkarīgais audits konstatēja, ka vidējā grupa bija pārāk koncentrēta uz IT un grūtajā grupā trūka izpildītu augstākās matemātikas uzdevumu. Gala atlasē saglabāti 12 piemērotie gadījumi un pievienoti 18 jauni. Sākotnējās atbildes saglabātas pilnībā ar norādītiem redakcionāliem labojumiem: [vēsturiskais izdevums](../2026-11-09/30-examples.lv.md) paliek pieejams. Kopā ir 48 atšķirīgi pamatuzdevumi; trīs salīdzinājuma uzdevumi uzskaitīti atsevišķi.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](../../PUBLICATION_SCOPE.md).

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

## 2. Ko nozīmē atbilžu pārbaude

Katram gadījumam saglabāta atbilde, avoti, apgalvojumu saites un sākotnējā faila SHA-256. Jaunajiem aprēķiniem saglabāts arī kods un tā izvade. Root neatkarīgi izlasīja visus septiņus jaunā autora matemātikas pierādījumus, pārbaudīja argumentu un saglabāto skaitlisko rezultātu saskaņu. Tas nav formāls pierādījumu asistenta sertifikāts. Iekšējais matemātikas pārskats šajā izdevumā nav publicēts.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](../../PUBLICATION_SCOPE.md).

Pamata izpēti katram piemēram veica viens aģents, pēc tam notika norādītā neatkarīgā pārskatīšana. Šis kopums neapliecina četrus neatkarīgus aģentus katra jautājuma formulēšanas un meklēšanas posmā; četru atsevišķu perspektīvu pieņemšanas audits faktiski izpildīts tālāk aprakstītajam stratēģijas salīdzinājumam.

Septiņām nozares atbildēm neatkarīgi pārbaudīta aprēķinu un secinājumu loģika. Papildu atsevišķs aģents pārbaudīja četras jaunās ikdienas atbildes un vēsturiskās adreses/loga gadījumus pret saglabātajiem pirmavotu fragmentiem; aprēķinus tas arī atkārtoja. Nav apgalvots, ka visi ārējie avoti katrā auditā no jauna atvērti tīmeklī. Iekšējais nozaru pārskats un sešu atbilžu audits šajā izdevumā nav publicēti.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](../../PUBLICATION_SCOPE.md).

Publiskajam izdevumam pielāgots matemātikas noformējums un citātu saites. NE02 izlabotas atstarpes; NP04 divdomīgais atvērums precizēts uz “Kasetne, kurā ir tikai aktīvā ogle...”. Sākotnējie pētniecības ieraksti glabājas atsevišķi. Redakcija, 2026. gada 10. novembris: publiskajās atbildēs veikti arī norādītie gramatikas, pieturzīmju, atstarpju un pieraksta labojumi, saglabājot izpētes nozīmi, nosacījumus un rezultātus. Pašreizējais failu manifests identificē rediģēto publikāciju.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](../../PUBLICATION_SCOPE.md).

## 3. Mācības starp meklēšanas reizēm

Visi 18 jaunie pamatuzdevumi noslēgti ar faktisku sākuma/beigu ierakstu. Trīs tematiskās sērijas sāka ar tukšu testa atmiņu; **15 turpmākie uzdevumi ielādēja agrāk saglabātas mācības**. To identifikatori un aģenta norāde par izmantošanu vai neattiecināmību ir cikla pierādījumā. Piemēram, daudzuma un mērvienības nošķiršana pārnesta no miltiem uz krāsu un sausiem/vārītiem rīsiem; glāžu materiāla gadījumā iepriekšējās skaitliskās mācības atzīmētas kā neattiecināmas.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](../../PUBLICATION_SCOPE.md).

Šos sākuma/beigu soļus vadīja čats. Četrpadsmit jaunajām nozares un matemātikas atbildēm papildus izpildīts stingrais failu/atsauču pārbaudītājs. Tas nav pierādījums, ka šīs 18 izpētes startēja automātisks fona pakalpojums. Iepriekš saglabātā divu darbu demonstrācija caur stingro savienotāju apliecina atsevišķu reālu savienotāja darbu un nākamā uzdevuma mācības ielādi.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](../../PUBLICATION_SCOPE.md).

Pastāvīgais cikls ir izpildāms: ielādēt saistītās mācības → veikt uzdevumu → saglabāt noderīgo, neveiksmes un neskaidro → izpētīt konkrētu uzlabojuma hipotēzi → salīdzināt ar esošo metodi → pieņemt tikai izpildītu kritēriju gadījumā. Mācību ielāde pati par sevi nepierāda katras nākamās atbildes kvalitātes pieaugumu. Šajā laidienā pārbaudītas abas atšķirīgās lietas: atmiņas darbība un atsevišķa kandidāta atlase.

## 4. Divi izmērīti programmas uzlabojumi

| Kļūme pirms labojuma | Ko mainīja | Faktiskā pārbaude |
| --- | --- | --- |
| Agrāka mācību kartīte varēja aizsegt vēlāk saglabātu pretrunīgu neveiksmi. | Novērojumiem un kartītēm tagad ir viena hronoloģiska 16 ierakstu atlase. | Nākamais sākuma ieraksts satur arī jaunāko neveiksmes tekstu. |
| Pie 5 MiB robežas pēc neveiksmīga ieraksta palicis nesaistīts pierādījuma objekts neļāva saglabāt pat atmiņas atbrīvošanas rezultātu. | No precīzi apstiprinātā atbrīvošanas plāna pirms atomiskās saglabāšanas dzēš tikai jau nesaistītos objektus; vēl lietotos pierādījumus saglabā līdz sekmīgai stāvokļa nomaiņai. | Pie 5 242 680 aizņemtiem baitiem un 200 brīviem baitiem atbrīvošana sekmīgi atstāja 4806 baitus. Atsevišķs ievadītas rakstīšanas kļūmes tests saglabāja agrāko stāvokli un tā pierādījumus. |

Iekšējos ierakstos ir rezultāti pirms un pēc labojuma, regresiju pārbaude, 82 testu kvīts un pilnais testu žurnāls. Tie ir skaidri marķēti sintētiski mehānisma testi. Tie nepārvērš programmas kļūmes labojumu par pierādītu meklēšanas precizitātes pieaugumu.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](../../PUBLICATION_SCOPE.md).

## 5. Atsevišķais meklēšanas paņēmiena salīdzinājums

Kandidāts pievienoja vienu paņēmienu: vispirms pārbaudīt visvājāk pamatoto nepieciešamo nosacījumu, kas var mainīt lēmumu. Ideja iegūta ar apgalvojuma/pierādījuma argumentācijas pārnesi; atsevišķa mērvienību tipēšanas ideja atlikta, lai nesajauktu divas izmaiņas vienā izmēģinājumā.

Pirms abu pušu izpildes fiksēti kritēriji un budžets, trīs uzdevumi un pareizības pārbaudes, esošā politika un kandidāts. Pamatprasme baseline pusē netika vājināta. Puses veica divi svaigi aģentu konteksti ar vienādu deklarēto modeļa konfigurāciju, uzdevumu secību un ierobežojumu: ne vairāk par 16 tīmekļa darbībām, 8 vaicājumiem, 12 lasījumiem un 12 minūtēm katram uzdevumam. Arī kļūdains pieprasījums skaitās darbība.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](../../PUBLICATION_SCOPE.md).

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

Trīs jaunu uzdevumu salīdzinājumā abi paņēmieni izpildīja visus iepriekš fiksētos atbilžu kritērijus. Kandidāts izmantoja 43 tīmekļa darbības pret esošās metodes 47, bet nesasniedza prasīto precizitātes pieaugumu; tas netika ieviests kā jaunā pamatmetode. Tas ir **no_gain**, ne apgalvojums, ka kandidāts ir sliktāks visos lietojumos. Četru darbību ietaupījums ir novērojums šajā vienā pilotā; kandidāta darbu laiku summa vienlaikus bija lielāka. Tabulas laiku auditors vienādi pārrēķināja no pirmā reālā pieprasījuma līdz artefaktu pabeigšanai. Autoru pašu atšķirīgi definētie 461,75 un 569,59 sekunžu rādītāji saglabāti atsevišķi; tie nav tiešs ātruma salīdzinājums. Kritērijus pēc rezultātu ieraudzīšanas nepārslēdza uz izmaksām. Automātiskā izvērtējuma rezultāts un visu sešu darbu reģistrs šajā izdevumā nav publicēti; pieejamas [pilnās atbildes](comparison/answers.lv.md).

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](../../PUBLICATION_SCOPE.md).

Četri dažādi, nevienas puses atbildes nerakstījuši aģenti sniedza optimistisko, skeptisko, konservatīvo un inovatīvo pārskatu. Tie nav četri viena aģenta izdomāti viedokļi. Klātbūtnes lauku pārbaude nav cilvēku lasāmības pētījums; “inovācijas” skaitlis šeit vērtē dokumentētu lietderīgu komponentes izmantojumu, ne vēsturisku jaunatklājumu.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](../../PUBLICATION_SCOPE.md).

Izmēģinājuma robežas: tikai trīs veidoti uzdevumi un viena atbilde katrai pusei; kopīga failu sistēma ar instrukciju robežu, ne OS izolācija; modeļa identitāte ir vides deklarācija. Dizainers sagatavoja arī sākotnējo pareizo atbilžu etalonu pēc kandidāta fiksēšanas; root to neatkarīgi pārbaudīja pirmavotos un fiksēja pirms izpildes. Puses slotu pieejamības dēļ sāka ar apmēram sešu minūšu nobīdi. Šīs robežas neļauj apgalvot statistisku vai universālu pārākumu.

Baseline pabeigšanas ievadē bija shēmas kļūda: mācības atsauču sarakstā iedoti četri faili atļauto trīs vietā. Kontrolieris saglabāja noraidījumu un atsevišķus labojumu ierakstus, samazinot tikai šo atsauču sarakstu. Visas četras novērojuma pierādījumu atsauces, atbildes, laiki un vaicājumi palika nemainīti. Tā nebija atbilžu atkārtošana vai slēpts otrais mēģinājums.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](../../PUBLICATION_SCOPE.md).

Pēc noraidījuma veikts vēl viens faktiskas ielādes pārbaudes cikls. Tas ielādēja saglabāto lēmumu un nemainīto pamatpolitiku; ar to nepieskaita vēl vienu jaunu tīmekļa pētījumu.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](../../PUBLICATION_SCOPE.md).

## 6. Kas paturēts, noraidīts un atlikts

| Statuss | Konkrētais saturs |
| --- | --- |
| Paturēts | Abi reproducēto kļūmju labojumi, avotu/atbilžu kontrolsummas, kompaktās mācības par mērvienībām, koncentrāciju, numuru/objektu identitāti un pierādījumu priekšnosacījumiem. |
| Noraidīts kā jauna pamatmetode | Priekšnosacījuma prioritizēšanas kandidāts: prasītais precizitātes ieguvums nav sasniegts. Tā rezultāti un atteikuma iemesls paliek pieejami. |
| Atlikts ar pārbaudāmu hipotēzi | Mācību atbilstības atlase, atsevišķs izmaksu mērķa izmēģinājums un valodu papildu ieguvuma novērtējums. Vajadzīgi jauni uzdevumi un iepriekš noteikts pieņemšanas kritērijs. |

Atmiņa ir ierobežota. Saspiests secinājums nevar bezgalīgi saglabāt visu izejas materiālu; neapstrādāto pierādījumu atmešana notiek tikai pēc dokumentēta plāna. Šī laidiena pilnie privātie izpētes pieraksti tiek saglabāti atsevišķi; publiski pieejamas pašu atbildes, aprēķini un kompaktā izcelsmes uzskaite, ne svešo lapu pilntekstu kopijas.

## 7. Labota vēsturiskā uzskaite un izplatīšanas robeža

Sākotnējā ziņojuma kopskaitā 147 bija iekļauti četri deklarēti E10 sākuma vaicājumi, kuru toreizējā pilnā izvade nav saglabājusies. Neatkarīgā pārbaude apstiprina 143 dažādus vaicājumus ar saglabātām sākotnējām kvītīm. Jau esošie E10 atkopšanas lasījumi ir sasaistīti ar avotiem; trūkstošās kvītis nav izdomātas. Jaunās gala atlases 156 skaits attiecas tikai uz tās 30 gadījumiem.

Šeit minētie iekšējie ieraksti šajā izdevumā nav publicēti; skati [publikācijas tvērumu](../../PUBLICATION_SCOPE.md).

> Sākotnējā publikācijas piezīme, saglabāta vēsturei: Publiskā izplatīšanas lapa: https://reyrun-rekursive-deep-search.runcisreinis.chatgpt.site . Tajā ir lejupielāde, dokumentācija, šī pārbaude, visi piemēri, video un Facebook teksta sagatave. GitHub, Hugging Face, ModelScope un Gitee publiskie spoguļi šajā laidienā vēl nav izveidoti. Facebook ieraksts nav nosūtīts autora vietā.

Publikācijas stāvoklis 2026. gada 10. novembrī: publiskais [GitHub repozitorijs](https://github.com/runcisreinis-glitch/reyrun-recursive-deep-search) ir publicēts, un tā pirmais 111 failu izdevums ir pārbaudīts pret publikācijas manifestu. Ķīnas spoguļa publicēšana gaida konta pārbaudi: gan Gitee, gan ModelScope pieprasīja tālruņa piesaisti, un spogulis tajos vēl nav izveidots. Hugging Face spogulis nav izveidots. Facebook sagataves autora vietā nav publicētas.

Šī ir izpētes prasme un izpildāms mācību cikls pieslēdzamai aģenta videi. Pakotnes lejupielāde vai norādes ielīmēšana parastā čatā pati nepalaidīs diennakts procesu un negarantēs pastāvīgu atmiņu. Konkrētas instalācijas pieņemšanas pārbaude ir reāls pirmais darbs, otrais darbs un tajā ielādītā pirmā darba pieredze.
