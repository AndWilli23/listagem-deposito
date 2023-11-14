from codigo.modelo import Produto
import pytest


class TestProduto:

    def test_quando_descricao_produto_recebe_coleira_gato_vinte(self):

        esperado = f'Preço: 20 R$ - Animal: gato - Produto: coleira - Validade: 1/1/2000 - Itens em deposito: 0'

        produto_test = Produto(20, 'gato', 'coleira', '1/1/2000')
        resultado = produto_test.descrição_do_produto()

        assert resultado == esperado

    def test_quando_validade_recebe_20_10_2021_deve_retornar_2021(self):

        entrada = '20/10/2021'
        esperado = 2021

        validade_test = Produto(20, 'gato', 'coleira', entrada)
        resultado = validade_test.ano_validade_produto()

        assert resultado == esperado

    def test_quando_validade_recebe_20_10_2021_deve_retornar_vencido(self):

        entrada  = '20/10/2021'
        esperado = 'Vencido ou perto da data de validade. Confira o produto!'

        verificacao_test = Produto(20, 'gato', 'coleira', entrada)
        resultado = verificacao_test.verifica_validade()

        assert esperado == resultado

    def test_quando_validade_recebe_20_10_2024_deve_retornar_dentro_da_validade(self):

        entrada = '20/10/2024'
        esperado = 'Produto dentro da data de validade!'

        verificacao_test = Produto(20, 'gato', 'coleira', entrada)
        resultado = verificacao_test.verifica_validade()

        assert esperado == resultado

    def test_quando_deposito_recebe_um_valor_de_100_deve_retornar_100(self):

        entrada = 100
        esperado = 100

        deposito_test = Produto(20, 'gato', 'coleira', '20/10/2020')
        resultado = deposito_test.atualiza_deposito(entrada)

        assert esperado == resultado

    def test_quando_deposito_tira_um_valor_de_100_deve_retoranr_0(self):

        entrada = 100
        esperado = 0

        deposito_test = Produto(20, 'gato', 'coleira', '20/10/2020')
        deposito_test.atualiza_deposito(100)
        resultado = deposito_test.retira_deposito(entrada)

        assert esperado == resultado

    def test_quando_deposito_tira_um_valor_de_800_deve_retornar_uma_exception(self):

        with pytest.raises(Exception):
            entrada = 800

            deposito_test = Produto(20, 'gato', 'coleira', '20/10/2020')
            resultado = deposito_test.retira_deposito(entrada)

            assert resultado

    def test_quando_recebe_o_carro_deve_retornar_que_o_carro_nao_foi_cadastrado_no_sistema(self):

        entrada = 'carro'
        esperado = 'O item carro não foi encontrado no sistema!'

        resultado = Produto.produto_em_deposito(entrada)

        assert resultado == esperado

    def test_quando_registro_o_produto_racao_deve_retornar_item_registrado(self):

        esperado = 'Item ração adicionado ao sistema com sucesso!'

        resultado= Produto.registra_item('ração')

        assert resultado == esperado












