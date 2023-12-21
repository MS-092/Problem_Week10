
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


# Another solution using while loops, but it's so slow
n = int(input("Enter a number: "))

t = 0
bn = n

while t == 0:
    if bn % n == 0:
        nl = []
        for d in str(bn):
            if int(d) in nl:
                pass
            else:
                nl.append(int(d))

        if len(nl) == 1:
            t += 1
            print(f"The smallest beautiful number is {bn}")

    bn += 1

# Another solution, using while loops and still slow
def smallest_beautiful_number(x):
    current_number = x

    while True:
        digits = set(str(current_number))
        if len(digits) == 1 and '0' not in digits:
            return current_number
        current_number += x

def main():
    try:
        x = int(input("Enter a number: "))
        if x % 2 != 0 and x % 5 != 0:
            result = smallest_beautiful_number(x)
            print(f"The smallest beautiful number divisible by {x} is: {result}")
        else:
            print("Please enter a number that is not divisible by 2 and 5.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()