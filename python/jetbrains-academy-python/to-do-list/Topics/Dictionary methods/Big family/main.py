# The following lines create dictionaries from the input. Do not modify them, please
first_family = json.loads(input())
second_family = json.loads(input())
# first_family = {"wife": "Janet", "wife's mother": "Katie", "wife's father": "George"}
# second_family = {"husband": "Leon", "husband's mother": "Eva", "husband's father": "Gaspard", "husband's sister": "Isabelle"}

# Work with the 'first_family' and 'second_family' and create a new dictionary
new_family = dict()
new_family.update(first_family)
new_family.update(second_family)
# Also works
# new_family = {**first_family, **second_family}
print(new_family)
