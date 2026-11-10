import json
from fractions import Fraction as F
w=F(130+8);h=F(240+16);sw=F(3,100);sl=F(5,100)
values={'required_afterwash_width_cm':w,'required_afterwash_length_per_panel_cm':h,'raw_width_min_cm':w/(1-sw),'raw_length_each_cm':h/(1-sl),'raw_total_length_m':2*h/(1-sl)/100,'available_afterwash_width_cm':150*(1-sw),'available_afterwash_length_cm':520*(1-sl),'postwash_total_shortfall_cm':2*h-520*(1-sl),'prewash_extra_cm':2*h/(1-sl)-520,'finished_height_if_halved_cm':520*(1-sl)/2-16,'max_length_shrinkage_for_5_2m_percent':(1-2*h/520)*100,'afterwash_spare_with_5_4m_cm':540*(1-sl)-2*h}
print(json.dumps({k:{'exact':str(v),'decimal':float(v)} for k,v in values.items()},indent=2))
assert 150*(1-sw)>=w
assert 520*(1-sl)<2*h
assert (2*h/(1-sl))*(1-sl)==2*h
