import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from keyboards.inline_buttons import questionnaire_keyboard
from database import sql_commands


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