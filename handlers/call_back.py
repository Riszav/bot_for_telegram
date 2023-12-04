import sqlite3

from aiogram import types, Dispatcher
from config import bot, ADMIN_ID
from database.sql_commands import Database
from keyboards.inline_buttons import questionnaire_keyboard, stats_keyboard, save_anime_keyboard
from scraping.scraper_file import AnimeScraper
from scraping.async_scrap import AsyncScraper
import asyncio



async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Choose model your phone?",
        reply_markup=await questionnaire_keyboard()
    )


async def iphone_call(call: types.CallbackQuery):
    try:
        db = Database()
        db.sql_insert_answer(
            username=call.from_user.username,
            users_phone='Iphone'
        )
    except sqlite3.IntegrityError:
        db.sql_delete_answer(username=call.from_user.username)
        db.sql_insert_answer(
            username=call.from_user.username,
            users_phone='Iphone'
        )
    await bot.send_message(
        chat_id=call.from_user.id,
        text="U R use IPhone 🔥"
    )


async def samsung_call(call: types.CallbackQuery):
    try:
        db = Database()
        db.sql_insert_answer(
            username=call.from_user.username,
            users_phone='Samsung'
        )
    except sqlite3.IntegrityError:
        db.sql_delete_answer(username=call.from_user.username)
        db.sql_insert_answer(
            username=call.from_user.username,
            users_phone='Samsung'
        )
    await bot.send_message(
        chat_id=call.from_user.id,
        text="U R use Samsung 🔥"
    )


async def xiaomi_call(call: types.CallbackQuery):
    try:
        db = Database()
        db.sql_insert_answer(
            username=call.from_user.username,
            users_phone='Xiaomi'
        )
    except sqlite3.IntegrityError:
        db.sql_delete_answer(username=call.from_user.username)
        db.sql_insert_answer(
            username=call.from_user.username,
            users_phone='Xiaomi'
        )
    await bot.send_message(
        chat_id=call.from_user.id,
        text="U R use Xiaomi 🔥"
    )


async def other_call(call: types.CallbackQuery):
    try:
        db = Database()
        db.sql_insert_answer(
            username=call.from_user.username,
            users_phone='Other model'
        )
    except sqlite3.IntegrityError:
        db.sql_delete_answer(username=call.from_user.username)
        db.sql_insert_answer(
            username=call.from_user.username,
            users_phone='Other model'
        )
    await bot.send_message(
        chat_id=call.from_user.id,
        text="U R use other model 🔥"
    )

async def admin_call(message: types.Message):
    if message.from_user.id == int(ADMIN_ID):
        await message.delete()
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Choose a button, Mr.Admin",
            reply_markup=await stats_keyboard()
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="You`re not admin, you just mortal"
        )

async def all_users_stats(call: types.CallbackQuery):
    db = Database()
    print(db.sql_select_all_users())
    db_data = db.sql_select_all_users()
    new_data = ''
    for user in db_data:
        new_data += f'{user["telegram_id"]}'
        new_data += f', {user["first_name"]}\n'
    await bot.send_message(
        chat_id=call.from_user.id,
        text=new_data
    )


async def ban_list_users_stats(call: types.CallbackQuery):
    db = Database()
    db_data = db.sql_select_all_ban_users()
    new_data = ''
    for user in db_data:
        new_data += f'{user["telegram_id"]}'
        new_data += f', {user["count"]}\n'
        print(user)
    await bot.send_message(
        chat_id=call.from_user.id,
        text=new_data
    )

# async def complain_profiles(call: types.CallbackQuery):
#     db = Database()
#     await bot.send_message(
#         chat_id=call.from_user.id,
#         text='Send me user`s username or first name ✈️'
#     )
#     def users_data
#     db_data = db.sql_select_user()

async def delete_user_form(call: types.CallbackQuery):
    db = Database()
    db.sql_delete_user_form(telegram_id=call.from_user.id)
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Your profile deleted'
    )

async def scraper_anime_call(call: types.CallbackQuery):
    scraper = AnimeScraper()
    data = scraper.parse_data()
    id=0
    newest = data[:5]
    print(data)
    for url in newest:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Название: {url}",
            reply_markup=await save_anime_keyboard()
        )
        id+=1
    return newest

async def scraper_films_call(call: types.CallbackQuery):
    scraper = AsyncScraper()
    data = asyncio.run(scraper.parse_pages())
    id = 0
    # newest = data[:5]
    print(data)
    # for url in data:
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"{data}",
        reply_markup=await save_anime_keyboard()
    )
    id += 1
    # await bot.send_message(
    #     chat_id=call.from_user.id,
    #     text=f"Страница: {p}",
    #     reply_markup=await save_anime_keyboard()
    # )
    return data

async def save_call(call: types.CallbackQuery):
    db = Database()
    # news_id = int(call.data.split('_')[1]) - 1
    # print(news_id)
    db.sql_insert_favorite_anime(telegram_id=call.from_user.id,first_name=call.from_user.first_name, name_anime=None)
    await bot.send_message(
        chat_id = call.from_user.id,
        text = 'Succsesfully'
    )

def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(iphone_call,
                                       lambda call: call.data == "iphone")
    dp.register_callback_query_handler(samsung_call,
                                       lambda call: call.data == "samsung")
    dp.register_callback_query_handler(xiaomi_call,
                                       lambda call: call.data == "xiaomi")
    dp.register_callback_query_handler(other_call,
                                       lambda call: call.data == "other")
    dp.register_message_handler(admin_call,
                                lambda word: "dorei" in word.text)
    dp.register_callback_query_handler(all_users_stats,
                                       lambda call: call.data == "all list")
    dp.register_callback_query_handler(ban_list_users_stats,
                                       lambda call: call.data == "ban list")
    dp.register_callback_query_handler(delete_user_form,
                                       lambda call: call.data == "delete_profiles")
    dp.register_callback_query_handler(scraper_anime_call,
                                       lambda call: call.data == "anime")
    dp.register_callback_query_handler(scraper_films_call,
                                       lambda call: call.data == "films")
    dp.register_callback_query_handler(save_call,
                                       lambda call: call.data == "save")
