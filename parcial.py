import tkinter as tk
from tkinter import messagebox, Menu
import random
import sys

class JuegoPiedraPapelTijera:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra, Papel o Tijera")
        self.root.geometry("600x500")
        
        # Solución definitiva para el icono en VS Code
        self.cargar_icono()
        
        # Variables para contadores
        self.victorias_usuario = tk.IntVar(value=0)
        self.victorias_maquina = tk.IntVar(value=0)
        
        # Crear menú
        self.crear_menu()
        
        # Crear interfaz
        self.crear_interfaz()
    
    def cargar_icono(self):
        # Intentar cargar el icono con múltiples métodos
        try:
            # Método 1: Ruta relativa simple
            self.root.iconbitmap("tijeras.ico")
            print("Icono cargado con ruta relativa")
            return
        except:
            pass
        
        try:
            # Método 2: Ruta absoluta usando sys
            ruta_absoluta = sys.path[0] + "/tijeras.ico"
            self.root.iconbitmap(ruta_absoluta)
            print(f"Icono cargado con ruta absoluta: {ruta_absoluta}")
            return
        except:
            pass
        
        # Si nada funciona, mostrar mensaje
        print("No se pudo cargar el icono. El programa continuará sin icono.")
    
    def crear_menu(self):
        barra_menu = Menu(self.root)
        
        menu_inicio = Menu(barra_menu, tearoff=0)
        menu_inicio.add_command(label="Salir", command=self.root.quit)
        barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
        
        menu_ayuda = Menu(barra_menu, tearoff=0)
        menu_ayuda.add_command(label="Instrucciones", command=self.mostrar_instrucciones)
        barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
        
        menu_acerca = Menu(barra_menu, tearoff=0)
        menu_acerca.add_command(label="Acerca de", command=self.mostrar_acerca_de)
        barra_menu.add_cascade(label="Acerca de", menu=menu_acerca)
        
        self.root.config(menu=barra_menu)
    
    def crear_interfaz(self):
        # Marco izquierdo
        marco_izq = tk.Frame(self.root, width=200, bg="lightgray")
        marco_izq.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tk.Label(marco_izq, text="¡Que vas a escoger?", bg="lightgray", font=("Arial", 12, "bold")).pack(pady=10)
        
        # Botones de juego
        tk.Button(marco_izq, text="Piedra", command=lambda: self.jugar("Piedra"), width=15, height=2).pack(pady=5)
        tk.Button(marco_izq, text="Papel", command=lambda: self.jugar("Papel"), width=15, height=2).pack(pady=5)
        tk.Button(marco_izq, text="Tijera", command=lambda: self.jugar("Tijera"), width=15, height=2).pack(pady=5)
        
        # Marco derecho
        marco_der = tk.Frame(self.root, width=400, bg="white")
        marco_der.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        tk.Label(marco_der, text="Resultado del Juego", bg="white", font=("Arial", 14, "bold")).pack(pady=10)
        
        self.etiqueta_resultado = tk.Label(
            marco_der, 
            text="Escoge bien cual vas a escoger", 
            bg="white", 
            justify=tk.CENTER, 
            font=("Arial", 12),
            wraplength=350
        )
        self.etiqueta_resultado.pack(pady=10)
        
        # Contadores
        marco_contadores = tk.Frame(marco_der, bg="white")
        marco_contadores.pack(pady=10)
        
        tk.Label(marco_contadores, text="Victorias del Usuario:", bg="white", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(marco_contadores, textvariable=self.victorias_usuario, bg="white", font=("Arial", 12), fg="black").grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(marco_contadores, text="Victorias de la Máquina:", bg="white", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, pady=5)
        tk.Label(marco_contadores, textvariable=self.victorias_maquina, bg="white", font=("Arial", 12), fg="black").grid(row=1, column=1, padx=5, pady=5)
        
        tk.Button(marco_der, text="Reiniciar Contadores", command=self.reiniciar_contadores, width=20, height=2).pack(pady=10)
    
    def jugar(self, eleccion_jugador):
        opciones = ["Piedra", "Papel", "Tijera"]
        eleccion_computadora = random.choice(opciones)
        
        # Determinar resultado
        if eleccion_jugador == eleccion_computadora:
            resultado = "Termino en empate"
        elif (
            (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijera") or
            (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra") or
            (eleccion_jugador == "Tijera" and eleccion_computadora == "Papel")
        ):
            resultado = "Ganaste"
            self.victorias_usuario.set(self.victorias_usuario.get() + 1)
        else:
            resultado = "Perdiste"
            self.victorias_maquina.set(self.victorias_maquina.get() + 1)
        
        self.etiqueta_resultado.config(
            text=f"Tu eleccion: {eleccion_jugador}\n\n"
                 f"Elección del programa {eleccion_computadora}\n\n"
                 f"Resultado: {resultado}"
        )
    
    def reiniciar_contadores(self):
        self.victorias_usuario.set(0)
        self.victorias_maquina.set(0)
        self.etiqueta_resultado.config(text="Contadores reiniciados correctamente :) ")
    
    def mostrar_instrucciones(self):
        messagebox.showinfo(
            "Instrucciones de Piedra, Papel o Tijera",
            "1. Haz clic en uno de los tres botones: Piedra, Papel o Tijera.\n\n"
            "2. La computadora elegirá aleatoriamente su jugada.\n\n"
            "3. El sentido del juego es utilizar algo de los objetos para vencer al otro, esta determinado asi:\n"
            "   - Piedra vence a Tijera\n"
            "   - Tijera vence a Papel\n"
            "   - Papel vence a Piedra\n\n"
            "4. Si ambos eligen lo mismo, termina quedando empate \n\n"
            "5. Puedes reiniciar el contador con el botón reinciar contadores" 
        )
    
    def mostrar_acerca_de(self):
        messagebox.showinfo(
            "Acerca de",
            "Juego de Piedra, Papel o Tijera\n\n"
            "Python 3.13\n\n"
            "Desarrollado por Joseph Alexander Morales Cardona\n\n"
            "Características:\n"
            "- Contadores de victorias\n"
            "- Botón para reiniciar contadores\n"
        )

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoPiedraPapelTijera(root)
    root.mainloop()