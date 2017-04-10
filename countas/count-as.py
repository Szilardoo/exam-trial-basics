def count_as(file_name):
    try:
        counts = {'a' : 0}
        myfile = open(file_name, 'r')
        text = myfile.read()
        for letter in data:
            counts[letter] += 1
        return counts
    except FileNotFoundError:
        return 0
    # Create a function that takes a filename as string parameter,
    # counts the occurances of the letter "a", and returns it as a number.
    # If the file does not exist, the function should return 0 and not break.

print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0
