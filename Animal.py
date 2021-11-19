class Animal():
    nome = ''
    peso = 0

    def __init__(self, nome, peso):

        self.__nome = nome
        self.__peso = peso

    def __str__(self):
        return f'Nome: {self.nome}\nPeso: {self.peso:.2f}'

    def alimentar(self, comida):
        self.peso += comida

    def imprimir(self):
        print('Meu nome é: ', self.nome)
        print('Meu peso é: ', self.peso, 'kg')

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if (type(novo_nome) == type(str())):
            self.__nome = novo_nome
        else:
            print('Digite apenas texto.')
