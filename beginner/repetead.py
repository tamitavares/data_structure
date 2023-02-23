#Repeated Elements

numbers=[1,2,3,3,4,5,5]
aux=[]
repeated=[]

for i in numbers:
    if i not in aux:
        aux.append(i)
    else:
        if i not in repeated:
            repeated.append(i)
print("Repeated Elements: ", repeated)
