import os
import shutil
import mimetypes
from tkinter import Tk, Label, Button, filedialog, StringVar, OptionMenu, ttk
from tkinter import font as tkFont
from tkinter import messagebox  # For error messages
from tkinter.ttk import Progressbar

class ImageSorterApp:
    def __init__(self, master):
        self.master = master
        master.title("Stephydlb - Classificateur d'Images")
        master.geometry("600x400")  # Larger window size

        # Google-like Styling
        style = ttk.Style()
        style.theme_use('clam')
        bleu_google = "#4285F4"
        gris_clair = "#F5F5F5"
        blanc = "#FFFFFF"
        style.configure("TLabel", background=gris_clair, foreground="black", 
                        padding=10, font=("Roboto", 14))
        style.configure("TButton", background=bleu_google, foreground=blanc, 
                        padding=10, font=("Roboto", 12, "bold"))
        style.configure("TMenubutton", background=bleu_google, foreground=blanc, 
                        padding=5, font=("Roboto", 12))
        title_font = tkFont.Font(family="Product Sans", size=20, weight="bold")

        # Title
        self.title_label = ttk.Label(master, text="Stephydlb", font=title_font)
        self.title_label.pack(pady=(20, 10))

        # Folder Selection
        self.label = ttk.Label(master, text="Choisissez un dossier contenant des images:")
        self.label.pack(pady=10)

        self.select_button = ttk.Button(master, text="Sélectionner le dossier", 
                                        command=self.select_folder)
        self.select_button.pack(pady=10)

        # Sorting Options
        self.folder_var = StringVar(master)
        self.folder_var.set("Sélectionnez un dossier cible")
        options = ["images", "musique", "photos", "téléchargement", "documents"]
        self.option_menu = ttk.OptionMenu(master, self.folder_var, *options)
        self.option_menu.pack(pady=10)

        # Sort Button (initially disabled)
        self.sort_button = ttk.Button(master, text="Classer les images", 
                                        command=self.sort_images, state="disabled")
        self.sort_button.pack(pady=10)

        # Progress Bar
        self.progress = Progressbar(master, orient="horizontal", 
                                    length=300, mode="determinate")
        self.progress.pack(pady=20)

        # Button Hover Effects
        self.select_button.bind("<Enter>", lambda e: self.select_button.config(background="#357AE8"))
        self.select_button.bind("<Leave>", lambda e: self.select_button.config(background=bleu_google))
        self.sort_button.bind("<Enter>", lambda e: self.sort_button.config(background="#357AE8"))
        self.sort_button.bind("<Leave>", lambda e: self.sort_button.config(background=bleu_google))

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.label.config(text=f"Dossier sélectionné: {self.folder_path}")
            self.sort_button.config(state="normal")  # Enable sort button

    def sort_images(self):
        target_folder = self.folder_var.get()
        if target_folder == "Sélectionnez un dossier cible":
            messagebox.showwarning("Attention", "Veuillez sélectionner un dossier cible.")
            return

        if hasattr(self, 'folder_path'):
            destination_path = os.path.join(self.folder_path, target_folder)
            os.makedirs(destination_path, exist_ok=True)

            image_count = 0
            total_images = 0
            for f in os.listdir(self.folder_path):
                if os.path.isfile(os.path.join(self.folder_path, f)):
                    total_images += 1

            for filename in os.listdir(self.folder_path):
                file_path = os.path.join(self.folder_path, filename)
                if os.path.isfile(file_path):
                    file_type = mimetypes.guess_type(filename)[0]
                    if file_type and file_type.startswith('image/'):
                        shutil.move(file_path, destination_path)
                        image_count += 1
                        progress = (image_count / total_images) * 100
                        self.progress['value'] = progress
                        self.master.update_idletasks()

            self.label.config(text=f"Images classées dans: {destination_path}")
            messagebox.showinfo("Terminé", f"{image_count} images classées dans {destination_path}")

if __name__ == "__main__":
    root = Tk()
    app = ImageSorterApp(root)
    root.mainloop()
