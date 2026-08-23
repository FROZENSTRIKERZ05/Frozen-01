from keep_alive import keep_alive
import telebot
from telebot import types
import threading
import time

TOKEN = "8934154969:AAHZ9bPI5PF18yfzEhcoMroAqUVLIkYRtkA"
bot = telebot.TeleBot(TOKEN)

def delayed_delete(chat_id, message_ids):
    time.sleep(300)
    for m_id in message_ids:
        try:
            bot.delete_message(chat_id, m_id)
        except Exception:
            pass

MENU = (
    "<b>💎 GHOST IN THE WASTELAND 💎</b>\n\n"
    "Hey! If you go for the full feature package, it's normally $35, but right now we have a special offer for just <b>$20!</b>\n\n"
    "<b>Here is what you get with lifetime access:</b>\n\n"
    "🔹 <b>Step-by-step video tutorials</b> to easily learn everything from scratch.\n\n"
    "🔹 <b>24/7 dedicated support</b>—feel free to message me anytime, and I'll be there to help you out.\n\n"
    "🔹 <b>100% free future updates</b>—whenever a new game update drops, you'll get the updated codes at absolutely no extra cost!\n\n"
    "<i>It's a one-time payment for lifetime access. Let me know if you want to grab this deal!</i>"
)

GAME = (
    "===========================\n"
    "  🤠 <b>WESTLAND SURVIVAL: VIP</b> 🤠\n"
    "===========================\n"
    "😈 Game : Westland Survival\n"
    "👑 Status : VIP Lifetime Pass\n"
    "🤝 Contact : @BLACKSUNGOD05\n"
    "-------------------------------------\n"
    "🤟 <b>FEATURES & PRICING:</b>\n"
    "-------------------------------------\n"
    "[🛡] AntiBan() .............. $2🛍\n"
    "[👑] SuperVIP() ............. $2💸\n"
    "[👑] VIP() .................. $1🛍\n"
    "[🔙] InstantTravel() ........ $1💸\n"
    "[🔥] FastFarming() .......... $1🛍\n"
    "[🔪] GodMod() ............... $1💸\n"
    "[🚑] Durability() .......... $1🛍\n"
    "[📦] FreeCraft() ........... $1💸\n"
    "[⏫] FreeUpgrade() ......... $1💸\n"
    "[🔓] UnlockBaitAndHours() ... $1💸\n"
    "[🔓] UnlockEventPass() ..... $1💸\n"
    "[🔝] AllSkillButton() ...... $1💸\n"
    "[🚫] SkipGrowPet() ......... $1🛍\n"
    "[🤬] ModPet() ............... $1💸\n"
    "[🛒] FreeShopSilverton() ... $1🛍\n"
    "[❓] BuildInAnyLocation() .. $1💸\n"
    "[🪙] FreeExchangeGold() .... $1💸\n"
    "[🎖] HackScore() ........... $1💸\n"
    "[📦] DailyReward() ......... $1🛍\n"
    "[🔫] UnlimitedDamage() ..... $1💸\n"
    "[😵] UnlimitedRange() ...... $1💸\n"
    "[🏆] Coins() ............... $1💸\n"
    "[⬆️] LevelUp() ............. $1🛍\n"
    "[🔮] NewEventBoost() ....... $1💸\n"
    "[🏆] UnlimitedEventReward()  $1🛍\n"
    "[🔄] SilvertonEquipment() .. $1💸\n"
    "[👉] MachinesFreeTime() ..... $1🛍\n"
    "[🛠] FreeBuilderZone() ..... $1🛍\n"
    "[👥] FreeSplit() ........... $1🛍\n"
    "[😴] AutoComplaintQuest() .. $1🛍\n"
    "[🌡] FreeXP() .............. $1🛍\n"
    "[🔪] OneTimeHeel() ......... $1💸\n"
    "[⚔️] HackAchievement() ..... $1💸\n"
    "[✉️] InboxUnlimited() ...... $1💸\n"
    "-------------------------------------\n"
    "Full Unlock 🥰 Lifetime 🛍 $35. Special Offer! UNLOCK EVERYTHING FOR JUST $20💸\n"
    "-------------------------------------\n"
    "🤟 ONCE YOU LEARN ALL THIS, YOU CAN HACK FOR THE REST OF YOUR LIFE 🥰\n"
    "==========================="
)

