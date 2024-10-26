# Accessible anywhere
my_global_var = 1


def my_function():
    # Only accessible within my_function()
    my_local_var = 2
    return my_local_var


for _ in range(10):
    # Accessible anywhere
    my_block_var = 3

print(my_global_var)
print(my_function())
print(my_block_var)