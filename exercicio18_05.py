ontologia = '''Class: Person
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

while 'Individual' in ontologia:
        nomeperson = 'Individual:'
        posicaoinicial = ontologia.index(nomeperson) + len(nomeperson)
        nomeperson = ontologia[posicaoinicial:]
        posicaofinal = nomeperson.index('\n')
        print(nomeperson[0:posicaofinal])
        print(ontologia[posicaoinicial:posicaofinal])
        print("#"*20)
        ontologia = ontologia[posicaoinicial:]

ontologia = '''Class: Person
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
Prosposta do exercicio:
 *Mostrar as pessoas identificadas com a chave ???Individual???
 *Mostrar o coment??rio rdfs de Jeff
"""
while 'Annotations: rdfs:comment "' in ontologia:
        anotacoes= 'Annotations: rdfs:comment "'
        posiincial = ontologia.index(anotacoes) + len(anotacoes)
        anotacoes = ontologia[posiincial:]
        posifinal = anotacoes.index('"')
        print(anotacoes[0:posifinal])
        print(ontologia[posiincial:posifinal])
        print("#"*20)
        ontologia = ontologia[posiincial:]
