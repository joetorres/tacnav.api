
import os

DB = os.getenv('DB', 'mysql+mysqlconnector://root:tartaruga@localhost:3306/tacnav')
JWT_TOKEN = os.getenv('JWT_TOKEN', "b8cd87c9343bgaff87c3c28a6559ba7afe17f7a4d98790b1dfe703c14441790529068d7ed5dc3a0fdbdda2b2721a1a03")
FILE_FOLDER = os.getenv("FILE_FOLDER", "./app_files")
