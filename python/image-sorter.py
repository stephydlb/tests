import os
import shutil
from tkinter import Tk, Label, Button, filedialog, StringVar, OptionMenu

class ImageSorterApp:
    def __init__(self, master):
        self.master = master
        master.title("Classificateur d'Images")

        self.label = Label(master, text="Choisissez un dossier contenant des images:")
        self.label.pack()

        self.select_button = Button(master, text="Sélectionner le dossier", command=self.select_folder)
        self.select_button.pack()

        self.folder_var = StringVar(master)
        self.folder_var.set("Sélectionnez un dossier")  # valeur par défaut

        self.option_menu = OptionMenu(master, self.folder_var, "images", "musique", "photos", "téléchargement", "documents")
        self.option_menu.pack()

        self.sort_button = Button(master, text="Classer les images", command=self.sort_images)
        self.sort_button.pack()

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.label.config(text=f"Dossier sélectionné: {self.folder_path}")

    def sort_images(self):
        target_folder = self.folder_var.get()
        if target_folder == "Sélectionnez un dossier":
            return

        # Crée le dossier de destination s'il n'existe pas
        destination_path = os.path.join(self.folder_path, target_folder)
        os.makedirs(destination_path, exist_ok=True)

        # Parcourt les fichiers dans le dossier sélectionné
        for filename in os.listdir(self.folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                source_file = os.path.join(self.folder_path, filename)
                shutil.move(source_file, destination_path)
        
        self.label.config(text=f"Images classées dans: {destination_path}")

if __name__ == "__main__":
    root = Tk()
    app = ImageSorterApp(root)
    root.mainloop()
