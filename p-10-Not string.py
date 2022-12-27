string='practice problem for list comprehension in python' 
ans=[]
for i in string:
    if i not in 'AEIOUaeiou':
        ans.append(i)
print(*ans)
