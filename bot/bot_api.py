import requests
url_server = 'https://uzbekbazar.uz'

token = '7517285002:AAHNGRiAsweRqsKeokDjlvDFrVcmIBojtKY'
# chat_id = '-1002151522778'
url = f'https://api.telegram.org/bot{token}/'

def send_message(chat_id, text, reply_markup=None):
    data = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'html'
    }
    if reply_markup:
        data['reply_markup'] = reply_markup

    response = requests.post(url + 'sendMessage', data=data)
    return response.json()

def send_photo(chat_id, photo, caption, reply_markup=None):
    data = {
        'chat_id': chat_id,
        'photo': photo,
        'caption': caption,
        'parse_mode': 'html'
    }
    if reply_markup:
        data['reply_markup'] = reply_markup

    response = requests.post(url + 'sendPhoto', data=data)
    return response.json()

def order_product_one_click(data, chat_id):
    if not chat_id:
        return True
    order_id = data.uuid
    text = f"<b>Yangi Buyurtma</b> \n" \
           f"Telefon raqam: {data.phone_number} \n" \
           f"Mijoz ismi: {data.first_name} {data.last_name} \n" \
           f"Mahsulot: {data.product.title} \n" \
           f"Rangi: {data.color} \n" \
           f"O'lchami: {data.size} \n" \
           f"Narxi: {data.price} \n" \
           f"Savdo Turi: 1 Click \n"

    # reply_markup = {
    #     'inline_keyboard': [[
    #         {'text': "✅ Qabul qilish", 'callback_data': f"completed-{order_id}"},
    #         {'text': "❌ Qaytarish", 'callback_data': f"canceled-{order_id}"}
    #     ]]
    # }

    photo_url = url_server + data.product_image.image.url
    res = send_photo(chat_id, photo_url, text)
    # res = send_message(chat_id, text)


def order_product_variant(data, chat_id):
    if not chat_id:
        return True
    order_id = data.uuid
    text = f"<b>Yangi Buyurtma --> {data.variant.duration} oy {data.variant.name}</b> \n" \
           f"Telefon raqam: {data.user.phone} \n" \
           f"Mijoz ismi: {data.user.first_name} {data.user.last_name} \n" \
           f"Mahsulot: {data.product.title} \n" \
           f"Rangi: {data.color} \n" \
           f"O'lchami: {data.size} \n" \
           f"Narxi: {data.price} \n" \
           f"Muddat: {data.variant.duration} oy\n" \
           f"Savdo Turi: {data.variant.name} \n"

    # reply_markup = {
    #     'inline_keyboard': [[
    #         {'text': "✅ Qabul qilish", 'callback_data': f"completed-{order_id}"},
    #         {'text': "❌ Qaytarish", 'callback_data': f"canceled-{order_id}"}
    #     ]]
    # }

    photo_url = url_server + data.product_image.image.url
    send_photo(chat_id, photo_url, text)

def order_product_shop(data, order_item, chat_id):
    if not chat_id:
        return True
    order_id = data.uuid
    text = f"<b>Yangi Buyurtma</b> \n" \
           f"Telefon raqam: {data.user.phone} \n" \
           f"Mijoz ismi: {data.user.first_name} {data.user.last_name} \n" \
           f"----------------------------------------\n"

    for order in order_item:
        text += f"Mahsulot: {order['product']} \n" \
                f"Rangi: {order['product_color']} \n" \
                f"O'lchami: {order['product_size']} \n" \
                f"Narxi: {order['product_price']} \n" \
                f"Miqdori: {order['quenty']} ta \n" \
                f"Savdo Turi: Oddiy \n" \
                f"----------------------------------------\n"

    # reply_markup = {
    #     'inline_keyboard': [[
    #         {'text': "✅ Qabul qilish", 'callback_data': f"completed-{order_id}"},
    #         {'text': "❌ Qaytarish", 'callback_data': f"canceled-{order_id}"}
    #     ]]
    # }

    send_message(chat_id, text)

def order_product_info(data, chat_id):
    if not chat_id:
        return True
    order_id = data.uuid
    text = f"<b>Yangi Ogohlantiruv</b> \n" \
           f"Telefon raqam: {data.user.phone} \n" \
           f"Mijoz ismi: {data.user.first_name} {data.user.last_name} \n" \
           f"Mahsulot: {data.product.title} \n" \
           f"Rangi: {data.product_image} \n" \
           f"O'lchami: {data.product_size} \n" \
           f"<b>mahsulot kelganda foydalanuvchi xabar berishingizni xoxladi</b> \n"

    # reply_markup = {
    #     'inline_keyboard': [[
    #         {'text': "✅ Qabul qilish", 'callback_data': f"completed-{order_id}"},
    #         {'text': "❌ Qaytarish", 'callback_data': f"canceled-{order_id}"}
    #     ]]
    # }

    photo_url = url_server + data.product_image.image.url
    res = send_photo(chat_id, photo_url, text)


# # order_product_one_click 
# data = {
#     'uuid': '123',
#     'phone_number': '+998901234567',
#     'first_name': 'John',
#     'last_name': 'Doe',
#     'product': {
#         'title': 'Product title'
#     },
#     'color': 'red',
#     'size': 'XL',
#     'price': '10000',
#     'product_image': {
#         'image': {
#             'url': '/media/products/Blue_Titanium_1_mFRYhxd.jpeg'
#         }
#     }
# }
# order_product_one_click(data)