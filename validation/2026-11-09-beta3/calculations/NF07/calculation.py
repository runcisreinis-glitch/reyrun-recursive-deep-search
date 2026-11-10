import json, itertools, collections, warnings
import sympy as s
from sympy.utilities.exceptions import SymPyDeprecationWarning
warnings.filterwarnings("ignore",category=SymPyDeprecationWarning)
x=s.symbols("x"); f=x**5-x-1; fp=s.diff(f,x)
def expr(poly):
    return str(poly.as_expr() if hasattr(poly,"as_expr") else poly)
factorizations={}
for p in (2,3):
    unit,factors=s.factor_list(f,modulus=p)
    product=s.Integer(unit)
    for fac,m in factors: product*=fac**m
    assert s.Poly(s.expand(product-f),x,modulus=p).is_zero
    factorizations[str(p)]={"unit":int(unit),"factors":[{"poly":str(a),"multiplicity":int(m)} for a,m in factors],
        "gcd_derivative":expr(s.gcd(s.Poly(f,x,modulus=p),s.Poly(fp,x,modulus=p)))}
quadratic_tests=[]
for b,c in itertools.product(range(3),repeat=2):
    q=x*x+b*x+c
    if all(int(q.subs(x,t))%3 for t in range(3)):
        remainder=s.rem(f,q,domain=s.GF(3))
        quadratic_tests.append({"quadratic":str(q),"remainder":str(remainder)})
        assert remainder!=0
assert len(quadratic_tests)==3
assert all(int(f.subs(x,t))%3 for t in range(3))
bezout_u,bezout_v,gcd=s.gcdex(s.Poly(f,x,modulus=3),s.Poly(x**9-x,x,modulus=3))
assert gcd.as_expr()==1
assert (bezout_u*s.Poly(f,x,modulus=3)+bezout_v*s.Poly(x**9-x,x,modulus=3)).as_expr()==1
fc=s.Poly(f,x).all_coeffs(); gc=s.Poly(fp,x).all_coeffs()
rows=[]
for i in range(4): rows.append([0]*i+fc+[0]*(3-i))
for i in range(5): rows.append([0]*i+gc+[0]*(4-i))
sylvester=s.Matrix(rows)
disc=s.discriminant(f,x); resultant=s.resultant(f,fp,x)
assert disc==resultant==sylvester.det()==2869
assert 4**4*fp.subs(x,-s.Rational(5,4))==disc
def compose(a,b):return tuple(a[b[i]] for i in range(len(a)))
def inverse(a):return tuple(a.index(i) for i in range(len(a)))
def parity(a):
    return sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))%2
def cycles(a):
    seen=set();out=[]
    for i in range(len(a)):
        if i in seen:continue
        cur=i;k=0
        while cur not in seen:seen.add(cur);k+=1;cur=a[cur]
        out.append(k)
    return tuple(sorted(out))
identity=tuple(range(5))
def generated(gens):
    found={identity}; queue=[identity]
    while queue:
        a=queue.pop()
        for g in gens:
            b=compose(g,a)
            if b not in found:found.add(b);queue.append(b)
    return found
cycle=tuple((i+1)%5 for i in range(5))
generator_checks=[]
for a,b in itertools.combinations(range(5),2):
    swap=list(range(5));swap[a],swap[b]=swap[b],swap[a]
    group=generated([cycle,tuple(swap)])
    assert len(group)==120
    generator_checks.append({"transposition":[a,b],"generated_order":len(group)})
affine={tuple((a*i+b)%5 for i in range(5)) for a in range(1,5) for b in range(5)}
assert len(affine)==20
assert all(compose(a,b) in affine for a in affine for b in affine)
affine_types=collections.Counter(cycles(a) for a in affine)
assert any(parity(a)==1 for a in affine)
assert (2,3) not in affine_types
A5={a for a in itertools.permutations(range(5)) if not parity(a)}
remaining=set(A5);class_sizes=[]
while remaining:
    a=next(iter(remaining))
    cl={compose(compose(g,a),inverse(g)) for g in A5}
    class_sizes.append(len(cl));remaining-=cl
class_sizes.sort()
assert class_sizes==[1,12,12,15,20]
possible_normal_orders=sorted({1+sum(sub) for mask in itertools.product([0,1],repeat=4)
                              for sub in [[v for v,flag in zip([12,12,15,20],mask) if flag]]})
orders_dividing60=[v for v in possible_normal_orders if 60%v==0]
assert orders_dividing60==[1,60]
print(json.dumps({
"polynomial":str(f),"factorizations":factorizations,
"mod3_value_at_0_1_2":[int(f.subs(x,t))%3 for t in range(3)],
"mod3_irreducible_quadratic_remainders":quadratic_tests,
"mod3_bezout_certificate":{"u":expr(bezout_u),"v":expr(bezout_v),"identity":"u*f+v*(x^9-x)=1 in F3[x]"},
"discriminant":int(disc),"prime_factorization":{str(k):int(v) for k,v in s.factorint(disc).items()},
"resultant":int(resultant),"sylvester_determinant":int(sylvester.det()),
"sylvester_matrix":[[int(a) for a in row] for row in rows],
"prime_remainders":{"2":int(disc)%2,"3":int(disc)%3},
"five_cycle_with_each_transposition":generator_checks,
"affine_countermodel":{"order":len(affine),"cycle_type_counts":{str(k):v for k,v in sorted(affine_types.items())},
                      "contains_odd_permutation":True,"contains_2_3_cycle":False},
"A5_conjugacy_class_sizes":class_sizes,"A5_union_sizes_including_identity":possible_normal_orders,
"A5_union_sizes_dividing60":orders_dividing60
},indent=2,allow_nan=False))

