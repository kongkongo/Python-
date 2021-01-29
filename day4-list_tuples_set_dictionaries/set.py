# # Creating a Set
# # syntax
# st = {}
# # or
# st = set()
# # syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# # eg:
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# # Getting Set's Length
# st = {'item1', 'item2', 'item3', 'item4'}
# len(st)
# print(len(st))

# # Checking an Item
# st = {'item1', 'item2', 'item3', 'item4'}
# print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True

# # Adding Items to a Set
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.add('lime')#添加结果在首位
# print(fruits)

# # Add multiple items using update()     顺序随机
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
# fruits.update(vegetables)
# print(fruits)
# st = {'item1', 'item2', 'item3', 'item4'}
# st.update(['item5','item6','item7'])
# print(st)

# # Removing Items from a Set
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print(st)
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes the last element from the set
print(fruits)

# Clearing Items in a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

# Deleting a Set
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# del fruits
# print(fruits)


# Converting List to Set
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
print(fruits)

# Joining Sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

# Finding Intersection Items
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
print(st1.intersection(st2))

python = {'p', 'y', 't', 'h', 'o','n'}
dragon= {'d', 'r', 'a', 'g', 'o','n'}
print(python.intersection(dragon))     # {'o', 'n'})

# Checking Subset and Super Set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # Fales

# Checking the Difference Between Two Sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2


st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st

# Finding Symmetric Difference Between Two Sets

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}


# Joining Sets

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}

