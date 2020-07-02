def name_of_best(sales,customers):
    sales1=sorted(sales)
    print("the best customer:",end="")
    if sales1.index(max(sales1))<(len(sales)-1):
        for i in range(len(sales)):
            if sales[i]==max(sales):
                print(customers[i],end=" ")
    else:
        print(customers[sales.index(max(sales))])

sales=[]
customers=[]
print("enter the customers name and money,divide them by space:")
nameandmoney=input()
my_list=nameandmoney.split(" ")
m=my_list[1::2]
n=my_list[0::2]
for i in range(len(m)):
    sales.append(int(m[i]))
    customers.append(n[i])
name_of_best(sales,customers)

