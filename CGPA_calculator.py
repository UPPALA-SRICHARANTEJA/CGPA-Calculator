n=int(input("Enter no.of sems : ")) 

sumuplist=[]
sumdownlist=[]

for i in range(n):

    print(i+1,"sem :")
    sub=int(input("enter no.of subs = "))

    marks=list(map(int, input("Enter marks seperated by space : ").split()))


    credits=list(map(float, input("Enter credits seperated by space : ").split()))


    uptotal_list=[]
    for j in range(sub):
        uptotal_list.append(marks[j]*credits[j])

    sumuptotal=sum(uptotal_list)
    sumuplist.append(sumuptotal)

    sumcredits=sum(credits)
    sumdownlist.append(sumcredits)

    total=sumuptotal/sumcredits

    print("\n")
    print("SGPA of",i+1,"sem = ",total)

    print("-----------------------------------------------------------\n")

CGPA=sum(sumuplist)/sum(sumdownlist)

print("CGPA = ",CGPA)
print("\n")

print("percentage = ",CGPA*9.5,"%")
