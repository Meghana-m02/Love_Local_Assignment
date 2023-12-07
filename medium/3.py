#the logic i have used here is temp = dp[j] is used to temporarily store 
# the previous value in the dp array.
#If the current cell in the matrix is 1then dp[j] is updated to the minimum of the left, upper, and upper-left neighbors in the dp array, plus 1.
#length is updated to the maximum of the current dp[j] and the previous max length.
#If the current cell in the matrix is 0 then dp[j] is set to 0.
#back = temp is used to store the previous value in the dp array before it was updated.
matrix = [["1","0","1","0","0"],
    ["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]
]

row=len(matrix) 
col=len(matrix[0])
dp=[0]*(col + 1)  
length=0
back=0  
for i in range(1,row+1):
    for j in range(1,col+1):
        temp=dp[j]
        if matrix[i-1][j-1]=='1':
            dp[j]=min(dp[j-1],back,dp[j])+1
            length=max(length,dp[j])
        else:
            dp[j]=0
        back=temp

print(length*length)