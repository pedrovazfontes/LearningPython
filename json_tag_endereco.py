"""
Proposta do exercicio:
No XML, mostrar o texto que está entre dentro da tag: “TAG” Endereco

"""



json = '''
{
  "id":1,
  "nome":"Alexandre gama",
  "endereco":"R. Qualquer"
}
'''


for i in range (len(json)):
  if json[i: i+10] == '"endereco"':
    i = i + 12
    print(json[i: i+11])

