import random
import json

# Load responses from JSON file
with open("data.json", "r") as file:
    responses = json.load(file)

# Function to get a response based on user input
def get_response(user_input: str) -> str:
    user_input = user_input.lower()

    for key, value in responses.items():
        if key in user_input:
            return random.choice(value)

    return random.choice(responses["default"])