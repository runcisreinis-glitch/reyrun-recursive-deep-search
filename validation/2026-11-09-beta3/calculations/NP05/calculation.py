"""NP05: tikai lietotāja hipotētiskie dati; EUR un veselas krūzes."""
import json
from math import ceil
v=9+6
normal=24-v
special=18-v
def account(n,s=0,k=0):
    revenue=24*n+18*s
    variable=v*(n+s)
    return {"normal_units":n,"special_units":s,"revenue_eur":revenue,
            "variable_cost_eur":variable,"contribution_eur":revenue-variable,
            "fixed_cost_eur":360+k,"profit_eur":revenue-variable-360-k}
base=account(40)
combined=account(40,30)
assert normal==9 and special==3
assert base["profit_eur"]==0 and combined["profit_eur"]==90
assert combined["profit_eur"]-base["profit_eur"]==30*(18-v)
assert 40+30<=120
out={"inputs":{"normal_price":24,"special_price":18,"materials_packaging":9,
 "piecework_per_produced_unit":6,"fixed_month":360,"capacity":120,
 "base_order":40,"special_order":30,"provenance":"task; all produced units sold"},
 "unit_variable_eur":v,"normal_contribution_eur":normal,"special_contribution_eur":special,
 "base":base,"combined":combined,
 "increment":{"revenue_eur":540,"variable_cost_eur":450,"contribution_eur":90,"profit_eur":90},
 "spare_before":80,"spare_after":50,
 "normal_only_breakeven":ceil(360/normal),
 "normal_breakeven_with_30_special":ceil((360-30*special)/normal),
 "boundary_normal_only":[account(n) for n in [39,40,41]],
 "boundary_with_special":[account(n,30) for n in [29,30,31]],
 "hypothetical_extra_order_cost":[{"extra_cost_eur":k,"incremental_profit_eur":90-k}
                                  for k in [0,50,90,100]],
 "hypothetical_displacement":[{"lost_normal_units":n,"incremental_profit_eur":90-9*n}
                              for n in [0,10,11,30]],
 "scope":"No actual workshop observation; changed-premise scenarios are hypothetical"}
assert out["boundary_normal_only"][0]["profit_eur"]==-9
assert out["boundary_with_special"][1]["profit_eur"]==0
print(json.dumps(out,ensure_ascii=False,indent=2))

