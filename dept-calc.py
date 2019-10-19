from random import randint

#number of friends who have depts to each other
number_of_people = 4

#list of depts
depts = []

# a dept is a tuple(who should give, who should get, amount of money).

number_of_depts = 10

for i in range(number_of_depts):
    a = randint(0, number_of_people - 1)
    b = randint(0, number_of_people - 1)
    c = randint(0, 100)

    if not(a == b):
        dept = (a, b ,c)
        depts.append(dept)

# a node-node matrix to save depts graph between peope
depts_matrix = [[0 for i in range(number_of_people)] for j in range(number_of_people)]

# add depts to matrix
for dept in depts:
    a, b, c = dept
    depts_matrix[a][b] += c

# simplify transactions between people (two by two)
for a in range(number_of_people):
    for b in range(number_of_people):
        depts_matrix[a][b] -= depts_matrix[b][a]
        depts_matrix[b][a] = - depts_matrix[a][b]

# after this matrix will be like this for 3 people:
# [0, +a, +b]
# [-a, 0, +c]
# [-b, -c, 0]

# after this, we assume that people are friends
# sum of depts for each one
total_depth = [0 for i in range(number_of_people)]

# calculate who should give how much
for a in range(number_of_people):
    for b in range(number_of_people):
        total_depth[a] += depts_matrix[a][b]

print(total_depth)