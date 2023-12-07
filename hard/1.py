# logic i have used is to keep two pointers  left-i and right-j,
# then running a loop untill right pointer reaches end of array.
#here inside loop first i will see if the gap between left and 
# right pointer is less then or greater than window size.
#if its less simply i will increment right pointer along with check max among the traversed.
#if its more then same thing ill do but i will also move my right ponter
i=0 
j=0
k=1
arr=[1]
mx=-100000
while(j<len(arr)):
    if(j-i+1!=k):
        mx=max(arr[j],mx)
        j=j+1
    elif(j-i+1==k):
        mx=max(arr[j],mx)
        print(mx)
        i=i+1
        j=j+1