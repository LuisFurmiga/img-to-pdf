import os
from tkinter import Tk, filedialog, messagebox, Listbox, Button, Label, END, Scrollbar, SINGLE
from PIL import Image # type: ignore


class ImageToPDFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Imagens para PDF")

        # Lista para armazenar os caminhos das imagens
        self.image_paths = []

        # Elementos da interface
        self.label = Label(root, text="Imagens Selecionadas:")
        self.label.pack(pady=5)

        # Lista de imagens
        self.listbox = Listbox(root, selectmode=SINGLE, width=50, height=15)
        self.listbox.pack(padx=10, pady=5, side="left")

        # Barra de rolagem
        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side="left", fill="y")
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Botões para funcionalidades
        self.add_button = Button(root, text="Adicionar Imagens", command=self.add_images)
        self.add_button.pack(pady=5)

        self.remove_button = Button(root, text="Remover Imagem", command=self.remove_image)
        self.remove_button.pack(pady=5)

        self.up_button = Button(root, text="Mover Para Cima", command=self.move_up)
        self.up_button.pack(pady=5)

        self.down_button = Button(root, text="Mover Para Baixo", command=self.move_down)
        self.down_button.pack(pady=5)

        self.convert_button = Button(root, text="Converter para PDF", command=self.convert_to_pdf)
        self.convert_button.pack(pady=10)

    def add_images(self):
        # Selecionar imagens
        new_images = filedialog.askopenfilenames(
            title="Selecione as imagens",
            filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp *.tiff")]
        )
        if new_images:
            self.image_paths.extend(new_images)
            for image in new_images:
                self.listbox.insert(END, os.path.basename(image))

    def remove_image(self):
        # Remover imagem selecionada
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index)
            del self.image_paths[selected_index[0]]

    def move_up(self):
        # Mover a imagem selecionada para cima
        selected_index = self.listbox.curselection()
        if selected_index and selected_index[0] > 0:
            index = selected_index[0]
            self.image_paths[index], self.image_paths[index - 1] = (
                self.image_paths[index - 1],
                self.image_paths[index],
            )
            text = self.listbox.get(index)
            self.listbox.delete(index)
            self.listbox.insert(index - 1, text)
            self.listbox.select_set(index - 1)

    def move_down(self):
        # Mover a imagem selecionada para baixo
        selected_index = self.listbox.curselection()
        if selected_index and selected_index[0] < len(self.image_paths) - 1:
            index = selected_index[0]
            self.image_paths[index], self.image_paths[index + 1] = (
                self.image_paths[index + 1],
                self.image_paths[index],
            )
            text = self.listbox.get(index)
            self.listbox.delete(index)
            self.listbox.insert(index + 1, text)
            self.listbox.select_set(index + 1)

    def convert_to_pdf(self):
        if not self.image_paths:
            messagebox.showwarning("Aviso", "Nenhuma imagem foi selecionada.")
            return

        # Selecionar a pasta de destino
        output_folder = filedialog.askdirectory(title="Selecione a pasta de destino")
        if not output_folder:
            messagebox.showwarning("Aviso", "Nenhuma pasta de destino foi selecionada.")
            return

        # Nome do arquivo de saída baseado na primeira imagem
        first_image_name = os.path.splitext(os.path.basename(self.image_paths[0]))[0]
        output_pdf = os.path.join(output_folder, f"{first_image_name}.pdf")

        # Converter as imagens para PDF
        a4_width_px, a4_height_px = 2480, 3508  # A4 em 300 DPI
        images = []
        for image_path in self.image_paths:
            try:
                img = Image.open(image_path)
                if img.mode != "RGB":
                    img = img.convert("RGB")

                # Redimensionar a imagem para caber na folha A4
                img.thumbnail((a4_width_px, a4_height_px))
                images.append(img)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao processar a imagem {image_path}: {e}")
                return

        try:
            images[0].save(output_pdf, save_all=True, append_images=images[1:])
            messagebox.showinfo("Sucesso", f"PDF criado com sucesso: {output_pdf}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar o PDF: {e}")


if __name__ == "__main__":
    root = Tk()
    app = ImageToPDFApp(root)
    root.mainloop()
