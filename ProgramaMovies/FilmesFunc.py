def menu(lista):
    import PySimpleGUI as sg
    menu_def = [['Visualizar', ['Lista de filmes', 'Lista por genero', 'Lista por streaming', ]],
                ['Editar', ['Inserir novo filme','Remover Filme','Undo'], ],
                ['Sobre', 'Estatisticas'], ]

    op=''

    from colorama import init, Fore, Back, Style
    #chamadamenu='\033[1m'+' MENU '+'\033[0m'
    textomenu='\nOpcoes até o momento: \n(1)Ver lista de filmes\n' \
                                              '(2)Lista de filmes por streaming\n' \
                                              '(3)Lista do genero\n' \
                                              '(4)Inserir Filme\n' \
                                              '(5)Remover Filme\n' \
                                            '(6)Estatisticas \n'
    sg.theme("Reddit")

    choices = ('Lista de filmes', 'Lista por genero', 'Lista por streaming', 'Inserir novo filme', 'Remover Filme','Estatisticas')

    layout=[[sg.Menu(menu_def)],
            [sg.Text('Escolha sua opcao: ')],
             [sg.Listbox(choices, size=(20, len(choices)+2), key='-opcao-')],
             [sg.Button('Ok')]]

    print(Style.RESET_ALL)
    window = sg.Window('Filmes ! ', (layout) ,no_titlebar=False,grab_anywhere=True,alpha_channel=1,size=(640,480),margins=(200,100))
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
        op=values[0]
        op=values['-opcao-'][0]
        lista = chamafuncao(op, lista)
    window.close()




def chamafuncao(op,lista) :
    if op=='Lista de filmes':
        printatudo(lista)
    elif op=='Lista por streaming':
        buscastreaming(lista)
    elif op=='Lista por genero':
        buscagenero2(lista)
    elif op=='Inserir novo filme':
        lista=escrevearq2(lista)
    elif op=='Remover Filme':
        lista=remove(lista)
        pass
    elif op=='Estatisticas':
        graficos(lista)
        print('\n\n')
    return lista



def abrearq():
    lista=[]
    from csv import DictReader
    from FilmesB import Filme
    arq=open('C:\\Users\\Cliente\\Desktop\\Programming\\PYTHON\\projetos\\filmes\\filmes.csv','r+')
    #next(arq)
    leitor=DictReader(arq,delimiter=',')
    i=0
    for linha in leitor:
        lista.append(Filme(linha['ID'],linha['Nome'],linha['Genero'],linha['Streaming'],linha['duracao'])) #ja usa o construtor colocando cada linha do cabecalho nele
    arq.close()
    return lista

"""def escrevearq(lista):
    arq=open('C:\\Users\\Cliente\\Desktop\\Programming\\PYTHON\\projetos\\filmes\\filmes.csv','a')
    from csv import DictWriter
    ID=1
    cabecalho=['ID','Nome','Genero','Streaming','Duracao(min)']
    escritor=DictWriter(arq,fieldnames=cabecalho)
    op=''
    print('\nIncluir filme? Digite "sim" ou "nao": ')
    while op!='nao':
        op=input()
        ID=len(lista)+1
        nome=input(str(('Digite o nome do filme: ')))
        genero = input(str(('Digite o genero do filme: ')))
        streaming = input(str(('Digite o streaming em que o filme se encontra: ')))
        duracao=input((('Digite a duracao(em minutos) do filme: ')))
        escritor.writerow({'ID':ID,'Nome':nome,'Genero':genero,'Streaming':streaming,'Duracao(min)':duracao})
        op=input('Incluir filme? Digite "sim" ou "nao": ')
    arq.close()
    lista=abrearq()
    return lista
    """

