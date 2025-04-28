import tkinter as tk
from tkinter import ttk
from tareas import SimpleTask

class TaskApp:
    def __init__(self, root, storage, manager):
        self.storage = storage
        self.manager = manager
        self.root = root
        self.root.title(" 📋 Gestor de Tareas")
        self.root.geometry("400x500")

        # ── 1) Tema base ──────────────────────────────────────────────
        self.style = ttk.Style(self.root)
        self.style.theme_use('clam')

        # ── 2) Colores personalizados ─────────────────────────────────
        bg_color   = '#2e2e2e'   # fondo general
        fg_color   = '#f0f0f0'   # texto claro
        btn_bg     = '#3a3a3a'
        entry_bg   = '#3a3a3a'
        list_bg    = '#1e1e1e'

        # Aplicar fondo al root
        self.root.configure(bg=bg_color)

        # Configurar estilos ttk
        self.style.configure('TFrame',    background=bg_color)
        self.style.configure('TLabel',    background=bg_color, foreground=fg_color)
        self.style.configure('TButton',   background=btn_bg,    foreground=fg_color)
        self.style.configure('TEntry',    fieldbackground=entry_bg, foreground=fg_color)

        # ── 3) Estructura con Frames ──────────────────────────────────
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill="both", expand=True)

        # Entrada de texto
        self.entry = ttk.Entry(main_frame)
        self.entry.pack(pady=10, fill="x")

        self.entry.bind('<Return>', self.agregar_tarea)

        # Botones
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(pady=10)

        self.add_button = ttk.Button(buttons_frame, text="➕ Agregar", command=self.agregar_tarea)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = ttk.Button(buttons_frame, text="✅ Completar", command=self.marcar_completada)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = ttk.Button(buttons_frame, text="🗑️ Eliminar", command=self.eliminar_tarea)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Lista de tareas (modo oscuro)
        self.task_listbox = tk.Listbox(
            main_frame,
            bg=list_bg,
            fg=fg_color,
            selectbackground='#555555',
            selectforeground=fg_color,
            font=("Arial", 12),
            highlightthickness=0,
            bd=0
        )
        self.task_listbox.pack(pady=10, fill="both", expand=True)

        self.refresh_view()

    def agregar_tarea(self, event=None):
        descripcion = self.entry.get()
        if descripcion:
            nueva = SimpleTask(id=len(self.manager.tasks)+1, descripcion=descripcion)
            self.manager.agregar_tarea(nueva)
            self.storage.guardar_tareas(self.manager.tasks)
            self.entry.delete(0, tk.END)
            self.refresh_view()

    def eliminar_tarea(self):
        sel = self.task_listbox.get(tk.ACTIVE)
        if sel:
            task_id = int(sel.split()[0].replace(".", ""))
            self.manager.eliminar_tarea(task_id)
            self.storage.guardar_tareas(self.manager.tasks)
            self.refresh_view()

    def marcar_completada(self):
        sel = self.task_listbox.get(tk.ACTIVE)
        if sel:
            task_id = int(sel.split()[0].replace(".", ""))
            self.manager.marcar_completada(task_id)
            self.storage.guardar_tareas(self.manager.tasks)
            self.refresh_view()

    def refresh_view(self):
        self.task_listbox.delete(0, tk.END)
        for idx, tarea in enumerate(self.manager.tasks):
            estado = "✅" if tarea.completada else "(Pendiente)"
            texto = f"{tarea.id}. {tarea.descripcion} {estado}"
            self.task_listbox.insert(tk.END, texto)
            color = 'green' if tarea.completada else 'white'
            self.task_listbox.itemconfig(idx, fg=color)
