a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] 
alpha = input() 

for s in a: 
    alpha = alpha.replace(s, '*') 

print(len(alpha))
