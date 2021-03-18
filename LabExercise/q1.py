# N student take K apples and distribute them among each students eventually.
# the remaining parts remain in basket.
# how many apples should each student get?
# how many apples will remain in the basket?the programs read number N and K

N=int(input("enter the number of students in class: "))
K=int(input("enter the number of apples: "))
apples_get=(K//N)
remaining_apples =(K%N)
print(f"each student get {apples_get} ")
print(f"the remaining apples are {remaining_apples} ")