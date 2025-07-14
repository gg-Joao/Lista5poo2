from datetime import datetime

class Contato:
    def __init__(self, id, nome, email, telefone, nascimento):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nascimento = nascimento
    
    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome
    
    def get_email(self):
        return self.email
    
    def get_telefone(self):
        return self.telefone
    
    def get_nascimento(self):
        return self.nascimento
    
    def set_nome(self, nome):
        self.nome = nome
    
    def set_email(self, email):
        self.email = email
    
    def set_telefone(self, telefone):
        self.telefone = telefone
    
    def set_nascimento(self, nascimento):
        self.nascimento = nascimento
    
    def toString(self):
        return f"ID: {self.id} | Nome: {self.nome} | Email: {self.email} | Telefone: {self.telefone} | Nascimento: {self.nascimento.strftime('%d/%m/%Y')}"

class ContatoUI:
    def __init__(self):
        self.contatos = []
        self.proximo_id = 1
    
    def main(self):
        while True:
            opcao = self.menu()
            if opcao == '1':
                self.inserir()
            elif opcao == '2':
                self.listar()
            elif opcao == '3':
                self.atualizar()
            elif opcao == '4':
                self.excluir()
            elif opcao == '5':
                self.pesquisar()
            elif opcao == '6':
                self.aniversariantes()
            elif opcao == '7':
                break
    
    def menu(self):
        print("\n1. Inserir\n2. Listar\n3. Atualizar\n4. Excluir\n5. Pesquisar\n6. Aniversariantes\n7. Sair")
        return input("Opção: ")
    
    def inserir(self):
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        data_str = input("Data nascimento (DD/MM/AAAA): ")
        nascimento = datetime.strptime(data_str, "%d/%m/%Y")
        contato = Contato(self.proximo_id, nome, email, telefone, nascimento)
        self.contatos.append(contato)
        self.proximo_id += 1
    
    def listar(self):
        for contato in self.contatos:
            print(contato.toString())
    
    def atualizar(self):
        id_contato = int(input("ID: "))
        contato = self.buscar_por_id(id_contato)
        if contato:
            nome = input("Novo nome: ")
            if nome:
                contato.set_nome(nome)
            email = input("Novo email: ")
            if email:
                contato.set_email(email)
            telefone = input("Novo telefone: ")
            if telefone:
                contato.set_telefone(telefone)
    
    def excluir(self):
        id_contato = int(input("ID: "))
        contato = self.buscar_por_id(id_contato)
        if contato:
            self.contatos.remove(contato)
    
    def pesquisar(self):
        iniciais = input("Iniciais: ").lower()
        for contato in self.contatos:
            if contato.get_nome().lower().startswith(iniciais):
                print(contato.toString())
    
    def aniversariantes(self):
        mes = int(input("Mês: "))
        for contato in self.contatos:
            if contato.get_nascimento().month == mes:
                print(contato.toString())
    
    def buscar_por_id(self, id_contato):
        for contato in self.contatos:
            if contato.get_id() == id_contato:
                return contato
        return None

if __name__ == "__main__":
    app = ContatoUI()
    app.main()