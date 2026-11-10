"""NP07: hipotētiski izvietojuma un novērojumu piemēri, nav lietotāja loga mērījumu."""
import json,math
def dot_grid(width_mm,height_mm,max_pitch_mm=50,diameter_mm=6):
    nx=math.ceil(width_mm/max_pitch_mm)
    ny=math.ceil(height_mm/max_pitch_mm)
    px=width_mm/nx
    py=height_mm/ny
    assert px<=max_pitch_mm and py<=max_pitch_mm
    return {"hypothetical":True,"width_mm":width_mm,"height_mm":height_mm,
      "diameter_mm":diameter_mm,"columns":nx,"rows":ny,"dots":nx*ny,
      "horizontal_center_pitch_mm":px,"vertical_center_pitch_mm":py,
      "outer_center_to_edge_mm":[px/2,py/2],
      "clear_internal_gaps_mm":[px-diameter_mm,py-diameter_mm],
      "marked_surface_percent":100*nx*ny*math.pi*(diameter_mm/2)**2/(width_mm*height_mm)}
g=dot_grid(1000,1000)
assert g["dots"]==400 and g["clear_internal_gaps_mm"]==[44,44]
# The 6-mm diameter is a chosen illustration, above the source minimum of 5 mm.
# 30 window-days and zero complete detections are hypothetical, not user observations.
T=30
alpha=.05
upper_rate=-math.log(alpha)/T
assert upper_rate>0
assert math.isclose(math.exp(-upper_rate*T),alpha)
out={"user_data":{"observed_collisions":2,"observation_days":None,
      "window_dimensions":None,"baseline_rate":None,"efficacy_reduction_percent":None},
 "source_based_design":{"max_gap_mm":50,"minimum_marker_width_mm":5,"source":"S1"},
 "hypothetical_grid":g,
 "hypothetical_rate_examples":{"two_in_30_window_days":2/30,"one_in_30_window_days":1/30,
      "raw_relative_decrease_percent":50,"does_not_prove_causation":True},
 "hypothetical_zero_events":{"window_days":T,"events":0,
      "one_sided_confidence":.95,"poisson_rate_upper_per_window_day":upper_rate,
      "formula":"lambda_upper=-ln(0.05)/T",
      "assumptions":["constant Poisson event rate","independent events","perfect detection","fixed exposure"],
      "applicable_to_user_window_as_measured_result":False},
 "limitations":["No real window measurements","No collision-monitoring experiment performed",
  "Small marked-area percentage is not an efficacy measure",
  "No proportional reduction inferred from the user's two events"]}
print(json.dumps(out,ensure_ascii=False,indent=2))

