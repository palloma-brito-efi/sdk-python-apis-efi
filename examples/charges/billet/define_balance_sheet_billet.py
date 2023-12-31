# encoding: utf-8

from efipay import EfiPay
from ...credentials import credentials

efi = EfiPay(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
    'title': 'Balancete Demonstrativo',
    'body': [
        {
            'header': 'Demonstrativo de Consumo',
            'tables': [
                {
                    'rows': [
                        [
                            {
                                'align': 'left',
                                'color': '#000000',
                                'style': 'bold',
                                'text': 'Exemplo de despesa',
                                'colspan': 2
                            },
                            {
                                'align': 'left',
                                'color': '#000000',
                                'style': 'bold',
                                'text': 'Total lançado',
                                'colspan': 2
                            }
                        ],
                        [
                            {
                                'align': 'left',
                                'color': '#000000',
                                'style': 'normal',
                                'text': 'Instalação',
                                'colspan': 2
                            },
                            {
                                'align': 'left',
                                'color': '#000000',
                                'style': 'normal',
                                'text': 'R$ 100,00',
                                'colspan': 2
                            }
                        ]
                    ]
                }
            ]
        },
        {
            'header': 'Balancete Geral',
            'tables': [
                {
                    'rows': [
                        [
                            {
                                'align': 'left',
                                'color': '#000000',
                                'style': 'normal',
                                'text': 'Confira na documentação da Gerencianet todas as configurações possíveis.',
                                'colspan': 4
                            }
                        ]
                    ]
                }
            ]
        }
    ]
}

response = efi.define_balance_sheet_billet(params=params, body=body)
print(response)
