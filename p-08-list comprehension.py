string='''Practice problems for
list comprehension in python.'''

ans=[]
for i in string:
    if i in 'AEIOUaeiou':
        ans.append(i)
print(*ans)


ans=[i for i in string if i in 'AEIOUaeiou']
print(len(ans))
