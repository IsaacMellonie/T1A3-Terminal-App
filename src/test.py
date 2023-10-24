import csv

my_file = open("credentials.csv", "r+" )
print("The contents before appending:")
print(my_file.read())
emails_dict = {"email": "isaaceveans@gmail.com", "name": "Isaac"}
print("The dictionary is:")
print(emails_dict)
writer = csv.writer(my_file)
writer.writerow(emails_dict.values())
my_file.close()
my_file = open("credentials.csv", "r")
print("The content of this file after appending is:")
print(my_file.read())