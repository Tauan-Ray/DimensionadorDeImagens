from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
from PIL import Image

# Cores
Colorfont = '#000000'
Colorbackground = '#FFFFFF'
Colorsendimg = '#59b'
Colorconvert = '#59b356'

# Criando janela
app = Tk()
app.title('Redimensiona imagens')
app.geometry('400x250')
app.config(bg=Colorbackground)

# Criando o header
header = Frame(app, width=401, height=35, relief='raised', bg=Colorbackground, borderwidth=1)
header.place(x=0, y=0)

titleHeader = Label(header, text='Picture Resizer', width=20, height=1, font=('Serif-Font 15 bold'), relief='flat', bg=Colorbackground, fg=Colorfont)
titleHeader.place(x=83, y=0)

# Função para abrir imagem
def newArchive():
    choicedImg = askopenfilename()
    img = Image.open(choicedImg)

    # Obtendo tamanho original da imagem
    imgWidth, imgHeight  = img.size

    def convert():
        # Pegando valores dos entrys
        width = int(widthEntry.get())
        height = int(heightEntry.get())

        # Mudando tamanho da imagem
        newValues = (width, height)
        newImg = img.resize(newValues)

        # Salvando imagem redimensionada
        imgSave = asksaveasfilename()
        newImg.save(imgSave + '.png')
        
        # Mensagem de sucesso
        messagebox.showinfo('Sucesso',
                            'A imagem foi salva com sucesso!!!')
        
        # Resetando a janela para outro uso
        originSize.destroy()
        newHeight.destroy()
        newWidth.destroy()
        heightEntry.destroy()
        widthEntry.destroy()
        convert_button.destroy()

    # Mostrado tamanho original e solicitando novos valores
    originSize = Label(app, text=f'Largura e altura originais {imgWidth} x {imgHeight}', width=38, height=1, anchor='center', padx=8 ,font=('Courier 13 bold'), relief='flat', bg=Colorbackground, fg=Colorfont)
    originSize.place(x=0, y=75)

    newHeight = Label(app, text='Digite a nova altura', width=20, height=1, anchor='center', font=('Courier 10 bold'), relief='flat', bg=Colorbackground, fg=Colorfont)
    newHeight.place(x=10, y=120)

    newWidth = Label(app, text='Digite a nova largura', width=21, height=1, anchor='center', font=('Courier 10 bold'), relief='flat', bg=Colorbackground, fg=Colorfont)
    newWidth.place(x=215, y=120)

    heightEntry = Entry(app, width=25, justify='center', relief='solid', borderwidth=1)
    heightEntry.place(x=15, y=145)

    widthEntry = Entry(app, width=25, justify='center', relief='solid', borderwidth=1)
    widthEntry.place(x=225, y=145)

    # Botão para converter
    convert_button = Button(app, command=convert ,text='Converter' ,width=15, height=1 ,anchor='center', font=('Arial 10'), relief='raised', overrelief='sunken', borderwidth=2, bg=Colorconvert, fg=Colorfont)
    convert_button.place(x=130, y=170)

# Botão para adicionar imagem
add_button = Button(app, command=newArchive ,text='+Novo' ,width=43, height=1, padx=3 ,anchor='center', font=('Arial 12'), relief='raised', overrelief='sunken', borderwidth=2, bg=Colorsendimg, fg=Colorfont)
add_button.place(x=0, y=35)

app.mainloop()
