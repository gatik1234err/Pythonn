while True:
    user_input = input("You: ")
    if user_input.lower() == "stop":
        print("Bot: Bye 👋")
        break
    else:
        print("Bot: Hello! How can I help you?")
