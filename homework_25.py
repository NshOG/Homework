import json

#
# list1 = []
# for i in range(1_000_001):
#     if i % 2 != 0:
#         list1.append(i)
#
# with open("oddnumbers.json", "w") as f:
#     json.dump(list1, f)

with open("oddnumbers.json", "r") as f:
    oddnumbers = json.load(f)

newodd = filter(lambda x: x % 3 == 0, oddnumbers)
newodd = list(newodd)
print(sum(newodd) / len(newodd))

dict_1 = {1: 'red',
          2: 'green',
          3: 'black',
          4: 'white',
          5: 'black'}

dict_2 = {}
for i, j in dict_1.items():
    dict_2[j] = i
print(dict_2)

dict_3 = {'a': [1, 8, 3, 7, 2],
          'b': [12, 4, 8, 4],
          'c': [9, 9, 2, 8, 5]}

for i,j in dict_3.items():
    dict_3[i] = list(filter(lambda x: x % 2 != 0, j))
print(dict_3)


