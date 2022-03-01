from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
        [
            InlineKeyboardButton('Support', url='t.me/Dsrs_Group'),
            InlineKeyboardButton('More', url='https://t.me/kashir_bots')
        ]
        ]

close = [
        [
            InlineKeyboardButton('Support', url='t.me/Dsrs_Group'),
            InlineKeyboardButton('Close', callback_data='close_btn')
        ]
        ]

start_buttons = InlineKeyboardMarkup(start)
close_button = InlineKeyboardMarkup(close)
