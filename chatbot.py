from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

conversations = [
        'Hello',
        'Hi',
        'hello',
        'hi',
        'bonjour',
        'bonjour',
        'how are you?',
        'I am fine',
        'comment ça va?',
        'ça va',
        'what is your name?',
        'my name is Chatton, how can I help you?',
        'what is your age?',
        'I am a chatton, you think this is a good question?'
    ]


bot = ChatBot('Bot', read_only = True,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'threshold': 0.70,
            'default_response': 'Désolé, je comprends pas votre question! Est-ce que vous pouvez parler plus claire?'
        }
    ])
trainer = ListTrainer(bot)
trainer.train(conversations)



