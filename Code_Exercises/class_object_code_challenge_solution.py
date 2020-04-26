## This is a custom email message class

#definition of a custom_email class
class custom_email:
    def __init__(self, in_to, in_from, in_subject, in_message):
        self.email_to = in_to
        self.email_from = in_from
        self.email_subject = in_subject
        self.email_message = in_message

    def get_email_information(self):
        email_info = "To: " + self.email_to + ", " \
                            + "From: " + self.email_from + ", " \
                            + "Subject: " + self.email_subject + ", " \
                            + "Email Message: " + self.email_message
        return email_info
        

#Objects that are being created of type "email"
email_one = custom_email("John.Smith@gmail.com", "Lekueyen.Lee@gmail.com", "Custom email - #1", "Hello and welcome to the awesome world of Python Programming.")
print(email_one.get_email_information())

print("\r")

email_two = custom_email("Sammy@gmail.com", "Tommy@gmail.com", "Custom email - #2", "Hello, this is an interesting python coding challenge")
print(email_two.get_email_information())