# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

payment = {
    'payment': {
        'credit_card': {
            'payment_token': '', #see credit card flow to see how to get this
            'billing_address': {
                'street': 'Av. JK',
                'number': 909,
                'neighborhood': 'Bauxita',
                'zipcode': '35400000',
                'city': 'Ouro Preto',
                'state': 'MG'
            },
            'customer': {
                'name': 'Gorbadoc Oldbuck',
                'email': 'oldbuck@efipay.com.br',
                'cpf': '04267484171',
                'birth': '1977-01-15',
                'phone_number': '5144916523'
            }
        }
    }
}

response =  efi.define_subscription_pay_method(params=params, body=payment)
print(response)
