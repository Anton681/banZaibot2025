from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import (CallbackQuery, InlineKeyboardButton, InputMediaPhoto,
                           InlineKeyboardMarkup, Message, PhotoSize, InputFile, FSInputFile, URLInputFile, BufferedInputFile, LinkPreviewOptions)
from lexicon.lexicon import LEXICON_RU
from keyboards.keys import keyboard_main,keyboard_e, keyboard10, keyboardcard, keyboard_end, keyboard1, keyboard11, keyboard111, keyboard12, keyboard121,keyboard6, keyboard61, keyboard122, keyboard31, keyboard311, keyboard2, keyboard2e, keyboard23, keyboard33, keyboard34,keyboard23e, keyboard25, keyboard251, keyboard26, keyboard261, keyboard27, keyboard271, keyboard13, keyboard131, keyboard14, keyboard141, keyboard15, keyboard151, keyboard3, keyboard4, keyboard41
from contetnt.electro import resource, groups, faq
from contetnt.institute import inst_txt
from contetnt.okrest import okrest_txt
from contetnt.punk import punk_txt
from contetnt.images.image import photo_ids
from contetnt.aktiv import aktiv_txt
router = Router()

options_1 = LinkPreviewOptions(is_disabled=True)

@router.message(CommandStart())
async def process_html_command(message: Message):
    await message.answer_photo(photo=photo_ids['cat'],
                               caption='Привет!\nЭтот бот создан активистами Института химии для того, чтобы помочь вам освоиться в этом прекрасном месте.\n\n'
                         'Тут мы постарались собрать всю важную информацию, свои наблюдения, опыт и многие другие вещи, с которыми вам еще предстоит столкнуться.\n\n'
                         'Здесь вы узнаете об учёбе и досуге, о заселении и жизни в общежитии, о научной деятельности и о развитии новых навыков.\n\n'
                         'Что вас интересует?', reply_markup=keyboard_main)

@router.message(F.text == 'В начало🔙')
async def process_dog_answer(message: Message):
    await message.answer(text='Что вас интересует?', reply_markup=keyboard_main)


@router.message(F.document)
async def photo_handler(message: Message) -> None:
    await message.answer(f"ID документа {message.document.file_id}")

@router.message(F.photo)
async def document_handler(message: Message) -> None:
    photo_data = message.photo[-1]
    await message.answer(f'{photo_data}')

@router.message(F.text == 'Институт и учёба👩‍🏫')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['institute'], reply_markup=keyboard1)

@router.message(F.text == 'Обучение в институте📚')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['opisuch'], reply_markup=keyboard11)

@router.message(F.text == 'Что нужно взять для учёбы?🎒')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['brat'], reply_markup=keyboard10)

@router.message(F.text == 'Общая структура учёбы📝')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['ucheba'], reply_markup=keyboard111)

@router.message(F.text == 'Контроль знаний🔠')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['control'], reply_markup=keyboard111)

@router.message(F.text == 'Английский язык🇬🇧')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['english'], reply_markup=keyboard111, link_preview_options=options_1)

@router.message(F.text == 'Физическая культура⚽')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['fizra'], reply_markup=keyboard111, link_preview_options=options_1)

@router.message(F.text == 'Научная деятельность🧑‍🔬')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['sience'], reply_markup=keyboard12, link_preview_options=options_1)

@router.message(F.text == 'Виртуальные экскурсии по научным группам')
async def process_dog_answer(message: Message):
    await message.answer(text='будет позже!', reply_markup=keyboard121)

@router.message(F.text == 'Советы по выбору научной группы💬')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['soviet'], reply_markup=keyboard122)

@router.message(F.text == 'Олимпиады и конкурсы🏆')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['olymps_cocn'], reply_markup=keyboard13)

@router.message(F.text == 'Студенческие олимпиады🥇')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['olymp'], reply_markup=keyboard131, link_preview_options=options_1)

