# method code challenge
#

user_input_name = input("What is your name? ")
user_input_contact_info = input("What is your contact info? ")
user_id = input("What is your user ID?")

def show_my_info(in_name, in_contact_info, in_user_id):
    print("\n")
    print("!----------------------  Your Information  ----------------------!")
    print("User ID " + in_user_id)
    print("Name: " + in_name)
    print("Contact: " + in_contact_info)

show_my_info(user_input_name, user_input_contact_info, user_id)

