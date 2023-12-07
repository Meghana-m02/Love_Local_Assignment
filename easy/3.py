#here the logic i have used is for 1st row i will append 1 to output.
# if not first row then first i will insert 1 to that row  as 
# first element then take the previous row and keep appending the sum of the adjacent items
# and at end again append 1.and i will repeat the same for number of rows asked

inp= int(input())
outpt=[]
for i in range(inp):
    row =[1] 
    if outpt:
        bdry=outpt[-1]
        for i in range(len(bdry)-1):
            row.append(bdry[i]+bdry[i+1])
        row.append(1)
      
    outpt.append(row)
print(outpt)