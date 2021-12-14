number = 10
array = [1, 2, 3, 4]

print( all(number == a for a in array) )
# False

array = [10, 10, 10, 10]
print( all(number == a for a in array) )
# True