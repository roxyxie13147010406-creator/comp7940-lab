# === COMP7940 Lab1 Python Exercises 1-3 ===
# 基于原始文件扩写，保留所有原始框架和注释

# Exercise 1: Factors
# Write a program to print all factors of a number:
# Find all the factors of x using a loop and the operator %
# % means find remainder, for example 10 % 2 = 0; 10 % 3 = 1
print("===== Exercise 1 =====")
x = 52633
print(f"Factors of {x}:")
print(1)
for i in range(2, x):
    if x % i == 0:
        print(i)
print(x)

# Exercise 2: Function
# Encapsulate the logic in a function:
# Write a function that prints all factors of the given parameter x
print("\n===== Exercise 2 =====")
def print_factor(x):
    print(f"Factors of {x}:")
    print(1)
    for i in range(2, x):
        if x % i == 0:
            print(i)
    print(x)
# 测试函数
print_factor(52633)

# Exercise 3: List Iteration
# Apply the function to a list:
# Write a program to find all factors of the numbers in the list l
print("\n===== Exercise 3 =====")
l = [52633, 8137, 1024, 999]
# 遍历列表并调用函数
print("=== All Factors of List Numbers ===")
for num in l:
    print_factor(num)