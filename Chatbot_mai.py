from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Transporter
chatbot = ChatBot("Tester")


# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)
conversation1 = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

conversation2 = [
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."]

conversation3 = [
    "Hello!",
    "Hi!",
    "Hi!",
    "How are you?",
    "How are you?",
    "Very well, thank you.",
    "Very well, thank you.",
    "Do you like music?",
    "Very well, thank you.",
    "Good.",
    "Do you like music?",
    "Yes, a lot!",
    "How are you?",
    "In a very good mood.",
    "Good.",
    "Indeed.",
    "Indeed.",
    "What is the weather like?",
    "Yes, a lot!",
    "Okay...",
    "What is the weather like?",
    "Quite rainy today.",
    "Indeed.",
    "I have to go. Goodbye!",
    "How are you?",
    "In a good mood.",
    "Indeed.",
    "See you later!",
    "Okay...",
    "Bye, I'll talk to you later :)",
    "Do you like music?",
    "I like it.",
    "I have to go. Goodbye!",
    "Bye!"
]
# Training
trainer.train(conversation3)

# Get a response to the input text 'Good morning!'
response = chatbot.get_response("Good morning!")
#response = chatbot.get_response("I would like to book a flight.")

print(response)