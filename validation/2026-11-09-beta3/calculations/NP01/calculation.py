import random,json
seed=20261109
rng=random.Random(seed)
plants=list(range(1,13));rng.shuffle(plants)
rows=[]
for pair in range(1,7):
    assignments=['A','B'];rng.shuffle(assignments)
    rows.append({'pair':pair,'light_zone':'saulaināka' if pair<=3 else 'mazāk saulaina','left':{'plant':plants[2*(pair-1)],'fertilizer':assignments[0]},'right':{'plant':plants[2*(pair-1)+1],'fertilizer':assignments[1]}})
assert all(sorted([r['left']['fertilizer'],r['right']['fertilizer']])==['A','B'] for r in rows)
print(json.dumps({'seed':seed,'kind':'generated random allocation, no growth measurements','layout':rows,'plants_per_treatment':6,'plants_per_treatment_per_light_zone':3,'independent_pairs':6,'measurement_days':[0,7,14,21,28],'total_repeated_measurements':60,'experimental_units':12,'within_pair_allocation_count':2**6,'smallest_nonzero_two_sided_p_for_extreme_sign_pattern':2/2**6},ensure_ascii=False,indent=2))
