a=input("Enter your name:")
def chatbot_response(user_input):
    user_input = user_input.lower()

    
    if 'hello' in user_input or 'hi' in user_input:
        return f"Hello {a}! How can I assist you today?"
    elif 'bye' in user_input:
        return f"Goodbye {a}! Have a great day!"
    elif 'how are you' in user_input:
        return "I'm just a bot, but I'm functioning as expected. How about you?"
    elif 'weather' in user_input:
        return "I'm not connected to the internet right now, but you can check the weather on your favorite app!"
    elif 'name' in user_input:
        return "I'm a simple and cute chatbot created by another cutie karana to assist you with basic queries."
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"


while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print(f"Chatbot: Goodbye {a}!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
