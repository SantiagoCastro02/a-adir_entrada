import tkinter as tk
import tkinter.ttk as ttk
from tkinter import ttk
from tkinter.font import Font, BOLD
from tkinter import messagebox

class MesEntrada:
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

        # Crear la tabla
        self.treeview = ttk.Treeview(self.master, columns=('ID', 'MES'), show='headings')
        self.treeview.column("ID", width=200, anchor="center")
        self.treeview.column("MES", width=200, anchor="center")
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("MES", text="MES")
        self.treeview.pack()

        self.treeview.place(x=200, y=200, width=800, height=300)



        # Crear el botón para agregar un mes
        self.add_button = tk.Button(self.master, text='Agregar', font=('Freehando521 BT', 10, 'bold'), command=self.agregar_mes, bg='#3a7ff6', bd=0, fg='white' ,width=14, height=2)
        self.add_button.place(x=1100,y=300)

        # Crear el botón para eliminar un mes
        self.del_button = tk.Button(self.master, text='Eliminar', font=('Freehando521 BT', 10, 'bold'), command=self.eliminar_mes, bg='red', bd=0, fg='white' ,width=14, height=2)
        self.del_button.place(x=1100,y=400)

        # Contador para el ID
        self.id_counter = 1

        # Límite de filas
        self.max_filas = 12

    def agregar_mes(self):
        # Verificar si se puede agregar un nuevo mes
        if len(self.treeview.get_children()) >= self.max_filas:
            self.add_button.config(state='disabled')
            return

        # Obtener el mes siguiente
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        num_meses = len(self.treeview.get_children())
        if num_meses < len(meses):
            mes_siguiente = meses[num_meses]
        else:
            mes_siguiente = 'Mes {}'.format(num_meses+1)

        # Agregar el mes a la tabla
        self.treeview.insert('', 'end', values=(self.id_counter, mes_siguiente))

        self.id_counter += 1

        # Verificar si se alcanzó el límite de filas
        if len(self.treeview.get_children()) >= self.max_filas:
            self.add_button.config(state='disabled')

    def eliminar_mes(self):
        # Obtener la fila seleccionada
        selected_row = self.treeview.focus()

        if selected_row:
            # Obtener el ID y el mes de la fila seleccionada
            id_, mes = self.treeview.item(selected_row, 'values')

            # Añadir mensaje de precaución antes de eliminar
            respuesta = messagebox.askquestion('Eliminar fila', f'¿Está seguro que desea ELIMINAR el mes "{mes}"?')

            # Si el usuario confirma la eliminación, proceder
            if respuesta == messagebox.YES:
                # Eliminar la fila seleccionada
                self.treeview.delete(selected_row)

                # Ajustar los IDs de las filas restantes
                for i, child in enumerate(self.treeview.get_children()):
                    self.treeview.item(child, values=(i+1, self.treeview.item(child, 'values')[1]))

                # Verificar si se puede agregar un nuevo mes
                meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
                if len(self.treeview.get_children()) < len(meses):
                    self.add_button.config(state='normal')
if __name__ == "__main__":
    root = tk.Tk()
    app = MesEntrada(root)
    #root.geometry("2000x700")  # Establecer el tamaño de la ventana principal
    root.attributes('-fullscreen', True)
    root.iconbitmap("C:/Users/Usuario/Desktop/Proyecto INCO/M.I software/logoico.ico")
    root.config(bg='white')
    root.mainloop()

