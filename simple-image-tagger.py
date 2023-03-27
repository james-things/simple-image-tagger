# a simple (but performant!) little tkinter GUI to help you tag your dreambooth-style datasets
import os
import tkinter as tk
import tkinter.filedialog as filedialog
from PIL import Image, ImageTk

class ImageTagger:
    def __init__(self, root):
        self.root = root
        self.image_folder = None
        self.image_paths = []
        self.current_image_index = 0

        self.root.geometry("800x600")
        self.root.title("simple image tagger")

        self.display_panel = tk.Label(self.root, bd=1)
        self.display_panel.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.display_panel.configure(background="#f2f2f2")

        self.text_box = tk.Text(self.root, wrap=tk.WORD, height=10) 
        self.text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.button_frame = tk.Frame(self.root) 
        self.button_frame.pack(side=tk.RIGHT, expand=False, fill=tk.Y, padx=10, pady=10)
        self.button_frame.configure(background="#f2f2f2")

        self.root.grid_rowconfigure(0, weight=1) 

        self.next_button = tk.Button(self.button_frame, text="Next", command=self.next_image)
        self.next_button.pack(side=tk.TOP, fill="both", expand=True, padx=10, pady=10)

        self.previous_button = tk.Button(self.button_frame, text="Previous", command=self.previous_image)
        self.previous_button.pack(side=tk.TOP, fill="both", expand=True, padx=10, pady=10)

        self.choose_folder()
        self.recursive_loading = tk.messagebox.askyesno("Recursive Loading", "Load images from subfolders recursively?")
        if self.image_folder:
            self.load_images(recursive=self.recursive_loading)
            self.display_image()

        self.root.mainloop()

    def choose_folder(self):
        self.image_folder = filedialog.askdirectory()
        if self.image_folder:
            self.load_images()
            self.display_image()

    def load_images(self, folder=None, recursive=False):
        if folder is None:
            folder = self.image_folder
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isdir(file_path) and recursive:
                self.load_images(file_path, recursive)
            elif filename.lower().endswith((".jpg", ".jpeg", ".png")):
                self.image_paths.append(file_path)

    def display_image(self):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        w, h = self.display_panel.winfo_width(), self.display_panel.winfo_height()
        image.thumbnail((w, h))
        photo = ImageTk.PhotoImage(image)
        self.display_panel.configure(image=photo)
        self.display_panel.image = photo
        self.load_tags()

    def next_image(self):
        self.save_tags()
        self.current_image_index += 1
        if self.current_image_index >= len(self.image_paths):
            self.current_image_index = 0
        self.display_image()

    def previous_image(self):
        self.save_tags()
        self.current_image_index -= 1
        if self.current_image_index < 0:
            self.current_image_index = len(self.image_paths) - 1
        self.display_image()

    def save_tags(self):
        if not self.image_folder:
            return
        image_path = self.image_paths[self.current_image_index]
        text_content = self.text_box.get(1.0, tk.END).strip()
        with open(os.path.splitext(image_path)[0] + ".txt", "w") as f:
            f.write(text_content)

    def load_tags(self):
        if not self.image_folder:
            return
        image_path = self.image_paths[self.current_image_index]
        text_file_path = os.path.splitext(image_path)[0] + ".txt"
        if os.path.exists(text_file_path):
            with open(text_file_path, "r") as f:
                text_content = f.read()
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, text_content)
        else:
            self.text_box.delete(1.0, tk.END)

app = ImageTagger(tk.Tk())
