"""NP06: avota nosaukumu pāreju loģisks tests, ne ēku ģeokodēšana."""
import json
from datetime import date
rules=[
 {"old":"Maskavas iela","segment":"13. janvāra iela–Lāčplēša iela","new":"Lastādijas iela","source":"S1, 2.1"},
 {"old":"Maskavas iela","segment":"Lāčplēša iela–Rīgas robeža","new":"Latgales iela","source":"S1, 2.2"},
 {"old":"Latgales iela","segment":"2024. lēmuma iepriekšējā Latgales iela","new":"Jāņa Klīdzēja iela","source":"S1, 1"}
]
def candidates(old,segment=None):
 return [r["new"] for r in rules if r["old"]==old and (segment is None or r["segment"]==segment)]
tests=[
 {"input":"Maskavas iela; posms nav dots","candidates":candidates("Maskavas iela"),"building_identity":None},
 {"input":"Maskavas iela; sākuma posms zināms","candidates":candidates("Maskavas iela",rules[0]["segment"]),"building_identity":None},
 {"input":"Latgales iela tieši pirms 2024. pārdēvēšanas","candidates":candidates("Latgales iela"),"building_identity":None}
]
assert len(tests[0]["candidates"])==2
assert tests[1]["candidates"]==["Lastādijas iela"]
assert tests[2]["candidates"]==["Jāņa Klīdzēja iela"]
assert all(x["building_identity"] is None for x in tests)
decision=date(2024,2,21)
publication=date(2024,2,28)
city_confirmation=date(2024,3,1)
assert decision < publication < city_confirmation
out={"scope":"2024. lēmumā nosauktās ielu pārejas, ne universāls visu vēsturisko laikposmu tulkotājs",
 "source_rules":rules,"tests":tests,
 "timeline":{"decision":str(decision),"official_publication":str(publication),
 "city_says_in_force_by":str(city_confirmation),"exact_effective_date":None},
 "arithmetic":{"rules":len(rules),"maskavas_successor_names":len(candidates("Maskavas iela")),
 "publication_after_decision_days":(publication-decision).days,
 "confirmation_after_publication_days":(city_confirmation-publication).days},
 "unperformed":["Nav nosaukts vai identificēts privāts nams","Nav pārbaudīta māju numuru pāreja",
 "Nav veikta konkrētas kartes ģeoreferencēšana","Nav pieņemts, ka lēmuma pieņemšanas datums ir spēkā stāšanās datums"]}
print(json.dumps(out,ensure_ascii=False,indent=2))

