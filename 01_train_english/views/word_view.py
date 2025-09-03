import tkinter as tk
from tkinter import messagebox

class WordView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # Título de la app
        self.root.title("PRACTICA INGLÉS")

        # --- Centrar la ventana ---
        window_width = 600
        window_height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        # ---------------------------

        # Frame / Ventana principal para menú
        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack(expand=True)

        # Etiqueta para elegir la opción
        label = tk.Label(self.menu_frame, text="Elige una opción", font=("Arial", 25, "bold"))
        label.pack(pady=5)

        # Lista de opciones
        self.menu_list = tk.Listbox(self.menu_frame, height=6, font=("Arial", 14), width=30)
        self.menu_list.insert(1, "Practicar un topic")
        self.menu_list.insert(2, "Ver topics disponibles")
        self.menu_list.insert(3, "Añadir un nuevo topic")
        self.menu_list.insert(4, "Salir")
        self.menu_list.pack(pady=10)
        
        # Bind para doble clic
        self.menu_list.bind("<Double-1>", self.on_double_click)

        # Frame para mostrar topics
        self.topics_frame = tk.Frame(root)

    def on_double_click(self, event):
        selection = self.menu_list.curselection()
        if not selection:
            messagebox.showwarning("Atención", "Debes seleccionar una opción.")
            return

        option = selection[0] + 1  # índice + 1
        match option:
            case 1:
                self.controller.start_practice()
            case 2:
                self.show_topics_screen()
            case 3:
                self.controller.add_word_menu()
            case 4:
                self.root.quit()

    # ------------------ Pantalla topics ------------------
    def show_topics_screen(self):
        # Ocultar menú
        self.menu_frame.pack_forget()

        # Limpiar topics_frame
        for w in self.topics_frame.winfo_children():
            w.destroy()
        self.topics_frame.pack(expand=True)

        # Obtener topics del controller
        topics = self.controller.get_topics()

        if not topics:
            messagebox.showwarning("Atención", "No hay topics aún!")
        else:
            label = tk.Label(self.topics_frame, text="Topics disponibles:", font=("Arial", 20, "bold"))
            label.pack(pady=10)
            for t in topics:
                lbl = tk.Label(self.topics_frame, text=f"- {t}", font=("Arial", 16), anchor="w")
                lbl.pack(pady=2)

        # Botón volver
        btn_volver = tk.Button(self.topics_frame, text="Volver", font=("Arial", 14), command=self.back_to_menu)
        btn_volver.pack(pady=20)

    def back_to_menu(self):
        # Ocultar topics
        self.topics_frame.pack_forget()
        # Mostrar menú
        self.menu_frame.pack(expand=True)