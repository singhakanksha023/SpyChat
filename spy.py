#importing details of default user
from spy_details import spy,Spy,ChatMessage
#Steganography library is used to hide message inside image
from steganography.steganography import Steganography

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']
FRIENDS=[]

# Delete the spy when speaking too much(100 words)
def delete_spy(secret_text,spy_index):
    if len(secret_text.split())>100:
        print "Spy is speacking to much."
        del FRIENDS[spy_index]
        print "Spy is deleted."

################################## ADD STATUS ##########################
def add_status(current_status_message):
    updated_status_message = None
    #display the current status message
    if current_status_message != None:
        print 'Your current status message is %s \n' % (current_status_message)
    else:
        print 'You don\'t have any status message currently \n'
    #choose from the older status updates or create a new status update
    default = raw_input("Do you want to select from the older status (y/n)? ")
    #add a new status update add it to the older status messages and set it as the current one
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")
        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    #select from the older status updates
    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1
        message_selection = int(raw_input("\nChoose from the above messages "))
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'
    #print the updated status message
    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'
    return updated_status_message


####################### ADD FRIEND ########################################
def add_friend():
    new_friend = Spy ('','',0,0.0)
    #input name, age and rating of spy friend
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation= raw_input("Are they Mr. or Ms.?: ")
    new_friend.name = new_friend.salutation + " " + new_friend.name
    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)
    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)
    #check name is not empty, age is greater than 12 and rating of the friend spy is greater than or equal to the user spy rating
    if len(new_friend.name) > 0 :
        if new_friend.age > 12:
            if new_friend.rating >= spy.rating:
                FRIENDS.append(new_friend)
                print 'Friend Added!'
            else:
                print 'Sorry! Invalid rating entry. We can\'t add spy with the details you provided'
        else:
            print 'Sorry! Invalid age entry. We can\'t add spy with the details you provided'
    else:
        print 'Sorry! Invalid name entry. We can\'t add spy with the details you provided'
    #return number of spy friends user has
    return len(FRIENDS)

######################### SELECT A FRIEND ####################################
def select_a_friend():
    item_position = 1
    #list all spy friends added by the user
    for friend in FRIENDS:
        print "%d %s aged %d with rating %f is onlie" % (item_position, friend.name, friend.age, friend.rating)
        item_position = item_position + 1
    friend = raw_input("choose a friend from the above list")
    friend = int(friend)
    #return the index of the selected friend
    return friend-1

########################### SEND A MESSAGE ###############################
def send_a_message():
    #choose from the list of spy friends added by the user
    friend_choice = select_a_friend()
    print friend_choice
    #name of the image user want to encode the secret message with
    original_image = raw_input("What is the name of the image?")
    original_image = "secret\%s" %(original_image)
    output_path = raw_input("Save image as")
    #secret message want to hide
    output_path = "secret\%s" %(output_path)
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)
    new_chat = ChatMessage(text,True)
    #Append the chat message to 'chats' key for the friends list
    FRIENDS[friend_choice].chats.append(new_chat)
    print "Your secret message image is ready!"

################### READ A MESSAGE #######################################
def read_a_message():
    #choose from the list of spy friends added by the user
    sender = select_a_friend()
    #input the name of the image they want to decode the message from
    output_path = raw_input("What is the name of the file?")
    output_path = "secret\%s" %(output_path)
    secret_text = Steganography.decode(output_path)
    new_chat = ChatMessage(secret_text,False)
    #Append the chat message to 'chats' key for the friends
    FRIENDS[sender].chats.append(new_chat)
    print "Your secret message has been saved!"
    #deleting spy for speaking too much
    delete_spy(secret_text,sender)

####################### READ CHAT (CHAT HISTORY) ####################################
def read_chat():
    #choose from the list of spy friends added by the user
    friend_choice = select_a_friend()
    print '\n'
    #read the entire chat history of a particular friend
    for chat in FRIENDS[friend_choice].chats:
        if chat.sender_is_me:
            #printing Time in Blue, Spy Name in Red, Message in Black
            print u"[\x1b[34mmy %s \x1b[0m] \x1b[31m %s \x1b[0m: %s" %(chat.time.strftime("%d %B %Y"),'Send by you:',chat.message)
        else:
            print u"[\x1b[34mmy %s \x1b[0m] \x1b[31m %s \x1b[0m: %s" % (chat.time.strftime("%d %B %Y"), FRIENDS[friend_choice].name, chat.message)

############################### M E N U #######################################
def start_chat(spy):
    current_status_message = None
    show_menu = True
    while show_menu:
        menu_choices = raw_input("\nAPP MENU:\n1) Add a status update \n2) Add a friend \n3) Send a secret message \n4) Read a secret message \n5) Read chats from a user \n6) Close application \n")
        menu_choices = int(menu_choices)
        if menu_choices == 1:
            current_status_message = add_status(current_status_message)
        elif menu_choices == 2:
            number_of_friends = add_friend()
            #print the number of friends the user has
            print 'You have %d friends' % (number_of_friends)
        elif menu_choices == 3:
            send_a_message()
        elif menu_choices == 4:
            read_a_message()
        elif menu_choices == 5:
            read_chat()
        elif menu_choices == 6:
            show_menu = False
        else:
            print "Wrong choice"

############################START SPYCHAT##############################

print "Let's get started"
user = raw_input(" if they want to continue with \n1-default user \n2-create their own\n")

#for default user
if int(user)==1:
    # spy rating displaying if, elif and else sequence
    if spy.rating > 4.5:
        print "Great ace!"
    elif spy.rating > 3.5:
        print "You are one of the good ones."
    elif spy.rating > 2.5:
        print "You can always do better."
    else:
        print "We can always use somebody to help in the office."
    #welcome message with the name, salutation, age and rating of the spy.
    print "Authentication complete \n Welcome %s age: %d and rating : %.1f .Proud to be have you onboard\n" % (
        spy.name, spy.age, spy.rating)
    # Entering into menu
    start_chat(spy)

#For custom user app should ask for the name of the user
elif int(user)==2:
    spy.name=raw_input("Welcome to spy chat, you must tell your spy name first:")
    # check that the user has not entered an invalid name
    if len(spy.name)>0:
        print "Welcome "+ spy.name +" .Glad to have you back with us."
        #input the salutaion the user wants to be used in front of their name
        spy.salutation = raw_input("Should I call you Mr. or Ms.?")
        spy.name= spy.salutation +" "+spy.name
        print "Alright "+spy.name+" I'd like to know a little bit more about you!"
    else:
        print "A Spy needs to have a valid name. Try again please."

    spy.age= raw_input("What is your age?")
    spy.age=int(spy.age)
    #age of the user is greater than 12 and less than 50
    if spy.age>12 or spy.age<50:
        spy.rating= raw_input("Whatis your spy rating")
        spy.rating=float(spy.rating)
    else:
        print "sorry you are not of the correct age to be a spy"
    spy.is_online = True
    #spy rating displaying if, elif and else sequence
    if spy.rating > 4.5:
        print "Great ace!"
    elif spy.rating > 3.5:
        print "You are one of the good ones."
    elif spy.rating > 2.5:
        print "You can always do better."
    else:
        print "We can always use somebody to help in the office."
    #welcome message with the name, salutation, age and rating of the spy
    print "Authentication complete \n Welcome %s age: %d and rating : %.1f .Proud to be have you onboard\n" % (
    spy.name, spy.age, spy.rating)
    #Entering into menu
    start_chat(spy)