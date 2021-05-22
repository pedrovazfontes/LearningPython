texto ='''
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
Proposta do Exercicio:
*Criar uma lista com todas as classes da Ontologia.
"""

listclasses = []

while 'Class' in texto:
        nameclass = 'Class:'
        posicaoinicial = texto.index(nameclass) + len(nameclass)
        nameclass = texto[posicaoinicial:]
        posicaofinal = nameclass.index('\n')
        print(nameclass[0:posicaofinal])
        listclasses.append(nameclass[0:posicaofinal])
        print(texto[posicaoinicial:posicaofinal])
        print("#"*20)
        texto = texto[posicaoinicial:]
print(listclasses)





