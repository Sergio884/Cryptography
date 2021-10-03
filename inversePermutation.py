#Inverse Permutation
pix = [10,2,4,9,1,6,8,7,3,5]

x   = []
ix = []
for n in range(len(pix)):
    x.append(n+1)
    ix.append(0)


for i in range(len(x)):
    ix[pix[i]-1] = x[i]

print("  X  "+str(x))
print("X^-1 "+str(ix))