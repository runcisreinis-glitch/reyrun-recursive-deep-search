from fractions import Fraction as F
import json
m=F(80);c=F(4186,1000);dT=F(50);eta=F(9,10);tariff=F(15,100)
q_kj=m*c*dT;q=q_kj/3600;e=q/eta;cost=e*tariff
hot=F(50)*(40-10)/(60-10);cold=50-hot
results={'heat_kJ':q_kj,'heat_kWh':q,'electricity_kWh':e,'cost_eur':cost,'process_loss_kWh':e-q,'hot_water_L':hot,'cold_water_L':cold,'mixture_C':(hot*60+cold*10)/50,'hot_heat_lost_kJ':hot*c*(60-40),'cold_heat_gained_kJ':cold*c*(40-10)}
assert e*eta==q
assert hot+cold==50
assert hot*c*(60-40)==cold*c*(40-10)
print(json.dumps({k:{'exact':str(v),'decimal':float(v)} for k,v in results.items()},indent=2))
