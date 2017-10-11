from datetime import datetime
#class has details of each spy as declare variables for age, rating and online status with appropriate values for your spy

class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#default user
spy = Spy('Batman','Mr.', 23, 4.5)



# class contain the message, time of the message and a boolean indicating whether the sender was you or a friend
class ChatMessage:
    def __init__(self, message, sender_is_me):
        self.message = message
        self.time = datetime.now()
        self.sender_is_me = sender_is_me