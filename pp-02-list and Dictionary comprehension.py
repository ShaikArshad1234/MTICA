
#use transpose of a matrix


m=[[1,2],[3,4],[5,6],[7,8]]
ans=[]
for i in range(len(m[0])):
    temp=[]
    for j in range(len(m)):
        temp.append(m[i][j])
    ans.append(temp)
print(ans)


