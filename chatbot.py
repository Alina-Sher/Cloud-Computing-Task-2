import random

# Predefined patterns (extendable for commercial use)
patterns = {
    "hello": ["Hi there!", "Hello! How can I help you today?", "Hey!"],
    "bye": ["Goodbye!", "See you soon!", "Bye! Have a nice day!"],
    "services": ["We offer cloud computing, AI solutions, and IT consulting."],
    "pricing": ["Our pricing depends on your needs. Would you like basic or enterprise plans?"],
    "default": ["Sorry, I didn’t understand. Can you rephrase?"]
}

def get_response(user_input):
    user_input = user_input.lower()

    # Simple retrieval-based matching
    for key in patterns:
        if key in user_input:
            return random.choice(patterns[key])

    return random.choice(patterns["default"])
