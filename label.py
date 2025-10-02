from tkinter import *

janela = Tk() #instancia tkinter

janela.title('Label') #titulo
janela.geometry('250x250') #tamanho da tela

label_nome = Label(janela, width=10, height=2, text='Nome : ', font=('Arial 10'), fg='Blue', bg='Yellow') #posição na janela
# label_nome.grid(row=0, column=0, pady=5) posicionamento no container
# label_nome.place(x=10, y=10) posicionamento no container
# label_nome.pack(side=LEFT) 
label_nome.grid(row=0, column=0)


nome = Label(janela, width=10, height=2, text='Gabriel Silva', font=('Arial 10'), fg='Blue', bg='Yellow') #posição na janela
nome.grid(row=0, column=1)


label_idade = Label(janela, width=10, height=2, text='Idade : ', font=('Arial 10 bold'), fg='Green', bg='Black') #posição na janela
label_idade.grid(row=1, column=0)



idade = Label(janela, width=10, height=2, text='27', font=('Arial 10 bold'), fg='Green', bg='Black') #posição na janela
idade.grid(row=1, column=1)



label_pais = Label(janela, width=10, height=2, text='País : ',  font=('Arial 10'), fg='Black', bg='Blue') #posição na janela
label_pais.grid(row=2, column=0)



pais = Label(janela, width=10, height=2, text='Brasil',  font=('Arial 10'), fg='Black', bg='Blue') #posição na janela
pais.grid(row=2, column=1)




janela.mainloop()
