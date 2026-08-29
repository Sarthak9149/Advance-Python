my_list = [n for n in range(1, 11)]

my_list2 = [n * n for n in range(1, 11)]
# using map
mylist2_map = map(lambda n: n * n, my_list)
# print(list(mylist2_map))


# using filter
my_list3 = list(filter(lambda n: n % 2 == 0, my_list))

my_list4 = [n for n in range(1, 11) if n % 2 == 0]

# Cartesian Product (Multiple for clauses)
cart_prod = [(num, letter) for num in range(4) for letter in "abcd"]

# Safe Nested List Initialization
board = [["_"] * 3 for i in range(3)]


# Sequence filtering by predicate
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
pos = [n for n in mylist if n > 0]

# Simultaneous Transformation and Filtering
roots = [n**0.5 for n in mylist if n > 0]


# Conditional Value Replacement
clip_neg = [n if n > 0 else 0 for n in mylist]


# Memory profiling list comprehension instantiation
# x = [n for n in range(int(1e8))]
# print(x)
