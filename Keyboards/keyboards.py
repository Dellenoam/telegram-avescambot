from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_keyboard1 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
command_button1 = KeyboardButton(text='OpenWeb')
command_button2 = KeyboardButton(text='OpenNotepad')
command_button3 = KeyboardButton(text='CloseCurrentWindow')
command_button4 = KeyboardButton(text='GetScreenShot')
command_button5 = KeyboardButton(text='OpenImage')
command_button6 = KeyboardButton(text='GetInfo')
commands_keyboard1.add(command_button1, command_button2, command_button3,
                       command_button4, command_button5, command_button6)

commands_keyboard2 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
website_button1 = KeyboardButton(text="Садовник")
website_button2 = KeyboardButton(text="Завтра не наступит")
commands_keyboard2.add(website_button1, website_button2)
