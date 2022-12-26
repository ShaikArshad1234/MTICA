def extract_spechar(s):
    spechar=''
    for i in s:
        if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ\
        abcdefghijklmnopqrstuvwxyz0123456789':
            spechar+=i
    return spechar
str1=input()
a=extract_spechar(str1)
print("no of special character in:",str1,"is",a)
 
