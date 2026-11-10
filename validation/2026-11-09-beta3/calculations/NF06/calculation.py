import json, math
import numpy as np
import sympy as s

h=s.symbols("h", real=True)
A=s.Matrix([[0,1],[0,0]]); B=s.Matrix([[0,0],[-1,0]])
M=s.simplify((s.eye(2)+h*A/2)*(s.eye(2)+h*B)*(s.eye(2)+h*A/2))
P=s.diag(1,1-h*h/4)
residual=s.simplify(M.T*P*M-P)
E=s.eye(2)+h*(A+B)
assert residual == s.zeros(2)
assert s.simplify(M.det()) == 1
assert s.simplify(E.T*E-(1+h*h)*s.eye(2)) == s.zeros(2)
stable=[]
for step in [0.1,1.0,1.9,1.999]:
    c=1-step*step/4
    mat=np.array(M.subs(h,step),dtype=float)
    weight=np.diag([1.0,c])
    power=np.eye(2)
    maxnorm=1.0; maxdefect=0.0; minenergy=maxenergy=1.0
    for k in range(1,10001):
        power=mat@power
        maxnorm=max(maxnorm,float(np.linalg.norm(power,2)))
        maxdefect=max(maxdefect,float(np.linalg.norm(power.T@weight@power-weight,2)))
        euclidean_energy=float(power[:,0]@power[:,0])
        minenergy=min(minenergy,euclidean_energy)
        maxenergy=max(maxenergy,euclidean_energy)
    theta=math.acos(1-step*step/2)
    stable.append(dict(h=step,steps=10000,final_operator_norm=float(np.linalg.norm(power,2)),
                       max_operator_norm=maxnorm,proven_bound=1/math.sqrt(c),
                       max_invariant_matrix_defect=maxdefect,
                       initial_state=[1,0],true_energy_min=minenergy,true_energy_max=maxenergy,
                       phase_per_step=theta,phase_error_after_10000_steps=10000*(theta-step)))
boundary=[]
for k in [1,2,100,10000]:
    exact=M.subs(h,2)**k
    formula=(-1)**k*s.Matrix([[1,0],[2*k,1]])
    assert exact==formula
    boundary.append(dict(steps=k,power=[list(map(int,exact.row(j))) for j in range(2)],
                         operator_norm=k+math.sqrt(k*k+1)))
mat=np.array(M.subs(h,2),dtype=float); power=np.eye(2)
for k in range(10000):
    power=mat@power
assert np.array_equal(power,np.array([[1,0],[20000,1]],dtype=float))
unstable_mat=np.array(M.subs(h,2.1),dtype=float); power=np.eye(2)
for k in range(1000):
    power=unstable_mat@power
unstable=dict(h=2.1,steps=1000,eigenvalues=np.linalg.eigvals(unstable_mat).tolist(),
              operator_norm=float(np.linalg.norm(power,2)),
              log10_operator_norm=math.log10(float(np.linalg.norm(power,2))))
euler=[]
for step,k in [(0.1,10000),(1.0,1000)]:
    mat=np.array([[1,step],[-step,1.0]]); power=np.eye(2)
    for j in range(k):
        power=mat@power
    observed=float(np.linalg.norm(power,2))
    predicted=math.exp(0.5*k*math.log1p(step*step))
    euler.append(dict(h=step,steps=k,operator_norm=observed,
                      theoretical_norm=predicted,relative_error=abs(observed/predicted-1)))
print(json.dumps(dict(matrix=str(M),determinant=str(s.factor(M.det())),
                     invariant_matrix=str(P),invariant_residual=str(residual),
                     euler_energy_identity=str(s.simplify(E.T*E)),
                     stable_long_runs=stable,boundary_exact=boundary,
                     unstable_long_run=unstable,euler_long_runs=euler),
                 indent=2,allow_nan=False))

