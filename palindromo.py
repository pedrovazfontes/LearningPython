texto = '''
Class: Person
Annotations: rdfs:label "Person"@en
SubClassOf: 
hasAge exactly 1 
and hasGender exactly 1 
and hasGender only {female , male}
Class: Man SubClassOf: Person
EquivalentTo: Person that hasGender value male
Class: Parent SubClassOf: Person
EquivalentTo: Person that hasChild min 1 Person
Class: Teenager
EquivalentTo: Person that hasAge some integer[>= 13 , < 20]
Class: Narcissist EquivalentTo: Person that loves Self

ObjectProperty: hasWife
Characteristics: Functional, InverseFunctional, Irreflexive, Asymmetric
Domain: Person, Man
Range: Person, Woman
SubPropertyOf: hasSpouse, loves
Individual: Jeff
Annotations: rdfs:comment "Jeff is a narcissist"
Types: hasChild exactly 2
Facts: hasWife Emily,
hasChild Ellen,
hasAge 77,
loves Jeff
Individual: Ana 
Facts: not hasAge "53"^^integer
'''

"""
Proposto do exercicio:
*Mostrar as pessoas identificadas com a chave “Individual” que são palíndromos
"""
while 'Individual' in texto:
        nomeperson = 'Individual:'
        posicaoinicial = texto.index(nomeperson) + len(nomeperson)
        nomeperson = texto[posicaoinicial:]
        posicaofinal = nomeperson.index('\n')
        print(nomeperson[0:posicaofinal])
        nomefunc = nomeperson[0:posicaofinal].lower()
        inverso = nomefunc[::-1]
        if inverso == nomefunc:
            print('Esta frase é um palíndromo')
        else:
            print('Esta frase não é um palíndromo')
        #print(texto[posicaoinicial:posicaofinal])
        print("#"*20)
        texto = texto[posicaoinicial:]