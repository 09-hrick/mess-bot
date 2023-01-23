import os
import telebot
from datetime import datetime

# BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot('5974012175:AAELRJhSTpGDazZTosiBGUYvKx_pw4C2LIg')
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Chitkara Mess Reminder Bot")

print("Bot is running")
breakfast=["Aloo Parantha + Curd/Butter + Pickle +Tea","Pav Bhaji + Tea","Ajwain Parantha Aloo ki sabzi + Pickle + Tea","Macroni bread Jam & bread Butter+ Coffee","Methi Parantha+ Curd + Pickle+ Tea","(Mix/Gobhi Parantha) +Curd/Butter +Tea","Vegetable Sandwich + Sweet Daliya + Tea"]
lunch=["Rajmah Masala +Aloo Jeera + Steamed Rice + Roti +Boondi Raita","Mah Channa dal+ Aloo Methi + Steamed Rice+Roti + Raita + Pickle","Dal Makhni + Aloo Gajar Muttar + Steamed Rice +Roti +Mint Raita",	"Kadhi Pakoda + Aloo Muttar +Steamed Rice + Roti +Salad+ Pickle","Black Channa+ Chinese Nutri+ Steamed Rice + Roti +Cucumber raita",	"Dal Tadka + Kofta Curry +Roti +Steamed Rice+salad","Dal Makhni + Vegetable Pulao + Roti +Aloo Raita/ (white Channa+Kulcha +Steamed Rice +Mix Raita + Pickle)"]
snacks=["Bread Pakoda(G)/Cake (B) +Tea","Patty(G)/ Samosa(B) + Tomato Ketchup/Sonth Chutney + Tea","Bread Pakoda(B)/ Cake (G)+ Tea","Multigrain chips/ Noodles Masala + Tea","Samosa (G)/ Patty(B) + Tomato Ketchup/Sonth Chutney + Tea","Biscuit + Coffee","Namkeen + Tea"]
dinner=["Moong Saboot Dal +Muttar Paneer +Steamed Rice + Roti+ Pickle+ Ladoo","Arhar Malka Dal Vegetable Fried Rice + Vegetable Manchurian +Roti +Pickle + Gulab Jamun","Saboot Masoor +Pindi Channa +Roti Rice+ Hot Milk","Rajmah Masala+ Aloo Gobhi + Steamed Rice + Roti Pickle+ Basen Ke Ladoo/ Sweet Dish","Moong Masoor Dal + Kadhal Paneer/Mutter Pancer Egg Curry+ Rice + Roti + Rasgulla","Dal Lobhia+Mix Vegetable + Roti + Rice+ Hot Milk (G)/Gulab Jamun (B)","Sambhar/ Channa Dal +Chilli Potato / Aloo South Indian + Rice + Roti +Gulab Jamun (G)/Hot Milk (B)"]

dtobj=datetime.now()
day=dtobj.weekday()
timeofnow=dtobj.strftime("%H:%M")
"""
breakfast: 7:30
lunch: 12:00
snacks: 5
dinner: 7:30

"""
hrs=timeofnow.split(':')
mins=int(hrs[1])
hrs=int(hrs[0])
print(type(breakfast[day]))
# bot.send_message(chat_id="-1001524941511",text=breakfast[day])

if(hrs==7 and mins==15):
    bot.send_message(chat_id="-1001524941511",text=breakfast[day])
if(hrs==11 and mins==45):
    bot.send_message(chat_id="-1001524941511",text=lunch[day])
if(hrs==4 and mins==30):
    bot.send_message(chat_id="-1001524941511",text=snacks[day])
if(hrs==7 and mins==15):
    bot.send_message(chat_id="-1001524941511",text=dinner[day])

bot.infinity_polling()
