class Animal():
    nome = ''
    peso = 0

    def alimentar(self, comida):
        self.peso += comida

    def imprimir(self):
        print('Meu nome é: ', self.nome)
        print('Meu peso é: ', self.peso, 'kg')

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        if (type(novo_nome) == type(str())):
            self.nome = novo_nome
        else:
            print('Digite apenas texto.')
