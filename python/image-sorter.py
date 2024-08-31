import os
import shutil
from tkinter import Tk, Label, Button, filedialog, StringVar, OptionMenu
from tkinter import ttk  # Importe ttk pour le style moderne

class ImageSorterApp:
    def __init__(self, master):
        self.master = master
        master.title("Classificateur d'Images")

        # Configuration du style moderne avec ttk
        style = ttk.Style()
        style.theme_use('clam')  # Choisis un thème moderne (par exemple, 'clam')
        style.configure("TLabel", background="#DAE3F3", padding=10)  # Bleu clair pour le fond
        style.configure("TButton", background="#4285F4", foreground="white", padding=10)  # Bleu Google pour les boutons
        style.configure("TMenubutton", background="#4285F4", foreground="white", padding=5)  # Bleu Google pour le menu déroulant

        self.label = ttk.Label(master, text="Choisissez un dossier contenant des images:")
        self.label.pack(pady=10)

        self.select_button = ttk.Button(master, text="Sélectionner le dossier", command=self.select_folder)
        self.select_button.pack(pady=10)

        self.folder_var = StringVar(master)
        self.folder_var.set("Sélectionnez un dossier")

        options = ["images", "musique", "photos", "téléchargement", "documents"]
        self.option_menu = ttk.OptionMenu(master, self.folder_var, *options)
        self.option_menu.pack(pady=10)

        self.sort_button = ttk.Button(master, text="Classer les images", command=self.sort_images)
        self.sort_button.pack(pady=10)

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.label.config(text=f"Dossier sélectionné: {self.folder_path}")

    def sort_images(self):
        target_folder = self.folder_var.get()
        if target_folder == "Sélectionnez un dossier":
            return

        destination_path = os.path.join(self.folder_path, target_folder)
        os.makedirs(destination_path, exist_ok=True)

        for filename in os.listdir(self.folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                source_file = os.path.join(self.folder_path, filename)
                shutil.move(source_file, destination_path)
        
        self.label.config(text=f"Images classées dans: {destination_path}")

if __name__ == "__main__":
    root = Tk()
    app = ImageSorterApp(root)
    root.mainloop()
