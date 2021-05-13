# Creating class for the second scenario
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_attributes(self):
        print(self.name, self.age)

class officers(person):
    def __init__(self, name, age, years):
        super().__init__(name, age)
        self.years_of_service = years

    def officer_introduction(self, things_to_say, ):
        print(things_to_say)
        print("My name is " + self.name)
        print("My age is " + str(self.age))
        print("My years of service in the department is " + str(self.years_of_service))

    def arrest(self, things_to_say):
        print("Iam placing you under arrest. " + things_to_say)
    
class suspect(person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def innocence(self, things_to_say):
        print("Iam innocent! "+ things_to_say)

def get_user_name(toolslist):
    user_name = input("Lets start by knowing your name. What is your name? ")
    print(f"Ok {user_name}, your a police officer for Metro PD. As a police officer, you are equiped with tools to handle different scenarios. Depending on the situation will dictate which tool you will use.")
    print("Here is a list of tools you are equiped with: ") 
    print(toolslist)
    print("Now we will look at different scenarios and see how well you fair.")
    return user_name

def introduction():
    print("\tWelcome to COPS and ROBBERS!")
    print("\t\tBy JORIEL RIVAS")
    print("Here we will look a little into the life of a police officer. We'll look at some scenarios and see how well you handle them. We'll also take a deeper look at some of the tools used, such as firearms. Good luck on the scenarios!")
    
def first_scenario(user_name, toolslist):
    print(f"{user_name} you are patrolling on the streets of Downtown Blvd heading East.")
    print("You receive a call from dispatch of an active robbery at a gas station West of Downtown Blvd and Hiatus RD. ")
    print("Immediately you turn around, turn your lights on and head speed towards it since your closest to the locaiton. ")
    print("As you speed, dispatch notifies you that the suspect is a hispanic male, apprx 5'10, wearing a black shirt with blue jeans. Dispatch also notifies you that the suspect may be armed with a knife ")
    print("As you approach the gas station, you noticed someone with a similar discription running out of the gas station and runs towards the back of the building.")
    print("Immediately you give chase and cut off the suspect with your vehicle. You jump out of the vehicle and the suspect is in front of your vehicle. He is cornerd and has no where to go. He stands apprx 5 to 10 feet from you. ")
    print("At this point which tool do you use first? ")
    print("Your equipment: ")
    '''This for loop alows for all the items on the list to be listed one by one. '''
    for x in toolslist:
        print(x)
    first_option(toolslist)
    options = False
    while options == False:
        user_answer = input("Which option would you like to choose? A/B/C/D?")
        if user_answer.lower() == "a":
            print("You choose to pull a baton and tazer. A prudent choice since you don't want to shoot anyone.")
            print("You attempt to taze the suspect, however, the suspect quickly closed the distance and stabbed you on the neck.")
            print("Sorry, you chose the wrong tools.")
            print("The rule of thumb when confronting a suspected armed with a knife,")
            print("when a suspect is within 21 feet from you, is to pull your service weapon. Why? It has been statistically proven that")
            print("a suspect armed with a knife can close the distance and cut you within a matter of seconds if within 21 feet.")
            print("In fact it has been proven that an officer would need at least 21 feet distance from a knife wielding attacker to")
            print("have enough time to pull his/her service weapon, place the weapon on target, and shoot accurately to defend themselves.")
            options = True
        elif user_answer.lower() == "b":
            print("You choose to pull your firearm. The suspect initially posed to attack you, but was stopped on his tracks")
            print("when he saw your weapon. You quickly yell at him and demand that he stop and to raise his hands. He complies.")
            print("You maintain pointing your weapon, however you have not called for backup. Because of this, backup takes longer to arrive.")
            print("You rightly don't approach the suspect but try to keep him detained will pointing your weapon. Your arms are getting tired ")
            print("and you take a look to your left hoping that backup arrives. The suspect sees this hiccup in attention and decides to take a run")
            print("for it. He vanishes within the shadows of the passage way adjacent to you. The suspect got away.")
            print("Sorry this was not the right choice.")
            options = True
        elif user_answer.lower() == "c":
            print("You choose to pull your firearm. The suspect initially posed to attack you, but was stopped on his tracks")
            print("when he saw your weapon. You quickly yell at him and demand that he stop and to raise his hands. He complies.")
            print("You maintain pointing your weapon and call for backup. Immediately fellow officers arrive at the scene as you maintain")
            print("your distance and keep your focus on the suspect. Officers finally arrive with their guns drawn and order the suspect on the ground.")
            print("He complies and while officers maintain their weapons drawn, you go in to handcuff the suspect. Another officer assists you to try to secure the knife.")
            print("The suspect has been secured and everyone ended the day without getting hurt. Congratulations, you made the right choice.")
            options = True
        elif user_answer.lower() == "d":
            print("You choose to go hand to hand combat since your so good at it. However, the suspect is armed with a knife, and within seconds comes right under your neck and stabs you there.")
            print("Your attempt to stop lethal force with non lethal force has costed you your life. Sorry but this was not the right choice. ")
            print("The rule of thumb when confronting a suspected armed with a knife,")
            print("and is within 21 feet from you, is to pull your service weapon. Why? It has been statistically proven that")
            print("a suspect armed with a knife can close the distance and cut you within a matter of seconds if within 21 feet.")
            print("In fact it has been proven that an officer would need at least 21 feet distance from a knife wielding attacker ")
            print("have enough time to pull his/her weapon, place weapon on target, and shoot accurately to defend themselves.")
            options = True
        else:
            invalid_option()
            options == False
    return toolslist

def invalid_option():
    print("This is an invalid option. Please try again.")
'''Here is how we select which items in the list to display. REMEMBER THE FIRST ITEM ON THE LIST IS 0. SO IF YOU CHOOSE # 1, IT WILL BE THE SECOND ITEM ON THE LIST! '''
def first_option(toolslist):
    print("Option A ")
    print((toolslist[1:3]))
    print("Option B ")
    print((toolslist[3]))
    print("Option C ")
    print((toolslist[3:5]))
    print("or")
    print("Option D ")
    print((toolslist[5]))




def secondOption(toolslist, user_name):
    ''' Here we are using the append method to add an item to the list. We also use (len(toolslist)) to give a numerical value of all the items in the list. '''
    print("Here are other combinations that can be used for this scenario:")
    print("Lets start by adding a tool to our inventory. Lets add 'working with a partner': ")
    toolslist.append("Work with a partner")
    print(toolslist)
    print("How many tools do we now have in our inventory?")
    print(len(toolslist))
    print("If you don't want to add the last item, or would like to remove it, you can. ")
    pop_last(toolslist)
    delete_item(toolslist, user_name)
    print("Here's an updated list of your current inventory:")
    print(toolslist)
    print("Here is the quantity amount in your list: ")
    print(len(toolslist))

def pop_last(toolslist):
    ''' Here we are using the pop method to remove the last item from the list. '''
    this_option = False
    while this_option == False:
        remove_item = input("Would you like to remove the previously added item? Y/N?")
        if remove_item.lower() == "y":
            toolslist.pop()
            print("Tool has been removed.")
            print("Your newly updated list: ")
            print(toolslist)
            print("Total amount of tools left: ")
            print(len(toolslist))
            this_option = True
        elif remove_item.lower() == "n":
            print("Item was not removed from inventory")
            print("Current inventory: ")
            print(len(toolslist))
            this_option = True
        else:
            invalid_option()
            this_option = False

def delete_item(toolslist, user_name):
    '''Here we are going to use the del method to remove items from the list '''
    print(f"{user_name} would you like to delete an item? If so, just choose A through H going alphabetical order from the list. Heres the list for reference: ")
    print(toolslist)
    third_option = False
    while third_option == False:
        user_option = input("Which item would you like to delete? A/B/C/D/E/F/G or none?")
        if user_option.lower() == "a":
            del toolslist[0]
            print("Pepper Spray has been removed.")
            third_option = True
        elif user_option.lower() == "b":
            del toolslist[1]
            print("Baton has been removed.")
            third_option = True
        elif user_option.lower() == "c":
            del toolslist[2]
            print("Tazer has been removed.")
            third_option = True
        elif user_option.lower() == "d":
            del toolslist[3]
            print("Firearm has been removed.")
            third_option = True
        elif user_option.lower() == "e":
            del toolslist[4]
            print("Call for backup has been removed.")
            third_option = True
        elif user_option.lower() == "f":
            del toolslist[5]
            print("Hand to hand combat has been removed.")
            third_option = True
        elif user_option.lower() == "g":
            del toolslist[6]
            print("Handcuffs have been removed.")
            third_option = True
        elif user_option.lower() == "none":
            print("Nothing has been removed from your list as requested.")
            third_option = True
        else:
            invalid_option()
            third_option = False

def firearms():
    print("Here we will look at two popular brands used in Law Enforcement: 'Glock' and 'Sig Sauer': ")
    ''' Here we are making a cluster of dictionaries all under one family name. To access info on a particular module, call out the name of the model. See how the modules are called later in the function'''
    glock_dict = {
        "9mm models": {
        "Brand": "Glock",
        "Models": "19, 17, 26, 34, 43, 45, 48,",
        "Caliber": "9x9mm"
        },
        ".40 S&W models": {
        "Brand": "Glock",
        "Models": "22, 23, 27, 35,",
        "Caliber": ".40 S&W"
        },
        ".45 G.A.P models":{
        "Brand": "Glock",
        "Models": "37, 38, 39",
        "Caliber": ".45 G.A.P"
        }
    }
    sigsauer_dict = {
        "9mm models": {
        "Brand": "Sig Sauer",
        "Models": "P229, P226, P320, P365",
        "Caliber": "9x9mm"
        },
        ".40 S&W models": {
        "Brand": "Sig Sauer",
        "Models": "P229, P226, P320",
        "Caliber": "40 S&W"
        },
        ".10mm auto models": {
        "Brand": "Sig Sauer",
        "Models": "P220, P226, 1911",
        "Caliber": "10mm auto"
        }
    }
    ''' here we use a for loop to show all of the items in the dictionary.'''
    for x, y in glock_dict.items(): # this method will show the x and y of the dictionary. Notice how items() is called.
        print(x,y)   
    for x in sigsauer_dict.values(): # this method will show all the values of the dictionary. Notice how values() is called.
        print(x) # might seem redundant because they show the same information. However, ultimately the format is different.
    print("Firearms are characterized by the caliber size of the bullet. Common caliber sizes used by police officers are: ")
    firearms_list = ['1: 9mm', '2: 40 S&W','3: 45 G.A.P', '4: 10mm' ]
    print("Here is a list of calibers. Choose a number to know more about these calibers in relation to Glock and Sig Sauer: ")
    for x in firearms_list:
        print(x)
    fourth_option = False
    while fourth_option == False:
        user_choice_two = input("Which number choice whould you like to look at? 1, 2, 3, or 4? ")
        if user_choice_two == "1":
            print(glock_dict.get("9mm models"))
            print(sigsauer_dict.get("9mm models"))
            user_choice_three = input("Would you like to add color on the models? Yes or No? Choose y/n")
            if user_choice_three.lower() == "y":
                print("Black was now added to the model. Here's an updated list: ")
                glock_dict["color"] = "black" # here we are adding to the dicionary
                print(glock_dict)
                sigsauer_dict["color"] = "black"
                print("Black was now added to the model. Here's an updated list: ")
                print(sigsauer_dict)
                user_choice_four = input("Would you rather remove the color you just added to the models? Yes or No? Choose y/n")
                if user_choice_four.lower() == "y":
                    print("The last input has been removed.")
                    glock_dict.popitem()  # remove previous item
                    sigsauer_dict.popitem()
                    print("Updated Glock Dictionary: ")
                    print(glock_dict)
                    print("Updated Sig Sauer Dictionary: ")
                    print(sigsauer_dict)
                elif user_choice_four.lower() == "n":
                    print("Last input was not removed")    
            elif user_choice_three.lower() == "n":
                print("No color has been added")
            fourth_option = True
        elif user_choice_two == "2":
            print(glock_dict.get(".40 S&W models"))
            print(glock_dict.get(".40 S&W models"))
            user_choice_three = input("Would you like to add color on the models? Yes or No? Choose y/n")
            if user_choice_three.lower() == "y":
                print("Black was now added to the model. Here's an updated list: ")
                glock_dict["color"] = "black" # here we are adding to the dicionary
                print(glock_dict)
                sigsauer_dict["color"] = "black"
                print("Black was now added to the model. Here's an updated list: ")
                print(sigsauer_dict)
                user_choice_four = input("Would you rather remove the color you just added to the models? Yes or No? Choose y/n")
                if user_choice_four.lower() == "y":
                    print("The last input has been removed.")
                    glock_dict.popitem()  # remove previous item
                    sigsauer_dict.popitem()
                    print("Updated Glock Dictionary: ")
                    print(glock_dict)
                    print("Updated Sig Sauer Dictionary: ")
                    print(sigsauer_dict)
                elif user_choice_four.lower() == "n":
                    print("Last input was not removed")    
            elif user_choice_three.lower() == "n":
                print("No color has been added")
            fourth_option = True
        elif user_choice_two == "3":
            print(glock_dict.get(".45 G.A.P models"))
            user_choice_three = input("Would you like to add color on the models? Yes or No? Choose y/n")
            if user_choice_three.lower() == "y":
                print("Black was now added to the model. Here's an updated list: ")
                glock_dict["color"] = "black" # here we are adding to the dicionary
                print(glock_dict)
                sigsauer_dict["color"] = "black"
                print("Black was now added to the model. Here's an updated list: ")
                print(sigsauer_dict)
                user_choice_four = input("Would you rather remove the color you just added to the models? Yes or No? Choose y/n")
                if user_choice_four.lower() == "y":
                    print("The last input has been removed.")
                    glock_dict.popitem()  # remove previous item
                    sigsauer_dict.popitem()
                    print("Updated Glock Dictionary: ")
                    print(glock_dict)
                    print("Updated Sig Sauer Dictionary: ")
                    print(sigsauer_dict)
                elif user_choice_four.lower() == "n":
                    print("Last input was not removed")    
            elif user_choice_three.lower() == "n":
                print("No color has been added")
            fourth_option = True
        elif user_choice_two == "4":
            print(sigsauer_dict.get(".10mm auto models"))
            user_choice_three = input("Would you like to add color on the models? Yes or No? Choose y/n")
            if user_choice_three.lower() == "y":
                print("Black was now added to the model. Here's an updated list: ")
                glock_dict["color"] = "black" # here we are adding to the dicionary
                print(glock_dict)
                sigsauer_dict["color"] = "black"
                print("Black was now added to the model. Here's an updated list: ")
                print(sigsauer_dict)
                user_choice_four = input("Would you rather remove the color you just added to the models? Yes or No? Choose y/n")
                if user_choice_four.lower() == "y":
                    print("The last input has been removed.")
                    glock_dict.popitem()  # remove previous item
                    sigsauer_dict.popitem()
                    print("Updated Glock Dictionary: ")
                    print(glock_dict)
                    print("Updated Sig Sauer Dictionary: ")
                    print(sigsauer_dict)
                elif user_choice_four.lower() == "n":
                    print("Last input was not removed")    
            elif user_choice_three.lower() == "n":
                print("No color has been added")
            fourth_option = True
        else:
            invalid_option()
            fourth_option = False




def secondScenario(officers, person, toolslist):
    print("***********Now lets try the second scenario!************")
    print("You are a Sargent of the force.")
    print("Your task is to supervise your assigned officers.")
    print("As you get on the field, your introduced by each officer under your command: ")
    first_officer = officers("Officer Johnson", 42, 10)
    second_officer = officers("Officer Robinson", 32, 2 )
    detective = officers("Detective Milly", 49, 25)
    suspect_number_one = suspect("John Smith", 37)
    
    first_officer.officer_introduction("")
    print("It's good to be part of the team.")
    second_officer.officer_introduction(" ")
    print("Glad to be here. ")
    detective.officer_introduction("")
    print("Anything you need. Call me. ")

    print("Later on the evening. You get a call that Officer Johnson just pulled over a vehicle.")
    print("After running the plates on the vehicle, he discovered that he vehicle was registerd as stolen and the driver has a warrent for his arrest.")
    print("You arrive at the seen to assist with the arrest.")
    print("Officer Johnson cleared the suspect of any weapons.")
    print("Officer Johnson then tells the suspect the following: ")
    first_officer.arrest("Are you aware why I am placing you under arrest?")
    suspect_number_one.innocence("I did nothing!")
    print("The suspect decides to run away on foot. You and officer Johnson give chase. ")
    print("Officer Johnson manages to hold the suspect. But the suspect decides to fight back.")
    print("What tool should you use? ")
    print("Here's a list of your tools: ")

    for x in toolslist:
        print(x)
    first_option(toolslist)

    options = False
    while options == False:
        user_answer = input("Which option would you like to choose? A/B/C/D?")
        if user_answer.lower() == "a":
            print("You choose to pull a baton and tazer. A prudent choice since you don't want to shoot anyone.")
            print("You attempt to taze the suspect, but all prongs did not hit the suspect, making the taser ineffective.")
            print("You try a second tazer shot. All prongs hit, but the suspect shows a high tolerance of resistance. Now you pull your baton.")
            print("and as according to your training you use the baton for complience and strike the suspect in authorized areas. ")
            print("After landing strong blows on the thigh, Officer Johnson assist you by going behind the suspect and handcuff the suspect. ")
            print("The suspect complies. You and Officer Johnson managed to successfully arrest the suspect.")
            print("Good job, you made the right choice.")
            options = True
        elif user_answer.lower() == "b":
            print("You choose to pull your firearm. The suspect trys to run away with his back towards you. You fire your weapon.")
            print("The suspect is wounded. You call for backup and EMT to arrive to provide care.")
            print("But you shoot an armed suspect who's back was facing you. THIS IS WRONG.")
            print("For this reason, you go on adminstrative leave (as it's normal proceedure for any officer envolved shooting) and is investigated. ")
            print("After carefull review by the Internal Affairs, they state finds you guilty for attempted manslaughter and face years of prison.")
            print("Sorry, you choose the wrong option. You wouldn't have failed if you only pulled your weapon and attempted to arrest the suspect. But the ")
            print("fact that you shot the suspect while he was running away and knowing that he was not armed subjects you to charges placed against you.")
            options = True
        elif user_answer.lower() == "c":
            print("You choose to pull your firearm. The suspect trys to run away with his back towards you. You give chase while calling for backup.")
            print("You yell at the suspect to stop running, and more officers come from the opposite way, stopping the suspect on his tracks.")
            print("You maintain pointing your weapon and order the suspect to get down on the ground. He complies. You order the other officers to initialized the arrest. ")
            print("Officers comply to your orders and the suspect is now in custody. ")
            print("Great job, you choose the right option.")
            print("The suspect has been secured and everyone ended the day without getting hurt.")
            options = True
        elif user_answer.lower() == "d":
            print("You choose to go hand to hand combat since your so good at it. However, this proves exhaustive as the suspect is very skilled and very strong.")
            print("Officer Johnson trys to assit you, however, the suspect grabbed a hold of your weapon, and manages to shoot both you and Officer Johnson. ")
            print("Sorry, you made a deadly mistake. Remember that when your in a struggle, there is always a weapon present in that fight. It's yours.")
            print("By going hands on with the suspect, you lend yourself to the possibility of your weapon becoming compromised.")
            options = True
        else:
            invalid_option()
            options == False
    return toolslist

def main():
    
    toolslist = ['Pepper Spray', 'Baton', 'Tazer', 'Firearm', 'Call for Backup', 'Hand to hand combat', 'Handcuffs']
    #secondScenario(officers, person, toolslist)
    introduction()
    # the while loop is created to allow the user to multiple choices in how to use the program
    user_choice_three = False
    while user_choice_three == False:
        user_choice = input("Would you like to try a scenario or look at firearms first? Press : 's' for scenario, 'f' for firearms: ")
        if user_choice.lower() == "s":
            user_name = get_user_name(toolslist)
            first_scenario(user_name, toolslist)
            secondOption(toolslist,user_name)
            secondScenario(officers, person, toolslist)
            user_choice_three = True
        elif user_choice.lower() == "f":
            firearms()
            user_choice_three = True
        else:
            invalid_option()
            user_choice_three = False
        invalid_option_bool = False
        # create this while loop so that user can re-enter choice if they made an invalid choice.
        # to do this, the if and elif statements need to leave the nested loop by making the bool true or false on both loops
        while invalid_option_bool == False:
            try_another_choice = input("Would you like to go to the main menu? Yes or no? Choose Y/N")
            if try_another_choice.lower() == "y":
                print("Going to main menu...")
                invalid_option_bool = True
                user_choice_three = False
            elif try_another_choice.lower() == "n":
                print("Thanks for playing!")
                invalid_option_bool = True
                user_choice_three = True
            else:
                invalid_option()
                invalid_option_bool = False



if __name__ == "__main__":

    main()