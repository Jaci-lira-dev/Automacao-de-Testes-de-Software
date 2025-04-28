# tests/test_venda_dibastos.py

import sys
import os
import unittest
from unittest.mock import MagicMock

# Adiciona o caminho do diretório src para poder importar a classe VendaDiBastos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from venda_dibastos import VendaDiBastos

class TestVendaDiBastos(unittest.TestCase):
    def test_venda_produtos_confeitaria(self):
        mock_estoque = MagicMock()
        mock_pagamento = MagicMock()
        mock_entrega = MagicMock()
        mock_email = MagicMock()

        # Definindo o comportamento simulado para o estoque
        mock_estoque.verificar_produto.side_effect = lambda nome: {
            'Bolo de Chocolate': {'preco': 50.0, 'quantidade': 10},
            'Torta de Limão': {'preco': 40.0, 'quantidade': 5},
            'Brigadeiro Gourmet': {'preco': 5.0, 'quantidade': 50}
        }.get(nome, None)

        # Simulando o processamento de pagamento
        mock_pagamento.processar_pagamento.return_value = True

        # Criando a instância de VendaDiBastos com mocks
        venda = VendaDiBastos(mock_estoque, mock_pagamento, mock_entrega, mock_email)

        # Adicionando produtos ao carrinho
        venda.adicionar_produto('Bolo de Chocolate', quantidade=1)
        venda.adicionar_produto('Brigadeiro Gourmet', quantidade=5)

        # Finalizando a venda
        venda.finalizar_venda(cliente='Maria', endereco='Rua das Flores, 123')

        # Verificando o total da venda
        self.assertEqual(venda.total, 75.0)

        # Verificando se os métodos foram chamados corretamente
        mock_pagamento.processar_pagamento.assert_called_once_with('Maria', 75.0)
        mock_estoque.reduzir_estoque.assert_any_call('Bolo de Chocolate', 1)
        mock_estoque.reduzir_estoque.assert_any_call('Brigadeiro Gourmet', 5)
        mock_entrega.realizar_entrega.assert_called_once_with('Maria', 'Rua das Flores, 123')

        # Verificando se o e-mail de confirmação foi enviado corretamente
        mock_email.enviar_confirmacao.assert_called_once_with(
            'Maria',
            'Olá Maria, sua compra na Confeitaria Di Bastos foi finalizada! Valor total: R$75.0.'
        )

if __name__ == "__main__":
    unittest.main()
