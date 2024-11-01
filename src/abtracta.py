from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import messagebox

# Definición de la clase abstracta Persona
class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def mostrar_info(self):
        pass

# Definición de la clase Docente
class Docente(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def mostrar_info(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Materia: {self.materia}'

# Definición de la clase Administrativa
class Administrativa(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto = puesto

    def mostrar_info(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Puesto: {self.puesto}'

# Clase principal de la interfaz gráfica
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Información de Personas")

        # Títulos de entrada
        tk.Label(root, text="Nombre").grid(row=0, column=0)
        tk.Label(root, text="Edad").grid(row=1, column=0)
        tk.Label(root, text="Materia/Puesto").grid(row=2, column=0)
        
        # Campos de entrada
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=0, column=1)
        self.edad_entry = tk.Entry(root)
        self.edad_entry.grid(row=1, column=1)
        self.especial_entry = tk.Entry(root)
        self.especial_entry.grid(row=2, column=1)
        
        # Selección de tipo de persona
        self.persona_tipo = tk.StringVar(value="Docente")
        tk.Radiobutton(root, text="Docente", variable=self.persona_tipo, value="Docente").grid(row=3, column=0)
        tk.Radiobutton(root, text="Administrativa", variable=self.persona_tipo, value="Administrativa").grid(row=3, column=1)

        # Botones
        tk.Button(root, text="Agregar", command=self.agregar_persona).grid(row=4, column=0)
        tk.Button(root, text="Mostrar Información", command=self.mostrar_info).grid(row=4, column=1)

        # Área de visualización de resultados
        self.resultado = tk.Text(root, height=10, width=50)
        self.resultado.grid(row=5, column=0, columnspan=2)

        # Lista de personas
        self.personas = []

    def agregar_persona(self):
        nombre = self.nombre_entry.get()
        edad = self.edad_entry.get()
        especial = self.especial_entry.get()

        try:
            edad = int(edad)  # Convertir edad a entero
            if self.persona_tipo.get() == "Docente":
                persona = Docente(nombre, edad, especial)
            else:
                persona = Administrativa(nombre, edad, especial)
            
            self.personas.append(persona)
            messagebox.showinfo("Éxito", "Persona agregada exitosamente")
            
            # Limpiar campos
            self.nombre_entry.delete(0, tk.END)
            self.edad_entry.delete(0, tk.END)
            self.especial_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa una edad válida.")

    def mostrar_info(self):
        self.resultado.delete("1.0", tk.END)  # Limpiar el área de resultados
        for persona in self.personas:
            self.resultado.insert(tk.END, persona.mostrar_info() + "\n")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
