import telebot, wikipedia, re
bot = telebot.TeleBot('')
wikipedia.set_lang("ru")
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.') # Разделяем по точкам
        wikimas = wikimas[:-1] # Отброс символов после последней точки
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        wikiurl=wikipedia.page(s).url
        return wikitext2
        bot.register_next_step_handler(s, url);
    except Exception as e:
        return 'В энциклопедии нет информации об этом'
def url(s):
    wikiurl=wikipedia.page(s).url
    return wikiurl
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
    bot.send_message(message.chat.id, 'Для полного ознакомления перейдите по ссылке: ' + url(message.text))
bot.polling(none_stop=True, interval=0)