def escrevearq2(lista):
    arq = open('C:\\Users\\Cliente\\Desktop\\Programming\\PYTHON\\projetos\\filmes\\filmes.csv', 'a')
    from csv import DictWriter
    import PySimpleGUI as sg
    ID = int(lista[len(lista)-1].id)
    cabecalho = ['ID', 'Nome', 'Genero', 'Streaming', 'Duracao(min)']
    escritor = DictWriter(arq, fieldnames=cabecalho)
    op = ''

    layout = [[sg.Text('Nome: '),sg.InputText()],
              [sg.Text('Genero: '), sg.InputText()],
              [sg.Text('Streaming: '), sg.InputText()],
              [sg.Text('Duracao: '), sg.InputText()],
              [sg.Cancel(), sg.Ok()]]

    window = sg.Window('Incluindo Filmes ! ', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
        ID+=1
        nome = values[0]
        genero=values[1]
        streaming=values[2]
        duracao=values[3]
        escritor.writerow({'ID': ID, 'Nome': nome, 'Genero': genero, 'Streaming': streaming, 'Duracao(min)': duracao})
        if event =='Ok':
            break

    window.close()
    arq.close()
    lista = abrearq()
    return lista



def printatudo(lista):
    import PySimpleGUI as sg
    from colorama import init,Fore,Back,Style
    from tabulate import tabulate
    init()
    table=[]
    for i in range(len(lista)):
        id=f'{lista[i].id}'
        nome=f'{lista[i].nome.title()}'
        genero=  f'{lista[i].genero.title()}'
        streaming=f'{lista[i].streaming.title()}'
        duracao=f'{lista[i].duracao.title()}'+' min'
        table.append([id,nome,genero,streaming,duracao])
        print(Style.RESET_ALL)
    print(Fore.GREEN)
    sg.Print(tabulate(table,headers=["ID","Nome do Filme","Genero","Streaming","Duracao(min)"],tablefmt="presto"))



"""def buscagenero(lista):
    from colorama import init, Fore, Back, Style
    from tabulate import tabulate
    import PySimpleGUI as sg
    gen=input(str('\n\nDigite o genero à ser buscado: '))
    chamada=Fore.RED + f'Filmes do genero {Fore.MAGENTA+gen.title()}: '
    print('\n')
    print(chamada)
    table=[]

    for i in range(len(lista)):
        if lista[i].genero.casefold()==gen.casefold():

            ID = Fore.GREEN + lista[i].id
            strnome=  Fore.WHITE + lista[i].nome.title()
            strstre = Fore.RED + lista[i].streaming.title()
            duracao = Fore.MAGENTA + f'{lista[i].duracao} min'
            table.append([ID,strnome,strstre,duracao])
    print(Fore.GREEN)
    print(tabulate(table, headers=["ID","Nome do Filme", "Streaming","Duracao"], tablefmt="presto"))
    print(Style.RESET_ALL)
"""
def buscagenero2(lista):
    import PySimpleGUI as sg
    from tabulate import tabulate
    table=[]
    layout = [[sg.Button('Acao',key='Acao'),sg.Button('Comedia',key='Comedia'),sg.Button('Suspense',key='Suspense'),sg.Button('Terror',key='Terror'),sg.Button('Drama',key='Drama')],
                        ]

    window=sg.Window('Filmes por Genero',layout)
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
        op = str(event)
        if op=='Voltar':
            break
        table=buscagenerobusca(lista,op)
        sg.Print(tabulate(table, headers=["ID", "Nome do Filme", "Streaming", "Duracao"], tablefmt="presto"))


def teste():
    import PySimpleGUI as sg

    choices = ('Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Chartreuse')

    layout = [[sg.Text('What is your favorite color?')],
              [sg.Listbox(choices, size=(15, len(choices)), key='-COLOR-')],
              [sg.Button('Ok')]]

    window = sg.Window('Pick a color', layout)

    while True:  # the event loop
        event, values = window.read()
        if event is None:
            break
        if event == 'Ok':
            if values['-COLOR-']:  # if something is highlighted in the list
                sg.popup(f"Your favorite color is {values['-COLOR-'][0]}")
    window.close()






def buscagenerobusca(lista,op):
    table = []

    for i in range(len(lista)):
        if lista[i].genero.casefold() == op.casefold():
            ID = lista[i].id
            strnome = lista[i].nome.title()
            strstre =  lista[i].streaming.title()
            duracao =  f'{lista[i].duracao} min'
            table.append([ID, strnome, strstre, duracao])

    return table






def buscastreaming(lista):
    from colorama import init, Fore, Back, Style
    from tabulate import tabulate
    import PySimpleGUI as sg


    table = []



    layout = [[sg.Button('Netflix',image_filename='NETFLIX.png',image_size=(150,150)), sg.Button('Prime Video',image_filename='PRIME.png',image_size=(150,150)),
                       sg.Button('Telecine',image_filename='TELECINE.png',image_size=(150,150)), sg.Button('Globo Play',image_filename='GLOBO.png',image_size=(150,150)),
                       sg.Button('Hbo Go',image_filename='HBO.png',image_size=(150,150)),
                      sg.Button('Outros'),
                      ]]

    window = sg.Window('Filmes por Streaming', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
        op = str(event)
        table=buscastr(op,lista)
        sg.Print(tabulate(table, headers=["ID", "Nome do Filme", "Genero", "Duracao"], tablefmt="presto"))






def buscastr(gen,lista):
    from tabulate import tabulate
    table=[]
    for i in range(len(lista)):
        if lista[i].streaming.casefold() == gen.casefold():
            id=lista[i].id
            strnome = lista[i].nome.title()
            strstre = lista[i].genero.title()
            duracao=lista[i].duracao
            table.append([id,strnome, strstre,duracao])
    return table



def remove(lista):
    """
    lista = []
    from csv import reader
    from FilmesB import Filme

    arq = open('C:\\Users\\Cliente\\Desktop\\Programming\\PYTHON\\projetos\\filmes\\filmes.csv', 'a+')
    # next(arq)
    leitor = reader(arq, delimiter=',')
    """
    import PySimpleGUI as sg
    layout=[[sg.Text('Digite o nome do filme: '),sg.InputText(),sg.Ok()]]
    window=sg.Window('Removendo',layout)
    achou=False
    while True:
        event, values = window.read()
        if event is None:
            break
        name=values[0]
        for i in lista:
            while achou==False:
                if i.nome.casefold()==name.casefold():
                    lista.remove(i)
                    achou=True
                else:
                    achou=False
            if achou==False:
                sg.popup("Filme não encontrado!")



    return lista











def abreimdb():
    from csv import DictReader
    from FilmesB import FilmesIMDB
    import pandas as pd
    #arq = open('C:\\Users\\Cliente\\Desktop\\Programming\\PYTHON\\projetos\\filmes\\data.tsv', 'r+')
    # next(arq)
    dfBasics = pd.read_csv('C:\\Users\\Cliente\\Desktop\\Programming\\PYTHON\\projetos\\filmes\\data.tsv', sep="\t", low_memory=False, chunksize=200000, iterator=True)
    i = 0
    print(list(dfBasics))
    lista2=[]
    """for linha in leitor:
        if linha['titleType']=='Movie':
            lista2.append(FilmesIMDB(linha['primaryTitle'], linha['genres'],linha['startYear'],linha['runtimeMinutes']))
                             # ja usa o construtor colocando cada linha do cabecalho nele
    arq.close()
    print(lista2)
"""




def graficos(lista):
    from colorama import Back,Fore,Style
    import PySimpleGUI as sg


    texto='Estatistica por: \n 1 - Genero \n 2 - Streaming \n 3 - Duracao'
    layout=[[sg.Text(texto)],
            [sg.InputText()],
            [sg.Ok(),sg.Cancel()]]
    window=sg.Window('Estatisticas',layout)
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
        op=values[0]
        if op == '1':
            graficogenero(lista)
        elif op == '2':
            graficostreaming(lista)
        elif op == '3':
            graficominuto(lista)
        if event == 'Ok':
            break




def graficogenero(lista):
    import matplotlib.pyplot as plt

    contdrama = 0
    contacao = 0
    contcomedia = 0
    contsuspense = 0
    contterror = 0
    for i in lista:
        if i.genero.casefold() == 'Drama'.casefold():
            contdrama += 1
        elif i.genero.casefold() == 'Acao'.casefold():
            contacao += 1
        elif i.genero.casefold() == 'Comedia'.casefold():
            contcomedia += 1
        elif i.genero.casefold() == 'Suspense'.casefold():
            contsuspense += 1
        elif i.genero.casefold() == 'Terror'.casefold():
            contterror += 1
    labels = f'Drama = {contdrama}',f'Acao = {contacao}', f'Suspense = {contsuspense}', f'Terror = {contterror}',f'Comedia = {contcomedia}'
    sizes = [contdrama, contacao, contsuspense, contterror,contcomedia]
    colors = ['red', 'yellowgreen', 'lightcoral','black', 'lightskyblue']
    patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def graficostreaming(lista):
    import matplotlib.pyplot as plt
    contnetflix = 0;
    contprime = 0;
    conttelecine = 0;
    contglobo = 0;
    conthbo = 0;
    contoutros = 0

    for i in lista:
        if i.streaming.casefold() == 'Netflix'.casefold():
            contnetflix += 1
        elif i.streaming.casefold() == 'Prime Video'.casefold():
            contprime += 1
        elif i.streaming.casefold() == 'Hbo GO'.casefold():
            conthbo += 1
        elif i.streaming.casefold() == 'Telecine'.casefold():
            conttelecine += 1
        elif i.streaming.casefold() == 'Globo Play'.casefold():
            contglobo += 1
        elif i.streaming.casefold() == 'Outros'.casefold():
            contoutros += 1

    labels = 'Netflix', 'Prime Video', 'Globo Play', 'Outros', 'Telecine','HBO GO'
    sizes = [contnetflix, contprime, contglobo, contoutros, conttelecine,conthbo]
    colors = ['red', 'lightskyblue','yellowgreen',  'black', 'lightyellow','darkblue']
    patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


def graficominuto(lista):

    import PySimpleGUI as sg
    layout=[[sg.Text('Estatistica por quanto tempo? (min) '),sg.InputText()],
            [sg.Ok(),sg.Cancel()]]
    window=sg.Window('Filtragem por tempo',layout)


    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
        min=values[0]
        printagrafmin(lista,min)
        if event == 'Ok':
            break
    window.close()




def printagrafmin(lista,min):
    import matplotlib.pyplot as plt
    contmaiorq = 0
    contmenorq = 0
    contigualq = 0
    for i in lista:
        if i.duracao > min:
            contmaiorq += 1
        elif i.duracao < min:
            contmenorq += 1
        elif i.duracao == min:
            contigualq += 1

    labels = f'Maiores que {min} min = {contmaiorq}', f'Menores que {min} min = {contmenorq}', f'Iguais a {min} min = {contigualq}'
    sizes = [contmaiorq, contmenorq, contigualq]
    colors = ['salmon', 'lightskyblue', 'yellowgreen']
    patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()



