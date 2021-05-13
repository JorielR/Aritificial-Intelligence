# Import the package lib to use
import wikipedia

# Welcome title
print("\n\n\t\t***Research Robot ***\n")
# print out a line to break up page for a better ux
print("_" * 100,"\n")
# ask user waht they would like research robot to research?
#then use input to get the topic and assign into a string variable
users_main_topic_choice = input("\nWhat would you like me, Jarvis, to research?")
print("Robot researching " + users_main_topic_choice)
# Print out a line to break up page for a better ux
print("_" * 100,"\n")
# Give our AI the ability to research for us!
# Create a var to hold the research results
raw_research_results = wikipedia.page(users_main_topic_choice)
# Print out our raw research data jarvis found
print("\n\n\t\t ### Research on " + users_main_topic_choice + " ###\n")
# print out a line to break up page for a better ux
print("_" * 100,"\n")
# print out just the summary of the research!
print("\n\n\t\t *** Summary of My research ***\n")
print(raw_research_results.summary)
# print out a line to break up page for a better ux
print("_" * 100,"\n")
# print out the expanded research content
print("\n\n\t\t *** Expanded research content ***\n")
print(raw_research_results.content)
# print out a line to break up page for a better ux
print("_" * 100,"\n")
# try to make a better UI by adding questions the way you want it to do


