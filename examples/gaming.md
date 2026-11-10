# Kā čīti strādā un kā atšķirt tehnoloģiju no pārdošanas pasakas

**Wallhack un aimbot apraksta iegūto priekšrocību; DMA apraksta piekļuves mehānismu.** Vienā sistēmā šīs lietas var būt apvienotas. Tāpēc uzraksts “DMA aimbot” vēl neko nepasaka par kvalitāti, drošumu vai to, vai demonstrācija vispār ir īsta.

## Trīs atšķirīgas lietas

**Wallhack un plašākais ESP** izmanto informāciju, kuru spēle spēlētājam parasti neparāda: pretinieka atrašanās vietu, kontūru vai citus datus. Tā var būt atmiņā pieejamas informācijas attēlošana atsevišķā slānī vai izmaiņas attēlošanā. Būtiska robeža: ja serveris klientam slēpto pozīciju vispār nenosūta, atmiņas lasīšana to neuzburs. Riot apraksta tieši šādu *Fog of War* pieeju; praksē jāņem vērā arī redzamības maiņa un aizture. [Riot tehniskais skaidrojums](https://www.riotgames.com/en/news/demolishing-wallhacks-valorants-fog-war)

**Aimbot** automatizē mērķēšanas darbību. Vieni varianti izmanto spēles datus, citi analizē redzamos ekrāna pikseļus ar datorredzi un pēc tiem koriģē vadību. “AI” var nozīmēt reālu atpazīšanas modeli, bet var būt arī reklāmas uzlīme. Ekrāna analīze pati neredz cauri sienai; tā arī neatceļ iespēju analizēt rezultātā radušos spēlētāja uzvedību. Pētījums *GAN-Aimbots* aplūko gan šīs pieejas, gan uzvedības atdarināšanu; tā eksperimenta iznākums nav garantija visām spēlēm. [Pētījums, 2022](https://arxiv.org/html/2205.07060v1)

**DMA — Direct Memory Access** ir aparatūras tiešā piekļuve atmiņai, ko normāli izmanto arī derīgas ierīces. Negodīgā sistēmā to mēģina izmantot spēles datu iegūšanai. Tā nav “neredzamības karte”: IOMMU ierobežo, kurām atmiņas zonām ierīce drīkst piekļūt. Rezultāts atkarīgs no aparatūras, programmaparatūras un aizsardzības darbības. Microsoft dokumentācija skaidri nošķir Windows aizsardzību pēc sistēmas ielādes no aizsardzības sāknēšanas laikā. [Microsoft](https://learn.microsoft.com/de-de/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt)

## Kas to izstrādā un ko dara anticheat?

Lietderīgi nošķirt autoru, pielāgotāju, pārdevēju un pētnieku. Autors izprot spēles datu plūsmu; citam darbs ir grafika, ievades automatizācija vai draiveri. Pārdevējs var tirgot cita darbu. Savukārt pētnieki līdzīgus mehānismus pēta, lai pārbaudītu aizsardzību. Tās ir dažādas lomas: tehnisks video nepierāda ne autorību, ne uzticamību.

Anticheat parasti veido vairākus slāņus: spēles un sistēmas integritātes pārbaudes, piekļuves uzraudzību, servera noteikumu pārbaudes un uzvedības analīzi. Kodola draiveris dod citu redzamību nekā parasta programma, tomēr nav visu problēmu atrisinājums. Arhitektūras atšķiras: Epic aprakstītajā EAC Linux v2 paredzēts izmantot platformas aizsardzību un eBPF bez sava anticheat kodola moduļa. [Epic arhitektūra](https://onlineservices.epicgames.com/news/introducing-easy-anti-cheat-linux-v2?lang=ja)

**Servera autoritāte** nozīmē, ka serveris pieņem galīgo lēmumu par spēles stāvokli. Taču arī serverim jāizvērtē klienta pieprasījumi; centrālais serveris pats par sevi nenovērš liekas informācijas nosūtīšanu vai automatizētu mērķēšanu. [Unreal tīkla modelis](https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-overview-for-unreal-engine)

**Pašziņota izstrādātāju pieredze:** Inferna Studio raksta, ka pašu anticheat kļūdaini bloķējis izstrādātāja kontu. Tas ir konkrēts autora stāsts, ne neatkarīgi pārbaudīts tests vai kļūdainu banu biežuma mērījums. Tas palīdz saprast, kādēļ aizdomīgs signāls un pierādīta krāpšanās nav sinonīmi. [Pieredzes apraksts](https://infernastudio.com/articles/our-anti-cheat-banned-a-player-it-was-us)

## Kur mācīties un kam neticēt?

Tehniskiem jautājumiem noder [Reverse Engineering Stack Exchange](https://reverseengineering.stackexchange.com/tour), Ghidra projekta diskusijas un spēļu dzinēju izstrādātāju dokumentācija. **Ghidra** palīdz pētīt kompilētu kodu; **debuggeri**, piemēram, WinDbg, ļauj apskatīt savas programmas izpildi, atmiņu un reģistrus. Tie ir vispārīgi izpētes rīki. [Ghidra](https://github.com/NationalSecurityAgency/ghidra) · [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/)

Vērtējot apgalvojumu, prasītu trīs lietas:

- **Ko tieši demonstrē?** Versija, vide, ievade, pilns rezultāts un zināmie ierobežojumi ir vērtīgāki par atlasītu uzvaru montāžu.
- **Vai apgalvojums ir pārbaudāms?** “Nekad nenosakāms”, “strādā visur” un “AI, tāpēc drošs” nav tehniski pierādījumi.
- **Vai avoti sakrīt?** Repozitorija vēsture, autora skaidrojums un atkārtojama demonstrācija palīdz pārbaudīt izcelsmi. Atsauksmju skaits vai prasība izslēgt aizsardzību paši par sevi uzticamību neapliecina.

**Labs nākamais solis:** savā Unity vai Unreal bezsaistes ainā izveidot divus tēlus un sienu, ieslēgt izstrādātāja diagnostikas attēlojumu un salīdzināt “dati pastāv” ar “objekts ir redzams”. Pēc tam savā lokālā klienta/servera piemērā pārbaudīt, kuri dati tiek nosūtīti. Tā kļūst saprotama problēmas sakne un aizsardzības jēga.

