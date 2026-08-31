import tkinter as tk
import webbrowser
from tkinter import Canvas
from PIL import Image, ImageTk

class InvitacionBoda:
    def __init__(self, window):
        self.window = window
        self.width = 800
        self.height = 600
        window.title("Invtacion de Boda")
        self.canvas = Canvas(self.window, width=self.width, height=self.height)
        self.canvas.pack()
        self.cargar_imagen("C:/Users/usuario/Documents/Invitacion boda maria alejandra python/fondo tarjeta.png")
        self.cargar_imagen("C:/Users/usuario/Documents/Invitacion boda maria alejandra python/foto2.jpeg")
        self.distancia_movida = 0
        self.animar_apertura()
        self.mostrar_texto()
        self.boton = tk.Button(self.window, text="Confirmar Asistencia", command=self.confirmar_asistencia)
        self.canvas.create_window(400, 450, window=self.boton)
        
        
        
        
#método de cargar imagen 
    def cargar_imagen(self, ruta):
        imagen = Image.open(ruta)
        imagen = imagen.resize((350, 350))
        mitad_izquierda = imagen.crop((0,0,175,350))
        mitad_derecha = imagen.crop((175,0,350,350))
        self.photo_izquierda = ImageTk.PhotoImage(mitad_izquierda)
        self.photo_derecha = ImageTk.PhotoImage(mitad_derecha)
        fondo = Image.open("C:/Users/usuario/Documents/Invitacion boda maria alejandra python/fondo tarjeta.png")
        
        self.photo = ImageTk.PhotoImage(imagen)
        self.fondo = ImageTk.PhotoImage(fondo)
        self.canvas.create_image(400, 300, image=self.fondo)
        self.id_izquierda = self.canvas.create_image(313, 300, image=self.photo_izquierda)
        self.id_derecha = self.canvas.create_image(487, 300, image=self.photo_derecha)
        
        
    def animar_apertura(self):
        self.canvas.move(self.id_izquierda, -5, 0) 
        self.canvas.move(self.id_derecha, 5, 0)
        self.distancia_movida += 5
        if self.distancia_movida <150:
           self.window.after(50, self.animar_apertura)
        
        else:
            self.mostrar_texto()
           
    def mostrar_texto(self):
        self.canvas.create_text(400,250,text="¡Hoy nos unimos para siempre!\nMaria Alejandra y Kevin\nQueremos que celebres con nosotros"
                                       ,font= ("Pinyon Script", 15))
        self.canvas.create_text(400, 405,text="¡Nuestra Boda!", font=("Pinyon Script", 15))
        self.canvas.create_text(400, 320,text="Lugar:hfdjsfio", font=("Pinyon Script", 15))
        self.canvas.create_text(400, 350,text="Fecha:21 de noviembre", font=("Pinyon Script", 15))
        self.canvas.create_text(400, 380,text="Hora:4 pm", font=("Pinyon Script", 15))
        
    def confirmar_asistencia(self):
        webbrowser.open("https://wa.me/573337170317?text=¡Hola👋! Confirmo mi asistencia a la boda💐")
        
window = tk.Tk()
app = InvitacionBoda(window)
window.mainloop()
        
