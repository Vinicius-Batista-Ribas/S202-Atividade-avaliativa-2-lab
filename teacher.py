from db import database

class TeacherCRUD:
    def __init__(self):
        self.db = database()

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher{name:$name,ano_nasc:$ano_nasc,cpf:$cpf})"
        self.db.run_query(query, {"name": name, "ano_nasc": ano_nasc, "cpf": cpf})

    def read(self, name):
        query = "MATCH (t:Teacher{name: $name}) RETURN t.name AS name"
        return self.db.run_query(query, {"name": name})

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DELETE t"
        self.db.run_query(query, {"name": name})

    def update(self, name, novoCpf):
        query = "MATCH (t:Teacher{name: $name}) SET t.cpf = $novoCpf"
        self.db.run_query(query, {"name": name, "novoCpf": novoCpf})


crud = TeacherCRUD()


crud.create(name="Chris Lima",ano_nasc=1956, cpf='189.052.396-66')

teacher = crud.read(name="Chris Lima")

if teacher:
    print(teacher)
else:
    print("nao achei")

crud.update(name="Chris Lima", novoCpf='162.052.777-77')

