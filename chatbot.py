import requests
import json
import os

print('''

  ______    ______   __       __  ________  _______   __      __ 
 /      \  /      \ /  \     /  |/        |/       \ /  \    /  |
/$$$$$$  |/$$$$$$  |$$  \   /$$ |$$$$$$$$/ $$$$$$$  |$$  \  /$$/ 
$$ |  $$/ $$ |  $$ |$$$  \ /$$$ |$$ |__    $$ |  $$ | $$  \/$$/  
$$ |      $$ |  $$ |$$$$  /$$$$ |$$    |   $$ |  $$ |  $$  $$/   
$$ |   __ $$ |  $$ |$$ $$ $$/$$ |$$$$$/    $$ |  $$ |   $$$$/    
$$ \__/  |$$ \__$$ |$$ |$$$/ $$ |$$ |_____ $$ |__$$ |    $$ |    
$$    $$/ $$    $$/ $$ | $/  $$ |$$       |$$    $$/     $$ |    
 $$$$$$/   $$$$$$/  $$/      $$/ $$$$$$$$/ $$$$$$$/      $$/     
                                                              

''')

print('''

  ______   __    __   ______   ________  _______    ______   ________ 
 /      \ /  |  /  | /      \ /        |/       \  /      \ /        |
/$$$$$$  |$$ |  $$ |/$$$$$$  |$$$$$$$$/ $$$$$$$  |/$$$$$$  |$$$$$$$$/ 
$$ |  $$/ $$ |__$$ |$$ |__$$ |   $$ |   $$ |__$$ |$$ |  $$ |   $$ |   
$$ |      $$    $$ |$$    $$ |   $$ |   $$    $$< $$ |  $$ |   $$ |   
$$ |   __ $$$$$$$$ |$$$$$$$$ |   $$ |   $$$$$$$  |$$ |  $$ |   $$ |   
$$ \__/  |$$ |  $$ |$$ |  $$ |   $$ |   $$ |__$$ |$$ \__$$ |   $$ |   
$$    $$/ $$ |  $$ |$$ |  $$ |   $$ |   $$    $$/ $$    $$/    $$ |   
 $$$$$$/  $$/   $$/ $$/   $$/    $$/    $$$$$$$/   $$$$$$/     $$/    

''')

print('''

                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                 oo             o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""  
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$       
                                """"$$$$$$$$$$$        
                                    $$$$$$$$$$$$       
                                     $$$$$$$$$$"      
                                      "$$$""""

''')

