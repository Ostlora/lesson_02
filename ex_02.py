el_count = int(input("Enter amount of elements - "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Enter next list value "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)