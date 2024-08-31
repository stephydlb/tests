import os
import shutil
from tkinter import Tk, Label, Button, filedialog, StringVar, OptionMenu
from tkinter import ttk
from tkinter import font as tkFont  # Importer les polices

class ImageSorterApp:
    def __init__(self, master):
        self.master = master
        master.title("Stephydlb - Classificateur d'Images")  # Titre avec votre nom

        # Configuration du style Google avec ttk
        style = ttk.Style()
        style.theme_use('clam')  # Thème moderne comme base

        # Couleurs Google
        bleu_google = "#4285F4"
        gris_clair = "#F5F5F5"
        blanc = "#FFFFFF"

        # Configuration des widgets
        style.configure("TLabel", background=gris_clair, foreground="black", padding=10, font=("Roboto", 14))  # Police Roboto
        style.configure("TButton", background=bleu_google, foreground=blanc, padding=10, font=("Roboto", 12, "bold"))
        style.configure("TMenubutton", background=bleu_google, foreground=blanc, padding=5, font=("Roboto", 12))

        # Police pour le titre
        title_font = tkFont.Font(family="Product Sans", size=20, weight="bold") 

        # Titre en grand
        self.title_label = ttk.Label(master, text="Stephydlb", font=title_font)
        self.title_label.pack(pady=(20, 10))  # Marge supérieure plus importante

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

        # Animations sur les boutons (changement de couleur au survol)
        self.select_button.bind("<Enter>", lambda e: self.select_button.config(background="#357AE8"))
        self.select_button.bind("<Leave>", lambda e: self.select_button.config(background=bleu_google))

        self.sort_button.bind("<Enter>", lambda e: self.sort_button.config(background="#357AE8"))
        self.sort_button.bind("<Leave>", lambda e: self.sort_button.config(background=bleu_google))

        # Ajuster la taille de la fenêtre (un peu plus large)
        master.geometry("500x350")  # Ajustez les dimensions selon vos besoins

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.label.config(text=f"Dossier sélectionné: {self.folder_path}")

    def sort_images(self):
        target_folder = self.folder_var.get()
        if target_folder == "Sélectionnez un dossier":
            return

        if hasattr(self, 'folder_path'):
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
