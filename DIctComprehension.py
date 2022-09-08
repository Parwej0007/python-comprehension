# Dict comprehension perform operation inside dictionary
# A dictionary is an unordered collection of key-value pairs

dict1 = {'data': 4, 'sciences': 7, 'machine': 7, 'learning': 8}
# for x,y in dict1.items():
#     print(x,y)

# find length of key
dict2 = {d:len(d) for d in dict1}
print(dict2)

dict3 = {d:len(d) for d in dict1 if len(d) >=7}
print(dict3)

dict4 = {d:len(d) if len(d) > 7 else "Sort" for d in dict1}
print(dict4)

######### use of Zip ##############

words = ['data', 'science', 'machine', 'learning']
values = [5, 3, 1, 8]

dict5 = {x:y for x, y in zip(words, values)}
print(dict5)