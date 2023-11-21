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
    my_profile_button = InlineKeyboardButton(
        "My Profile 🐼",
        callback_data="my_profile"
    )
    random_profiles_button = InlineKeyboardButton(
        "View Profiles 🫶",
        callback_data="random_profiles"
    )
    complain_button = InlineKeyboardButton(
        "Complain user 🚩",
        callback_data="complain_profiles"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(random_profiles_button)
    markup.add(complain_button)
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

async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Like 👍🏻",
        callback_data=f"liked_profile_{owner_tg_id}"
    )
    dislike_button = InlineKeyboardButton(
        "Dislike 👎🏻",
        callback_data="random_profiles"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup


async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Update profile",
        callback_data=f"update_profile"
    )
    dislike_button = InlineKeyboardButton(
        "Delete profile",
        callback_data="delete_profiles"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup

