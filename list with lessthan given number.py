

##dict={'Arshad':1200,'Naveen':2000,'Arun':2400,'Prathap':1600,
##      'Gangully':2500,'Manohar':13600,'Praveen':110}

dict={'sedan':1500, 'svu':2000,'pickup':2500,'minivan':1600,'van':2400,
      'semi':13600,'bicyle':7,'motorcycle':110}
ans=[]
for i in dict:
    if dict[i]<5000:
        ans.append(i.upper())
print(ans)
    
