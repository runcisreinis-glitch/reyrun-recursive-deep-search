import json,math
from fractions import Fraction as F
rows=[]
for n in [1,10,100,1000,10**6]:
 mass=n*F(1,n)
 distance=(2*n-n)*F(1,2*n)+n*(F(1,n)-F(1,2*n))
 assert mass==1 and distance==1
 rows.append({'n':n,'integral_1':str(mass),'integral_x':str(F(1,2*n)),'integral_x_squared':str(F(1,3*n*n)),'integral_exp':n*math.expm1(1/n),'L1_norm':str(mass),'L1_distance_f_n_f_2n':str(distance)})
n=1000;M=100
fixed=sum(n if 0<(j+.5)/M<1/n else 0 for j in range(M))/M
scaled_mass=sum(1 for j in range(M))/M
scaled_exp=sum(math.exp((j+.5)/(M*n)) for j in range(M))/M
exact_exp=n*math.expm1(1/n)
out={'moments':rows,'fixed_grid':{'n':n,'M':M,'first_midpoint':.5/M,'support_end':1/n,'midpoint_mass':fixed,'exact_mass':1},'support_rescaling':{'substitution':'x=y/n','M':M,'mass':scaled_mass,'exp_integral_midpoint':scaled_exp,'exp_integral_exact':exact_exp,'error':abs(scaled_exp-exact_exp)},'uniform_integrability_counterexamples':[{'threshold':K,'choose_n':K+1,'integral_above_threshold':1} for K in [1,10,1000,10**6]]}
assert fixed==0 and scaled_mass==1
print(json.dumps(out,indent=2))
