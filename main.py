from codigo.modelo import Produto

ração = Produto(30, 'gato',  'ração', '20/08/2024')
ração.atualiza_deposito(30)
print(ração.descrição_do_produto())

Produto.registra_item('garrafa')


