def count_as(file_name):
    try:
        myfile = open(file_name, 'r')
        text = myfile.read()
        to_find = 'a'
        to_find2 = 'A'
        splitted = text.split(to_find)
        splitted2 = text.split(to_find2)
        number_of_a = len(splitted) - 1 + len(splitted2) - 1
        return number_of_a
    except FileNotFoundError:
        return 0
    # Create a function that takes a filename as string parameter,
    # counts the occurances of the letter "a", and returns it as a number.
    # If the file does not exist, the function should return 0 and not break.

print(count_as('afile.txt')) # should print 28
print(count_as("not-a-file")) # should print 0