@router.message(F.text == 'Конференция "Менделеев"🧬')
async def process_dog_answer(message: Message):
    await message.answer_photo(photo=photo_ids['mendel'],caption=inst_txt['mendel'], reply_markup=keyboard131, link_preview_options=options_1)

@router.message(F.text == 'Турнир естественных наук (ТЕН)🦠')
async def process_dog_answer(message: Message):
    await message.answer_photo(photo=photo_ids['ten'], caption=inst_txt['ten'], reply_markup=keyboard131, link_preview_options=options_1)

@router.message(F.text == 'Студенческие активности в Институте⚡️')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['aktiv'], reply_markup=keyboard14)

@router.message(F.text == 'Студсовет Института химии🏳️‍🌈')
async def process_dog_answer(message: Message):
    await message.answer_photo(photo=photo_ids['LSS'], caption=inst_txt['SS'], reply_markup=keyboard141, link_preview_options=options_1)

@router.message(F.text == 'Профбюро Института химии🧯')
async def process_dog_answer(message: Message):
    await message.answer_photo(photo=photo_ids['PB'],
                               caption=inst_txt['PB'], reply_markup=keyboard141, link_preview_options=options_1)

@router.message(F.text == 'СНО Института химии🗞️')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['SNO'], reply_markup=keyboard141, link_preview_options=options_1)


@router.message(F.text == 'Стипендии и матпомощь👛')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['stipsobsh'], reply_markup=keyboard15)

@router.message(F.text == 'Основные стипендии СПбГУ💶')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['stips'], reply_markup=keyboard151, link_preview_options=options_1)

@router.message(F.text == 'Стипендии от сторонних организаций💷')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['stipst'], reply_markup=keyboard151, link_preview_options=options_1)

@router.message(F.text == 'Материальная помощь🛟')
async def process_dog_answer(message: Message):
    await message.answer(text=inst_txt['matpom'], reply_markup=keyboard151, link_preview_options=options_1)

@router.message(F.text == 'Окрестности и коммуникации🏙')
async def process_dog_answer(message: Message):
    await message.answer(text=okrest_txt['okrest'], reply_markup=keyboard2)

@router.message(F.text == 'Другие факультеты🏚️')
async def process_dog_answer(message: Message):
    await message.answer_photo(photo=photo_ids['facults'],
                               caption=okrest_txt['fac'], reply_markup=keyboard2e, link_preview_options=options_1)

@router.message(F.text == 'Магазины🛒')
async def process_dog_answer(message: Message):
    await message.answer_photo(photo=photo_ids['shops'], caption=okrest_txt['mag'], reply_markup=keyboard2e)

@router.message(F.text == 'Кафе☕')
async def process_dog_answer(message: Message):
    await message.answer_photo(photo=photo_ids['cafe'])
    await message.answer(text=okrest_txt['kafe'], reply_markup=keyboard23)

@router.message(F.text == 'Доставки еды🛵')
async def process_dog_answer(message: Message):
    await message.answer(text=okrest_txt['dost'], reply_markup=keyboard2e, link_preview_options=options_1)

@router.message(F.text == 'Почты и службы доставки📫')
async def process_dog_answer(message: Message):
    await message.answer(text=okrest_txt['post'], reply_markup=keyboard2e, link_preview_options=options_1)

@router.message(F.text == 'Больницы и аптеки🚑')
async def process_dog_answer(message: Message):
    await message.answer(text=okrest_txt['bol'], reply_markup=keyboard25)

@router.message(F.text == 'Больницы🏥')
async def process_dog_answer(message: Message):
    await message.answer(text=okrest_txt['boln'], reply_markup=keyboard251, link_preview_options=options_1)

@router.message(F.text == 'Аптеки💊')
async def process_dog_answer(message: Message):
    await message.answer_photo(photo=photo_ids['apt'], caption=okrest_txt['apt'], reply_markup=keyboard251, link_preview_options=options_1)

@router.message(F.text == 'Развлечения и отдых🎡')
async def process_dog_answer(message: Message):
    await message.answer_photo(photo=photo_ids['park'], caption=okrest_txt['otd'], reply_markup=keyboard26)

