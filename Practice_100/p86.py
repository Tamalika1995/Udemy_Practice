'''By using list comprehension, please write a program to print the list after
removing the value 24 in [12,24,35,24,88,120,155].'''
l=[12,24,35,24,88,120,155]
n=[i for i in l if i!=24]
print(n)
