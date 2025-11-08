# Task 1 - Rule-Based Chatbot
# Created by Shabab Ahmad for CODSOFT Internship

print("🤖 ChatBot: Hello! I'm your virtual assistant. How can I help you today?")
print("Type 'bye' anytime to exit.\n")

while True:
    user_input = input("You: ").lower()

    if 'hello' in user_input or 'hi' in user_input:
        print("🤖 ChatBot: Hi there! How are you doing?")
    elif 'how are you' in user_input:
        print("🤖 ChatBot: I'm just a bunch of code, but I'm doing great! What about you?")
    elif 'your name' in user_input:
        print("🤖 ChatBot: I'm Shabab's friendly chatbot, built for the CODSOFT internship!")
    elif 'help' in user_input:
        print("🤖 ChatBot: Sure! You can ask me about my creator, date, or how to exit.")
    elif 'time' in user_input:
        from datetime import datetime
        print("🤖 ChatBot:", datetime.now().strftime("Current time is %H:%M:%S"))
    elif 'date' in user_input:
        from datetime import date
        print("🤖 ChatBot:", date.today().strftime("Today's date is %B %d, %Y"))
    elif 'bye' in user_input or 'exit' in user_input:
        print("🤖 ChatBot: Goodbye! Have a wonderful day! 😊")
        break
    else:
        print("🤖 ChatBot: Sorry, I didn’t understand that. Try asking something else!")
