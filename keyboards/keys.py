from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup)

button_1 = KeyboardButton(text='Институт и учёба👩‍🏫')
button_10 = KeyboardButton(text='Что нужно взять для учёбы?🎒')
button_11 = KeyboardButton(text='Обучение в институте📚')
button_111 = KeyboardButton(text='Английский язык🇬🇧')
button_112 = KeyboardButton(text='Физическая культура⚽')
button_113 = KeyboardButton(text='Общая структура учёбы📝')
button_114 = KeyboardButton(text='Контроль знаний🔠')
button_12 = KeyboardButton(text='Научная деятельность🧑‍🔬')
button_121 = KeyboardButton(text='Виртуальные экскурсии по научным группам')
button_122 = KeyboardButton(text='Советы по выбору научной группы💬')
button_13 = KeyboardButton(text='Олимпиады и конкурсы🏆')
button_131 = KeyboardButton(text='Студенческие олимпиады🥇')
button_132 = KeyboardButton(text='Конференция "Менделеев"🧬')
button_133 = KeyboardButton(text='Турнир естественных наук (ТЕН)🦠')
button_14 = KeyboardButton(text='Студенческие активности в Институте⚡️')
button_141 = KeyboardButton(text='Студсовет Института химии🏳️‍🌈')
button_142 = KeyboardButton(text='Профбюро Института химии🧯')
button_143 = KeyboardButton(text='СНО Института химии🗞️')
button_15 = KeyboardButton(text='Стипендии и матпомощь👛')
button_151 = KeyboardButton(text='Основные стипендии СПбГУ💶')
button_152 = KeyboardButton(text='Стипендии от сторонних организаций💷')
button_153= KeyboardButton(text='Материальная помощь🛟')
button_16 = KeyboardButton(text='Карта института📍')
button_2 = KeyboardButton(text='Окрестности и коммуникации🏙')
button_21 = KeyboardButton(text='Другие факультеты🏚️')
button_22 = KeyboardButton(text='Магазины🛒')
button_23 = KeyboardButton(text='Кафе☕')
button_231 = KeyboardButton(text='Доставки еды🛵')
button_24 = KeyboardButton(text='Почты и службы доставки📫')
button_25 = KeyboardButton(text='Больницы и аптеки🚑')
button_251 = KeyboardButton(text='Больницы🏥')
button_252 = KeyboardButton(text='Аптеки💊')
button_26 = KeyboardButton(text='Развлечения и отдых🎡')
button_261 = KeyboardButton(text='Отдых в Петергофе⛲️')
button_262 = KeyboardButton(text='Отдых в Санкт-Петербурге🏛')
button_27 = KeyboardButton(text='Транспорт🚌')
button_271 = KeyboardButton(text='Бесконтактная смарт-карта (БСК)🚇')
button_272 = KeyboardButton(text='Карта "Подорожник"🍀')
button_273 = KeyboardButton(text='Единая карта петербуржца(ЕКП)🪪')
button_274 = KeyboardButton(text='Электросамокаты🛴')
button_3 = KeyboardButton(text='Общежития🏘')
button_31 = KeyboardButton(text='Заезд и заселение🚚')
button_311 = KeyboardButton(text='Дорога до ПУНКа🛣️')
button_312 = KeyboardButton(text='Заселение для граждан РФ🪆')
button_313 = KeyboardButton(text='Заселение для нерусских🌏')
button_32 = KeyboardButton(text='Оснащение комнат🛏')
button_33 = KeyboardButton(text='Что есть внутри кампуса?🏟')
button_34 = KeyboardButton(text='Прикрепление к больнице')
button_341 = KeyboardButton(text='Инструкция для несовершеннолетних👶🏻')
button_342 = KeyboardButton(text='Инструкция для совершеннолетних🧓🏻')
button_35 = KeyboardButton(text='Интернет в общежитиях📶')
button_351 = KeyboardButton(text='Инструкция по подключению')
button_36 = KeyboardButton(text='Общежития для городских🛋')
button_37 = KeyboardButton(text='Беседы общежитий📳')
button_4 = KeyboardButton(text='Полезные электронные ресурсы🧑‍💻')
button_41 = KeyboardButton(text='Полезные группы ВК📱')
button_5 = KeyboardButton(text='По всем вопросамℹ️')
button_6 = KeyboardButton(text='Внеучебные активности🤹‍♂️')
button_61 = KeyboardButton(text='Студенческий совет СПбГУ🐦')
button_62 = KeyboardButton(text='Студенческие отряды СПбГУ🧑‍🌾')
button_63 = KeyboardButton(text='Спортивные объединения⛹️')
button_64 = KeyboardButton(text='Кружки и клубы🪗')
button_main = KeyboardButton(text='В начало🔙')

big_button_1 = InlineKeyboardButton(
    text='1 этаж',
    callback_data='big_button_1_pressed'
)
big_button_2 = InlineKeyboardButton(
    text='2 этаж',
    callback_data='big_button_2_pressed'
)
big_button_3 = InlineKeyboardButton(
    text='3 этаж',
    callback_data='big_button_3_pressed'
)
big_button_4 = InlineKeyboardButton(
    text='4 этаж',
    callback_data='big_button_4_pressed'
)
big_button_5 = InlineKeyboardButton(
    text='Назад',
    callback_data='big_button_5_pressed'
)

