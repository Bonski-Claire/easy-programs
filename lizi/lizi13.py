def is_odd(n):
    return (n % 2) == 1


print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))
x = True
print(x)
print(type(x))
"""Can someone of the given age and citizenship status
    run for president in the US?"""
"""The US Constitution says you must be a natural born 
    citizen *and* at least 35 years old."""
"""If n == 1, Candicate gets the citizenship.Otherwise n == 0."""


def can_run_for_president(age, n):
    return (n == 1) and (age >= 35)


age1 = int(input("age1 = "))
n1 = int(input("citizen1 = "))
age2 = int(input("age2 = "))
n2 = int(input("citizen2 = "))
age3 = int(input("age3 = "))
n3 = int(input("citizen3 = "))
print("Can candicate1 run for president?", can_run_for_president(age1, n1))
print("Can candicate2 run for president?", can_run_for_president(age2, n2))
print("Can candicate3 run for president?", can_run_for_president(age3, n3))
