def find_smallest_beautiful_number(x):
    max_num = 10 ** len(str(x)) - 1
    smallest_beautiful_number = -1

    for num in range(x, max_num + 1, x):
        num_str = str(num)
        if len(set(num_str)) == 1 and int(num_str[0]) != 0:
            smallest_beautiful_number = num
            break

    return smallest_beautiful_number if smallest_beautiful_number != -1 else "No beautiful number divisible by {} so I will return 111111 as an exception".format(x)

smallest = int(input("Enter number: "))
print(find_smallest_beautiful_number(smallest))