@router.message(F.text == 'Отдых в Петергофе⛲️')
async def process_dog_answer(message: Message):
    await message.answer(text=okrest_txt['pet'], reply_markup=keyboard261, link_preview_options=options_1)

@router.message(F.text == 'Отдых в Санкт-Петербурге🏛')
async def process_dog_answer(message: Message):
    await message.answer(text=okrest_txt['spb'], reply_markup=keyboard261, link_preview_options=options_1)

@router.message(F.text == 'Транспорт🚌')
async def process_dog_answer(message: Message):
    await message.answer(text=okrest_txt['trans'], reply_markup=keyboard27, link_preview_options=options_1)

@router.message(F.text == 'Бесконтактная смарт-карта (БСК)🚇')
async def process_dog_answer(message: Message):
    await message.answer(text=okrest_txt['bsk'], reply_markup=keyboard271, link_preview_options=options_1)

@router.message(F.text == 'Карта "Подорожник"🍀')
async def process_dog_answer(message: Message):
    await message.answer(text=okrest_txt['podor'], reply_markup=keyboard271, link_preview_options=options_1)

@router.message(F.text == 'Единая карта петербуржца(ЕКП)🪪')
async def process_dog_answer(message: Message):
    await message.answer(text=okrest_txt['ekp'], reply_markup=keyboard271, link_preview_options=options_1)

@router.message(F.text == 'Электросамокаты🛴')
async def process_dog_answer(message: Message):
    await message.answer(text=okrest_txt['samokat'], reply_markup=keyboard271, link_preview_options=options_1)

@router.message(F.text == 'Общежития🏘')
async def process_dog_answer(message: Message):
    await message.answer(text=punk_txt['punk'], reply_markup=keyboard3)

@router.message(F.text == 'Заезд и заселение🚚')
async def process_dog_answer(message: Message):
    await message.answer_photo(photo=photo_ids['durka'], caption=punk_txt['ZaZa'], reply_markup=keyboard31, link_preview_options=options_1)

@router.message(F.text == 'Дорога до ПУНКа🛣️')
async def process_dog_answer(message: Message):
    await message.answer(text=punk_txt['road'], reply_markup=keyboard311, link_preview_options=options_1)

@router.message(F.text == 'Заселение для граждан РФ🪆')
async def process_dog_answer(message: Message):
    await message.answer(text=punk_txt['russ'], reply_markup=keyboard311, link_preview_options=options_1)

@router.message(F.text == 'Заселение для иностранных граждан🌏')
async def process_dog_answer(message: Message):
    await message.answer(text=punk_txt['neruss'], reply_markup=keyboard311)

@router.message(F.text == 'Что есть внутри кампуса?🏟')
async def process_dog_answer(message: Message):
    await message.answer_photo(photo=photo_ids['campus'])
    await message.answer(text=punk_txt['terr'], reply_markup=keyboard33, link_preview_options=options_1)

@router.message(F.text == 'Оснащение комнат🛏')
async def process_dog_answer(message: Message):
    await message.answer_photo(photo=photo_ids['room'], caption=punk_txt['rooms'],reply_markup=keyboard33, link_preview_options=options_1)

@router.message(F.text == 'Интернет в общежитиях📶')
async def process_dog_answer(message: Message):
    await message.answer(text=punk_txt['intern'], reply_markup=keyboard33, link_preview_options=options_1)

@router.message(F.text == 'Общежития для городских🛋')
async def process_dog_answer(message: Message):
    await message.answer(text=punk_txt['gorod'], reply_markup=keyboard33, link_preview_options=options_1)

@router.message(F.text == 'Беседы общежитий📳')
async def process_dog_answer(message: Message):
    await message.answer(text=punk_txt['chats'], reply_markup=keyboard33, link_preview_options=options_1)

@router.message(F.text == 'Прикрепление к больнице👩‍⚕️')
async def process_dog_answer(message: Message):
    await message.answer(text=punk_txt['prik'], reply_markup=keyboard34, link_preview_options=options_1)

