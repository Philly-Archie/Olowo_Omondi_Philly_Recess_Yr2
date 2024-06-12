# Dictionaries
# Creating amd using dictionaries
# Dictionary methods and operations


"""
Dictionaries in pythons are collections of keys and values.
-Unordered
-Mutable
-Indexed by keys

"""

# Create a dictionary for a student pursuing software engineering,
# Key must be name, age technology interest, course and year of study
# Put your own details

context = {
    'name' : 'Olowo Omondi Philly',
    'age' : 24,
    'technology interest' : 'cyber_security',
    'course' : 'Software engineering',
    'Year of study' : 2,
}

print(context['age'])

# Access values
# Modify values

# Execise 1: Modify age and technology
context['age'] = 30
context['technology interest'] = "DevOps"
print(context)

# Adding keys and values
context['email'] = 'olowophilly77@gmail.com'
print(context)

# Exercise 2: Remove key and value
context.pop("technology interest")
print(context)

# Or
# del context("technology interest")