keyboardcard = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],[big_button_2],[big_button_3], [big_button_4], [big_button_5]]
)



keyboard_main = ReplyKeyboardMarkup(
    keyboard=[[button_1], [button_2], [button_3], [button_6], [button_4], [button_5]],
    resize_keyboard=True
    )
keyboard_end = ReplyKeyboardMarkup(
    keyboard=[[button_main]], resize_keyboard=True
    )
keyboard_e = ReplyKeyboardMarkup(
    keyboard=[[button_main]], resize_keyboard=True
    )
keyboard1 = ReplyKeyboardMarkup(
    keyboard=[[button_10], [button_11], [button_12], [button_13], [button_14], [button_15], [button_16],[button_main]],
    resize_keyboard=True
    )
keyboard10 = ReplyKeyboardMarkup(
    keyboard=[[button_1], [button_main]], resize_keyboard=True
    )
keyboard11 = ReplyKeyboardMarkup(
    keyboard=[[button_113], [button_114],[button_111], [button_112], [button_1], [button_main]], resize_keyboard=True
    )
keyboard111 = ReplyKeyboardMarkup(
    keyboard=[[button_11], [button_main]], resize_keyboard=True
    )
keyboard12 = ReplyKeyboardMarkup(
    keyboard=[[button_122], [button_1], [button_main]], resize_keyboard=True
    )
keyboard121 = ReplyKeyboardMarkup(
    keyboard=[[button_12], [button_main]], resize_keyboard=True
    )
keyboard122 = ReplyKeyboardMarkup(
    keyboard=[[button_12], [button_main]], resize_keyboard=True
    )
keyboard13 = ReplyKeyboardMarkup(
    keyboard=[[button_131], [button_132], [button_133], [button_1], [button_main]],resize_keyboard=True
)
keyboard131 = ReplyKeyboardMarkup(
    keyboard=[[button_13], [button_main]],resize_keyboard=True
)
keyboard14 = ReplyKeyboardMarkup(
    keyboard=[[button_141], [button_142], [button_143], [button_1], [button_main]],resize_keyboard=True
)
keyboard141 = ReplyKeyboardMarkup(
    keyboard=[[button_14], [button_main]], resize_keyboard=True
)
keyboard15 = ReplyKeyboardMarkup(
    keyboard=[[button_151], [button_152], [button_153], [button_1], [button_main]], resize_keyboard=True
)
keyboard151 = ReplyKeyboardMarkup(
    keyboard=[[button_15], [button_main]], resize_keyboard=True
)
keyboard2 = ReplyKeyboardMarkup(
    keyboard=[[button_21], [button_22], [button_23], [button_24], [button_25], [button_26], [button_27], [button_main]],
    resize_keyboard=True
    )
keyboard2e = ReplyKeyboardMarkup(
    keyboard=[[button_2], [button_main]],
    resize_keyboard=True
    )
keyboard23 = ReplyKeyboardMarkup(
    keyboard=[[button_231],[button_2], [button_main]],
    resize_keyboard=True
    )
keyboard23e = ReplyKeyboardMarkup(
    keyboard=[[button_23], [button_main]],
    resize_keyboard=True
    )
keyboard25 = ReplyKeyboardMarkup(
    keyboard=[[button_251], [button_252], [button_2], [button_main]],
    resize_keyboard=True
    )
keyboard251 = ReplyKeyboardMarkup(
    keyboard=[[button_25], [button_main]],
    resize_keyboard=True
    )
keyboard26 = ReplyKeyboardMarkup(
    keyboard=[[button_261],[button_262],[button_2], [button_main]],
    resize_keyboard=True
    )
keyboard261 = ReplyKeyboardMarkup(
    keyboard=[[button_26], [button_main]],
    resize_keyboard=True
    )
keyboard27 = ReplyKeyboardMarkup(
    keyboard=[[button_271],[button_272],[button_273],[button_274],[button_2], [button_main]],
    resize_keyboard=True
    )
keyboard271 = ReplyKeyboardMarkup(
    keyboard=[[button_27], [button_main]],
    resize_keyboard=True
)
keyboard3 = ReplyKeyboardMarkup(
    keyboard=[[button_31], [button_32], [button_33], [button_34], [button_35], [button_36], [button_37], [button_3], [button_main]],
    resize_keyboard=True
    )
keyboard31 = ReplyKeyboardMarkup(
    keyboard=[[button_311], [button_312], [button_313], [button_main]],
    resize_keyboard=True
    )
keyboard311 = ReplyKeyboardMarkup(
    keyboard=[[button_31], [button_main]],
    resize_keyboard=True
    )
keyboard33 = ReplyKeyboardMarkup(
    keyboard=[[button_3], [button_main]],
    resize_keyboard=True
    )
keyboard34 = ReplyKeyboardMarkup(
    keyboard=[[button_341],[button_342],[button_main]],
    resize_keyboard=True
    )
keyboard4 = ReplyKeyboardMarkup(keyboard=[[button_41],[button_main]], resize_keyboard=True)
keyboard41 = ReplyKeyboardMarkup(keyboard=[[button_4],[button_main]], resize_keyboard=True)
keyboard6 = ReplyKeyboardMarkup(keyboard=[[button_61], [button_62], [button_63], [button_64], [button_main]], resize_keyboard=True)
keyboard61 = ReplyKeyboardMarkup(keyboard=[[button_6], [button_main]], resize_keyboard=True)
