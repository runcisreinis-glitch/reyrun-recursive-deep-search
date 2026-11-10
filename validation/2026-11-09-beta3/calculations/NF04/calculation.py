import json
from fractions import Fraction as F
rows=[]
for e in [F(1),F(1,10),F(1,100),F(1,10**6)]:
 x=-e;lam=1/(2*e);mu=e/2;g=-1/(4*lam)-lam*e*e
 assert x*x-e*e==0 and 1+2*lam*x==0 and g==x
 assert mu/(e*e)==lam
 rows.append({'epsilon':str(e),'b':str(e*e),'x_star':str(x),'lambda_star':str(lam),'dual_value':str(g),'KKT_stationarity_residual':'0','normalized_mu':str(mu),'lambda_from_normalized_mu':str(mu/(e*e))})
out={'epsilon_positive_cases':rows,'epsilon_zero_dual_sequence':[{'lambda':L,'g':str(-F(1,4*L))} for L in [1,10,100,10**6]],'epsilon_zero_primal':0,'epsilon_zero_stationarity_at_x0':1,'sensitivity':'p(b)=-sqrt(b), p_prime(b)=-1/(2sqrt(b))=-lambda_star','normalized_parameter_warning':'x=epsilon*y is invertible only for epsilon>0'}
print(json.dumps(out,indent=2))
