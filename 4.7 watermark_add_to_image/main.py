import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import os

def upload_image():
    """Open file dialog to select an image."""
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if file_path:
        global selected_image_path
        selected_image_path = file_path
        status_label.config(text=f"Selected: {os.path.basename(file_path)}")
        preview_image()

def preview_image():
    """Display a preview of the selected image."""
    if selected_image_path:
        img = Image.open(selected_image_path)
        img.thumbnail((200, 200))  # Resize for preview
        img_tk = tk.PhotoImage(img)
        preview_label.config(image=img_tk)
        preview_label.image = img_tk

def add_watermark():
    """Add watermark to the image and save it."""
    if not selected_image_path:
        messagebox.showerror("Error", "Please select an image first.")
        return
    
    watermark_text = watermark_entry.get()
    if not watermark_text:
        messagebox.showerror("Error", "Please enter watermark text.")
        return
    
    try:
        # Open the image
        img = Image.open(selected_image_path)
        draw = ImageDraw.Draw(img)
        
        # Use a larger font size (proportional to image width for "big")
        font_size = int(img.width / 10)  # Adjust divisor for size; e.g., /10 makes it about 10% of width
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()
        
        # Calculate text bounding box
        text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Position in the center
        x = (img.width - text_width) // 2
        y = (img.height - text_height) // 2
        
        # Add semi-transparent text
        draw.text((x, y), watermark_text, fill=(255, 255, 255, 128), font=font)
        
        # Save the watermarked image
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg"), ("All Files", "*.*")]
        )
        if save_path:
            img.save(save_path)
            messagebox.showinfo("Success", f"Watermarked image saved as {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add watermark: {str(e)}")

# Initialize global variable
selected_image_path = None

# Create the main window
root = tk.Tk()
root.title("Image Watermark Tool")
root.geometry("400x500")

# Widgets
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

status_label = tk.Label(root, text="No image selected")
status_label.pack()

preview_label = tk.Label(root)
preview_label.pack(pady=10)

watermark_label = tk.Label(root, text="Watermark Text:")
watermark_label.pack()

watermark_entry = tk.Entry(root, width=30)
watermark_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Watermark and Save", command=add_watermark)
add_button.pack(pady=20)

# Run the application
root.mainloop()
