# WHAT IS HASH FUNCTION?

"""
WHAT DOES A HASH FUCTION DO?
in simple words, a hash function coverts a string key into an index of a list
"""
"""
IMPLEMENTING HASH FUNCTION USING ASCII:
COLLISION HANDLING IN HASH MAP: COMPLEXITY O(n)
"""
"""
COMPLEXITY --> LOOK UP BY KEY O(1)
           -->INSERTION/DELETION O(1)
"""


population_dict = {}
with open("/Users/anika/Documents/dicttable.csv","r") as f:
    for line in f:
        token = line.split(',')
        # print(token)
        place = token[0]
        population = token[1]
        population_dict[place] = population
print('population_dict',population_dict)



# ** WORK WITH DICTIONARIES **
# METHOD 1 --> DIFFERENT KEYS WITH SAME VALUES
keys = ['a','b','c','d']
dict_1 = {el:0 for el in keys}
print('dict_1',dict_1)




#METHOD 2 --> ONE DICTIONARY WITH DIFFERENT KEYS WITH DIFFERENT VALUES
vals = [1,2,3,4]
dict_3 = {}
for i in range(len(vals)):
    for j in range(len(keys)):
        if i ==j:
            key = keys[j]
            val = vals[i]
            dict_3[key] = val
print('dict_3',dict_3)


# METHOD 3 --> USING defaultdict
from collections import defaultdict
dist = ['Dhaka','Rajshahi']
precip = [20,30]
def def_value():
    return "Not Present"
d = defaultdict(def_value)
i= 0
for i in range(len(dist)-1):
    for j in precip:
        d[dist[i]] = j
        i+=1
print('dict_4',d)
print(d['Dhaka'])
print(d.get('Rajshahi'))



#METHOD 4 --> 
city = ['Dhaka','Rajshahi','Sylhet','Dhaka']
area = [20,30,40,50]
def_dict = defaultdict(list)
i = 0
for i in range(len(city)):
    for j in range(len(area)):
        if i == j:
            if city[i] in def_dict.keys():
                def_dict[city[i]].append(area[j])
            else:
                def_dict[city[i]].append(area[j])
print('dict_5',def_dict)
print(def_dict['Dhaka'])


# METHOD 4 --> A LIST OF DICTIONARIES WITH DIFFERENT KEYS AND DIFFERENT VALUES
list_1 = [1,2,3,4]
list_2 = ['a','b','c','d']
dict_list = []
for i in range(len(list_1)):
    for j in range(len(list_2)):
        if i == j:

            dict_new = {
                list_2[j]: list_1[i]
            }
            dict_list.append(dict_new)
print('DICT_6',dict_list)



# METHOD 5 --> LIST OF DICTIONARIES PAIRING EACH KEY WITH EVERY VALS OF THE VALUE LIST
list_3 =[]
fruits = ["Apple", "Pear", "Peach", "Banana"]
for i in range(len(list_2)):
    fruit_dictionary = dict.fromkeys(fruits, list_2[i])
    list_3.append(fruit_dictionary)
print('dict_7',list_3)



