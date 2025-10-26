numbers = [1, 2, 3, 4, 5]

def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def find_avg(numbers):
    return sum(numbers) / len(numbers)

def Action(num, func):
    return func(num)



print("Choice:\n1:Maximum\n2:Minimum\n3:Arithmetic mean")
choice = input()

if choice == "1":
    res = Action(numbers, find_max)
elif choice == "2":
    res = Action(numbers, find_min)
elif choice == "3":
    res = Action(numbers, find_avg)
else:
    print("Error")

print(res)