def run():
  print("Welcome to the chat bot, I'll make u laugh!")

  if not os.path.exists("saved_jokes.txt"):
    with open("saved_jokes.txt", "w"):
      pass

  list = []
  
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
      joke_input = input("Do you want to hear another joke? Type no to exit, type save to save a joke, type unsave to unsave a joke, type saved to see the saved jokes, rate to rate this chatbot, script to get a funny quote and anything else to continue, challenge to see if you can answer a joke correctly on your own, rate to rate the chatbot:\n").lower()
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
        print ('''
         .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     ____     | || |     ____     | || |              | || |     __       | || |     ____     | |
| |   .'    '.   | || |   .'    '.   | || |      _       | || |    /  |      | || |   .'    '.   | |
| |  |  .--.  |  | || |  |  .--.  |  | || |     (_)      | || |    `| |      | || |  |  .--.  |  | |
| |  | |    | |  | || |  | |    | |  | || |      _       | || |     | |      | || |  | |    | |  | |
| |  |  `--'  |  | || |  |  `--'  |  | || |     (_)      | || |    _| |_     | || |  |  `--'  |  | |
| |   '.____.'   | || |   '.____.'   | || |              | || |   |_____|    | || |   '.____.'   | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'
      
        ''')
        print('''
        /$$$$$$$$ /$$$$$$ /$$      /$$ /$$$$$$$$
|__  $$__/|_  $$_/| $$$    /$$$| $$_____/
   | $$     | $$  | $$$$  /$$$$| $$      
   | $$     | $$  | $$ $$/$$ $$| $$$$$   
   | $$     | $$  | $$  $$$| $$| $$__/   
   | $$     | $$  | $$\  $ | $$| $$      
   | $$    /$$$$$$| $$ \/  | $$| $$$$$$$$
   |__/   |______/|__/     |__/|________/
                                         
        ''')
        print('''
         /$$$$$$  /$$$$$$ 
|_  $$_/ /$$__  $$
  | $$  | $$  \__/
  | $$  |  $$$$$$ 
  | $$   \____  $$
  | $$   /$$  \ $$
 /$$$$$$|  $$$$$$/
|______/ \______/ 
                  
        ''')
        print('''
         /$$$$$$$$ /$$$$$$  /$$$$$$  /$$   /$$ /$$$$$$ /$$   /$$  /$$$$$$ 
|__  $$__/|_  $$_/ /$$__  $$| $$  /$$/|_  $$_/| $$$ | $$ /$$__  $$
   | $$     | $$  | $$  \__/| $$ /$$/   | $$  | $$$$| $$| $$  \__/
   | $$     | $$  | $$      | $$$$$/    | $$  | $$ $$ $$| $$ /$$$$
   | $$     | $$  | $$      | $$  $$    | $$  | $$  $$$$| $$|_  $$
   | $$     | $$  | $$    $$| $$\  $$   | $$  | $$\  $$$| $$  \ $$
   | $$    /$$$$$$|  $$$$$$/| $$ \  $$ /$$$$$$| $$ \  $$|  $$$$$$/
   |__/   |______/ \______/ |__/  \__/|______/|__/  \__/ \______/ 
                                                              
        ''')
        print("----This is the hardest joke in the world, you have to answer it correctly to get 5 stars, if you get it wrong you will lose 5 stars----")
        print("Can February March?")
        import datetime
        before = datetime.datetime.now()
        answer_input = input("Enter your answer: ")
        after = datetime.datetime.now()

        if (after - before).seconds >= 10:
          print("TIME'S UP, YOU DIDN'T ANSWER IN TIME, U EARNED NO STARS :(")
        elif answer_input == "No but April May".lower():
          print("Correct!")
          stars += 5
          print("You have " + str(stars) + " star(s).")
        else:
          print("No, you're wrong")
          stars = 0
          print("You have 0 stars ")      
      elif joke_input == "rating" or joke_input == "rate":
        while True:
          rating = input("Please enter from 1-5 to rate this chatbot:")
          if rating.isdigit():
            if int(rating) <= 5:
              print(f"Thank you for rating this chatbot {rating}/5")
            if int(rating) < 1:
              print("Please enter a number from 1-5")
            if int(rating) < 5 and int(rating) > 0:
              print("Please enter a number from 1-5")
              print("Enter the most apporiate number input as if why you gave the rating:"
                    "1: I don't like it at all, jokes were too hard, waste of time, and I didn't like the chatbot at all. Joke challenge was so hard couldn't answer it, 10 seconds was way too short for me"
                    "2: I like it, just bored, feels like I'm talking to a boring person who isn't funny at all"
                    "3: It's okay, I like the joke challenge feature, that question was too easy for me! Heck, I answered in like 2 seconds LOL"
                    "4: I LOVE IT, Well, almost, the joke challenge was way too easy for me, it needs to be a A LOT HARDER & A LOT Less time to figure it out, well for me I type very fast, but for others, they know the answer but they still need time typing, so I guess try to increase the time a bit")
            my_opinion = input("Enter your opinion on this chatbot:")
            if my_opinion == "1":
              print('''
                 ▄████████    ▄█   ▄█▄  ▄█   ▄█        ▄█       
  ███    ███   ███ ▄███▀ ███  ███       ███       
  ███    █▀    ███▐██▀   ███▌ ███       ███       
  ███         ▄█████▀    ███▌ ███       ███       
▀███████████ ▀▀█████▄    ███▌ ███       ███       
         ███   ███▐██▄   ███  ███       ███       
   ▄█    ███   ███ ▀███▄ ███  ███▌    ▄ ███▌    ▄ 
 ▄████████▀    ███   ▀█▀ █▀   █████▄▄██ █████▄▄██
              
              ''')
              print('''
               ▄█     ▄████████    ▄████████ ███    █▄     ▄████████ 
███    ███    ███   ███    ███ ███    ███   ███    ███ 
███▌   ███    █▀    ███    █▀  ███    ███   ███    █▀  
███▌   ███          ███        ███    ███  ▄███▄▄▄     
███▌ ▀███████████ ▀███████████ ███    ███ ▀▀███▀▀▀     
███           ███          ███ ███    ███   ███    █▄  
███     ▄█    ███    ▄█    ███ ███    ███   ███    ███ 
█▀    ▄████████▀   ▄████████▀  ████████▀    ██████████
              
            ''')
            elif my_opinion == "2":
              print("I'm a chatbot, I'm not a human, I don't ahve any emotions, but don't call me boring at least, the jokebot was funny if u actually have a sense of humor, which in this, I assume u don't. ROASTED & TOASTED!")
            elif my_opinion == "3":
              print("Next time I'll give u ultra-hard one & u'll have only 5 seconds to answer, how bout' that?")
            elif my_opinion == "4":
              print("THAT'S WHAT IM TALKIN ABOUT")
        
      
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
