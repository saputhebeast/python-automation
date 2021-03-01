#if ypu dont have instapy, then install it.
#pip install instapy
from instabot import Bot
bot = Bot()
bot.login(username = "username", password = "password") #enter your login details
bot.upload_photo(image = "image", caption = "This post was posted by MYINSTA BOT!") #image url and caption
