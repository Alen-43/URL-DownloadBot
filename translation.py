from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hey {} , I'am a url to telegram file or media uploader bot with permanent thumbnail support.

ᴘᴏᴡᴇʀᴅ ʙʏ: [sᴘᴀᴄᴇ4ᴄɪɴᴇᴍᴀs](https://t.me/space4cinemas)
"""
    HELP_TEXT = """
<b><u>Link to Media or File</u></b>
➠ Send a link for upload to telegram file or media.

<b><u>Set Thumbnail</u></b>
➠ Send a photo to make it as permanent thumbnail.

<b><u>Deleting Thumbnail</u></b>
➠ Send /delthumb to deleting thumbnail.

<b><u>Show Thumbnail</u></b>
➠ Send /showthumb to view custom thumbnail.

Made by @Mo_Tech_YT
"""
    ABOUT_TEXT = """
- **ʙᴏᴛ      :** URL Uploader
- **ᴄʀᴇᴀᴛᴏʀ  :**
- **ᴄʀᴇᴅɪᴛs  :** `Everyone in this journey`
- **sᴏᴜʀᴄᴇ   :** [Click here](https://github.com/MRK-YT/MT-URL-Uploader)
- **ʟᴀɴɢᴜᴀɢᴇ :** [Python3](https://python.org)
- **ʟɪʙʀᴀʀʏ  :** [Pyrogram v1.2.0](https://pyrogram.org)
- **sᴇʀᴠᴇʀ   :** [Heroku](https://heroku.com)
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔎sᴇᴀʀᴄʜ ᴍᴏᴠɪᴇs🔍', url='https://t.me/space4cinemas')
        ],[
        InlineKeyboardButton('🤖Bot List', url='https://t.me/Mo_Tech_YT/176'),
        InlineKeyboardButton('👨‍💻Source', url='https://youtu.be/nRSbkf3memQ')
        ],[
        InlineKeyboardButton('ʜᴇʟᴘ🤌', callback_data='help'),
        InlineKeyboardButton('ᴀʙᴏᴜᴛ😎', callback_data='about'),
        InlineKeyboardButton('ᴄʟᴏsᴇ🚮', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🗣️𝙶𝚛𝚘𝚞𝚙', url='https://t.me/Mo_tech_group'),
        InlineKeyboardButton('🤖Bot List', url='https://t.me/Mo_Tech_YT/176'),
        InlineKeyboardButton('👨‍💻Source', url='https://youtu.be/nRSbkf3memQ')
        ],[
        InlineKeyboardButton('ʙᴀᴄᴋ↩️', callback_data='home'),
        InlineKeyboardButton('ᴀʙᴏᴜᴛ😎', callback_data='about'),
        InlineKeyboardButton('ᴄʟᴏsᴇ🚮', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🗣️𝙶𝚛𝚘𝚞𝚙', url='https://t.me/Mo_tech_group'),
        InlineKeyboardButton('🤖Bot List', url='https://t.me/Mo_Tech_YT/176'),
        InlineKeyboardButton('👨‍💻Source', url='https://youtu.be/nRSbkf3memQ')
        ],[
        InlineKeyboardButton('ʙᴀᴄᴋ↩️', callback_data='home'),
        InlineKeyboardButton('ʜᴇʟᴘ🤌', callback_data='help'),
        InlineKeyboardButton('ᴄʟᴏsᴇ🚮', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = """<b>Select the desired format:</b> <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /delthumb to delete the auto-generated thumbnail."""
    CHECKING_LINK = "<code>Analysing Your Link</code>⏳"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""
    DOWNLOAD_START = "<code>Downloading To My server Please Wait...</code>"    
    UPLOAD_START = "<code>Uploading into Telegram...</code>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    CUSTOM_CAPTION_UL_FILE = "<b>Join :-</b> @Mo_Tech_YT"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    REPORT_SITE_TEXT = "<code>Sorry not uploading in this site here because this site is reporting site.</code>"
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    FORCE_SUBSCRIBE_TEXT = "<code>Sorry Dear You Must Join My Updates Channel for using me 😌😉....</code>"
    FREE_USER_LIMIT_Q_SZE = "Sorry Friend, Free users can only 1 request per {} minutes. Please try again after {} seconds later."
