import os
import telebot
import telegram
from telebot import types
import emoji
import time
import pickle
from flask import Flask, request
from instagram_private_api import Client
from igramscraper.instagram import Instagram
from dotenv import load_dotenv
load_dotenv()

DEBUG = True
# Telegram variables
TOKEN = os.getenv("5509535105:AAHRRi4KpRlPVDXw4xlvKkEMRjRpdBD9ZPo")

# Instagram variables
USERNAME = os.getenv("gym_kzmetk_akssuar")
PASSWORD = os.getenv("enes.2112")

WEBHOOK_URL = os.getenv("8b85c6e8-d393-40de-a713-c14cf4b3ce04")

bot = telebot.TeleBot(TOKEN, threaded=True)

client = Client("gym_kzmetk_akssuar", "enes.2112")

ADMIN_ID = os.getenv("2122568291")
GROUP_ID = os.getenv("-686372494")

insta = Instagram()

force_reply = types.ReplyKeyboardRemove(selective=False)
