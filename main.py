from Animal import Animal
from Zoo import Zoo

leao = Animal()
leao.nome = 'Simba'
leao.peso = 7.5
leao.alimentar(1.5)
leao.imprimir()

z = Zoo()
z.adicionar(leao)
z.imprimir()