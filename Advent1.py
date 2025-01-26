with open('Advent1.txt', 'r') as file:
    lines = file.readlines() # read numbers from .txt file
   # print(lines) # print lines 

array1 = [] # creating array1
array2 = [] # creating array2

for line in lines:
   
    both_numbers = line.rsplit(" ", 1)

    first_number = both_numbers[0]
    strip_first_number = first_number.strip()
    converted_first_number = int(strip_first_number)

    second_number = both_numbers[1]
    strip_second_number = second_number.strip()
    converted_second_number = int(strip_second_number)

    array1.append(converted_first_number)
    array2.append(converted_second_number)

array1.sort()
array2.sort() 
print(array1)
print(array2)

sum = 0
for i, value in enumerate(array1):
    distance = abs(array1[i] - array2[i])
    sum=sum+distance

print(sum)