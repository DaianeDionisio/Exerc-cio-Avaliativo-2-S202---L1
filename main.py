from pprintpp import pprint as pp
from db.database import Graph
from db.TeacherCRUD import TeacherCrud
from helper.write_a_json import write_a_json as wj

db = Graph(uri='bolt://54.167.219.122:7687', user='neo4j', password='copies-prime-experts')

# Questão 01
# A
query = "MATCH (t:Teacher) WHERE t.name = \'Renzo\' RETURN t.ano_nasc,t.cpf"
aux = (db.execute_query(query))
wj(aux, '1A')

# B
query = "MATCH (t:Teacher) WHERE t.name =~ \'M.*\' RETURN t.name,t.cpf"
aux = (db.execute_query(query))
wj(aux, '1B')

# C
query = "MATCH (c:City) RETURN c.name"
aux = (db.execute_query(query))
wj(aux, '1C')

# D
query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name,s.address,s.number"
aux = (db.execute_query(query))
wj(aux, '1D')

# Questão 02
# A
#Professor mais jovem
query = "MATCH (t:Teacher) RETURN MAX(t.ano_nasc)"
aux = (db.execute_query(query))
#Professor mais velho
query = "MATCH (t:Teacher) RETURN MIN(t.ano_nasc)"
aux += (db.execute_query(query))
wj(aux, '2A')

# B
query = "MATCH (c:City) RETURN AVG(c.population)"
aux = (db.execute_query(query))
wj(aux, '2B')

# C
query = "MATCH (c:City) WHERE c.cep = \'37540-000\' RETURN REPLACE(c.name,\'a\',\'A\')"
aux = (db.execute_query(query))
wj(aux, '2C')

# D
query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name,2,1)"
aux = (db.execute_query(query))
wj(aux, '2D')

# Questão 03
# A
teacherCrud = TeacherCrud()

# B
teacherCrud.create('Chris Lima','1956','189.052.396-66')

# C
teacherCrud.read('Chris Lima')

# D
teacherCrud.update('Chris Lima','162.052.777-77')
