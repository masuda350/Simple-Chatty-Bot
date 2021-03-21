number_1 = int(input())
number_2 = int(input())

if number_1 >= number_2:
    print(number_1)
    print(number_2)
else:
    print(number_2)
    print(number_1)

# Another solution 1
print(number_1 if number_2 < number_1 else number_2)
print(number_2 if number_2 < number_1 else number_1)

# Another solution 2
nums = [int(input()), int(input())]
print(max(nums))
print(min(nums))

# Another solution 3
v = int(input()), int(input())
print(max(v), min(v), sep='\n')