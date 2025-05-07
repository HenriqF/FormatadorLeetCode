import tkinter as tk
#criar a porra toda
#########################################
janela = tk.Tk()
janela.geometry('1250x950')
janela.title("Analisador de estermificações para desmistrificar e até almejar o código para modelar à leetcode")

printchange = tk.BooleanVar()
printchange.set(True)
tabular = tk.BooleanVar()
tabular.set(True)


#Código que roda quando eu quero
#########################################
def analise(code):
    out = ""
    if tabular.get():
        code = code.splitlines()
        naovazias = []
        for line in code:
            if line.strip():
                naovazias.append(line)
        code = '\n'.join(naovazias)
    code = code + "       "
    
    count = 0
    i = 0
    while i < len(code):
        try:
            if code[i:i+1] == "\n" and tabular.get():
                out = out+"\n        "
                i+=1
            if code[i:i+6] == "print(" and printchange.get():
                out = out+"return("
                i += 5
            else:
                out = out+code[i]   
        except:
            out = out+code[i]
        i += 1

    return(out)




#funcoes tkinter
#########################################
def enviar():
    user_text = input.get("1.0", tk.END).strip()
    result = analise(user_text)
    output.config(state=tk.NORMAL)
    output.delete("1.0", tk.END)
    output.insert(tk.END, str(result))
    janela.clipboard_clear()
    janela.clipboard_append(result)
    janela.update()

def atualizar(*args):
    enviar()

#Detalhes, textos
#########################################
textoinput = tk.Label(janela, text="Coloca a porra do codigo aqui:")
textoinput.grid(row=0, column=1, padx=10, pady=10)
textoinput2 = tk.Label(janela, text="Outs:")
textoinput2.grid(row=0, column=2, padx=10, pady=10)

#Botoes
#########################################
botao = tk.Button(janela, text="Analisar e Estermificar código", command=atualizar, width=80, height=2)
botao.grid(row=2, column=1, padx=10, pady=10)
c1 = tk.Checkbutton(janela, text="Mudar print pra return", variable=printchange, onvalue=True, offvalue=False, command=atualizar)
c1.grid(row=2, column=2, padx=10, pady=0)
c2 = tk.Checkbutton(janela, text="Tabular para leetcode", variable=tabular, onvalue=True, offvalue=False, command=atualizar)
c2.grid(row=3, column=2, padx=10, pady=0)

#Caixas de input, output
#########################################
output = tk.Text(janela, height=50, width=75, state=tk.DISABLED)
output.grid(row=1, column=2, padx=10, pady=10)

input = tk.Text(janela, height=50, width=75)
input.grid(row=1, column=1, padx=10, pady=10)
input.bind("<Return>", atualizar)


#necessario
#########################################
janela.mainloop()