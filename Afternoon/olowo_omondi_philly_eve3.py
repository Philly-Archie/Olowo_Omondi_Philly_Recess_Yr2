# Day 4 presentation

# Advanced OOP Concepts

# • Encapsulation and data hiding
# • Magic methods and operator overloading
# • Composition vs. inheritance

# Ssentongo Henry Atanus (Encapsulation And Data Hiding)




# Kisembo Rodgers Bangirana (Magic Methods) 




# David Hope Kavuma (Operator Overloading)




# Olowo Omondi Philly (Composition Vs Inheritance)
# Inheritance is used where a class wants to derive the nature of parent class and then modify 
# or extend the functionality of it. 
# Inheritance will extend the functionality with extra features allows overriding of methods, 

# but in the case of Composition, we can only use that class we can not modify or extend the 
# functionality of it. It will not provide extra features. Thus, when one needs to use the 
# class as it without any modification, the composition is recommended and when one needs to 
# change the behavior of the method in another class, then inheritance is recommended.


# parent class 
class Region: 

	def m1(self): 
		print('We are in the central region') 

# child class inheriting parent class 
class District(Region): 

	# child class constructor 
	def __init__(self): 
		print('Child Class object created') 

	# child class method 
	def m2(self): 
		print('We are in Kampala District') 


# creating object of child class 
obj = District() 

# calling parent class m1() method 
obj.m1() 

# calling child class m2() method 
obj.m2() 



# Composition
# Composition in classes is done by the Has-A Relation
# Example Class A can have or contain an object in another class B



class Parent: 
	def __init__(self): 
		print('Parent class object created...') 

	def m1(self): 
		print('Parent class m1() method executed...') 


class Child: 
	def __init__(self): 

		# creating object of parent class 
		self.obj1 = Parent() 
		print('Child class object also created...') 

	def m2(self): 
		print('Child class m2() method executed...') 
		# calling m1() method of parent class 
		self.obj1.m1() 


# creating object of child class 
obj2 = Child() 

# calling m2() method of child class 
obj2.m2() 
