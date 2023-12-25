#Machine Learning Club-Chatbot 
#Chatbot Name- Alex
#Submitted by- Dhruv Aggarwal (23BCE7474) Projects 2.0 Team 2023-24

#Importing necessary modules
from datetime import datetime
import random 

#Defining function & If-Else Statements
print("Alex: Hello! My name is Alex, your personal chatbot!")
print("         How can i help you today?")
def Alex_chatbot(a):
    if "hello" in a or "hi" in a or "hey" in a:
        return "Hello! Good to see you!"
    elif "good morning" in a:
        return "Good Morning! Hope you will have a delightful day."
    elif "good afternoon" in a:
        return "Good Afternoon! Hope you are doing good."
    elif "good evening" in a:
        return "Good Evening! Time for tea and snack."
    elif "good night" in a:
        return "Good Night! Sweet Dreams."
    elif 'your name' in a:
        return "My name is Alex, Nice to meet you!"
    elif "how are you" in a or "whats up" in a or "what's up" in a:
        return "I am doing good. Hope you are also doing well! "
    elif "time" in a or "date" in a:
        a="Currently, the date & time is:"
        b = str(datetime.now())
        return a+b
    elif "hungry" in a:
        return "You should grab a snack to eat."
    elif "thirsty" in a:
        return "You should drink water."
    elif "who are you" in a:
        return "I am Alex,your personal chatbot! I am programmed to answer all your questions."
    elif "my birthday" in a:
        return "Happy Birthday! Hope all your wishes come true."
    elif "something funny" in a or "joke" in a:
         jokes={"Which is faster, hot or cold? Hot, because you can catch cold.","What do you call a fake noodle? An impasta.","How do celebrities stay cool? They have many fans.","Where do young trees go to learn? Elementree school."}
         if True:
              x=random.choice(list(jokes))
              return x
    elif "day today" in a:
        dt=datetime.now()
        x=dt.weekday()
        if x==0:
             return "Today is Monday."
        elif x==1:
             return "Today is Tuesday."
        elif x==2:
             return "Today is Wednesday."
        elif x==3:
             return "Today is Thursday."
        elif x==4:
             return "Today is Friday."
        elif x==5:
             return "Today is Saturday."
        else:
             return "Today is Sunday."
    elif "thanks" in a or "thank you" in a or "appreciate" in a:
         return "Welcome! Glad to help you."
    elif "nice" in a or "good" in a:
         return "Thank you!"
    elif "movie" in a or "film" in a:
         Movies=["1. Interstellar","2. Martian","3. RRR","4. Top Gun: Maverick", "5. Oppenheimer","6. Chhichhore","7. Tenet","8. Avengers: Age of Ultron","9. The Creator","10. Uncharted"]
         print("Alex: Here is a list of ten blockbuster movies:")
         for i in Movies:
          print(i)
         return "Hope you liked my recommendation."
    elif "how was your day" in a:
         return "It was good. Hope your day also went good."
    elif "fact" in a or "something interesting" in a:
         fact=["1. Avocados are a fruit, not a vegetable. They're technically considered a single-seeded berry, believe it or not.",
               "2. The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, the particles gain kinetic energy and take up more space.",
               "3. Australia is wider than the moon. The moon sits at 3400km in diameter, while Australia’s diameter from east to west is almost 4000km.",
               "4. Human teeth are the only part of the body that cannot heal themselves. Teeth are coated in enamel which is not a living tissue.",
               "5. Venus is the only planet to spin clockwise. It travels around the sun once every 225 Earth days but it rotates clockwise once every 243 days."]
         print("Alex: Here are some random facts that will blow your mind!:")
         for i in fact:
             print(i)
         return "Hope you liked these mind-blowing facts."
    elif "random number" in a:
         a=int(input("Alex: Enter a minimum value:"))
         b=int(input("Alex: Enter a maximum value:"))
         c='Here is your random number in the range:'
         d=str(random.randint(a,b))   
         return str(c+d)
    elif "roll a dice" in a or "dice" in a:
          c="Rolling the Dice:"
          d=str(random.randint(1,6))
          return str(c+d)
    elif "riddle" in a:
         print("Alex: Here is a riddle for you:")
         riddles=["What month of the year has 28 days?","What is full of holes but still holds water?","What is always in front of you but can’t be seen?"," What can you break, even if you never pick it up or touch it?","What goes up but never comes down?"]
         b=random.choice(riddles)
         print("Q.",b)
         s=input("You:")
         x=s.lower()
         if "all" in x:
                   return ("Gotcha! Your answer is correct.")
         elif "sponge" in x:
                    return ("Gotcha! Your answer is correct.")
         elif "future" in x:
                    return ("Gotcha! Your answer is correct.")
         elif  "promise" in x:
                    return ("Gotcha! Your answer is correct.")
         elif "age" in x or "height" in x:
                    return ("Gotcha! Your answer is correct.")
         else:
               return ("Sorry! Your answer is incorrect.") 
    elif "travel" in a or "destination" in a or "place" in a or "country" in a:
          places=["1. London","2. Japan","3. India","4. USA", "5. Australia"]
          print("Alex: Here are some best places to visit:")
          for i in places:
                print(i) 
          return "Hope you liked my recommendation."  
    else:
          return("Sorry! I am unable to understand that.")

#Declaring while loop and calling the function
while True:
    user_input = input("You: ")
    a=user_input.lower()
    if a == 'exit' or a== "goodbye" or a=="bye":
        print("Alex: Goodbye!")
        break
    response = Alex_chatbot(a)
    print("Alex:", response)
