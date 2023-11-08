from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire 🔥",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    iphone_button = InlineKeyboardButton(
        "Iphone 🔥",
        callback_data="iphone"
    )
    samsung_button = InlineKeyboardButton(
        "Samsung 🔥",
        callback_data="samsung"
    )
    xiaomi_button = InlineKeyboardButton(
        "Xiaomi 🔥",
        callback_data="xiaomi"
    )
    other_button = InlineKeyboardButton(
        "Other 🔥",
        callback_data="other"
    )
    markup.add(iphone_button)
    markup.add(samsung_button)
    markup.add(xiaomi_button)
    markup.add(other_button)
    return markup