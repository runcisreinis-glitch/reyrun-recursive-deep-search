# Salīdzinājuma sešas pilnās atbildes

Visu sešu izpētes atbilžu pilnais saturs ir saglabāts no pārskatītā latviešu izdevuma. Redakcija, 2026. gada 10. novembris: vienā teikumā izlabots lietvārda locījums; rezultāti, strukturētie lauki un avotu adreses nav mainīti. Pirmavotu adreses paliek tekstā un katras atbildes strukturētajā avotu sarakstā. Strukturētie lauki ir pašu autorēto atbilžu sastāvdaļa; atsevišķas vērtētāju izvades, testu veidnes un izpildes ieraksti nav iekļauti.

Pieejamas arī [atbildes angliski](answers.en.md) un [publicētie salīdzinājuma rezultāti](../../../PUBLISHED_FINDINGS.lv.md). Izdevums nepievieno jaunu izpētes izmēģinājumu. Pierādījumu robežas norādītas [publikācijas tvērumā](../../../PUBLICATION_SCOPE.md).

## baseline / IT01-depth-output

**Nē, šī kontrolpunkta izvadam nav pamatoti pievienot mērvienību `m`.** `depth-anything/Depth-Anything-V2-Small-hf` kartītē norādīts relatīvais dziļums, un arī autoru repozitorijs pamatmodeļus pieskaita relatīvā dziļuma novērtēšanai. Kartītes vispārīgais teikums par relatīvo un absolūto dziļumu neapstiprina, ka tieši šis kontrolpunkts izvada metrus. [Modeļa kartīte](https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf), [autoru repozitorijs](https://github.com/DepthAnything/Depth-Anything-V2).

Projekta autors precizē, ka modelis prognozē apgriezto dziļumu: mazāka prognozes vērtība atbilst tālākam punktam. Tādēļ komponenti var paturēt attēla apgabalu relatīvā tuvuma secībai. Šī secība pati nedod fizisku attālumu metros. [Autora skaidrojums](https://github.com/DepthAnything/Depth-Anything-V2/issues/174).

Nākamais solis ir izvēlēties atsevišķu metriskajam dziļumam pielāgotu kontrolpunktu, piemēram, telpām `Depth-Anything-V2-Metric-Indoor-Small-hf`. Tas jau ir autora pielāgots modelis; pašam jauna apmācība nav jāveic, taču dotā uzdevuma kodu nozīmē tā ir `replace_core` izvēle. Pirms paļauties uz tā attālumiem, jāpārbauda kļūda saviem attēliem pret izmērītiem attālumiem. [Metriskā modeļa kartīte](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf). Lietotājs projekta diskusijā apraksta nepareizu mērogu punktu mākoņa veidošanā; tas ir konkrētas pieredzes ziņojums, ne universāls kļūdas mērījums. [Pieredzes ziņojums](https://github.com/DepthAnything/Depth-Anything-V2/issues/152).

Šeit pārbaudīti avoti un konfigurācija. Inferenci neizpildīju, pakotnes neinstalēju un svarus nelejupielādēju.

## evaluation_fields

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



## baseline / IT02-clip-generation

**Nē, oficiālais CLIP `ViT-B/32` ar norādīto piemēru brīvu apraksta teikumu neģenerē.** `encode_image` un `encode_text` atgriež pazīmju vektorus. Izsaukums ar attēlu un tekstiem dod to savstarpējās līdzības vērtības; piemērā teksti ir ievadīti iepriekš, un rezultāts ir šo kandidātu vērtējums. [Dokumentētais piemērs un API](https://github.com/openai/CLIP).

Tas redzams arī `clip/model.py`: teksta kodētājs izveido vektoru, bet `forward` normalizē abu veidu vektorus un atgriež līdzības matricas. Šajā izpildes ceļā nav jauna teikuma tokenu ģenerēšanas posma. Prasītajam brīvajam aprakstam būtu vajadzīga cita vai papildu apmācīta komponente ar teksta dekoderi, tātad dotajā kodu sistēmā `replace_core`. [Modeļa kods](https://github.com/openai/CLIP/blob/main/clip/model.py).

Bibliotēkai var paturēt meklēšanu pēc līdzības. Nākamais izveidojamais posms: saglabāt katra attēla normalizētu `encode_image` vektoru kopā ar faila ceļu, teksta vaicājumu kodēt ar `encode_text` un sarindot attēlus pēc kosinusa līdzības. Tas balstās dokumentētajā vektoru salīdzināšanas mehānismā. [API un normalizēšanas piemērs](https://github.com/openai/CLIP). Rezultātu atbilstība jāpārbauda uz savas bibliotēkas; sākotnējā modeļa kartīte norāda, ka citas valodas ārpus angļu valodas nav mērķtiecīgi apmācītas vai novērtētas. [Modeļa kartīte](https://github.com/openai/CLIP/blob/main/model-card.md).

Šeit izlasīta dokumentācija un attiecīgais kods. Modelis nav palaists, pakotnes nav instalētas un svari nav lejupielādēti.

## evaluation_fields

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



## baseline / IT03-dinov2-retrieval

**Jā, DINOv2 `ViT-S/14` dod izmantojamu attēla reprezentāciju šādai meklēšanai bez jaunas pamatmodeļa apmācības.** Autoru modeļa kartīte tieši min attēlu meklēšanu ar tuvākajiem kaimiņiem; ViT-S vektoram ir 384 elementi. Klašu etiķetes attēlu vektoru savstarpējai sarindošanai nav vajadzīgas. [Modeļa kartīte](https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md).

Avotos ir modeļa kods, svaru saites un `dinov2_vits14` ielādes piemērs. `forward_features` dod globālo `x_norm_clstoken` un lokālās attēla daļu pazīmes; parastais `forward` atgriež globālo reprezentāciju caur `Identity` galvu. [Repozitorijs](https://github.com/facebookresearch/dinov2), [modeļa kods](https://github.com/facebookresearch/dinov2/blob/main/dinov2/models/vision_transformer.py).

Lai iegūtu savas mapes meklētāju, vēl jāizveido šāda apstrāde:

1. Sagatavot lokālu koda un jau lejupielādēto svaru ielādi. Pamatmodeļa ielādes kods pieņem arī svaru ceļu. [Ielādes kods](https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/backbones.py).
2. Visus attēlus apstrādāt vienādi, iegūt globālos vektorus, atsevišķi veikt L2 normalizēšanu un saglabāt vektorus ar failu ceļiem.
3. Iesniegtajam attēlam aprēķināt tādu pašu vektoru, sarindot bibliotēku pēc kosinusa līdzības un atgriezt izvēlēto tuvāko rezultātu skaitu.
4. Pievienot attēla iesniegšanu un rezultātu attēlošanu, pēc tam pārbaudīt atbilstību savos piemēros. Šie ir lietotnes apstrādes posmi ap dokumentēto tuvāko kaimiņu mehānismu. [Modeļa lietojumi](https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md).

Tādēļ izvēle ir `adapt_output`. Rezultātu kvalitāte savā mapē vēl jāpārbauda: projekta lietotājs ziņoja par meklēšanas pasliktināšanos, attēlu apgriežot; tas ir konkrēts pieredzes ziņojums. [Diskusija](https://github.com/facebookresearch/dinov2/issues/103). Šeit inferenci neizpildīju, pakotnes neinstalēju un svarus nelejupielādēju.

## evaluation_fields

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



## candidate / IT01-depth-output

## Slēdziens

Mērvienību **m** šā kontrolpunkta izvadam pievienot nedrīkst. `depth-anything/Depth-Anything-V2-Small-hf` dod relatīvu dziļuma karti. Modeļa kartīte to marķē kā relatīvu, un autoru repozitorijs tieši šo Transformers piemēru saista ar relatīvajiem pamata modeļiem. Kartītes plašais teksts par absolūtā dziļuma rezultātiem neapstiprina metru skalu šim kontrolpunktam. 

Komponenti var paturēt attēla apgabalu relatīvam **tuvāk/tālāk kārtojumam**. Adapteris var mainīt kartes izmēru, to attēlot vai nolasīt izvēlēta apgabala vērtības. No šīm darbībām neiegūst trūkstošo fizisko mērogu; arī autors skalas pielāgošanai prasa patiesas metriskas dziļuma vērtības. Tas ir secinājums par dotajiem nosacījumiem, kuros šādu etalonu nav. 

Ja vajadzīgs metriskas dziļuma kartes novērtējums bez paša veiktas apmācības, nākamais solis ir izvēlēties autoru jau publicēto metrisko Small kontrolpunktu: Hypersim telpām vai Virtual KITTI 2 ārtelpām. To piemērs norāda izvadi metros. Tā ir kontrolpunkta maiņa (`replace_core`); precizitāte konkrētajai ainai vēl jāpārbauda. 

Šeit pārbaudīta dokumentācija, konfigurācija un izvades galvas kods. Modelis nav palaists, svari nav lejupielādēti, instalācija nav veikta.

## evaluation_fields

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



## candidate / IT02-clip-generation

## Slēdziens

**Nē.** Oficiālais CLIP `ViT-B/32` ar publicēto piemēru brīvas formas attēla apraksta teikumu nerada. `encode_image` un `encode_text` atgriež pazīmju vektorus, bet `model(image, text)` atgriež attēla un iepriekš ievadīto tekstu līdzības rezultātus. Arī koda `forward` funkcija beidzas ar šiem līdzības tensoriem. Izvades saime ir `embeddings`. 

Ar adapteri var atlasīt piemērotāko jau uzrakstīto teikumu no kandidātu bankas. Tas joprojām izvēlas kādu no dotajiem tekstiem. Ja nepieciešams jauns brīvi veidots apraksts, jāizmanto attēla aprakstu modelis ar apmācītu teksta ģeneratoru vai jāpievieno šāda komponente. Pēc uzdevuma definīcijas tā ir `replace_core` darbība un prasa mainīt sākotnējo ierobežojumu. 

Attēlu bibliotēkai CLIP ir paturams **līdzības meklēšanai**. Nākamais praktiskais solis: ar `encode_image` saglabāt attēlu vektorus kopā ar failu ceļiem, ar `encode_text` kodēt angļu vaicājumu un sakārtot attēlus pēc normalizēto vektoru līdzības. Tas ir adapteris ap esošo modeli, kam nav vajadzīga jauna pamatmodeļa apmācība. Šī ir dokumentēto funkciju izmantošanas rekomendācija; savas kolekcijas rezultāti vēl jāpārbauda. Angļu vaicājums ievēro sākotnējās modeļa kartītes valodas robežu. 

Šeit nolasīta dokumentācija un kods. Modelis nav palaists, nekas nav instalēts un modeļa svari nav lejupielādēti.

## evaluation_fields

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



## candidate / IT03-dinov2-retrieval

## Slēdziens

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

## evaluation_fields

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

