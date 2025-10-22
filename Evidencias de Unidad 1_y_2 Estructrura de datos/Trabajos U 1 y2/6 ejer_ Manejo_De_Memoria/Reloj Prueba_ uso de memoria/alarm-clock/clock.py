import tkinter as tk
from tkinter.font import Font
from time import strftime, localtime
import time
import tracemalloc

tracemalloc.start()  # iniciar seguimiento de memoria

class Clock(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.start_time = time.time()   # momento inicial para medir tiempo de ejecución

        # Etiquetas del reloj
        self.time_label = tk.Label(self, font=Font(family='Helvetica', size=36, weight='bold'))
        self.date_label = tk.Label(self, font=Font(family='Helvetica', size=27, weight='bold'))
        self.elapsed_label = tk.Label(self, font=Font(family='Helvetica', size=14))
        self.mem_label = tk.Label(self, font=Font(family='Helvetica', size=14))

        self.time_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.date_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.elapsed_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1, pady=(6,0))
        self.mem_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Empieza la actualización periódica usando after (seguro para la GUI)
        self.update_clock()

    def format_seconds(self, secs):
        # devuelve hh:mm:ss desde segundos
        h = int(secs // 3600)
        m = int((secs % 3600) // 60)
        s = int(secs % 60)
        return f"{h:02d}:{m:02d}:{s:02d}"

    def update_clock(self):
        # hora y fecha
        now_time = strftime("%I:%M:%S %p", localtime())
        now_date = strftime("%a, %b, %d", localtime())
        self.time_label["text"] = now_time
        self.date_label["text"] = now_date

        # tiempo transcurrido
        elapsed = time.time() - self.start_time
        self.elapsed_label["text"] = "Tiempo transcurrido: " + self.format_seconds(elapsed)

        # memoria (tracemalloc)
        memoria_actual, memoria_max = tracemalloc.get_traced_memory()
        # convertir a KB y MB (ejemplos)
        memoria_actual_kb = memoria_actual / 1024
        memoria_max_kb = memoria_max / 1024
        memoria_actual_mb = memoria_actual / (1024**2)
        memoria_max_mb = memoria_max / (1024**2)

        self.mem_label["text"] = (
            f"Memoria actual: {memoria_actual_kb:.1f} KB ({memoria_actual_mb:.3f} MB) — "
            f"Memoria máxima: {memoria_max_kb:.1f} KB ({memoria_max_mb:.3f} MB)"
        )

        # volver a llamar en 1000 ms (1 segundo)
        self.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Clock con tiempo y memoria")
    root.geometry("700x220")
    root.minsize(480, 180)

    clock = Clock(root)
    clock.pack(fill=tk.BOTH, expand=1)

    # manejar cierre: detener tracemalloc y cerrar ventana
    def on_close():
        memoria_actual, memoria_max = tracemalloc.get_traced_memory()
        print("\nEstadísticas finales (imprimidas en consola):")
        print(f"Memoria actual usada: {memoria_actual / 1024:.1f} KB ({memoria_actual / (1024**2):.3f} MB)")
        print(f"Memoria máxima usada: {memoria_max / 1024:.1f} KB ({memoria_max / (1024**2):.3f} MB)")
        print(f"Tiempo total de ejecución: {time.time() - clock.start_time:.3f} segundos\n")
        tracemalloc.stop()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
