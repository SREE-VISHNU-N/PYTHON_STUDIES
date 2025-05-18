#Get 10 inputs from user , then find the sum and average of those inputs
a=[]
print("Enter 10 numers : ")
for i in range(5):
    get=int(input("Enter "+str(i+1)+" num : "))
    a.append(get)


sum=0
count=0
for i in a:
    sum=sum+i
    count=count+1

avg=sum/count

print("The value of A is : ",a)
print("The sum is : ",sum)
print("The average is : ",avg) 


"""a = []
a.append(10)
a.append(20)
b=int(input())
a.append(b)
a.append(50)
print(a)"""



