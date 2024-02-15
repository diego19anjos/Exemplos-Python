import tkinter as tk
from tkinter import messagebox
import random

NUM_LINHA = 4
NUM_COLUNHA = 4
CARTAO_SIZE_W = 10
CARTAO_SIZE_H = 5
CORES_CARTAO =['red','blue','green','yelow','purple','orange','cyan','magent']
COR_FUNDO = '#343a40'
COR_LETRA = '#ffffff'
FONTE_STYLE = ('Arial',12,'bold')
MAX_TENTATIVA = 25

def cread_card_grid():
    cores = CORES_CARTAO*2
    random.shuffle(cores)
    grid = []

    for _ in range(NUM_LINHA):
        linha = []
    for _ in range(NUM_COLUNHA):
        cor = cores.pop()
        linha.append(cor)
        grid.append(linha)
        return grid

def card_clicked(linha,coluna,):
    cartao = cartoes[linha][coluna]
    cor = cartao['bg']
    if cor == 'black':
        cartao['bg'] = grid[linha][coluna]
        cartao_revelado.append(cartao)
        if len (cartao_revelado) == 2:
            check_match()
            

def check_match():
    carta1,carta2 = cartao_revelado
    if carta1['bg'] == carta2['bg']:
        carta1.after(1000,carta1.destroy)
        carta2.after(1000,carta2.destroy)
        cartao_correspondentes.extend([carta1,carta2])
        check_win()    
    else:
        carta1.after(1000,lambda:carta1.config(bg='black'))
        carta2.after(1000,lambda:carta2.config(bg='black'))
        cartao_revelado.clear()
        update_scorre()
        



def   check_win():
    if len (cartao_correspondentes) == NUM_LINHA *  NUM_COLUNHA:
        messagebox.showinfo('PARABENS GANHOU O JOGO !')
        janela.quit()  


def update_scorre():  
    global numeros_tentativas
    numeros_tentativas +=1
    label_tentativa.config(text='tentaivas: {}/{}'.format(numeros_tentativas,MAX_TENTATIVA)) 
    if numeros_tentativas > MAX_TENTATIVA:         
        messagebox.showinfo("FIM DE JOGO",'VOCE PERDEU!')
        janela.quit()

janela = tk.Tk()
janela.title("JODO DA MEMORIA ")
janela.configure(bg=COR_FUNDO)

grid = cread_card_grid()
cartoes = {}
cartao_revelado = {}
cartao_correspondentes = {}
numeros_tentativas = 0

for linha in range(NUM_LINHA):
    linha_de_cortoes = []
    for col in range(NUM_COLUNHA):
        cartao = tk.Button(janela, command=lambda r=linha, c=col: card_clicked(r,c), width=CARTAO_SIZE_W,height=CARTAO_SIZE_H,bg='black',relief=tk.RAISED,bd=3)
        cartao.grid(row=linha,column=col,padx=5,pady=5)
        linha_de_cortoes.append(cartao)


button_style = {'activabackground':'#f8f9fa','font':FONTE_STYLE, 'fg':COR_LETRA}
janela.option_add('*button',button_style)


label_tentativa =tk.Label(janela,text='tentaivas: {}/{}'.format(numeros_tentativas,MAX_TENTATIVA),fg=COR_LETRA,bg=COR_FUNDO,font=FONTE_STYLE)
label_tentativa.grid(row=NUM_LINHA,columnspan=NUM_COLUNHA,padx=10,pady=10)

janela.mainloop()