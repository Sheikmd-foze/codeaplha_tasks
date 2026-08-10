# chatboxx 🤖

A simple rule-based chatbot built in Python. It matches user input against predefined patterns and responds accordingly — a great starting point for learning basic natural language handling with conditionals.

## Features

- Responds to greetings (`hello`, `hi`, `hey`)
- Answers "how are you" style questions
- Tells you its name when asked
- Says thanks when thanked
- Exits gracefully on `bye`, `goodbye`, or `see you`
- Falls back to a generic response for anything it doesn't recognize

## Requirements

- Python 3.x (no external dependencies)

## Usage

Run the script from your terminal:

```bash
python chatboxx.py
```

Example session:

```
Chatbot: Hello! Type 'bye' to exit.
You: hi
Chatbot: Hi!
You: how are you
Chatbot: I'm fine, thanks! How about you?
You: what's your name
Chatbot: I'm a simple rule-based chatbot.
You: thanks
Chatbot: You're welcome!
You: bye
Chatbot: Goodbye!
```

## How It Works

1. `get_response()` takes the raw user input, lowercases and strips it, then checks it against a series of `if-elif` rules.
2. Depending on which pattern matches (exact phrase or substring), it returns a fitting reply.
3. `chat()` runs the main loop: it keeps prompting the user, printing the chatbot's response, and exits when the user says a goodbye phrase.

## Notes / Future Improvements

- Responses are entirely rule-based — could be extended with NLP libraries (e.g., NLTK, spaCy) for more flexible understanding.
- Could add support for more intents (jokes, weather, small talk).
- Pattern matching could be moved to a config file (JSON/YAML) for easier editing without touching code.
- Could integrate an actual language model for open-ended conversation.

## License

Feel free to use, modify, and distribute this project.
