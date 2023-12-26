from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

token = '6786050219:AAGAqVw26jBafZtU7HDzltCp4aW4kJA0ZIc'
url = 'http://127.0.0.1:8000/'
url_server = 'https://test.azbo.uz'
bot = Bot(token=token)

# dp = Dispatcher(bot)

chat = '-4021014751'


async def order_product_one_clik(data):
    order_id = data.uuid
    categoryMenu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Qabul qilish", callback_data=f"completed-{order_id}"),
                InlineKeyboardButton(text="❌ Qaytarish", callback_data=f"canceled-{order_id}"),
            ],
        ])

    text = f"<b>Yangi Buyurtma</b> \n" \
           f"Telefon raqam: {data.phone_number} \n" \
           f"Mijoz ismi: {data.first_name} {data.last_name} \n" \
            f"Mahsulot: {data.product.title} \n" \
            f"Rangi: {data.color} \n" \
            f"O'lchami: {data.size} \n" \
            f"Narxi: {data.price} \n" \
            f"Savdo Turi: 1 Click \n" \


    photo_url = url_server + data.product_image.image.url
    
    
    await bot.send_photo(chat_id=chat, photo="https://azbo.uz/media/products/Blue_Titanium_1_mFRYhxd.jpeg",  caption=text, reply_markup=categoryMenu, parse_mode='html')
 
async def order_product_variant(data):
    order_id = data.uuid 
    categoryMenu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Qabul qilish", callback_data=f"completed-{order_id}"),
                InlineKeyboardButton(text="❌ Qaytarish", callback_data=f"canceled-{order_id}"),
            ],
        ])
    text = f"<b>Yangi Buyurtma --> {data.variant.duration} oy {data.variant.name}</b> \n" \
           f"Telefon raqam: {data.user.phone} \n" \
           f"Mijoz ismi: {data.user.first_name} {data.user.last_name} \n" \
            f"Mahsulot: {data.product.title} \n" \
            f"Rangi: {data.color} \n" \
            f"O'lchami: {data.size} \n" \
            f"Narxi: {data.price} \n" \
            f"Muddat: {data.variant.duration} oy\n" \
            f"Savdo Turi: {data.variant.name} \n" \
    
    photo_url =url_server + data.product_image.image.url
    
    
    await bot.send_photo(chat_id=chat, photo="https://azbo.uz/media/products/Blue_Titanium_1_mFRYhxd.jpeg",  caption=text, reply_markup=categoryMenu, parse_mode='html')
    
    
async def order_product_shop(data, order_item):
    order_id = data.uuid 
    media = []
    categoryMenu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Qabul qilish", callback_data=f"completed-{order_id}"),
                InlineKeyboardButton(text="❌ Qaytarish", callback_data=f"canceled-{order_id}"),
            ],
        ])
    text = f"<b>Yangi Buyurtma</b> \n" \
           f"Telefon raqam: {data.user.phone} \n" \
           f"Mijoz ismi: {data.user.first_name} {data.user.last_name} \n" \
           f"----------------------------------------\n" \
    
    for order in order_item:
        #photo_url = url_server + data.product_image.image.url
       # media.append(types.InputMediaPhoto(media=photo_url))
        text += f"Mahsulot: {order['product']} \n" \
                f"Rangi: {order['product_color']} \n" \
                f"O'lchami: {order['product_size']} \n" \
                f"Narxi: {order['product_price']} \n" \
                f"Miqdori: {order['quenty']} ta \n" \
                f"Savdo Turi: Oddiy \n" \
                f"----------------------------------------\n" \
                    
         
    
    #await bot.send_media_group(chat_id=chat, media=media)
    await bot.send_message(chat_id=chat, text=text, reply_markup=categoryMenu, parse_mode='html')
    
    
async def order_product_info(data):
    order_id = data.uuid 
    categoryMenu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Qabul qilish", callback_data=f"completed-{order_id}"),
                InlineKeyboardButton(text="❌ Qaytarish", callback_data=f"canceled-{order_id}"),
            ],
        ])
    text = f"<b>Yangi Ogohlantiruv</b> \n" \
           f"Telefon raqam: {data.user.phone} \n" \
           f"Mijoz ismi: {data.user.first_name} {data.user.last_name} \n" \
            f"Mahsulot: {data.product.title} \n" \
            f"Rangi: {data.color} \n" \
            f"O'lchami: {data.size} \n" \
            f"<b>mahsulot kelganda foydalanuvchi xabar berishingizni xoxladi</b> \n" \
                
    photo_url = url_server + data.product_image.image.url
    
    
    await bot.send_photo(chat_id=chat, photo="https://azbo.uz/media/products/Blue_Titanium_1_mFRYhxd.jpeg",  caption=text, reply_markup=categoryMenu, parse_mode='html')
