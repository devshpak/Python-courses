import  random

n = int(input("Enter count of elements: "))
lst = list(random.sample(range(1,100),n))

print(lst)

for index, item in enumerate(lst):
    print("item ", index, " is ", item )

print ("Sum of elements : ",sum(lst))
print ("Average of elements : ",sum(lst)/len(lst))