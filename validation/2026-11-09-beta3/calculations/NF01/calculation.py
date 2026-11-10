import math,json
delta=1e-6
rows=[{'n':n,'signal':math.exp(-n*n),'above_delta':math.exp(-n*n)>delta,'amplified_noise':delta*math.exp(n*n)} for n in range(1,7)]
assert max(r['n'] for r in rows if r['above_delta'])==3
out={'delta':delta,'sqrt_log_inverse_delta':math.sqrt(math.log(1/delta)),'modes':rows,'cutoff_3_noise_bound':delta*math.exp(9),'cutoff_4_noise_bound':delta*math.exp(16),'same_bias_averaging':{'replicates':100,'per_replicate_mode4_error':delta,'average_mode4_error':sum([delta]*100)/100,'inverse_coefficient_error':delta*math.exp(16)},'normalization_squared_integral':'(2/pi)*(pi/2) = 1'}
print(json.dumps(out,indent=2))
