import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", ""))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "Maxx_Seaching_Bot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1001818361226")) 
    BOT_USERNAME = os.getenv("BOT_USERNAME", "Maxx_Seaching_Bot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", "2061410793"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "TR_TG_46")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "Technical_rakesh_01")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", """**𝗛ᴇʏ 𝗕ᴜᴅᴅʏ! {}😃, 

𝗜'ᴍ 𝗔 𝗕ᴏᴛ 𝗙ᴏʀ 𝗦ᴇɴᴅɪɴɢ 𝗙ʀᴏᴍ 𝗬ᴏᴜʀ 𝗖ʜᴀɴɴᴇʟ 𝗧ᴏ 𝗬ᴏᴜʀ 𝗚ʀᴏᴜᴘ.😚

𝗬ᴏᴜ 𝗖ᴀɴ 𝗔ᴅᴅ 𝗠ᴇ 𝗧ᴏ 𝗬ᴏᴜʀ 𝗚ʀᴏᴜᴘ.☺️

𝗙ᴏʀ 𝗠ᴏʀᴇ 𝗜ɴꜰᴏ 𝗖ʟɪᴄᴋ 𝗢ɴ 𝗛ᴇʟᴘ ✅

𝗠𝗔𝗗𝗘 𝗪𝗜𝗧𝗛 ❤️ 𝗕𝗬
@Rakesh_Owner_Bot

""" ) 
    START_PHOTO = os.getenv("START_PHOTO", "https://telegra.ph/file/44e7072ec7355745a4ab5.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", """ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕

𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝚃𝙷𝙴𝚁𝙴 𝚈𝙾𝚄 𝙻𝙸𝙽𝙺𝚂.

𝙵𝙾𝚁 𝙼𝙾𝚁𝙴 𝙸𝙽𝙵𝙾 𝙲𝙻𝙸𝙲𝙺 𝙾𝙽 𝙷𝙴𝙻𝙿 ✅""" )
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "-1001862060552")
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://postbot:postbot@cluster0.ouwne8q.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001816512392"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 5))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "Technical_rakesh_01")
    FORCE_SUB = os.getenv("FORCE_SUB", "True")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 180))
    MDISK_API = os.getenv("MDISK_API", "fY4fnY9kkWCwfra5bYcE")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "31"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", """𝙸 𝙾𝙽𝙻𝚈 𝚂𝙷𝙰𝚁𝙴 𝚃𝙷𝙴 𝙿𝙾𝚂𝚃 𝙵𝚁𝙾𝙼 𝙿𝙴𝙾𝙿𝙻𝙴'𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻! 

𝚆𝙷𝙾 𝙼𝙰𝙳𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽 𝙸𝙽 𝚃𝙷𝙰𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻, 

𝙸 𝙽𝙾𝚃 𝚂𝚃𝙾𝚁𝙴 𝙰𝙽𝚈 𝙵𝙸𝙻𝙴 𝙾𝚁 𝚃𝙴𝚇𝚃 𝙸𝙽 𝙼𝚈 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴.

𝙳𝙼 𝙵𝙾𝚁 𝙰𝙽𝚈 𝚀𝚄𝙴𝚁𝚈 @Rakesh_Owner_Bot 🤖""" )
    
    ABOUT_HELP_TEXT = """

🍓 RᴇQᴜɪʀᴇᴍᴇɴᴛ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ!

🍓 Sᴛᴇᴘ 1 - Aᴘᴋᴏ ᴇᴋ ɢʀᴏᴜᴘ ᴋɪ ᴊᴀʀᴜʀᴀᴛ ʜᴏɢɪ, ᴊɪꜱᴍᴇ ᴍᴇᴍʙᴇʀꜱ ʙʜɪ ʜᴏ, ᴀᴜʀ ᴇᴋ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴋɪ ᴊᴀʀᴜʀᴀᴛ ʜᴏɢɪ, ᴊɪꜱᴍᴇ ᴀᴘᴋᴇ ꜱᴀʀᴇ ᴘᴏꜱᴛ ʜᴏɴɢᴇ!

🍓 Sᴛᴇᴘ 2 - ʙᴏᴛ ᴋᴏ ᴀᴘɴᴇ ɢʀᴏᴜᴘ ᴀᴜʀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴋᴀ ᴀᴅᴍɪɴ ʙᴀɴᴀɴᴀ ʜᴏɢᴀ.

🍓 Sᴛᴇᴘ 3 - ɢʀᴏᴜᴘ ᴍᴇ "/License" ᴛʏᴘᴇ ᴋᴀʀ ᴋᴇ ꜱᴇɴᴅ ᴋᴀʀɴᴀ ʜᴏɢᴀ!

ꜰɪʀ ʙᴏᴛ ᴋᴇ ᴏᴡɴᴇʀ ᴀᴘᴋᴀ ʏᴇ ʀᴇQᴜᴇꜱᴛ ᴀᴄᴄᴇᴘᴛ ᴋᴀʀ ʟᴇɴɢᴇ. 

🍓 Sᴛᴇᴘ 4 - ɢʀᴏᴜᴘ ᴍᴇ "/database - ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ɪᴅ" ᴛʏᴘᴇ ᴋᴀʀ ᴋᴇ ꜱᴇɴᴅ ᴋᴀʀɴᴀ ʜᴏɢᴀ.

ꜰɪʀ ʙᴏᴛ ᴋᴇ ᴏᴡɴᴇʀ ᴀᴘᴋᴀ ʏᴇ ʀᴇQᴜᴇꜱᴛ ʙʜɪ ᴀᴄᴄᴇᴘᴛ ᴋᴀʀ ʟᴇɴɢᴇ 

🍓 Sᴛᴇᴘ 5 - ᴀʙ ᴀᴘᴋᴏ ᴀᴘɴᴇ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴍᴇ ᴘᴏꜱᴛ ᴅᴀʟɴɪ ʜᴏɢɪ,

ᴊɪꜱꜱᴇ ᴋɪ ᴀɢᴀʀ ɢʀᴏᴜᴘ ᴍᴇ ᴋᴏɪ ᴜꜱᴇʀ ꜱᴇᴀʀᴄʜ ᴋᴀʀᴇ ᴛᴏ ʏᴇ ʙᴏᴛ ᴜɴ ᴜꜱᴇʀ ᴋᴇ Qᴜᴀʀʏ ᴋᴏ ꜱᴀᴍᴀᴊʜ ᴋᴇ ᴀᴘᴋᴇ ᴄʜᴀɴɴᴇʟ ꜱᴇ ᴘᴏꜱᴛ ᴜᴛʜᴀ ᴋᴇ ᴜɴʜᴇ ᴅᴇ ᴘᴀʏᴇ.

🍓 Nᴏᴛᴇ : Bᴏᴛ ᴀᴅᴍɪɴ ᴀᴘᴋᴇ ᴄʜᴀɴɴᴇʟ ᴍᴇ ᴊᴏɪɴ ʜᴏɴᴇ ᴄʜᴀʜɪʏᴇ,

ᴀɢᴀʀ ʙᴏᴛ ᴀᴅᴍɪɴ ᴀᴘᴋᴀ ʀᴇQᴜᴇꜱᴛ ᴀᴄᴄᴇᴘᴛ ɴʜɪ ᴋᴀʀ ʀᴀʜᴇ ʜᴀɪɴ ᴛᴏ ᴜɴʜᴇ ᴘᴇʀꜱᴏɴᴀʟ ᴍꜱɢ ᴋᴀʀᴇɴ.

👉 @Rakesh_Owner_Bot

"""

