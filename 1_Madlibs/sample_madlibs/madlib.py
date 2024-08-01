# #string concatenation
# # suppose we want to create a string that says "subscribe to ______"
# youtuber = "Manpreet"

# # a few ways to do this 
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

def madlib():
    adj  = input("Adjective: ")
    verb1 = input("Verb 1: ")
    verb2 = input("verb 2: ")
    famous_person = input("Famous Person : ")

    madlib = f"Programming is so {adj}! It makes me happy all the time becasue \
    I love {verb1} mathematical problems. Stay hydrated and {verb2} like you are a {famous_person}!"

    print(madlib)