lst = [chr(i) for i in range(65, 91)]
print(lst)

lst1 = [chr(i) for i in range(65, 91) if i not in [70, 75, 80, 85]]
print(lst1)

lst2 = [chr(i) for i in range(65, 91) if i not in range(70, 80, 2)]

print("index of O: ", ord("O"))

print(lst2)