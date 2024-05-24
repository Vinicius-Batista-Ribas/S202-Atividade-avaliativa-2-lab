from teacher import TeacherCRUD
class CLI:
    def __init__(self):
        self.crud = TeacherCRUD()

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Criar Teacher")
            print("2. Pesquisar Teacher")
            print("3. Atualizar CPF do Teacher")
            print("4. Deletar Teacher")
            print("5. Sair")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.create_teacher()
            elif choice == '2':
                self.read_teacher()
            elif choice == '3':
                self.update_teacher()
            elif choice == '4':
                self.delete_teacher()
            elif choice == '5':
                break
            else:
                print("Opção inválida!")

    def create_teacher(self):
        name = input("Nome: ")
        ano_nasc = int(input("Ano de Nascimento: "))
        cpf = input("CPF: ")
        self.crud.create(name, ano_nasc, cpf)
        print("Teacher criado com sucesso!")

    def read_teacher(self):
        name = input("Nome: ")
        teacher = self.crud.read(name)
        if teacher:
            print(f"Name: {teacher['name']}, Ano de Nascimento: {teacher['ano_nasc']}, CPF: {teacher['cpf']}")
        else:
            print("Teacher não encontrado")

    def update_teacher(self):
        name = input("Nome: ")
        new_cpf = input("Novo CPF: ")
        self.crud.update(name, new_cpf)
        print("CPF atualizado com sucesso!")

    def delete_teacher(self):
        name = input("Nome: ")
        self.crud.delete(name)
        print("Teacher deletado com sucesso!")


cli = CLI()
cli.menu()        