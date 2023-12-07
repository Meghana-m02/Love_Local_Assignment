#sr=13
sr=input()# we are taking the input number as string
res=0# initilzing to print result
for i in range(1,int(sr)+1): #provinding range by coveting to int and adding one to include the number
    st=str(i) #converting to str in order to use count method which works only on string,returning number of occurences of given letter
    if(st.count("1")!=0): #check if one 1 is present or not if yes adding the no of occurence to the res else not 
        res+=st.count("1")
print(res)