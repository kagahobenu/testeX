class Zoo():
    catalogo = list()

    def adicionar(self, animal):
        self.catalogo.append(animal)

    def imprimir(self):
        for animal in self.catalogo:
            animal.imprimir()
            print()
