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




empty_list = []
object1 = CreateUser("sexyangel69@hotmail.com", "secretpassword1", "Isaac", "Eveans", "123wer")
object2 = CreateUser("evilangel69@hotmail.com", "secretpassword69", "Callum", "Ginty", "345wer")

empty_list.append(object1)
empty_list.append(object2)
# for i in empty_list:
#     if i.email == "evilangel69@hotmail.com":
#         print(i.email)
# print(empty_list[1].first)
object1.user_info()
quit()