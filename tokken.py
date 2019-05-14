import nltk
from nltk.tokenize import regexp_tokenize
import datetime
from connect_db import *
#from age import *



def select_date_of_birth(question):
    tokens = nltk.wordpunct_tokenize(question)
    for i in tokens:
        if i.lower() in prenom:
            sql_select_query = """select date_of_birth from promo10 where last_name = %s"""
            curr.execute(sql_select_query, (i,))
            reponse = str(curr.fetchall()).replace("[(datetime.date(","").replace("),)]","")
            print(reponse)

def select_lat_lon(question):
    tokens = nltk.wordpunct_tokenize(question)
    for i in tokens:
        if i.lower() in prenom:
            sql_select_query = """select lat,lon from promo10 where last_name = %s"""
            curr.execute(sql_select_query, (i,))
            reponse = str(curr.fetchall()).replace("[(","").replace(")]","")
            print(reponse)

def select_telephone(question):
    tokens = nltk.wordpunct_tokenize(question)
    for i in tokens:
        if i.lower() in prenom:
            sql_select_query = """select telephone from promo10 where last_name = %s"""
            curr.execute(sql_select_query, (i,))
            reponse = str(curr.fetchall()).replace("[(","0").replace(",)]","")
            print(reponse)

def select_email(question):
    tokens = nltk.wordpunct_tokenize(question)
    for i in tokens:
        if i.lower() in prenom:
            sql_select_query = """select email from promo10 where last_name = %s"""
            curr.execute(sql_select_query, (i,))
            reponse = str(curr.fetchall()).replace("[('","").replace("',)]","")
            print(reponse)

def select_adresse(question):
    tokens = nltk.wordpunct_tokenize(question)
    for i in tokens:
        if i.lower() in prenom:
            sql_select_query = """select adress from promo10 where last_name = %s"""
            curr.execute(sql_select_query, (i,))
            reponse = str(curr.fetchall()).replace("[('","").replace("',)]","")
            print(reponse)

def select_age(question):
    tokens = nltk.wordpunct_tokenize(question)
    for i in tokens:
        if i.lower() in prenom:
            sql_select_query = """select date_of_birth from promo10 where last_name = %s"""
            curr.execute(sql_select_query, (i,))
            date = str(curr.fetchall())
            st = date.replace("[(datetime.date(","").replace("),)]","")
            t = regexp_tokenize(st, pattern='\d+')
            y = int(t[0])
            m = int(t[1])
            d = int(t[2])
            d_today = int(datetime.date.today().day)
            m_today = int(datetime.date.today().month)
            y_today = int(datetime.date.today().year)

            if m > m_today:
                age = y_today - y - 1
            elif m == m_today:
                if d >= d_today:
                    age = y_today - y - 1
            else:
                age = y_today - y

            print(age)



