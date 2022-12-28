string='''
practice problems for list comprehensions in python
'''
wordlist=string.split(' ')
print(wordlist)
wordlist=[i.strip("\n") for i in wordlist]
print(wordlist)
ans={i:i[::-1] for i in wordlist}
print(ans)
 
