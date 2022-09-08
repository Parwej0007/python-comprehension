# Performing operation inside list (we interate, condition)
# List comprehension is basically creating lists based on existing iterables. 
# It can also be described as representing for and if loops with a simpler and
#  more appealing syntax. List comprehensions are relatively faster than for loops.
#  [x for x in a if x > 5]

#-------------------------------------------------------------------------------#
# if age is greater than 20 means mature person 
# [21-> mature , 14-adult]

age = [14, 27, 18, 32, 24, 12, 26, 21, 23, 14]

# only If condition with for loop
L = [a for a in age if a>=20]

#---------------------------------------------------------------------------------#

# IF , Else conditional with for loop 
# L = [(print(if)) IF(a>10) is Ture Else (Print(else))  for a in loop]
L1 = [f'{a} -> Mature' if a >= 20 else f'{a} -> Adult' for a in age  ]
print(L1)

#----------------------------------------------------------------------------------#

# print name start with "c"

names = ['Ch','Dh','Eh','cb','Tb','Td']

name = [name for name in names if name.lower().startswith('c')]
print(name)

#-----------------------------------------------------------------------------------#

# remove neasted list into single list

vals = [[1,2,3],[4,5,2],[3,2,6]]

list1 = [x for v in vals for x in v]
print(list1)

# want string whose len is greater than 3
text = [['bar','foo','fooba'],['Rome','Madrid','Houston'], ['aa','bb','cc','dd']]

list2 = [x for t in text for x in t if len(x) > 3]
print(list2)

# want list whose length is greater than 3 and store in single list
text = [['bar','foo','fooba'],['Rome','Madrid','Houston'], ['aa','bb','cc','dd']]

list3 = [x for t in text if len(t) > 3 for x in t]
print(list3)

