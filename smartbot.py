# Advanced Basic Chatbot - Horizon TechX Internship Python 

import datetime
import random

def greet():
    print("======================================")
    print("      Welcome to Smart ChatBot")
    print("======================================")
    print("Type 'bye' to exit the chatbot.\n")

# Random jokes
jokes = [
    "Why do programmers prefer Python? Because it's easy to code!",
    "Why was the computer cold? Because it forgot to close Windows.",
    "Why did the developer go broke? Because he used up all his cache."
]

# Motivational quotes
quotes = [
    "Success starts with self-belief.",
    "Never stop learning.",
    "Small progress is still progress."
]

def chatbot():
    greet()

    while True:
        user = input("You: ").lower()

        # Greetings
        if user in ["hello", "hi", "hey"]:
            print("Bot: Hi! How are you?")

        # How are you
        elif "how are you" in user:
            print("Bot: I am fine. Thanks for asking!")

        # Name
        elif "what is your name" in user:
            print("Bot: My name is SmartBot.")

        # Best programming language
        elif "best programming language" in user:
            print("Bot: Python is one of the best programming languages because it is simple and powerful.")

        # Time
        elif "time" in user:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print("Bot: Current time is", current_time)

        # Date
        elif "date" in user:
            current_date = datetime.datetime.now().strftime("%d-%m-%Y")
            print("Bot: Today's date is", current_date)

        # Day
        elif "day" in user:
            current_day = datetime.datetime.now().strftime("%A")
            print("Bot: Today is", current_day)

        # Python
        elif "python" in user:
            print("Bot: Python is a popular and easy programming language.")

        # Internship
        elif "internship" in user:
            print("Bot: Internships improve practical skills and experience.")

        # College
        elif "college" in user:
            print("Bot: College life is full of learning and memories.")

        # Joke
        elif "joke" in user:
            print("Bot:", random.choice(jokes))

        # Motivation
        elif "motivate" in user or "motivation" in user:
            print("Bot:", random.choice(quotes))

        # Favourite color
        elif "favorite color" in user or "favourite color" in user:
            print("Bot: I like blue because it looks calm and cool.")

        # Weather
        elif "weather" in user:
            print("Bot: I cannot check live weather, but I hope it's pleasant outside.")

        # Food
        elif "food" in user:
            print("Bot: I don't eat food, but pizza sounds tasty!")

        # Help
        elif "help" in user:
            print("Bot: You can ask me about time, date, jokes, motivation, Python, and more.")

        # Thank you
        elif "thank you" in user or "thanks" in user:
            print("Bot: You're welcome!")

        # Bye
        elif "bye" in user:
            print("Bot: Bye! Nice talking to you.")
            break

        # Default
        else:
            print("Bot: Sorry, I didn't understand that.")

# Run chatbot
chatbot()