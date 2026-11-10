# Publicētie rezultāti un to robežas

Gala izpētes kopā ir 10 ikdienas jautājumi, 10 vidēji sarežģīti jautājumi dažādās nozarēs un 10 sarežģīti jautājumi. Tajā saglabāti 12 agrākie gadījumi un pievienoti 18 jauni; kopā ar vēsturisko atlasi tie veido 48 atšķirīgus pamatuzdevumus. Septiņos jaunajos sarežģītajos gadījumos ir pilns matemātisks pierādījums vai atvasinājums un faktiski palaists aprēķins. Abas 30 gadījumu kopas ir pilnībā pieejamas angļu un latviešu valodā.

Atsevišķais meklēšanas stratēģijas izmēģinājums **nepierādīja precizitātes uzlabojumu**. Kandidāts netika pieņemts par jauno pamatmetodi, un saglabātais lēmums ir `no_gain`.

## Trīs uzdevumu salīdzinājums

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

## Izpētes tvērums un labojumi

Gala 30 gadījumiem ziņoti 156 izpildīti vaicājumi. Katram gadījumam meklēts angliski, vāciski, ķīniski un japāniski. Vaicājums kādā valodā nepierāda, ka šajā valodā atrasts un izlasīts secinājumu atbalstošs pirmavots. Piekļuves kļūmes un ierobežoti avotu lasījumi atbildēs paliek norādīti.

Sākotnējās atlases vidējā grupa bija pārāk koncentrēta uz IT, bet sarežģītajā grupā trūka pabeigtu augstākās matemātikas uzdevumu. Jaunā atlase novērš šos trūkumus, saglabājot agrākās atbildes. Vēsturiskajā kopskaitā 147 bija iekļauti četri deklarēti E10 vaicājumi, kuru pilnā sākotnējā izvade nav saglabājusies. Pamatotais vēsturiskais skaits ir 143 dažādi vaicājumi ar saglabātām kvītīm; trūkstošās kvītis nav izgatavotas no jauna un uzdotas par sākotnējiem pierādījumiem.

Jautājumi veidoti pārbaudei, un simulētie precizējumi ir marķēti. Katram piemēram galveno izpēti veica viens aģents, pēc tam notika ziņotās pārskatīšanas. Šis kopums neapliecina četru neatkarīgu aģentu meklēšanu katrā gadījumā. Matemātiskie argumenti izlasīti un salīdzināti ar saglabātajiem aprēķiniem; formāla pierādījumu asistenta sertifikācija nav apgalvota. [Laidiena ziņojumā](validation/2026-11-09-beta3/release-report.lv.md) saglabāti rezultāti un to nosacījumi.

## Kas uzlabots programmā

Ziņotajā laidiena pārbaudē izpildīti 82 programmas testi. Izlabotas divas reproducētas kļūmes: agrāka mācību kartīte varēja aizsegt jaunāku pretrunīgu novērojumu, savukārt nesaistīts pierādījumu objekts pie atmiņas robežas varēja neļaut saglabāt atmiņas atbrīvošanas rezultātu. Pašreizējais pirmkods, testi, aprēķinu programmas un to izvades ir iekļautas, lai lasītāji tās varētu pārbaudīt un palaist. Programmas mehānisma testi nepierāda augstāku meklēšanas precizitāti.

Visi 18 jaunie pamatuzdevumi noslēdza reģistrētu mācību ciklu, un 15 vēlākie uzdevumi ielādēja agrākās mācības. Šīs darbības vadīja čats. Pieredzes ielāde nepierāda, ka katra nākamā atbilde kļūst labāka vai ka darbojas patstāvīgs fona pakalpojums. Atsevišķā divu uzdevumu izpildes demonstrācija šeit aprakstīta tikai ar tās ziņoto rezultātu: nākamais uzdevums ielādēja saglabātu mācību. Tās iekšējie izpildes ieraksti nav iekļauti.

Noderīgie labojumi un kompaktās mācības saglabātas. Priekšnosacījuma prioritizēšanas kandidāts netika ieviests. Mācību atbilstība, izmēģinājums ar izmaksu mērķi un vairāku meklēšanas valodu papildu ieguvums paliek hipotēzes, kurām vajadzīgi jauni uzdevumi un iepriekš fiksēti pieņemšanas kritēriji.

## Kas ir publicēts

Šis ir autorēts rezultātu pārskats. Pilnas vērtētāju izvades, norāžu momentuzņēmumi, izpildes ieraksti, atmiņas momentuzņēmumi, neapstrādātie žurnāli, rīku vaicājumu izdrukas un iekšējās kvītis nav iekļautas ne kā atsevišķi faili, ne kā kopijas kopējā eksperimentu ziņojumā. Šie izlaidumi ierobežo iespēju neatkarīgi rekonstruēt sākotnējo izpildes vadību. Pilnās izpētes atbildes, matemātiskie argumenti, aprēķinu kods, ziņotais negatīvais rezultāts un norādītās robežas paliek pieejamas.

Lasāms [publikācijas tvērums](PUBLICATION_SCOPE.md), [izpētes un eksperimentu ziņojums angliski](EXPERIMENTS.md) un [ziņojums latviski](EXPERIMENTS.lv.md). [Failu manifests](file-manifest.json) norāda šā izdevuma precīzos failus. Publikācija nesniedz pretvīrusu sertifikātu, vispārēju izpētes kvalitātes garantiju vai apgalvojumu par pastāvīgi strādājošu uzlabošanās pakalpojumu.
