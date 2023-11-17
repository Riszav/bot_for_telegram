import datetime
import sqlite3

from aiogram import types, Dispatcher
from config import bot, dp
from database.sql_commands import Database
from keyboards.inline_buttons import stats_keyboard
from profanity_check import predict, predict_prob
from aiogram.dispatcher.filters import BoundFilter

#
# class MyFilter(BoundFilter):
#     key = 'is_admin'
#
#     def __init__(self, is_admin):
#         self.is_admin = is_admin
#
#     async def check(self, message: types.Message):
#         member = await bot.get_chat_member(message.chat.id, message.from_user.id)
#         return member.is_chat_admin()
#
# dp.filters_factory.bind(MyFilter)
#
# @dp.message_handler(is_admin=True)
# async def for_admin(message: types.Message):
#     # db = Database()
#     if message.text==''
#     await bot.send_message(
#         chat_id=message.from_user.id,
#         text='Choose what command you use?',
#         reply_markup= await stats_keyboard(),
#     )
#
#
# @dp.message_handler(is_admin=False)
# async def for_mortals(message: types.message):
#     await bot.send_message(
#         chat_id=message.chat.id,
#         text='You`re not admin, you`re just mortal')


async def chat_messages(message: types.Message):
    db = Database()
    print(message)
    if message.chat.id == -1002013774865:
        ban_word_predict_prob = predict_prob([message.text])
        if ban_word_predict_prob > 0.1:
            user = db.sql_select_ban_user(
                telegram_id=message.from_user.id
            )
            count = None
            try:
                count = user['count']
            except TypeError:
                pass
            await message.delete()

            await bot.send_message(
                chat_id=message.chat.id,
                text=f"User: {message.from_user.id} {message.from_user.first_name}\n"
                     f"Please don't swear\n"
                     f"On the third time you will be blocked"
            )
            print(user)
            # count = None
            # try:
            #     count = user['count']
            # except TypeError:
            #     pass
            if not user:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"User: {message.from_user.first_name}\n"
                         f"You added a ban list")
                db.sql_insert_ban_user(
                    telegram_id=message.from_user.id
                )
            elif count >= 3:
                new = types.ChatPermissions(can_send_messages=False)
                await message.bot.restrict_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.from_user.id,
                    permissions=new,
                    until_date=datetime.datetime.now()+datetime.timedelta(seconds=120)
                )
                # await bot.ban_chat_member(
                #     chat_id=message.chat.id,
                #     user_id=message.from_user.id,
                #     until_date=datetime.datetime.now() + datetime.timedelta(seconds=10)
                # )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f'User {message.from_user.first_name} can`t muted on 120sec.'
                )
            elif user:
                db.sql_update_ban_user_count(
                    telegram_id=message.from_user.id
                )
    else:
        await message.reply(
            text=f'"{message.text}" - This command not exist'
        )




def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(chat_messages)