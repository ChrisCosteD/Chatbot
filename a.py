
from tokken import *
from chatbot import *
d = 0
mot_cles = ["date","lon", "mail","longitude", "téléphone","telephone","numero","email","city","ville","adresse","numéro","age"]
while True:
    request = input('you: ')
    tokens = nltk.wordpunct_tokenize(request)
    if request.strip().lower() != 'bye':
        for i in tokens:
            if i.lower() in mot_cles:
                if i.lower() == "date":
                    select_date_of_birth(request)
                    d = d + 1
               # if i == "lon" or "longitude":
                    #select_lat_lon(request)
                if i.lower() == "numero" or i == "telephone" or i.lower() == "numéro" or i.lower() == "téléphone":
                    select_telephone(request)
                    d = d + 1
                if i.lower() == "email" or i.lower() == "mail":
                    select_email(request)
                    d = d + 1
                if i.lower() == "adresse" or i.lower() == "ville" or i.lower() == "city":
                    select_adresse(request)
                    d = d + 1
                if i.lower() == "age":
                    select_age(request)
                    d = d + 1

    if request.strip().lower() in conversations:
        response = bot.get_response(request)
        print(response)
    elif d < 1 and request.strip().lower() != 'bye':
        print("Désolé, je comprends pas votre question! Est-ce que vous pouvez parler plus claire?")

    if request.strip().lower() == 'bye':
        print('See you later!')
        break
