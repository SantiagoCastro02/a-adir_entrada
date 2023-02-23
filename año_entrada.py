import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font, BOLD
from tkinter import messagebox


class AnoEntrada:
    def __init__(self, master):
        self.master = master
        self.master.title("Maderas Industriales")

        # TITULOS
        self.frame_top = tk.Frame(self.master, bg='#135D9B')
        self.frame_top.pack(side='top', fill='x')

        self.titulo = tk.Label(self.frame_top, text='MADERAS INDUSTRIALES SOFTWARE', bg='#135D9B', fg='white', font=Font(family='Freehand521 BT', size=15, slant='italic', weight='bold'))
        self.titulo.pack(expand=1)

        self.bienvenido_label = tk.Label(self.master, text="INGRESO DE MADERA", font=('Freehand521 BT', 22, 'bold'), bg='white', fg='black', width='20', height='2')
        self.bienvenido_label.place(x=500, y=70)

        # Crear un widget Treeview
        self.tree = ttk.Treeview(self.master, columns=("ID", "AÑO"), show="headings")
        self.tree.column("ID", width=400, anchor="center")
        self.tree.column("AÑO", width=400, anchor="center")
        self.tree.heading("ID", text="ID")
        self.tree.heading("AÑO", text="AÑO")
        
        
        # Agregar algunos datos de ejemplo
        for i in range(1):
            self.tree.insert("", tk.END, values=(i, 2023+i))

        # Configurar el tamaño del Treeview
        tree_width = 800
        tree_height = 300
        self.tree.place(x=200, y=200, width=tree_width, height=tree_height)

        # Agregar un widget Scrollbar
        self.scrollbar = ttk.Scrollbar(self.master, orient="vertical", command=self.tree.yview)
        self.scrollbar.place(x=200+tree_width, y=200, height=tree_height)

        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
        # Agregar un botón para agregar un nuevo año

        self.boton_ver = tk.Button(self.master, text="Ver Año", font=('Freehand521 BT', 10, 'bold'), command=self.ver_meses, bg='green', bd=0, fg='white' ,width=14, height=2)
        self.boton_ver.place(x=1100,y=200)

        self.boton_agregar = tk.Button(self.master, text="Agregar Año", font=('Freehand521 BT', 10, 'bold'), command=self.agregar_anio, bg='#3a7ff6', bd=0, fg='white' ,width=14, height=2)
        self.boton_agregar.place(x=1100,y=300)
        
        # Agregar un botón para eliminar una fila
        self.boton_eliminar = tk.Button(self.master, text="Eliminar Año", font=('Freehand521 BT', 10, 'bold'), command=self.eliminar_anio, bg='red', bd=0, fg='white' ,width=14, height=2)
        self.boton_eliminar.place(x=1100,y=400)
        

    def agregar_anio(self):
        # Obtener el número de años actuales
        n_anios = len(self.tree.get_children())
        
        # Agregar un nuevo año
        self.tree.insert("", tk.END, values=(n_anios, 2023+n_anios))

    def eliminar_anio(self):
        # Obtener el item seleccionado
        seleccion = self.tree.selection()
        if len(seleccion) == 0:
            # No se ha seleccionado ningún item
            messagebox.showinfo("Eliminar Año", "Selecciona un año para Eliminar.")
        else:
            # Se ha seleccionado un item
            respuesta = messagebox.showwarning("Eliminar Año", "¿Está seguro de que desea ELIMINAR el año seleccionado?")
            if respuesta:
                # Confirmar la eliminación del item
                self.tree.delete(seleccion[0])

    def ver_meses(self):
        # Obtener el item seleccionado en el Treeview
        seleccion = self.tree.selection()
        
        if seleccion:
            # Obtener el valor del año seleccionado
            valor = self.tree.item(seleccion[0])['values'][1]
            self.master.destroy()
            exec(open("C:\\Users\\Usuario\\Desktop\\Proyecto INCO\\M.I software\\modulos\\entrada\\mes_entrada.py").read())

            
        else:
            tk.messagebox.showwarning("No seleccionado", "Debe seleccionar un año primero")
                
if __name__ == "__main__":
    root = tk.Tk()
    app = AnoEntrada(root)
    #root.geometry("2000x700")  # Establecer el tamaño de la ventana principal
    root.attributes('-fullscreen', True)
    root.iconbitmap("C:/Users/Usuario/Desktop/Proyecto INCO/M.I software/logoico.ico")
    root.config(bg='white')
    root.mainloop()