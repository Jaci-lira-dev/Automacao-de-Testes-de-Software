# src/venda_dibastos.py

class VendaDiBastos:
    def __init__(self, estoque, pagamento, entrega, email):
        self.estoque = estoque
        self.pagamento = pagamento
        self.entrega = entrega
        self.email = email
        self.itens = []
        self.total = 0

    def adicionar_produto(self, nome_produto, quantidade=1):
        produto = self.estoque.verificar_produto(nome_produto)
        if produto and produto['quantidade'] >= quantidade:
            self.itens.append((nome_produto, quantidade, produto['preco']))
            self.total += produto['preco'] * quantidade
        else:
            raise Exception(f"Produto '{nome_produto}' indisponível ou quantidade insuficiente.")

    def finalizar_venda(self, cliente, endereco):
        if not self.itens:
            raise Exception("Nenhum produto no carrinho.")
        
        # Processando pagamento
        if self.pagamento.processar_pagamento(cliente, self.total):
            # Reduzindo estoque
            for nome_produto, quantidade, _ in self.itens:
                self.estoque.reduzir_estoque(nome_produto, quantidade)
            
            # Realizando entrega
            self.entrega.realizar_entrega(cliente, endereco)
            
            # Enviando confirmação via e-mail
            mensagem = f"Olá {cliente}, sua compra na Confeitaria Di Bastos foi finalizada! Valor total: R${self.total}."
            self.email.enviar_confirmacao(cliente, mensagem)
