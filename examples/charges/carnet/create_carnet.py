# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

body = {
    'expire_at': '2022-12-12',
    'items': [{
        'name': 'Carnet Item 1',
        'value': 1000,
        'amount': 2
    }],
    'customer': {
        'name': 'Gorbadoc Oldbuck',
        'email': 'oldbuck@efipay.com.br',
        'cpf': '62959186036',
        'birth': '1977-01-15',
        'phone_number': '5144916523'
    },
    'repeats': 12,
    'split_items': False
}

response =  efi.create_carnet(body=body)
print(response)
