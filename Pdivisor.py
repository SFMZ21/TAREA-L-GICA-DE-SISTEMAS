from tkinter import ttk
from tkinter import *

#SULMA FABIOLA MARTÍNEZ ZUÑIGA
#CARNET:0907-19-25172

#PROGRAMA QUE MUESTRA EL DIVIDENDO Y EL DIVISOR DE UNA DIVISIÓN, Y SI ESTA ES EXACTA O NO

class Desk:
    def __init__(self, window):
        # Initializations
        
        #ancho
        ancho = 800
        
        #alto
        alto = 600
        
        # asignamos la ventana a una variable de la clase llamada wind
        self.wind = window

        #le asignamos el ancho y el alto a la ventana con la propiedad geometry
        self.wind.geometry(str(ancho)+'x'+str(alto))

        #centramos el contenido 
        self.wind.columnconfigure(0, weight=1)
        
        #le damos un titulo a la ventana
        self.wind.title('Aplicación con interface gráfica')
        
        # creamos un contenedor
        frame = LabelFrame(self.wind, text = 'INGRESAR 2 VALORES')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        # creamos un etiqueta
        Label(frame, text = 'Escriba el dividendo: ').grid(row = 1, column = 0)
        
        #creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)
        
        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'Escriba el divisor: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)
        
    
        #creamos un boton para la division
        Button(frame, text= 'Dividir', command= self.dividir, background= "pink").grid(row= 6, columnspan= 2, sticky= W + E)


        #designamos un área para mensajes
        self.message = Label(text = '', fg = 'fuchsia')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        
    # creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0
    
    
    #esta es la funcion que ejecuta la division
    def dividir(self):
        if self.validation():
            cociente = int(self.var1.get()) // int(self.var2.get())
            residuo = int(self.var1.get()) % int(self.var2.get())
            
        else:
            self.message['text'] = 'Los campos son requeridos'
        
    #la division es exacta o no
   
        if int(residuo) == 0:
            self.message['text'] = 'La division es exacta. '+'Cociente: {}'.format(cociente) + ' Residuo: {}'.format(residuo)  
        
        else:
            self.message['text'] = 'La division no es exacta. '+'Cociente: {}'.format(cociente) + ' Residuo: {}'.format(residuo)  



#validamos si estamos en la aplicación inicial
if __name__ == '__main__':
    
    #asignamos la propiedad de tkinter a la variable window
    window = Tk()
    
    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = Desk(window)

    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()