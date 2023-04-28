num_list = list(map(int, input("Enter a list of integers separated by space: ").split()))
triple = lambda x: x * 3
tripled_list = list(map(triple, num_list))

print("Original list: ", num_list)
print("List after tripling all numbers: ", tripled_list)
