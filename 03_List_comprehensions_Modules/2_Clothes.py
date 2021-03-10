colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

clothes = [(i,j) for i in colors for j in sizes]
print(clothes)

soled_out = [('Black', 'm'), ('White', 's')]

clothes2 = [(i,j) for i in colors for j in sizes if (i,j) not in soled_out]
print(clothes2)