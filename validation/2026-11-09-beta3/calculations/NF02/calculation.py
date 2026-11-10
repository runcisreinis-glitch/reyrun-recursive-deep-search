import math,json
def em(h,k):
 a=1-2*h;m=1.;v=0.
 for _ in range(k): m=a*m;v=a*a*v+9*h
 direct=9*h*sum(a**(2*j) for j in range(k))
 assert math.isclose(v,direct,rel_tol=1e-12)
 return {'h':h,'k':k,'t':h*k,'a':a,'mean':m,'variance':v,'continuous_mean':math.exp(-2*h*k),'continuous_variance':2.25*(1-math.exp(-4*h*k))}
rows=[em(.25,k) for k in [1,4,20,100]]+[em(1.2,k) for k in [1,2,10,100]]+[em(1,100)]
h=.25;a=1-2*h
out={'method':'deterministic exact moment recursion, no Monte Carlo','continuous_stationary_variance':2.25,'em_stationary_variance_h025':9/(4*(1-h)),'relative_variance_bias_h025':1/(1-h)-1,'rows':rows,'noise_correction':{'a':a,'noise_variance':2.25*(1-a*a),'stationary_variance':2.25,'lag1_correlation':a,'true_lag1_correlation':math.exp(-2*h)},'exact_grid_transition':{'a':math.exp(-2*h),'noise_variance':2.25*(1-math.exp(-4*h))}}
print(json.dumps(out,indent=2))
