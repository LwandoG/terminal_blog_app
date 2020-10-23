import pymongo

from menu import Menu
from models.post import Post
from models.blog import Blog
from database import Database

Database.initialize()

menu = Menu()

menu.run_menu()