@router.message(F.text == 'Инструкция для несовершеннолетних👶🏻')
async def process_dog_answer(message: Message):
    await message.answer(text=punk_txt['18-'], reply_markup=keyboard33, link_preview_options=options_1)

@router.message(F.text == 'Инструкция для совершеннолетних🧓🏻')
async def process_dog_answer(message: Message):
    await message.answer(text=punk_txt['18+'], reply_markup=keyboard33, link_preview_options=options_1)

@router.message(F.text == 'Полезные электронные ресурсы')
async def process_dog_answer(message: Message):
    await message.answer(text=resource, reply_markup=keyboard4)

@router.message(F.text == 'Полезные электронные ресурсы🧑‍💻')
async def process_dog_answer(message: Message):
    await message.answer(text=resource, reply_markup=keyboard4, link_preview_options=options_1)

@router.message(F.text == 'Полезные группы ВК📱')
async def process_dog_answer(message: Message):
    await message.answer(
        text=groups,
        reply_markup=keyboard41, link_preview_options=options_1
    )

@router.message(F.text == 'По всем вопросамℹ️')
async def process_dog_answer(message: Message):
    await message.answer(text=faq, reply_markup=keyboard_e, link_preview_options=options_1)

@router.message(F.text == 'Внеучебные активности🤹‍♂️')
async def process_dog_answer(message: Message):
    await message.answer(text=aktiv_txt['opis'], reply_markup=keyboard6, link_preview_options=options_1)

@router.message(F.text == 'Студенческий совет СПбГУ🐦')
async def process_dog_answer(message: Message):
    await message.answer(text=aktiv_txt['bss'], reply_markup=keyboard61, link_preview_options=options_1)

@router.message(F.text == 'Студенческие отряды СПбГУ🧑‍🌾')
async def process_dog_answer(message: Message):
    await message.answer(text=aktiv_txt['otrads'], reply_markup=keyboard61, link_preview_options=options_1)

@router.message(F.text == 'Спортивные объединения⛹️')
async def process_dog_answer(message: Message):
    await message.answer(text=aktiv_txt['sport'], reply_markup=keyboard61, link_preview_options=options_1)

@router.message(F.text == 'Кружки и клубы🪗')
async def process_dog_answer(message: Message):
    await message.answer(text=aktiv_txt['clubs'], reply_markup=keyboard61, link_preview_options=options_1)


@router.message(F.text == 'Карта института📍')
async def process_start_command(message: Message):
    await message.answer_photo(
        photo=photo_ids['1fl'],
        caption='1 этаж',
        reply_markup=keyboardcard
    )

@router.callback_query(F.data == 'big_button_1_pressed')
async def process_button_press(callback: CallbackQuery, bot=Bot):
    await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=photo_ids['1fl'],
                caption='Этаж 1'
            ),
            reply_markup=callback.message.reply_markup
    )

@router.callback_query(F.data == 'big_button_2_pressed')
async def process_button_press(callback: CallbackQuery, bot=Bot):
    await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=photo_ids['2fl'],
                caption='Этаж 2'
            ),
            reply_markup=callback.message.reply_markup
    )

@router.callback_query(F.data == 'big_button_3_pressed')
async def process_button_press(callback: CallbackQuery, bot=Bot):
    await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=photo_ids['3fl'],
                caption='Этаж 3'
            ),
            reply_markup=callback.message.reply_markup
    )

@router.callback_query(F.data == 'big_button_4_pressed')
async def process_button_press(callback: CallbackQuery, bot=Bot):
    await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=photo_ids['4fl'],
                caption='Этаж 4'
            ),
            reply_markup=callback.message.reply_markup
    )

@router.callback_query(F.data == 'big_button_5_pressed')
async def process_button_press(callback: CallbackQuery, bot=Bot):
    await callback.message.delete(text='Что вас интересует?', reply_markup=keyboard_main)
    await callback.message.answer(
       text='Что вас интересует?', reply_markup=keyboard_main)
