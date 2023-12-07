#the logic i have used here is two pointer approach,i keep traversing both left and right pointer 
# untill left becomes greaterthan right.
#if char at left pointer index of input string and rignt pointer index are 
# same them left one is incremented and right one is decremented.
# If not same then the left pointer position is recorded in  
# array (we just need 1st position to append the required characters) and also the character 
# required that is at right pointer position(so i am basically forming a string).
#Then after that i am printing the resutant string by concatinating both the needed string and the input string according in respective position

st="abcd"
char=""
fre=[]
i=0
j=len(st)-1

    
while(i<j):
    if(st[i]==st[j]):
        i=i+1
        j=j-1
        continue
    else:
        fre.append(i)
        char+=st[j]
        j=j-1
if len(st)==0:
    print (" ")
elif len(st)==1:
    print (st*2)
else:
    print(st[:fre[0]]+char+st[fre[0]:])