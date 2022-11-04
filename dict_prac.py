population_dict = {}

with open("/Users/anika/Documents/dicttable.csv","r") as f:
    for line in f:
        token = line.split(',')
        # print(token)
        place = token[0]
        population = token[1]
        population_dict[place] = population
print(population_dict)
