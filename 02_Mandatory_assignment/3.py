set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

#Of the 2 sets create a Union
print(set1.union(set2))

#Of the 2 sets create a Symmetric Difference
print(set1.symmetric_difference(set2))

#Of the 2 sets create a Difference
print(set2.difference(set1))

#Of the 2 sets create a disjoint
print(set1.isdisjoint(set2))