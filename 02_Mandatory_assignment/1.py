directorsset = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}
managementset = {"Tine", "Trunte", "Rane"}
employeesset = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}

#who in the board of directors is not an employee?
print(directorsset.difference(employeesset))
#who in the board of directors is also an employee?
print(directorsset.intersection(employeesset))
#how many of the management is also member of the board?******
print(managementset.intersection(directorsset))
#All members of the managent also an employee
print(managementset.intersection(employeesset))
#All members of the management also in the board?
print(managementset.intersection(directorsset))
#Who is an employee, member of the management, and a member of the board?
print(employeesset.intersection(managementset.intersection(directorsset)))
#Who of the employee is neither a memeber or the board or management?
print(employeesset.difference(managementset,directorsset))