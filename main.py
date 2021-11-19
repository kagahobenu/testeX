from Animal import Animal
from Zoo import Zoo

leao = Animal()
leao.nome = 'Simba'
leao.peso = 7.5
leao.alimentar(1.5)
leao.set_nome('Mufasa')
leao.get_nome()

zebra = Animal()
zebra.nome = "Valentina"
zebra.peso = 85

foca = Animal()
foca.nome = "Pepita"
foca.peso = 115

z = Zoo()
z.adicionar(leao)
z.adicionar(zebra)
z.adicionar(foca)
z.imprimir()
