from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire 🔥",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Registration 👨‍💼",
        callback_data="registration"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
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

async def stats_keyboard():
    markup = InlineKeyboardMarkup()
    all_users_stats_button = InlineKeyboardButton(
        "Select from base all users",
        callback_data="all list"
    )
    ban_list_users_stats_button = InlineKeyboardButton(
        text="Select from base users who in ban list",
        callback_data="ban list"
    )
    markup.add(all_users_stats_button)
    markup.add(ban_list_users_stats_button)
    return markup

