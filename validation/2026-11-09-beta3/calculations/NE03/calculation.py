from fractions import Fraction as F
import json
energy=F(350); mass=F(280); per100=energy/mass*100
assert per100==125
print(json.dumps({'total_kcal':float(energy),'cooked_g':float(mass),'kcal_per_100g':float(per100),'portion_140g_kcal':float(energy*140/mass),'yield_factor':float(mass/100)},indent=2))
