# Mandatory af KCN

print("\n\n\t# OPGAVE 1")
# Model an organisation of employees, management and board of directors in 3 sets.
# Board of directors: Benny, Hans, Tine, Mille, Torben, Troels, Søren
# Management: Tine, Trunte, Rane
# Employees: Niels, Anna, Tine, Ole, Trunte, Bent, Rane, Allan, Stine, Claus, James, Lars

board = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
management = {'Tine', 'Trunte', 'Rane'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

print("Data:\nBoard:\t\t" + str(board))
print("Management:\t" + str(management))
print("Employees:\t" + str(employees))

question1A = 'who in the board of directors is not an employee?'
question1B = 'who in the board of directors is also an employee?'
question1C = 'how many of the management is also member of the board?'
question1D = 'All members of the managent also an employee'
question1E = 'All members of the management also in the board?'
question1F = 'Who is an employee, member of the management, and a member of the board?'
question1G = 'Who of the employee is neither a memeber or the board or management'

# 'who in the board of directors is not an employee?'
print("\n\n" + question1A)

boardNotEmployee = board.copy()
for person in employees:
    boardNotEmployee.discard(person)

print(boardNotEmployee)

# 'who in the board of directors is also an employee?'
print("\n\n" + question1B)

bothBoardAndEmployee = board.intersection(employees)

print(bothBoardAndEmployee)

# how many of the management is also member of the board?
print("\n\n" + question1C)

bothBoardAndManagement = board.intersection(management)

print("The intersection between the board and management has\t" + str(len(bothBoardAndManagement)) + " member(s)")

# All members of the managent also an employee
print("\n\n" + question1D)

intersectBtwManagementAndEmployee = management.intersection(employees)

print(intersectBtwManagementAndEmployee)

# All members of the management also in the board?
print("\n\n" + question1E)

print(bothBoardAndManagement)

# Who is an employee, member of the management, and a member of the board?
print("\n\n" + question1F)

intersectOfAllRanks = board.intersection(management, employees)
print(intersectOfAllRanks)

#
print("\n\n" + question1G)
onlyEmployee = employees.difference(management, board)
print(onlyEmployee)

print("\n\n\t# OPGAVE 2")
# Using a list comprehension create a list of tuples from the folowing datastructure
# {‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}
print("Using a list comprehension create a list of tuples from the folowing datastructure")
# SOLUTION WITHOUT LIST COMPREHENSION : WORKS FINE
# tupleList = []
# # newing up dictionary
# alphaGamma = {"a": "Alpha", "b": "Beta", "g": "Gamma"}
# for latin, greek in alphaGamma.items():
#     tupleList.append((latin, greek))

# SOLUTION WITH LIST COMPREHENSION
alphaBetaGamma = {"a": "Alpha", "b": "Beta", "g": "Gamma"}
newTupleList = [(latin, greek) for latin, greek in alphaBetaGamma.items()]

print(alphaBetaGamma)
print(newTupleList)

print("\n\n\t# OPGAVE 3")
# From these 2 sets:{'a', 'e', 'i', 'o', 'u', 'y'}
# {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}
# Of the 2 sets create a: Union
# Of the 2 sets create a: Symmetric Difference
# Of the 2 sets create a: Difference
# Of the 2 sets create a: Disjoint

setA = {"a", "e", "i", "o", "u", "y"}
setB = {"a", "e", "i", "o", "u", "y", "æ", "ø", "å"}
print("setA\t" + str(setA))
print("setB\t" + str(setB))

print("\n# Of the 2 sets create a: Union")
unionAB = setA.union(setB)
print(unionAB)

print("\n\n# Of the 2 sets create a: Symmetric Difference")
symmetricDiffAB = setA.symmetric_difference(setB)
print(symmetricDiffAB)

print("\n\n# Of the 2 sets create a: Difference")
differenceAB = setB.difference(setA)
print(differenceAB)

print("\n\n# Of the 2 sets create a: Disjoint")
commonAB = setA.intersection(setB)
disjointA = setA.difference(commonAB)
disjointB = setB.difference(commonAB)
print("Set A disjoint:\t" + str(disjointA))
print("Set B disjoint:\t" + str(disjointB))

print("\n\n\t# OPGAVE 4")
print("# Date Decoder.")
print("# A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.")
print("# Create a dict suitable for decoding month names to numbers.")
print("# Create a function which uses string operations to split the date into 3 items using the '-' character.")
print("# Translate the month, correct the year to include all of the digits.")
print(" The function will accept a date in the 'dd-MMM-yy' format and respond with a tuple of ( y , m , d ).")

months = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7,
          "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12}


def dateStringToTuple(stringDate):
    partedDate = stringDate.split('-')
    return {partedDate[2], months[partedDate[1]], partedDate[0]}


print("\nSupplying test case: 22-FEB-12")
print(dateStringToTuple("22-FEB-12"))
print("Supplying test case: 22-FEB-12")
print(dateStringToTuple("22-FEB-12"))
