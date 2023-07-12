def list_length (some_list):
    # Base case - empty list
    if some_list == []:
        return 0
    else:
        # Remove one element from some_list, then compute the length of what's left over
        return list_length (some_list[1:]) + 1

# This function recursively returns the reverse of a string
def reverse(some_string):
    # Base case - empty string
    if some_string == '':
        return ''
    else:
        # Remove the last character of some string, reverse whatever is
        # left over, and then combine the two together
        return some_string[-1] + reverse(some_string[:-1])

print(list_length([]))
print(list_length([1]))
print(list_length([1, 2]))
print(list_length([1, 2, 3]))
print(list_length([1, 2, 3, 4]))
#print(list_length([0] * 1000))

tests = ['', 'a', 'am', 'cat', 'cats', 'sloth', 'sloths', 'racecar', 'racecars']
for t in tests:
    print(t, reverse(t))

"""
Results:
0
1
2
3
4
 
a a
am ma
cat tac
cats stac
sloth htols
sloths shtols
racecar racecar
racecars sracecar
"""