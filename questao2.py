from enum import Enum
from datetime import datetime

class Pagamento(Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 3

class Boleto:
    def __init__(self, cod, emissao, venc, valor):
        self.codBarras = cod
        self.dateEmissao = emissao
        self.dateVencimento = venc
        self.valorBoleto = valor
        self.valorPago = 0
        self.dataPago = None
        self.situacaoPagamento = Pagamento.EmAberto

    def Pagar(self, valor):
        self.valorPago = valor
        self.dataPago = datetime.now()
        if self.valorPago == 0:
            self.situacaoPagamento = Pagamento.EmAberto
        elif self.valorPago < self.valorBoleto:
            self.situacaoPagamento = Pagamento.PagoParcial
        else:
            self.situacaoPagamento = Pagamento.Pago

    def ToString(self):
        texto = "Código: " + self.codBarras + "\n"
        texto += "Emissão: " + self.dateEmissao.strftime('%d/%m/%Y') + "\n"
        texto += "Venc: " + self.dateVencimento.strftime('%d/%m/%Y') + "\n"
        texto += "Valor: R$" + f"{self.valorBoleto:.2f}" + "\n"
        texto += "Pago: R$" + f"{self.valorPago:.2f}" + "\n"
        texto += "Situação: " + self.situacaoPagamento.name
        return texto


cod = input("Código de barras: ")
emissao = datetime.strptime(input("Data emissão (dd/mm/yyyy): "), "%d/%m/%Y")
venc = datetime.strptime(input("Data vencimento (dd/mm/yyyy): "), "%d/%m/%Y")
valor = float(input("Valor do boleto: "))

boleto = Boleto(cod, emissao, venc, valor)
print("\n" + boleto.ToString())

valorPago = float(input("\nValor a pagar: "))
boleto.Pagar(valorPago)
print("\n" + boleto.ToString())
