from chatterbot import ChatBot # import chatbot
from chatterbot.trainers import ListTrainer # methode for training chatbot

bot = ChatBot('test', read_only = True)#create the chatbot

conv = open('chats2.txt','r').readlines()

#conv2 = [
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

trainer = ListTrainer(bot)
#bot.set_trainer(ListTrainer)# set the trainer
trainer.train(conv2)
#bot.train(conv) #train the bot

while True:
    request = input('You :')
    response = bot.get_response(request)

    print('Bot: ',response)



