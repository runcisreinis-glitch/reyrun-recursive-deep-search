import json
from fractions import Fraction as F
inputs={'hardness_mg_L_as_CaCO3':280,'free_chlorine_mg_L':0.4}
# Explicit hypothetical outputs, not measurements or a product performance claim.
scenario={'hardness_after_mg_L_as_CaCO3':140,'free_chlorine_after_mg_L':0.04}
rh=100*(1-F(140,280));rc=100*(1-F('0.04')/F('0.4'))
print(json.dumps({'given_inputs':inputs,'hypothetical_outputs_NOT_MEASURED':scenario,'hypothetical_hardness_reduction_percent':float(rh),'hypothetical_chlorine_reduction_percent':float(rc),'actual_filter_performance':None,'formula':'100*(before-after)/before'},indent=2))
assert rh==50 and rc==90
