#the logic here i have used is keeping a dictonary to keep track of occurence of 
# each number of array.
# and i do this with help of setdefault method which returns a value if alredy present 
# or else defaullt value if not present then incrementing by one.
# After that traversing dictonary and appending the numbers(keys of dictionary) 
# which have value greater than length of arr/3
inp=[2, 2, 3, 1, 3, 2, 1, 1]

occ={}
res=[]
for i in inp:
    j=occ.setdefault(i,0)
    j=j+1
    occ[i]=j

for i,j in occ.items():
    if(j>int(len(inp)/3)):
        res.append(i)
print(res)