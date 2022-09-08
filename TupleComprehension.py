
#There is no tuple comprehension in Python. 
# Comprehension works by looping or iterating over items and 
# assigning them into a container, a Tuple is unable to receive assignments.
# tuple is mutable data type 


age = [14, 27, 18, 32, 24, 12, 26, 21, 23, 14]

# find age greater than 25

tuple1 = (a for a in age if a>=25)
# print tuple1 <generator object <genexpr> at 0x0000024B483C4900>
print(tuple(tuple1))