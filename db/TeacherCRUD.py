from db.database import Graph
from helper.write_a_json import write_a_json as wj

class TeacherCrud:

    def __init__(self):
        self.db = Graph(uri='bolt://54.167.219.122:7687', user='neo4j', password='copies-prime-experts')

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher{name: \"" + name + "\", ano_nasc: \"" + ano_nasc + "\", cpf: \"" + cpf + "\"})"
        self.db.execute_query(query)

    def read(self, name):
        query = "MATCH (t:Teacher) WHERE t.name = \'" + name + "\' RETURN t"
        aux = self.db.execute_query(query)
        wj(aux, 'Teacher ' + name)

    def delete(self, name):
        query = "MATCH (t:Teacher) WHERE t.name = \'" + name + "\' DETACH DELETE t"
        self.db.execute_query(query)

    def update(self, name, newCpf):
        query = "MATCH (t:Teacher{name: \"" + name + "\"}) SET t.cpf = \"" + newCpf + "\""
        self.db.execute_query(query)