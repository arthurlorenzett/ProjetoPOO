class PagamentoService:

    def realizar_pagamento(self, pagamento, total):

        # validações
        if pagamento.valor < total:
            raise ValueError("Pagamento não realizado. Dinheiro insuficiente!")

        print("\nProcessando pagamento...")
        print(f"Método utilizado: {pagamento.metodo}")

        # atualiza status
        pagamento.valor -= total
        pagamento.status = "pago"

        print("Pagamento concluído com sucesso!")
