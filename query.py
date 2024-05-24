from db import database

bd = database()

# QUESTAO 1

#A
query = "MATCH  (t:Teacher{name: 'Renzo'}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS CPF "
print(bd.run_query(query),'\n')

#B
query = "MATCH  (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS nome, t.cpf AS CPF "
print(bd.run_query(query),'\n')

#C
query = "MATCH (c:City) RETURN c.name AS name"
print(bd.run_query(query),'\n')

#D
query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS name, s.address AS address, s.number AS number"
print(bd.run_query(query),'\n')

# QUESTAO 2

#A
query = "MATCH (t:Teacher) RETURN MIN(t.ano_nasc) AS mais_velho, MAX(t.ano_nasc) AS mais_jovem"
print(bd.run_query(query),'\n')

#B
query = "MATCH (c:City) RETURN AVG(c.population) AS media_populacao "
print(bd.run_query(query),'\n')

#C
query = "MATCH (c:City{cep: '37540-000'}) RETURN REPLACE(c.name, 'a', 'A') AS nome_modificado"
print(bd.run_query(query),'\n')

#D
query7 = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1) AS caractere"
print(bd.run_query(query),'\n')

bd.close()