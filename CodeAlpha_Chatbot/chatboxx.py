
def get_response(user_input):
    """
    Take the user's input, normalize it, and return a matching
    predefined reply using if-elif rules.
    """
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"
    elif "your name" in text:
        return "I'm a simple rule-based chatbot."
    elif text in ("bye", "goodbye", "see you"):
        return "Goodbye!"
    elif "thank" in text:
        return "You're welcome!"
    elif text == "":
        return "Please say something!"
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"


def chat():
    """
    Run the main chatbot loop: repeatedly take input from the user,
    generate a response, and print it, until the user says bye.
    """
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ("bye", "goodbye", "see you"):
            break


if __name__ == "__main__":
    chat()