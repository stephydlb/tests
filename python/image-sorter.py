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
        self.bleu_google = "#4285F4"
        self.gris_clair = "#F5F5F5"
        self.blanc = "#FFFFFF"
        self.noir = "#000000"
        self.configure_styles()

        # Title
        title_font = tkFont.Font(family="Roboto", size=24, weight="bold")  # Define title_font here
        self.title_label = ttk.Label(master, text="Stephydlb", font=title_font)
        self.title_label.pack(pady=(20, 10))

        # Dark Mode Switch Button
        self.dark_mode_button = ttk.Button(master, text="Mode Sombre", command=self.toggle_dark_mode)
        self.dark_mode_button.pack(pady=(10, 0))

         # Dark Mode Switch
        self.dark_mode = False
        self.toggle_dark_mode()
        
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
        self.select_button.bind("<Leave>", lambda e: self.select_button.config(background=self.bleu_google))
        self.sort_button.bind("<Enter>", lambda e: self.sort_button.config(background="#357AE8"))
        self.sort_button.bind("<Leave>", lambda e: self.sort_button.config(background=self.bleu_google))

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.bleu_google = "#357AE8"
            self.gris_clair = "#333333"
            self.blanc = "#FFFFFF"
            self.noir = "#000000"
            self.dark_mode_button.config(text="Mode Clair")
        else:
            self.bleu_google = "#4285F4"
            self.gris_clair = "#F5F5F5"
            self.blanc = "#FFFFFF"
            self.noir = "#000000"
            self.dark_mode_button.config(text="Mode Sombre")
        self.configure_styles()

    def configure_styles(self):
        style = ttk.Style()
        style.configure("TLabel", background=self.gris_clair, foreground=self.noir, 
                        padding=10, font=("Roboto", 14))
        style.configure("TButton", background=self.bleu_google, foreground=self.blanc, 
                        padding=10, font=("Roboto", 12, "bold"))
        style.configure("TMenubutton", background=self.bleu_google, foreground=self.blanc, 
                        padding=5, font=("Roboto", 12))

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
