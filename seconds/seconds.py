def seconds(alist):
    new_list = alist[1::2]
    return new_list

    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]

print(seconds([1, 2, 3, 4, 5])) # should print [2, 4]
