from tkinter import *
# importar tudo do tkinter

janela = Tk() #instancia tkinter
janela.title('Janela') #nome para a janela

janela.geometry('600x250') #tamanho da janela

janela.config(bg='blue') #aplica cor ao fundo da tela

janela.iconphoto(False, PhotoImage(file='pin.png'))
janela.resizable(width=False, height=True)

janela.mainloop() # semopre no fim do código para chamar o método, serve para apresentar a janela Tk


