my_list = [10, 3, 6, 78, 22, 109, 99, 1]
list_second = [5, 2234, 655, 983, 22, 100]

# Task 1
print(max(my_list))

# Task 2
my_list.sort()
print("Second largest element is:", my_list[-2])


print("My list now is", my_list)
# Task 3
merged = my_list + list_second
print(sorted(merged))
# Task 4
first = my_list[0]
last = my_list[-1]
my_list[0] = last
my_list[-1] = first
print(my_list)

