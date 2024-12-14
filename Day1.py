print(type(1) == int)

print(42,500,900)
print(3.4, "hello" + str( 45 ))
print(str(18))
x = '10'
y = x
y += '10'
print(x)
hell_0 = 100
print(hell_0)
my_list = [0, 1, 2, 3, 4, 5]
print(my_list[1:4:2])  # Output: [1, 2, 3]
print(list(range(5)))
answer = 'Y'
if answer == 'Y' and answer == 'y':
   print('Continuing!')
   
print('p' in 'apple')
print('i' in 'apple')
print('ap' in 'apple')
print('pa' in 'apple')
import copy

# Create a list containing another list (nested list)
original_list = [1, 2, [3, 4]]

# Perform a shallow copy
shallow_copied_list = copy.copy(original_list)

# Modify the nested list
shallow_copied_list[2].append(5)
shallow_copied_list[0] = 100

# Both lists are affected
print("Original List:", original_list)  # Output: Original List: [1, 2, [3, 4, 5]]
print("Shallow Copied List:", shallow_copied_list)  # Output: Shallow Copied List: [1, 2, [3, 4, 5]]

x = 'hello'
# x[0] = 'g'
print(x[0])


alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']
print(alist)
alist[4:4] = ['e']
print(alist)

del alist[1]
print(alist)


print(f'Hello {x}!'.format('SL6'))

a = 5
b = 9
# setStr = 'The set is {​{}, {}​}​.'.format(a, b)
# print(setStr)


inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.values()))

for v in inventory.values():
    print("Got", v)


# key = inv bdon klam
# values just values
# items klh in ()
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.items()))

for k, v in inventory.items():
    print("Got", k, "that maps to", v)
print(inventory.keys())

x = 9

def adding():

    print(x)

adding()
def changeit(lst):
    lst[0] = "Michigan"
    lst[1] = "Wolverines"
    return lst

mylst = ['106', 'students', 'are', 'awesome']
newlst = changeit(list(mylst))
print(mylst)
print(newlst)

def test(alpha = 1.3,s:str,n:int):
    