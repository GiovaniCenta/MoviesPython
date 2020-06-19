class Filme:
    def __init__(self,id,nome,genero,streaming,duracao):
        self.id=id
        self.nome=nome
        self.genero=genero
        self.streaming=streaming
        self.duracao=duracao
class FilmesIMDB:
    def __init__(self,nome,genero,ano,duracao):

        self.nome=nome
        self.genero=genero
        self.ano=ano
        self.duracao=duracao