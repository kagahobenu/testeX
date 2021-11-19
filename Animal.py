class Animal():
    nome = ''
    peso = 0

    def alimentar(self, comida):
        self.peso += comida

    def imprimir(self):
        print('Meu nome é: ', self.nome)
        print('Meu peso é: ', self.peso, 'kg')
