from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento

    def idade(self):
        hoje = datetime.today()
        anos = hoje.year - self.__nascimento.year
        meses = hoje.month - self.__nascimento.month
        if hoje.day < self.__nascimento.day:
            meses -= 1
        if meses < 0:
            anos -= 1
            meses += 12
        return f"{anos} anos e {meses} meses"

    def __str__(self):
        nasc = self.__nascimento.strftime("%d/%m/%Y")
        return f"{self.__nome} - {self.__cpf} - {self.__telefone} - {nasc}"

 
    @property
    def nome(self): return self.__nome
    @nome.setter
    def nome(self, valor): self.__nome = valor

    @property
    def cpf(self): return self.__cpf
    @cpf.setter
    def cpf(self, valor): self.__cpf = valor

    @property
    def telefone(self): return self.__telefone
    @telefone.setter
    def telefone(self, valor): self.__telefone = valor

    @property
    def nascimento(self): return self.__nascimento
    @nascimento.setter
    def nascimento(self, valor): self.__nascimento = valor


def menu():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    nasc_str = input("Nascimento (dd/mm/aaaa): ")

    try:
        nasc = datetime.strptime(nasc_str, "%d/%m/%Y")
        p = Paciente(nome, cpf, telefone, nasc)
        print("\n--- Paciente ---")
        print(p)
        print("Idade:", p.idade())
    except:
        print("Data inválida.")

if __name__ == "__main__":
    menu()
