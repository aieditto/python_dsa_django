import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageTk, ImageDraw

class TShirtMockupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("T-Shirt Mockup Generator")
        self.tshirt_image = None
        self.design_image = None
        self.tshirt_color = None
        self.preview_canvas = None
        self.design_position = (0, 0)
        self.design_size = (300, 300)
        self.drag_start_x = 0
        self.drag_start_y = 0
        
        self.init_ui()

    def init_ui(self):
        # T-Shirt Path
        tk.Label(self.root, text="Blank T-Shirt Path:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.tshirt_entry = tk.Entry(self.root, width=40)
        self.tshirt_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Browse", command=self.load_tshirt_image).grid(row=0, column=2, padx=10, pady=5)

        # Design Path
        tk.Label(self.root, text="Design Path:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.design_entry = tk.Entry(self.root, width=40)
        self.design_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Browse", command=self.load_design_image).grid(row=1, column=2, padx=10, pady=5)

        # Output Path
        tk.Label(self.root, text="Output Path:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.output_entry = tk.Entry(self.root, width=40)
        self.output_entry.grid(row=2, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Browse", command=self.select_output_path).grid(row=2, column=2, padx=10, pady=5)

        # T-Shirt Color
        tk.Label(self.root, text="T-Shirt Color:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        tk.Button(self.root, text="Pick Color", command=self.pick_color).grid(row=3, column=1, pady=5)

        # Canvas for Preview
        self.preview_canvas = tk.Canvas(self.root, width=500, height=500, bg="white")
        self.preview_canvas.grid(row=4, column=0, columnspan=3, pady=10)
        self.preview_canvas.bind("<Button-1>", self.start_drag)
        self.preview_canvas.bind("<B1-Motion>", self.drag_design)
        self.preview_canvas.bind("<MouseWheel>", self.resize_design)

        # Generate Mockup Button
        tk.Button(self.root, text="Generate Mockup", command=self.generate_mockup, bg="green", fg="white").grid(row=5, column=1, pady=10)

    def load_tshirt_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        self.tshirt_entry.delete(0, tk.END)
        self.tshirt_entry.insert(0, path)
        self.tshirt_image = Image.open(path).convert("RGBA")
        self.update_preview()

    def load_design_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        self.design_entry.delete(0, tk.END)
        self.design_entry.insert(0, path)
        self.design_image = Image.open(path).convert("RGBA")
        self.design_image = self.design_image.resize(self.design_size)
        self.update_preview()

    def pick_color(self):
        color_code = colorchooser.askcolor(title="Choose T-Shirt Color")[0]
        if color_code:
            self.tshirt_color = tuple(map(int, color_code))
        self.update_preview()

    def start_drag(self, event):
        """Capture the starting point of the drag."""
        self.drag_start_x = event.x
        self.drag_start_y = event.y

    def drag_design(self, event):
        """Update the design position during dragging."""
        if self.design_image:
            dx = event.x - self.drag_start_x
            dy = event.y - self.drag_start_y
            self.design_position = (self.design_position[0] + dx, self.design_position[1] + dy)
            self.drag_start_x = event.x
            self.drag_start_y = event.y
            self.update_preview()

    def resize_design(self, event):
        """Resize the design using the mouse wheel."""
        if self.design_image:
            scale = 10 if event.delta > 0 else -10
            self.design_size = (max(50, self.design_size[0] + scale), max(50, self.design_size[1] + scale))
            self.design_image = self.design_image.resize(self.design_size)
            self.update_preview()

    def select_output_path(self):
        path = filedialog.asksaveasfilename(defaultextension=".png")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, path)

    def update_preview(self):
        if not self.tshirt_image:
            return

        # Create a copy of the t-shirt image
        preview = self.tshirt_image.copy()
        if self.tshirt_color:
            color_overlay = Image.new("RGBA", preview.size, self.tshirt_color + (255,))
            preview = Image.alpha_composite(color_overlay, preview)

        # Add the design
        if self.design_image:
            preview.paste(self.design_image, self.design_position, self.design_image)

        # Update the canvas
        preview.thumbnail((500, 500))
        self.tk_preview = ImageTk.PhotoImage(preview)
        self.preview_canvas.create_image(250, 250, image=self.tk_preview)

    def generate_mockup(self):
        output_path = self.output_entry.get()
        if not output_path:
            messagebox.showerror("Error", "Please specify an output path!")
            return

        try:
            final_image = self.tshirt_image.copy()
            if self.tshirt_color:
                color_overlay = Image.new("RGBA", final_image.size, self.tshirt_color + (255,))
                final_image = Image.alpha_composite(color_overlay, final_image)

            if self.design_image:
                final_image.paste(self.design_image, self.design_position, self.design_image)

            final_image.save(output_path, "PNG")
            messagebox.showinfo("Success", f"Mockup saved at {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate mockup: {e}")

# Run the application
root = tk.Tk()
app = TShirtMockupApp(root)
root.mainloop()
