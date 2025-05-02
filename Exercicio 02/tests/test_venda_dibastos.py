import sys
import os
import unittest
from unittest.mock import MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from venda_dibastos import VendaDiBastos

class TestVendaDiBastos(unittest.TestCase):
    def test_venda_produtos_confeitaria(self):
        mock_estoque = MagicMock()
        mock_pagamento = MagicMock()
        mock_entrega = MagicMock()
        mock_email = MagicMock()

        # Mock dos produtos e estoque
        mock_estoque.verificar_produto.side_effect = lambda nome: {
            'Bolo de Chocolate': {'preco': 50.0, 'quantidade': 10},
            'Torta de Limão': {'preco': 40.0, 'quantidade': 5},
            'Brigadeiro Gourmet': {'preco': 5.0, 'quantidade': 50}
        }.get(nome, None)

        mock_pagamento.processar_pagamento.return_value = True

        # Criação da instância da venda
        venda = VendaDiBastos(mock_estoque, mock_pagamento, mock_entrega, mock_email)

        # Adicionando produtos ao carrinho
        venda.adicionar_produto('Bolo de Chocolate', quantidade=1)
        venda.adicionar_produto('Brigadeiro Gourmet', quantidade=5)

        # Finalizando a venda
        venda.finalizar_venda(cliente='Maria', endereco='Rua das Flores, 123')

        # Verificações
        self.assertEqual(venda.total, 75.0)
        mock_pagamento.processar_pagamento.assert_called_once_with('Maria', 75.0)
        mock_estoque.reduzir_estoque.assert_any_call('Bolo de Chocolate', 1)
        mock_estoque.reduzir_estoque.assert_any_call('Brigadeiro Gourmet', 5)
        mock_entrega.realizar_entrega.assert_called_once_with('Maria', 'Rua das Flores, 123')
        mock_email.enviar_confirmacao.assert_called_once_with(
            'Maria',
            'Produto: Brigadeiro Gourmet; Cliente: Maria, Endereço: Rua das Flores, 123; Confirmação: Sua compra na Confeitaria Di Bastos foi finalizada! Valor total: R$75.0.'
        )

if __name__ == "__main__":
    unittest.main()

