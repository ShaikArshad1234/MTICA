def count_spechar(s):
    spechar=0
    for i in s:
        if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ\
        abcdefghijklmnopqrstuvwxyz0123456789':
            spechar+=1
    return spechar
str1=input()
a=count_spechar(str1)
print("no of special character in:",str1,"is",a)
 
