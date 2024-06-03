import requests
import json
import os

def run():
  print("Welcome to the chat bot")

  if not os.path.exists("saved_jokes.txt"):
    with open("saved_jokes.txt", "w"):
      pass

  list = []
  # call the joke endpoint
  while True:
    query = input("Enter your query:")

    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"

    if query is not None:
      url += "&contains=" + query
    res = requests.get(url)
    data = json.loads(res.text)

    while data in list:
      res = requests.get(url)
      data = json.loads(res.text)

    if data["error"] == True:
      print("Error: " + data["message"])
      continue
    
    if data["type"] == "single":
      print(data["joke"])
    elif data["type"] == "twopart":
      setup = data["setup"]
      delivery = data["delivery"]
      print(setup)
      if setup[-1] == "?":
        input("press any key to continue...")
        print("Answer:")
      print(delivery)
    print()
    list.append(data)

    while True:
      joke_input = input("Do you want to hear another joke? Type no to exit, type save to save a joke, type unsave to unsave a joke, type saved to see the saved jokes, rate to rate this chatbot, script to get a funny quote and anything else to continue, challenge to see if you can answer a joke correctly on your own:\n").lower()
      if joke_input == "no":
        return
      
      elif joke_input == "save":
        with open("saved_jokes.txt", "a") as f:
          if data["type"] == "single":
            f.write(data["joke"].replace("\n", " ") + "\n")
          elif data["type"] == "twopart":
            setup = data["setup"]
            delivery = data["delivery"]
            joke = "Setup: " + setup + " Delivery: " + delivery
            f.write(joke.replace("\n", " ") + "\n")
            print("Saved joke to saved_jokes.txt")
      
      elif joke_input == "saved":
        with open("saved_jokes.txt", "r") as f:
          j = f.readline()
          if j.strip() == "":
            print("You have no saved jokes.")
          else:
            print("Here are your saved jokes:")
            k = 1
            while j != "":
              print(str(k) + ": " + j)
              j = f.readline()
              k += 1
      
      elif joke_input == "joke challenge".lower():
        stars = 0
        print("----This is the hardest joke in the world, you have to answer it correctly to get 5 stars, if you get it wrong you will lose 5 stars----")
        print("Can February March?")
        answer_input = input("Enter your answer: ")
        if answer_input == "No but April May".lower():
          print("Correct!")
          stars += 5
          print("You have " + str(stars) + " star(s).")
        else:
          print("No, you're wrong")
          stars = 0
          print("You have 0 stars ")      
        
        elif joke_input == "script":
        print("--------START OF SCRIPT-----------")
        with open("saved_jokes.txt", "r") as f:
          j = f.readline()
          if j.strip() == "":
            print("Hello, I am a comedian, I am here to tell you some jokes. Ooops! I don't have any jokes to tell you. Sorry!")
          else:
            jokes = []
            while j != "":
              jokes.append(j)
              j = f.readline()
            if len(jokes) == 1:
              print("Hello! They paid me $20 to perform tonight, but I charge $20 per joke, so you only get one. Here goes:")
              print(jokes[0].strip())
              print("Haha, I know that was funny! That's all from me folks. Bye!")
            elif len(jokes) == 2:
              print("Hello! You are listening to me the comedian, I am here to tell you some jokes. Here goes: ") 
              print(jokes[0].strip())
              print("Haha, I bet you laughed! And if that one didn't make you pee your pants, here's another one:")
              print(jokes[1].strip())
              print("Alrighty folks, if you need me, I'll be at the bar half-joking and half-crying questioning the life decisions that got me here.")
            else:
              import random
              random.shuffle(jokes)
              print("Hello! It's me again! I've respawned! Who would've thought?! Seriously?! I know you want me here! I know you like me, so here's something so funny that'll never make you stop laughing:")
              print(jokes[0].strip())
              print("Heheheha!")
              print(jokes[1].strip())
              print("So funny right?")
              print(jokes[2].strip())
              print("OMG! It made you pee! Not sorry! Bye!")
        print("--------END OF SCRIPT-----------")
      elif joke_input == "unsave":
        while True:
          try:
            joke_number_to_delete = int(input("Enter the number of the joke you want to delete: ")) # from 1 to number of jokes
          except ValueError:
            print("Invalid joke number")
            continue
          if joke_number_to_delete <= 0:
            print("Invalid joke number")
            continue
          new_list = []
          with open("saved_jokes.txt", "r") as f:
            j = f.readline()
            k = 1
            while j != "":
              if k != joke_number_to_delete:
                new_list.append(j)
              j = f.readline()
              k += 1
          if k - 1 < joke_number_to_delete:
            print("Invalid joke number")
            continue
          with open("saved_jokes.txt", "w") as f:
            for joke in new_list:
              f.write(joke)      
          break
      else:
        break
        
run()
