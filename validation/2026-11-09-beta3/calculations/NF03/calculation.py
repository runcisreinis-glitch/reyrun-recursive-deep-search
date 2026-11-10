import math,json,numpy as np
import sympy as s
B=s.Matrix([[-1,20],[0,-1]])
P=s.Matrix([[s.Rational(1,2),5],[5,s.Rational(201,2)]])
assert B.T*P+P*B==-s.eye(2)
assert P[0,0]>0 and P.det()>0
tstar=math.sqrt(99)/10
def value(t):return math.exp(-t)*(math.sqrt(1+100*t*t)+10*t)
rows=[]
for t in [0,.01,.5,tstar,1,2,10]:
 M=math.exp(-t)*np.array([[1,20*t],[0,1]],dtype=float)
 numerical=float(np.linalg.svd(M,compute_uv=False)[0]);exact=value(t)
 assert math.isclose(numerical,exact,rel_tol=2e-15,abs_tol=1e-15)
 rows.append({'t':t,'formula_norm':exact,'svd_norm':numerical})
M=math.exp(-tstar)*np.array([[1,20*tstar],[0,1]])
u,sv,vh=np.linalg.svd(M);z=vh[0];achieved=float(np.linalg.norm(M@z))
out={'t_max_exact':'sqrt(99)/10','t_max':tstar,'norm_max_exact':'exp(-sqrt(99)/10)*(10+sqrt(99))','norm_max':value(tstar),'rows':rows,'derivative_log_at_tstar':-1+10/math.sqrt(1+100*tstar*tstar),'optimal_initial_vector':z.tolist(),'achieved_norm':achieved,'sym_B_eigenvalues':[-11,9],'energy_initial_derivative_z_equal_components':18,'P':str(P),'P_det':str(P.det()),'Lyapunov_residual':str(B.T*P+P*B+s.eye(2)),'P_eigenvalues':np.linalg.eigvalsh(np.array(P,float)).tolist()}
print(json.dumps(out,indent=2))
