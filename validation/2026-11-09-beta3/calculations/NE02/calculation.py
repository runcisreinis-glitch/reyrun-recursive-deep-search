from fractions import Fraction as F
import json
perimeter=2*(F(4)+F(3)); walls=perimeter*F('2.5')-F(5); litres=walls*2/F(10)
result={'perimeter_m':float(perimeter),'net_walls_m2':float(walls),'coverage_m2':float(walls*2),'litres':float(litres),'conditional_10_percent_reserve_litres':float(litres*F('1.1'))}
assert litres==6
print(json.dumps(result,indent=2))
