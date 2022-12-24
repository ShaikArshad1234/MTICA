student=[[4,'Arshad',77,85],[39,'Naveen',79,86],
         [5,'Arun',81,89],[45,'Pratap',77,83]]
student.sort()
print(student)
student.sort(key=lambda temp:temp[2])
print(student)
student.sort(key=lambda temp:temp[3])
print(student)
