integers = list(input ("Enter list of intergers"))
result = 0
for i in integers:
    result += int(i)
print(result)
my_books = ("Who moved my cheese", "Power of your mind", "Join This Chariot", "Don't pack your bags yet", "My Children my Africa")
for book in my_books:
    print(book,"\n")

my_dict = {"name": input("Please enter your name ! \n"), 
           "age": input("Please enter your age :\n"),
           "favorite color": input("Please enter your favorite color :\n")
           }
print(my_dict)

set1 = set(input("Enter integers for the first set (separated by space): "))
set2 = set(input("Enter integers for the second set (separated by space): "))

common_elements = set1.intersection(set2)
print("The common elements between the two sets are:", common_elements)

list_of_words = input("Please type in your words seperated by a space")
list_of_words = list_of_words.split()
new_list = [word for word in list_of_words if len(word) % 2 != 0]
print(new_list)