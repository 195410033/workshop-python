squares = [1, 4, 9, 16, 25]
squares


squares[0]  # indexing returns the item
squares[-1]
squares[-3:]  # slicing returns a new list


squares[:]


squares + [36, 49, 64, 81, 100]


cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
cubes


cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters

# replace some values
letters[2:5] = ['C', 'D', 'E']
letters

# now remove them
letters[2:5] = []
letters

# clear the list by replacing all the elements with an empty list
letters[:] = []
letters


letters = ['a', 'b', 'c', 'd']
len(letters)


a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
x[0]
x[0][1]