HELP = (
    "<b>🛠 GHOST HELP CENTER 🛠</b>\n\n"
    "<b>Available Commands:</b>\n"
    "• <code>/start</code> - Shows bot intro & your info\n"
    "• <code>/menu</code> - View VIP package & game functions\n"
    "• <code>/help</code> - Open this help center\n\n"
    "💡 <b>To purchase or get support, message the owner:</b>\n"
    "<a href='https://t.me/BLACKSUNGOD05'>@BLACKSUNGOD05</a>"
)

@bot.message_handler(commands=['start'])
def start(m):
    user = m.from_user
    msg_text = (
        f"⚡ <b>WELCOME TO GHOST IN THE WASTELAND, {user.first_name}!</b> ⚡\n\n"
        f"🤖 <i>I am Frozen 01, your dedicated assistant. I am here to guide you through the world of Westland Survival mods. For any queries regarding our Premium VIP features, game functions, or installation help, feel free to ask me first!</i>\n\n"
        f"👤 <b>User Profile:</b>\n"
        f"• <b>Name:</b> {user.first_name}\n"
        f"• <b>ID:</b> <code>{user.id}</code>\n\n"
        f"💡 Need personal assistance from the Owner?\n"
        f"👉 If you require further help or want to purchase a package, feel free to message me <a href='https://t.me/BLACKSUNGOD05'>@BLACKSUNGOD05</a>\n\n"
        f"<i>Type /menu to explore the VIP packages and all game functions.</i>"
    )
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("👑 View VIP Game Functions", callback_data="show_game"))
    markup.add(types.InlineKeyboardButton("💬 Message Owner", url="https://t.me/BLACKSUNGOD05"))
    sent_msg = bot.send_message(m.chat.id, msg_text, parse_mode="HTML", reply_markup=markup, disable_web_page_preview=True)
    if m.chat.type != 'private':
        threading.Thread(target=delayed_delete, args=(m.chat.id, [m.message_id, sent_msg.message_id])).start()

@bot.message_handler(commands=['menu'])
def menu(m):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("👑 View VIP Game Functions", callback_data="show_game"))
    sent_msg = bot.send_message(m.chat.id, MENU, parse_mode="HTML", reply_markup=markup)
    if m.chat.type != 'private':
        threading.Thread(target=delayed_delete, args=(m.chat.id, [m.message_id, sent_msg.message_id])).start()

@bot.message_handler(commands=['help'])
def help_cmd(m):
    sent_msg = bot.send_message(m.chat.id, HELP, parse_mode="HTML", disable_web_page_preview=True)
    if m.chat.type != 'private':
        threading.Thread(target=delayed_delete, args=(m.chat.id, [m.message_id, sent_msg.message_id])).start()

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "show_game":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔙 Help / Info", callback_data="show_help"))
        markup.add(types.InlineKeyboardButton("💬 Message Owner", url="https://t.me/BLACKSUNGOD05"))
        try:
            bot.edit_message_text(GAME, call.message.chat.id, call.message.message_id, parse_mode="HTML", reply_markup=markup)
        except Exception:
            pass
    elif call.data == "show_help":
        bot.answer_callback_query(call.id)
        sent_msg = bot.send_message(call.message.chat.id, HELP, parse_mode="HTML", disable_web_page_preview=True)
        if call.message.chat.type != 'private':
            threading.Thread(target=delayed_delete, args=(call.message.chat.id, [sent_msg.message_id])).start()

# Group Welcome Message for new members (With Name & ID)
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new(message):
    for member in message.new_chat_members:
        if member.is_self:
            continue
        user_name = member.first_name
        user_id = member.id
        welcome_text = (
            f"✨ <b>WELCOME TO GHOST IN THE WASTELAND!</b> ✨\n\n"
            f"👋 Hi {user_name}, Welcome aboard to our exclusive VIP family!\n\n"
            f"👤 <b>Name:</b> {user_name}\n"
            f"🆔 <b>ID:</b> <code>{user_id}</code>\n\n"
            f"🤖 I am Frozen 01, your dedicated assistant. I am here to guide you through using the Westland game mods smoothly. Feel free to explore our VIP features! 🚀"
        )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("👑 View VIP Game Functions", callback_data="show_game"))
        sent_msg = bot.send_message(message.chat.id, welcome_text, parse_mode="HTML", reply_markup=markup)
        threading.Thread(target=delayed_delete, args=(message.chat.id, [sent_msg.message_id])).start()

print("Frozen 01 Bot is running successfully with all features! 🚀")
keep_alive()
bot.polling(none_stop=True, interval=0)
