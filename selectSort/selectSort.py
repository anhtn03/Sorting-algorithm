array = [10,11,20,30,25,14]
print(array)

for i in range(len(array)):
    for j in range(i+1,len(array)):
        if(array[i] > array[j]):
           (array[i], array[j]) = (array[j], array[i])
print("Mảng đã được sắp xếp theo giải thuật selectSort:  ",array)
    

