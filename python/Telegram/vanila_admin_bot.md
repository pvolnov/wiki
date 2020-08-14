
Code
---

```python
import telebot
from telebot import types

bot = telebot.TeleBot(TG_BOT_APY_KEY)

parsels_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                             one_time_keyboard=True,
                                             row_width=2)
parsels_keyboard.add(
    types.KeyboardButton(text="Hello"),
)

@bot.message_handler(commands=['start', 'menu', 'status'])
def start(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Пришлите пароль для активации бота")


@bot.message_handler(content_types=['document'])
def new_doc(message):
    # save file
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("file.xlsx", "wb") as f:
        f.write(downloaded_file)

@bot.message_handler(content_types=["text"])
def text_mes(message):
    if message.text == config.TG_BOT_PASW:
        print("Heelo")

bot.polling(none_stop=False, timeout=60)

```