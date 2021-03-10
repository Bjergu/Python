##['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
##['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
##['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
##['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
##['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
##['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
##('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
##'Hello World Huston we are here' -> 'World Huston we'

a = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
print(a[1:5])
print(a[:2])
print(a[4:6])
print(a[4:5])
print(a[:1] + a[2:3] + a[4:5])
print(a[::-1])
b = 'Hello World Huston we are here'
print(b[6:21])