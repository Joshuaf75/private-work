#Lists and tuples works the same way, but tuples are immutable (cannot be changed) while lists are mutable (can be changed).
#Random list of developers
developer = ['Alice', 'Bob', ['Charlie', 'David'], ['Eve', 'Faythe']] #lists within lists
dad, mom, boys, girls = developer 
print(girls[1]) 

#Employee card
employee_card = ['Alice', 33, 'Engineer', 'New York']
name, age, position, location = employee_card
print(f"Name: {name}, Age: {age}, Position: {position}, Location: {location}")  # Output: Name: Alice, Age: 33, Position: Engineer, Location: New York

#Tuples are similar to lists, but they are immutable. You can use tuples when you want to ensure that the data cannot be changed. You can have lists in a tuple, but you cannot have a tuple in a list.
developer = ('Alice', 'Bob', ['Charlie', 'David'], ['Eve', 'Faythe']) #lists within lists
dad, mom, boys, girls = developer 
print(girls[1]) 

#Employee card
employee_card = ('Alice', 33, 'Engineer', 'New York')  
name, age, position, location = employee_card
print(f"Name: {name}, Age: {age}, Position: {position}, Location: {location}")  # Output: Name: Alice, Age: 33, Position: Engineer, Location: New York
