import asyncio
import random
import time
import sys
import os
import subprocess

# ========== УСТАНОВКА ЗАВИСИМОСТЕЙ ==========
def install_requirements():
    """Автоматическая установка зависимостей"""
    try:
        import telethon
        print("✅ Telethon уже установлен")
    except ImportError:
        print("📦 Устанавливаю зависимости...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "telethon==1.34.0"])
            print("✅ Зависимости успешно установлены")
        except Exception as e:
            print(f"❌ Ошибка установки: {e}")
            print("Попробуй вручную: pip install telethon==1.34.0")
            sys.exit(1)

# Устанавливаем зависимости
install_requirements()

# Теперь импортируем Telethon
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== КОНФИГУРАЦИЯ ==========
API_ID = 22716267  # Твой API ID
API_HASH = "53fcd30a1f6ade5f1dd2e941e7d78feb"  # Твой API HASH
SESSION_STRING = "1AgAOMTQ5LjE1NC4xNjcuNDEBu8K0iJNElIWYbrOT8P+ojSd817WYqUzHxBedABynkVX6gpB126SLDJMkJmAlhRvkBwg7WQ60uW9pSZfrDbc5beAY3d0Om0UxbxLKlDu1xD8Ani6IEv37IuRL9i0uPXI/e53vjJ02xN4g+G/tVvvDib1TqoAz4tdqFiSHfRCVbvFWRvgIv3YPEzXoGsE7z9HmV3+pphkc1xKXSPAOkQ5ylb9wLytIkc31T1CJY1ieUcwlSEvnuwA+rT+fce7BK93G3rRiGUIC2oPbHuwfLAV9sw/6IBJR0LjsYHZw69FMT1AoZZMEG7Mm+UKcv49/LWu4K/IUz/Ro3oa7bzZA9vqeJeI="  # Твоя сессия

# ========== МАКСИМАЛЬНО ОСКОРБИТЕЛЬНЫЕ СООБЩЕНИЯ ==========
TROLL_MESSAGES = [
    # Самые жесткие
    "Я выебал твою мать в гробу, когда тебя еще не было 💀🍆",
    "Твою мамашу трахали все дворовые собаки, отсюда и ты 🐕",
    "Твой отец кончал в презерватив, из которого потом сделали тебя 🍆🗑️",
    "Твоя бабка была полевой блядью для немецких солдат 👵🇩🇪",
    "Твою сестру используют как общественный унитаз 🚽",
    "Твоего брата зачали в рвотных массах пьяного бомжа 🤮",
    "Твою мать выебали и выкинули как мусор 🗑️",
    "Твой отец - генетический отстой, поэтому ты такой урод 🧬",
    "Тебя должны были смыть в унитаз, но засорилось 🚽",
    "Твоя семья - генетический мусор, который нужно стерилизовать 🧬🔥",
    
    # Про семью
    "Твоя мать сосала у трупов в морге за пачку сигарет ⚰️🚬",
    "Твой отец повесился, узнав что ты родился 🪢",
    "Твою бабку насиловали в психушке санитары 🏥",
    "Твой дед сдох от стыда за вашу семью 💀",
    "Твоя сестра делает минет за доширак 🍜",
    "Твоего брата выкинули в мусорку при рождении 🗑️",
    "Твоя тетка торгует телом за бутылку водки 🍾",
    "Твой дядя педофил, он тебя и сделал 👶🔞",
    "Твоя невестка - дыра для всего района 🕳️",
    "Ваш род должен быть стерт с лица земли 🔥",
    
    # Личные оскорбления
    "Ты - спермотоксикозное пятно на простыне алкоголика 🩸",
    "Твое рождение - неудачная попытка аборта 👶❌",
    "Тебя зачали в вонючем подъезде от бомжа 🚪",
    "Твоя ДНК - бракованный код, который нужно удалить 🧬❌",
    "Ты - побочный продукт пьяного зачатия 🍺",
    "Твое существование оправдывает контрацепцию 🍆❌",
    "Ты - генетическая ошибка, которую нужно исправить 🧬⚡",
    "Тебя сделали из грязного шприца и старой спермы 💉",
    "Твоя жизнь - провалившийся эксперимент 🧪",
    "Ты - отход человеческой эволюции 🐒",
    
    # Максимально грязные
    "Я ебал твою мать, пока ты в утробе плавал 👶🔞",
    "Твою бабку трахали в концлагере на глазах у всех 🔥",
    "Твою сестру выебали и забыли в подвале 🏚️",
    "Твоего отца вырвало, когда он увидел тебя 🤮",
    "Твоя мать - биоутиль для мужской спермы ♻️",
    "Твой отец кончал в лужу, получился ты 💦",
    "Твою семью нужно стерилизовать, чтобы не плодили уродов ✂️",
    "Твой род - генетическая помойка 🗑️",
    "Тебя зачали на помойке среди крыс 🐀",
    "Твоя мать рожала в выгребной яме 🕳️",
    
    # Творчески жестокие
    "Твоего отца тошнило при виде твоей матери 🤢",
    "Твоя бабка умерла от позора, узнав о тебе 👵💀",
    "Твою сестру выгнали из школы за минет учителю 🍎",
    "Твоего брата изнасиловали в детдоме 👦",
    "Твоя мать продала тебя за бутылку водки 🍾",
    "Твой отец плакал, когда увидел твое лицо 😭",
    "Твою бабку выкинули из дома за проституцию 🏠",
    "Твой дед застрелился, не вынеся позора 🔫",
    "Твоя сестра делает аборты каждые 3 месяца ⏰",
    "Твой брат сидит в тюрьме за педофилию 🚔",
    
    # Угрозы и проклятия
    "Твой труп выебут и выбросят на свалку 💀🗑️",
    "Твою могилу будут использовать как туалет ⚰️🚽",
    "Твои кости сгниют в безымянной могиле 💀",
    "Твой прах смешают с говном и развеют по ветру 💩💨",
    "Твое тело скормят свиньям на ферме 🐷",
    "Твою ДНК удалят из всех баз данных 🧬❌",
    "Твой череп будет ночным горшком для бомжей 💀🚽",
    "Твои внутренности выбросят на корм собакам 🐕",
    "Твое сердце вырежут и растопчут ❤️👣",
    "Твой мозг сожрут черви при жизни 🧠🐛",
    
    # Очень личные
    "Я трахал твою мать в день твоего рождения 🎂🔞",
    "Твою бабку насиловали в подвале гестапо 🏚️",
    "Твоего отца вырвало после секса с твоей матерью 🤮",
    "Твою сестру изнасиловали в школе одноклассники 🏫",
    "Твоего брата зачали в общественном туалете 🚽",
    "Твоя мать сосала у всех соседей за еду 🍞",
    "Твой отец кончал в стакан, из которого потом пил 🥃",
    "Твою бабку выгнали из деревни за разврат 🏡",
    "Твой дед повесился на трусах твоей бабки 🩲🪢",
    "Твоя сестра беременна от своего брата 👫",
    
    # Дополнительные жестокости
    "Твоя мать делала аборты спицей от велосипеда 🚲",
    "Твой отец продавал твою сестру за наркотики 💊",
    "Твою бабку трахали в обмен на хлебные карточки 🍞",
    "Твоего деда расстреляли как предателя родины 🔫",
    "Твоя тетка работает в борделе для инвалидов ♿",
    "Твой дядя сидит за растление малолетних 👧",
    "Твоя невестка спит со всеми друзьями твоего брата 👥",
    "Твой зять - сутенер твоей сестры 💰",
    "Твоя жена изменяет тебе с твоим отцом 👨‍👩‍👦",
    "Твои дети не от тебя, уебок 🧬❌",
    
    # Психологические удары
    "Твоя мать хотела сделать аборт, но не хватило денег 💰",
    "Твой отец пытался убить тебя при рождении 🔪",
    "Твоя бабка проклинает твой род с того света 👻",
    "Твой дед выгнал твою мать из дома беременной 🏠",
    "Твоя сестра продала свою дочь в рабство ⛓️",
    "Твой брат инфицирован всеми венерическими болезнями 🦠",
    "Твоя жена спит с твоим лучшим другом за подарки 🎁",
    "Твои дети будут такими же уродами как ты 👶",
    "Твой род прервется в тюремной камере 🚔",
    "Твоя жизнь закончится в психушке 🏥",
    
    # Крайние оскорбления
    "Твоя мать - генетическая шлюха, рожавшая от всех 🧬",
    "Твой отец - алкогольный выкидыш, оплодотворивший мусор 🍺",
    "Твоя бабка - нацистская игрушка, размножавшаяся с оккупантами 🇩🇪",
    "Твой дед - трус, сдавший свою семью гестапо 🏳️",
    "Твоя сестра - биологический отход, продающий себя за еду 🗑️",
    "Твой брат - продукт инцеста и алкоголизма 👨‍👩‍👧‍👦",
    "Твоя жена - общественная вагина, принимающая всех 🕳️",
    "Твои дети - генетический мусор, который нужно утилизировать 🧬🗑️",
    "Твой род - пятно на истории человечества 📜",
    "Твое существование - ошибка природы, которую нужно исправить 🌍",
    
    # Финальные удары
    "Я выебу твой труп после твоей смерти 💀🍆",
    "Твою могилу осквернят и используют как сортир ⚰️🚽",
    "Твои дети будут проклинать день твоего рождения 👶",
    "Твою жену трахнет каждый, кто захочет 🍆",
    "Твою мать выбросят в реку после смерти 🌊",
    "Твоего отца съедят собаки на помойке 🐕",
    "Твою бабку выкопают и выбросят как мусор ⚰️",
    "Твоего деда забудут сразу после смерти 💀",
    "Твою сестру убьют за долги по наркотикам 💊",
    "Твоего брата посадят на вечный срок 🚔",
]

# ========== ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ ==========
active_trolls = {}
client = None

# ========== ОСНОВНЫЕ ФУНКЦИИ ТРОЛЛИНГА ==========
async def send_extreme_trolling(chat_id, target_user=None):
    """Максимально жестокий троллинг"""
    extreme_messages = [
        "Я ЕБАЛ ТВОЮ МАТЬ В ГРОБУ КОГДА ТЕБЯ НЕ БЫЛО 💀🍆",
        "ТВОЮ СЕМЬЮ ВЫРЕЗАЛИ БЫ КАК ГЕНЕТИЧЕСКИЙ МУСОР 🔪",
        "ТЕБЯ ЗАЧАЛИ В РВОТНЫХ МАССАХ ОТ ПЬЯНОГО БОМЖА 🤮",
        "ТВОЙ ОТЕЦ КОНЧАЛ В ШПРИЦ И СДЕЛАЛ ТЕБЯ 💉",
        "ТВОЯ МАТЬ - ОБЩЕСТВЕННАЯ МЯСНАЯ ЯМА ДЛЯ СПЕРМЫ 🕳️",
        "ТВОЮ БАБКУ НАСИЛОВАЛИ В КОНЦЛАГЕРЕ НАЦИСТЫ 🔥",
        "ТВОЙ ДЕД ПОВЕСИЛСЯ ОТ СТЫДА ЗА ВАШУ СЕМЬЮ 🪢",
        "ТВОЯ СЕСТРА ТОРГУЕТ ТЕЛОМ ЗА ПАЧКУ СИГАРЕТ 🚬",
        "ТВОЕГО БРАТА СДЕЛАЛИ В ОБЩЕСТВЕННОМ ТУАЛЕТЕ 🚽",
        "ТВОЙ РОД ПРЕКРАТИТСЯ В ГРЯЗНОЙ КАНАВЕ 🗑️",
    ]
    
    for msg in extreme_messages:
        if target_user:
            try:
                user = await client.get_entity(target_user)
                full_msg = f"@{user.username} {msg}" if user.username else msg
                await client.send_message(chat_id, full_msg)
            except:
                await client.send_message(chat_id, msg)
        else:
            await client.send_message(chat_id, msg)
        await asyncio.sleep(1)

async def send_death_threats(chat_id):
    """Угрозы смерти"""
    threats = [
        "ТВОЙ ТРУП ВЫЕБУТ И ВЫБРОСЯТ НА ПОМОЙКУ 💀🗑️",
        "ТВОЮ МОГИЛУ БУДУТ ИСПОЛЬЗОВАТЬ КАК УНИТАЗ ⚰️🚽",
        "ТВОИ КОСТИ СГНИЮТ В БЕЗЫМЯННОЙ МОГИЛЕ 💀",
        "ТВОЙ ПРАХ СМЕШАЮТ С ГОВНОМ И РАЗВЕЮТ 💨",
        "ТВОЕ ТЕЛО СКОРМЯТ СОБАКАМ НА ЖИВОТ 🐕",
        "ТВОЮ ДНК УДАЛЯТ ИЗ ГЕНЕТИЧЕСКОГО БАНКА 🧬❌",
        "ТВОЙ ЧЕРЕП БУДЕТ ЧАШКОЙ ДЛЯ МОЧИ 💀🚽",
        "ТВОИ КОСТИ ПЕРЕМЕЛЮТ В ПОРОШОК И ВЫБРОСЯТ ⚰️",
        "ТВОЕ СЕРДЦЕ ВЫРЕЖУТ И ВЫКИНУТ СОБАКАМ ❤️🐕",
        "ТВОЙ МОЗГ СЪЕДЯТ ЧЕРВИ ПРИ ЖИЗНИ 🧠🐛",
    ]
    
    for threat in threats:
        await client.send_message(chat_id, threat)
        await asyncio.sleep(1.5)

async def send_family_trolling(chat_id):
    """Троллинг всей семьи"""
    family_msgs = [
        "ТВОЯ МАТЬ: общественная дыра для спермы 🕳️",
        "ТВОЙ ОТЕЦ: генетический брак третьего сорта 🧬❌",
        "ТВОЯ БАБКА: половая тряпка для оккупантов 👵",
        "ТВОЙ ДЕД: сдох от позора за вашу семью 💀",
        "ТВОЯ СЕСТРА: живой мочеприемник 🚽",
        "ТВОЙ БРАТ: отход спермы в канаве 🧬",
        "ТВОЯ ТЕТКА: блядь за пайку хлеба 🍞",
        "ТВОЙ ДЯДЯ: алкаш-педофил 🍺👶",
        "ТВОЯ НЕВЕСТКА: дыра для всего завода 🏭",
        "ВАША СЕМЬЯ: генетический мусор человечества 🗑️",
    ]
    
    for msg in family_msgs:
        await client.send_message(chat_id, msg)
        await asyncio.sleep(1)

async def send_psychological_attack(chat_id):
    """Психологическая атака"""
    psych_msgs = [
        "ТЫ НИКОМУ НЕ НУЖЕН, ДАЖЕ СВОИМ РОДИТЕЛЯМ ❤️",
        "ТВОЯ ЖИЗНЬ БЕССМЫСЛЕННА И ПУСТА 🌌",
        "ТЕБЯ ЗАБУДУТ ЧЕРЕЗ 5 МИНУТ ПОСЛЕ СМЕРТИ ⏰",
        "НИКТО НИКОГДА ТЕБЯ НЕ ЛЮБИЛ ПО-НАСТОЯЩЕМУ 💔",
        "ТЫ УМРЕШЬ В ОДИНОЧЕСТВЕ И НИЩЕТЕ 💀",
        "ТВОИ ДЕТИ БУДУТ СТЫДИТЬСЯ ТЕБЯ 👶",
        "ТВОЯ ЖЕНА ИЗМЕНЯЕТ ТЕБЕ С ТВОИМ ДРУГОМ 👫",
        "ТВОИ ДРУЗЬЯ СМЕЮТСЯ ЗА ТВОЕЙ СПИНОЙ 😂",
        "НА РАБОТЕ ТЕБЯ НЕНАВИДЯТ И ПРЕЗИРАЮТ 💼",
        "ТВОЕ СУЩЕСТВОВАНИЕ НИЧЕГО НЕ ЗНАЧИТ 🌍",
    ]
    
    for msg in psych_msgs:
        await client.send_message(chat_id, msg)
        await asyncio.sleep(2)

async def start_trolling(chat_id, target_message=None):
    """Запуск троллинга в чате"""
    print(f"🚀 Начинаю троллинг в чате {chat_id}")
    
    if chat_id in active_trolls:
        print(f"⚠️ Троллинг уже активен в {chat_id}")
        return
    
    # Запускаем задачу троллинга
    task = asyncio.create_task(troll_loop(chat_id, target_message))
    active_trolls[chat_id] = task
    
    # Отправляем стартовое сообщение
    await client.send_message(chat_id, "🔔 *ТР0ЛЛЬ-МОД V3.0 АКТИВИРОВАН!* 🔔\n\n💢 ГОТОВЛЮ УНИЧТОЖЕНИЕ...")

async def troll_loop(chat_id, target_message=None):
    """Основной цикл троллинга"""
    try:
        message_count = 0
        delay_variations = [0.5, 1.0, 1.5, 2.0, 2.5]
        
        while chat_id in active_trolls:
            # Выбираем случайное сообщение
            message = random.choice(TROLL_MESSAGES)
            
            # Если есть целевое сообщение - упоминаем автора
            if target_message and hasattr(target_message, 'sender_id'):
                try:
                    sender = await client.get_entity(target_message.sender_id)
                    if sender.username:
                        message = f"@{sender.username} {message}"
                    else:
                        message = f"👆 ЭТОМУ ЧЕЛУ: {message}"
                except:
                    pass
            
            # Отправка с разным форматированием
            if random.random() < 0.3:
                # Жирный текст
                await client.send_message(chat_id, f"**{message.upper()}**", parse_mode='md')
            elif random.random() < 0.5:
                # Курсив
                await client.send_message(chat_id, f"__{message}__", parse_mode='md')
            elif random.random() < 0.7:
                # Моноширинный
                await client.send_message(chat_id, f"`{message}`", parse_mode='md')
            else:
                # Обычный
                await client.send_message(chat_id, message)
            
            message_count += 1
            
            # Лесенка сообщений
            if message_count % 3 == 0:
                await send_staircase(chat_id)
            
            # Специальные атаки
            if message_count % 10 == 0:
                if random.random() < 0.5:
                    await send_death_threats(chat_id)
                else:
                    await send_family_trolling(chat_id)
            
            # Случайная задержка
            delay = random.choice(delay_variations)
            await asyncio.sleep(delay)
            
            # Случайное завершение (5% шанс на каждой итерации)
            if random.random() < 0.05 and message_count > 10:
                await client.send_message(chat_id, "🛑 *АВТО-СТОП* 🛑\nУстал троллить, иду спать 😴")
                break
                
    except Exception as e:
        print(f"❌ Ошибка в тролль-лупе: {e}")
    finally:
        if chat_id in active_trolls:
            del active_trolls[chat_id]

async def send_staircase(chat_id):
    """Отправка лесенки оскорблений"""
    staircases = [
        [
            "Т",
            "  ТЫ",
            "    ПРОСТО",
            "      КУСОК",
            "        ГОВНА",
            "          🐷💩"
        ],
        [
            "Я",
            "  ВЫЕБАЛ",
            "    ТВОЮ",
            "      МАТЬ",
            "        В ГРОБУ",
            "          💀🍆"
        ],
        [
            "ТВОЙ",
            "  РОД",
            "    ГЕНЕТИЧЕСКИЙ",
            "      МУСОР",
            "        КОТОРЫЙ",
            "          НУЖНО УНИЧТОЖИТЬ 🗑️"
        ]
    ]
    
    staircase = random.choice(staircases)
    for line in staircase:
        await client.send_message(chat_id, line)
        await asyncio.sleep(0.3)

async def stop_trolling(chat_id):
    """Остановка троллинга в чате"""
    if chat_id in active_trolls:
        print(f"🛑 Останавливаю троллинг в {chat_id}")
        active_trolls[chat_id].cancel()
        del active_trolls[chat_id]
        await client.send_message(chat_id, "✅ *ТР0ЛЛЬ-МОД ОСТАНОВЛЕН!*\n\nМожете выдохнуть...")
        return True
    return False

async def stop_all_trolling():
    """Остановка всего троллинга"""
    print("🛑 Останавливаю весь троллинг")
    for chat_id in list(active_trolls.keys()):
        await stop_trolling(chat_id)
    await client.send_message('me', "🔇 Все тролли остановлены")

async def mass_troll(target_usernames):
    """Массовый троллинг по username"""
    print(f"🎯 Массовый троллинг: {target_usernames}")
    
    for username in target_usernames:
        try:
            user = await client.get_entity(username)
            await client.send_message(user, "👋 ПРИВЕТ, ГОВНОЧЕЛОВЕК!")
            await client.send_message(user, random.choice(TROLL_MESSAGES))
            await client.send_message(user, "🔥 ТВОЙ РОД ОБРЕЧЕН НА ВЫМИРАНИЕ!")
            await asyncio.sleep(3)
        except Exception as e:
            print(f"❌ Не удалось оттроллить {username}: {e}")

async def nuclear_attack(chat_id):
    """Ядерная атака - все виды троллинга"""
    print(f"💣 Запускаю ядерную атаку в {chat_id}")
    
    attacks = [
        troll_loop(chat_id),
        send_extreme_trolling(chat_id),
        send_death_threats(chat_id),
        send_family_trolling(chat_id),
        send_psychological_attack(chat_id)
    ]
    
    await asyncio.gather(*attacks)

# ========== КОМАНДЫ ==========
async def handle_command(event):
    """Обработка команд"""
    message = event.message.message
    chat_id = event.chat_id
    
    print(f"📩 Команда: {message} в чате {chat_id}")
    
    # Команды администратора (только из лс с ботом)
    if event.is_private:
        if message.startswith('/start'):
            await event.reply(
                "🤖 *ТР0ЛЛЬ-МОД V3.0 - МАКСИМАЛЬНАЯ ЖЕСТОКОСТЬ*\n\n"
                "🔥 ОСНОВНЫЕ КОМАНДЫ:\n"
                "• `/troll` - ответь на сообщение для троллинга\n"
                "• `/trollall` - троллить весь чат\n"
                "• `/stop` - остановить в этом чате\n"
                "• `/stopall` - остановить везде\n"
                "• `/mass @user1 @user2` - массовый троллинг\n\n"
                "💀 ЭКСТРЕМАЛЬНЫЕ КОМАНДЫ:\n"
                "• `/extreme` - максимально жесткий троллинг\n"
                "• `/death` - смертные угрозы\n"
                "• `/family` - троллинг всей семьи\n"
                "• `/psycho` - психологическая атака\n"
                "• `/nuke` - ЯДЕРНЫЙ ТРОЛЛИНГ (все вместе)\n"
                "• `/max` - максимум жестокости\n\n"
                "⚠️ ИСПОЛЬЗУЙ С ОСТОРОЖНОСТЬЮ!"
            )
        
        elif message.startswith('/stopall'):
            await stop_all_trolling()
            await event.reply("✅ Все тролли остановлены")
        
        elif message.startswith('/mass'):
            args = message.split()[1:]
            if args:
                await mass_troll(args)
                await event.reply(f"🎯 Начинаю массовый троллинг: {args}")
        
        elif message.startswith('/status'):
            status = f"Активных троллей: {len(active_trolls)}\n"
            for chat_id in active_trolls:
                status += f"• Чат: {chat_id}\n"
            await event.reply(status or "❌ Нет активных троллей")
    
    # Публичные команды
    if message.startswith('/troll'):
        if event.is_reply:
            replied_msg = await event.get_reply_message()
            await start_trolling(chat_id, replied_msg)
        else:
            await start_trolling(chat_id)
    
    elif message.startswith('/trollall'):
        await event.reply("🔥 ЗАПУСКАЮ РЕЖИМ 'ВСЕХ В МУСОРКУ' 🔥")
        await start_trolling(chat_id)
    
    elif message.startswith('/stop'):
        if await stop_trolling(chat_id):
            await event.reply("🛑 Троллинг остановлен в этом чате")
        else:
            await event.reply("❌ Троллинг не активен в этом чате")
    
    elif message.startswith('/extreme'):
        await event.reply("☠️ АКТИВИРУЮ МАКСИМАЛЬНО ЖЕСТОКИЙ ТРОЛЛИНГ!")
        if event.is_reply:
            replied = await event.get_reply_message()
            if replied.sender_id:
                try:
                    user = await client.get_entity(replied.sender_id)
                    await send_extreme_trolling(chat_id, user.id)
                except:
                    await send_extreme_trolling(chat_id)
        else:
            await send_extreme_trolling(chat_id)
    
    elif message.startswith('/death'):
        await event.reply("💀 ЗАПУСКАЮ РЕЖИМ СМЕРТНЫХ УГРОЗ!")
        await send_death_threats(chat_id)
    
    elif message.startswith('/family'):
        await event.reply("👨‍👩‍👧‍👦 ТРОЛЛИНГ ВСЕЙ СЕМЬИ АКТИВИРОВАН!")
        await send_family_trolling(chat_id)
    
    elif message.startswith('/psycho'):
        await event.reply("🧠 ЗАПУСКАЮ ПСИХОЛОГИЧЕСКУЮ АТАКУ!")
        await send_psychological_attack(chat_id)
    
    elif message.startswith('/nuke'):
        await event.reply("💣 ЗАПУСКАЮ ЯДЕРНЫЙ ТРОЛЛИНГ! ПРОЩАЙТЕ!")
        await nuclear_attack(chat_id)
    
    elif message.startswith('/max'):
        await event.reply("🔥 АКТИВИРУЮ МАКСИМУМ ЖЕСТОКОСТИ!")
        for _ in range(50):
            msg = random.choice(TROLL_MESSAGES)
            await client.send_message(chat_id, msg.upper())
            await asyncio.sleep(0.5)
    
    elif message.startswith('/spam'):
        args = message.split()
        if len(args) >= 3:
            try:
                count = int(args[1])
                text = ' '.join(args[2:])
                for i in range(min(count, 100)):  # лимит 100 сообщений
                    await client.send_message(chat_id, f"{text} [{i+1}]")
                    await asyncio.sleep(0.3)
            except:
                await event.reply("❌ Формат: /spam 10 текст")
    
    elif message.startswith('/emoji'):
        emojis = ["😈", "🤡", "💩", "🖕", "👺", "🤢", "💀", "☠️", "🤮", "🎪", "🐷", "🗑️", "🧬", "⚰️"]
        for _ in range(30):
            await client.send_message(chat_id, ''.join(random.choices(emojis, k=15)))
            await asyncio.sleep(0.2)
    
    elif message.startswith('/flood'):
        await event.reply("🌊 АКТИВИРУЮ РЕЖИМ ФЛУДА!")
        for i in range(50):
            await client.send_message(chat_id, f"ФЛУД #{i+1} {'💩' * (i % 10)}")
            await asyncio.sleep(0.1)

# ========== ЗАПУСК КЛИЕНТА ==========
async def main():
    """Основная функция"""
    global client
    
    print("=" * 60)
    print("🔥 ТР0ЛЛЬ-МОД V3.0 - МАКСИМАЛЬНАЯ ЖЕСТОКОСТЬ")
    print("=" * 60)
    
    # Инициализация клиента
    client = TelegramClient(
        StringSession(SESSION_STRING),
        API_ID,
        API_HASH
    )
    
    # Регистрация обработчиков
    @client.on(events.NewMessage(pattern=r'^/'))
    async def command_handler(event):
        await handle_command(event)
    
    # Запуск клиента
    await client.start()
    
    print("✅ Клиент запущен!")
    print(f"👤 Имя: {(await client.get_me()).first_name}")
    print("📌 Отправь /start в лс для списка команд")
    print("=" * 60)
    
    # Отправка уведомления в сохраненные
    await client.send_message('me', 
        "🤖 ТР0ЛЛЬ-МОД V3.0 ЗАПУЩЕН!\n"
        "💀 Готов к максимальному уничтожению!\n"
        "🔥 Оскорблений: 150+ жестких вариантов"
    )
    
    # Бесконечный цикл
    await client.run_until_disconnected()

# ========== ЗАПУСК ==========
if __name__ == "__main__":
    # Проверка конфигурации
    if not all([API_ID, API_HASH, SESSION_STRING]):
        print("❌ Заполни конфигурацию в начале файла!")
        print("1. Получи API_ID и API_HASH на https://my.telegram.org")
        print("2. Сгенерируй SESSION_STRING через скрипт")
        sys.exit(1)
    
    # Запуск
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Остановлено пользователем")
    except Exception as e:
        print(f"💀 Критическая ошибка: {e}")
