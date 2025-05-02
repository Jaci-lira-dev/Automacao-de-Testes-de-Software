class VendaDiBastos:
    def __init__(self, estoque, pagamento, entrega, email):
        self.estoque = estoque
        self.pagamento = pagamento
        self.entrega = entrega
        self.email = email
        self.itens = []
        self.total = 0.0

    def adicionar_produto(self, nome_produto, quantidade):
        produto = self.estoque.verificar_produto(nome_produto)
        if produto and produto['quantidade'] >= quantidade:
            preco_total = produto['preco'] * quantidade
            self.itens.append((nome_produto, quantidade, preco_total))
            self.total += preco_total
            self.estoque.reduzir_estoque(nome_produto, quantidade)

    def finalizar_venda(self, cliente, endereco):
        if not self.itens:
            raise Exception("Nenhum produto no carrinho.")

        if self.pagamento.processar_pagamento(cliente, self.total):
            for nome_produto, quantidade, _ in self.itens:
                self.estoque.reduzir_estoque(nome_produto, quantidade)

            self.entrega.realizar_entrega(cliente, endereco)

            # Construindo a mensagem fictícia com correção para cliente e endereço como strings
            mensagem = f"Produto: {nome_produto}; Cliente: {cliente}, Endereço: {endereco}; Confirmação: Sua compra na Confeitaria Di Bastos foi finalizada! Valor total: R${self.total}."
            self.email.enviar_confirmacao(cliente, mensagem)
