from datetime import date, datetime


class Produto:

    def __init__(self, preco, animal, produto, data_validade):
        self.preco = preco
        self.animal = animal
        self.produto = produto
        self.data_validade = data_validade
        self.deposito = 0

    def __str__(self):
        return self.descrição_do_produto()

    @staticmethod
    def registra_item(produto):

        with open('produtos.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(produto + '\n')

            return f'Item {produto} adicionado ao sistema com sucesso!'

    @staticmethod
    def produto_em_deposito(produto):

        with open('produtos.txt', 'r', encoding='utf-8') as arquivo:
            for itens in arquivo:
                if produto not in itens:
                    return f'O item {produto} não foi encontrado no sistema!'
                else:
                    return f'Item {produto} está disponível no depósito!'

    def descrição_do_produto(self):
        return f'Preço: {self.preco} R$ - Animal: {self.animal} - Produto: {self.produto} - Validade: {self.data_validade} - Itens em deposito: {self.deposito}'

    def atualiza_deposito(self, valor):

        novo_deposito = self.deposito + valor
        self.deposito = novo_deposito
        return novo_deposito

    def retira_deposito(self, valor):

        if valor <= self.deposito:
            novo_deposito = self.deposito - valor
            self.deposito = novo_deposito
            return novo_deposito
        else:
            raise ValueError(f'Deposito não possui a quantidade necessária! Quantidade em deposito {self.deposito}')

    def ano_validade_produto(self):

        data_validade_quebrada = self.data_validade.split('/')
        ano_validade = data_validade_quebrada[-1]

        return int(ano_validade)

    def verifica_validade(self):

        ano_atual = date.today().year

        if self.ano_validade_produto() <= ano_atual:
            return 'Vencido ou perto da data de validade. Confira o produto!'

        elif self.ano_validade_produto() > ano_atual:
            return 'Produto dentro da data de validade!'


