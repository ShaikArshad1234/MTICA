
f0=open(r"C:\Users\User\Desktop\Pythonpractice04\Day10\append.txt","r")
f1=open(r"C:\Users\User\Desktop\Pythonpractice04\Day10\Apd1.txt","w+")

temp=f0.read()
f1.write(temp)
f0.close()
f1.close()
print("File Copied")
