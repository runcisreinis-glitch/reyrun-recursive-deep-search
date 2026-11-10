# Trešais piemērs: aģents, kas uzlabo arī savu mācīšanās kārtību

Pārbaudīts 2026. gada 9. novembrī. Šis ir reālas izpētes rezultāts un pārbaudāms arhitektūras priekšlikums; ārējie projekti šajā piemērā nav instalēti vai izmērīti.

## Jautājums

“Kā uzbūvēt lokālu MI aģentu, kas nemaina modeļa svarus, saglabā mazu pieredzes bibliotēku un uzlabo gan savas darbības, gan paņēmienu, ar kuru izvēlas, ko no pieredzes mācīties?”

## Atbilde

**Es sāktu ar gatavu atmiņas un prasmju pamatu un izmēģinātu vienu papildinājumu: pārbaudīt, vai konkrētā atmiņa patiešām uzlabo nākamo lēmumu.** Atmiņā ierakstīts padoms vēl nepierāda, ka modelis to saprata vai izmantoja pareizajā situācijā.

Šis ir perspektīvs virziens, taču nebūtu pamatoti teikt, ka neviens to nav realizējis. MemEvolve jau pēta gan aģenta pieredzes, gan pašas atmiņas arhitektūras attīstīšanu. EvolveLab sadala to četrās maināmās darbībās: pieredzes pārveidošana, glabāšana, atrašana un pārvaldība. Tas dod konkrētu pētniecības pamatu mūsu iecerei. [Pētījums](https://proceedings.mlr.press/v306/zhang26fa.html)

### Ko var izmantot jau tagad

| Pamats | Kāpēc tas ir interesants | Kas jāpārbauda pirms izvēles |
|---|---|---|
| **ReMe** | Failos glabāta, atlasāma atmiņa; dokumentācijā aprakstīta arī Hermes integrācija. Sākotnējai teksta meklēšanai nav obligāts atsevišķs iegultņu modelis. | Konkrētā Hermes versija, automatizācijas modeļa izmaksas un vai izvēlētajā konfigurācijā izdodas mūsu atmiņas robeža. |
| **Memento-Skills** | Gatavs projekts, kura darba kārtībā ietilpst prasmju izvēle, izpilde, kļūdu izvērtēšana un prasmju pārrakstīšana, saglabājot pamatmodeli nemainīgu. | Cik labi šis cikls darbojas ar mūsu modeli un uzdevumiem; projekta demonstrācijas neatbild uz to mūsu vietā. |
| **MemEvolve / EvolveLab** | Vistiešākais pamats eksperimentiem, kuros mainās arī pieredzes atlasīšanas un pārvaldības metode. | Pētniecības koda integrācija, konkrētais modulis un tā atkarības; tas nav šeit pārbaudīts ikdienas aģents. |

[ReMe pirmavots](https://reme.agentscope.io/zh/overview) · [Memento-Skills autoru apraksts](https://www.memento.run/research/skills/) · [MemEvolve kods](https://github.com/bingreeky/MemEvolve)

Šo projektu repozitoriji norāda Apache-2.0 licenci; pārņemot atsevišķus failus, atkarību, modeļu un datu tiesības jāpārbauda atsevišķi. Šajā izvērtējumā izlasīta dokumentācija un repozitoriju apraksti, ne reproducēti to rezultāti.

### Kādu papildinājumu būtu vērts izmēģināt

Mans priekšlikums ir **īsu pieredzes kartīšu bibliotēka ar piemērošanas nosacījumiem un pārbaudītu atlases kārtību**. Tā nav pretenzija uz pasaulē pirmu arhitektūru. Mūsu pārbaudāmais mērķis būtu mazāk atkārtotu kļūdu pie ierobežota glabāšanas un meklēšanas budžeta.

Kartīte saturētu situāciju, darbību, iznākumu, pierādījuma adresi un nosacījumu, kad padoms neder. Piemēram: “Ja meklētāja fragments un projekta fails atšķiras, pārbaudi konkrēto pašreizējo failu. No dokumentācijas vien nesecini, ka funkcija uz tava datora darbojas.”

Pirms darba aģents saņemtu tikai attiecīgās kartītes. Pēc darba tas saglabātu vienu būtisku mācību vai pamatotu secinājumu, ka jauna mācība nav iegūta. Atsevišķā pārbaudē salīdzinātu trīs variantus: bez kartītēm, ar pašreizējo atlasi un ar jauno atlasi. Tā var nošķirt bibliotēkas ieguvumu no paša modeļa spējas jau tāpat atrisināt jautājumu.

Šādas pārbaudes vajadzību pastiprina pētījums “Large Language Model Agents Are Not Always Faithful Self-Evolvers”: tā autori novēroja, ka modeļi mēdz ignorēt vai nepareizi interpretēt saīsinātu pieredzi. Tas nepierāda, ka īsa atmiņa neder; tas liek pārbaudīt, vai saīsinājumā saglabājies lēmumam vajadzīgais. [Pētījums](https://arxiv.org/abs/2601.22436)

Arī praktiska pieredze dod konkrētu norādi: amtr autors pēc 24 konteksta saīsināšanas paaudzēm apraksta problēmu, ka darba hipotēze pārtop šķietami apstiprinātā secinājumā. Viņa pielāgojums — kopā saglabāt pārbaudīto un vēl nepārbaudīto. Tas ir autora paša novērojums, ne vispārējas efektivitātes pierādījums. [Autora pieredze un saite uz kodu](https://zenn.dev/naoto256/articles/amtr-working-memory)

### Kad sintēze būtu izdevīgāka par gatavo

Vispirms salīdzinātu ar ReMe vai Memento-Skills konfigurāciju, kurai dots tāds pats modelis, rīki, atmiņas budžets un pielāgošanas darbs. Ja mūsu prasību var izpildīt ar nelielu gatavā projekta iestatījumu, izvēlētos to.

Piedāvāju sākuma pārbaudi ar 24 iepriekš neizmantotiem uzdevumiem, kuros ir arī nepiemērotas un novecojušas mācības. Pirms rezultātu redzēšanas noteiktu, piemēram, šādu mērķi: vismaz par 20% mazāk atkārtotu kļūdu, neviena jauna kritiska kļūda un nepieaugošs meklēšanas darbību skaits. Atsevišķs lasītājs pārbaudītu, vai ieteikums, pamatojums un nākamā darbība ir saprotami. **20% ir piedāvāts lēmuma slieksnis, ne sasniegts rezultāts.** Mazais tests palīdzētu izlemt par turpināšanu, ne pierādītu universālu pārākumu.

Plānošanas aplēse: 12–24 darba stundas nelielam savienotājam, 16–32 stundas uzdevumu un vērtēšanas sagatavošanai, 12–24 stundas kļūdu labošanai un atkārtojamai demonstrācijai — kopā 40–80 stundas, aptuveni 1–2 nedēļas vienam izstrādātājam ar gatavu vidi. Trīs varianti reiz 24 uzdevumi ir 72 aģenta uzdevumu izpildes, ne 72 atsevišķi modeļa pieprasījumi. Faktiskais modeļa izsaukumu skaits un ilgums vispirms jāmēra mazā izmēģinājumā.

Elektrību aprēķinātu kā izmērīto visa datora vidējo jaudu kW reiz aktīvās stundas; cenu — pēc konkrētā tarifa vai faktiski izmantotā pakalpojuma. Šīs vērtības šeit nav izmērītas. Regulārai uzturēšanai sākotnēji rezervētu 2–4 stundas nedēļā, līdz kļūst zināms atkarību un kļūdu biežums.

**Lēmums: ir pamats ierobežotam salīdzinošam eksperimentam. Vēl nav pamata solīt, ka mūsu sintēze pārspēs gatavos risinājumus vai ka tā jau darbojas autonomi.**

