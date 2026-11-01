"""
Image Forensics Tool
Author: Shivshankar Mali (Roll No: 49, Division: C)
Department of Computer Engineering
JSPM's Bhivarabai Sawant Institute of Technology and Research, Wagholi, Pune

Features:
- Image Property Analysis (Dimensions, Format, Mode, File Size)
- File Integrity via SHA-256 Cryptographic Hash
- EXIF Metadata Inspection
- Error Level Analysis (ELA) with JPEG Recompression & Difference Enhancement
- Export Analyzed ELA Images
"""

import hashlib
import io
import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageChops, ImageEnhance, ImageTk, ExifTags


class ImageForensicsApp:
    def __init__(self, root, initial_image=None):
        self.root = root
        self.root.title("Image Forensics Tool")
        self.root.geometry("1120x820")
        self.root.minsize(980, 720)

        # State variables
        self.current_image_path = None
        self.original_image = None
        self.ela_image = None
        self.photo_original = None
        self.photo_ela = None

        self._setup_ui()

        # If an initial image path was provided (e.g. from command line), open it
        if initial_image and os.path.exists(initial_image):
            self.root.after(100, lambda: self.process_image(initial_image))

    def _setup_ui(self):
        # Top Header Frame
        header_frame = ttk.Frame(self.root, padding="15 12 15 5")
        header_frame.pack(fill=tk.X)

        title_label = tk.Label(
            header_frame,
            text="IMAGE FORENSICS TOOL",
            font=("Arial", 22, "bold"),
            fg="#111827"
        )
        title_label.pack(anchor=tk.CENTER)

        subtitle_label = tk.Label(
            header_frame,
            text="Image metadata • SHA-256 integrity • Error Level Analysis (ELA)",
            font=("Arial", 10),
            fg="#4B5563"
        )
        subtitle_label.pack(anchor=tk.CENTER, pady=(2, 8))

        # Toolbar Frame
        toolbar_frame = ttk.Frame(self.root, padding="15 5 15 10")
        toolbar_frame.pack(fill=tk.X)

        btn_choose = tk.Button(
            toolbar_frame,
            text="Choose Image",
            font=("Arial", 10, "normal"),
            bg="#f3f4f6",
            fg="#111827",
            relief=tk.RAISED,
            padx=14,
            pady=4,
            command=self.choose_image
        )
        btn_choose.pack(side=tk.LEFT, padx=(0, 8))

        btn_save_ela = tk.Button(
            toolbar_frame,
            text="Save ELA Image",
            font=("Arial", 10, "normal"),
            bg="#f3f4f6",
            fg="#111827",
            relief=tk.RAISED,
            padx=14,
            pady=4,
            command=self.save_ela_image
        )
        btn_save_ela.pack(side=tk.LEFT, padx=(0, 8))

        btn_clear = tk.Button(
            toolbar_frame,
            text="Clear",
            font=("Arial", 10, "normal"),
            bg="#f3f4f6",
            fg="#111827",
            relief=tk.RAISED,
            padx=18,
            pady=4,
            command=self.clear_all
        )
        btn_clear.pack(side=tk.LEFT)

        # Center Preview Area (2 side-by-side frames)
        previews_container = ttk.Frame(self.root, padding="15 5 15 10")
        previews_container.pack(fill=tk.BOTH, expand=True)
        previews_container.columnconfigure(0, weight=1)
        previews_container.columnconfigure(1, weight=1)
        previews_container.rowconfigure(0, weight=1)

        # Left: Selected Image
        self.frame_selected = ttk.LabelFrame(previews_container, text="Selected Image", padding="8")
        self.frame_selected.grid(row=0, column=0, sticky="nsew", padx=(0, 6))

        self.canvas_orig = tk.Canvas(self.frame_selected, bg="#F9FAFB", highlightthickness=0)
        self.canvas_orig.pack(fill=tk.BOTH, expand=True)

        # Right: ELA Analysis Preview
        self.frame_ela = ttk.LabelFrame(previews_container, text="ELA Analysis Preview", padding="8")
        self.frame_ela.grid(row=0, column=1, sticky="nsew", padx=(6, 0))

        self.canvas_ela = tk.Canvas(self.frame_ela, bg="#000000", highlightthickness=0)
        self.canvas_ela.pack(fill=tk.BOTH, expand=True)

        # Bottom Area: Forensic Report
        report_container = ttk.Frame(self.root, padding="15 5 15 15")
        report_container.pack(fill=tk.X)

        frame_report = ttk.LabelFrame(report_container, text="Forensic Report", padding="8")
        frame_report.pack(fill=tk.X)

        text_frame = ttk.Frame(frame_report)
        text_frame.pack(fill=tk.BOTH, expand=True)

        self.report_text = tk.Text(
            text_frame,
            height=10,
            font=("Consolas", 10),
            wrap=tk.WORD,
            bg="#ffffff",
            fg="#111827",
            relief=tk.SUNKEN,
            bd=1
        )
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.report_text.yview)
        self.report_text.configure(yscrollcommand=scrollbar.set)

        self.report_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    @staticmethod
    def sha256_file(path):
        """Listing 4.1: SHA-256 hash generation."""
        hasher = hashlib.sha256()
        with open(path, "rb") as file:
            for chunk in iter(lambda: file.read(1024 * 1024), b""):
                hasher.update(chunk)
        return hasher.hexdigest()

    @staticmethod
    def generate_ela(source, quality=90, scale=15):
        """Listing 4.2: Error Level Analysis recompression and enhancement."""
        image = source.convert("RGB")
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG", quality=quality)
        buffer.seek(0)

        recompressed = Image.open(buffer).convert("RGB")
        difference = ImageChops.difference(image, recompressed)

        ela_result = ImageEnhance.Brightness(difference).enhance(scale)
        return ela_result

    @staticmethod
    def extract_exif(image):
        """Extracts available EXIF metadata up to 25 fields."""
        fields = []
        try:
            raw_exif = image._getexif()
            if raw_exif:
                for tag_id, value in raw_exif.items():
                    tag_name = ExifTags.TAGS.get(tag_id, str(tag_id))
                    # Truncate very long byte strings or thumbnails
                    val_str = str(value)
                    if len(val_str) > 80:
                        val_str = val_str[:77] + "..."
                    fields.append(f"{tag_name}: {val_str}")
                    if len(fields) >= 25:
                        break
        except Exception:
            pass
        return fields

    def choose_image(self):
        """Opens file dialog for user to select an image."""
        file_path = filedialog.askopenfilename(
            title="Select Image for Forensic Analysis",
            filetypes=[
                ("Image Files", "*.jpg *.jpeg *.png *.bmp *.tiff *.webp"),
                ("JPEG Images", "*.jpg *.jpeg"),
                ("PNG Images", "*.png"),
                ("All Files", "*.*")
            ]
        )
        if file_path:
            self.process_image(file_path)

    def process_image(self, file_path):
        """Performs full forensic inspection on the chosen image file."""
        try:
            self.current_image_path = os.path.abspath(file_path)
            self.original_image = Image.open(self.current_image_path)

            file_size_bytes = os.path.getsize(self.current_image_path)
            file_size_kb = file_size_bytes / 1024.0
            sha256_digest = self.sha256_file(self.current_image_path)

            width, height = self.original_image.size
            img_format = self.original_image.format or "Unknown"
            img_mode = self.original_image.mode

            # Generate ELA
            self.ela_image = self.generate_ela(self.original_image, quality=90, scale=15)

            # Extract EXIF
            exif_list = self.extract_exif(self.original_image)

            # Display Previews
            self._display_preview(self.canvas_orig, self.original_image, is_ela=False)
            self._display_preview(self.canvas_ela, self.ela_image, is_ela=True)

            # Build Forensic Report Text
            report_lines = [
                f"File name: {os.path.basename(self.current_image_path)}",
                f"Full path: {self.current_image_path.replace(os.sep, '/')}",
                f"File size: {file_size_bytes:,} bytes ({file_size_kb:.2f} KB)",
                f"Image format: {img_format}",
                f"Dimensions: {width} x {height} pixels",
                f"Color mode: {img_mode}",
                f"SHA-256: {sha256_digest}",
                "",
                "EXIF metadata (up to 25 fields):"
            ]

            if exif_list:
                for item in exif_list:
                    report_lines.append(f"  {item}")
            else:
                report_lines.append("No EXIF metadata found.")

            self.report_text.config(state=tk.NORMAL)
            self.report_text.delete("1.0", tk.END)
            self.report_text.insert(tk.END, "\n".join(report_lines) + "\n")

        except Exception as err:
            messagebox.showerror("Error", f"Failed to analyze image:\n{err}")

    def _display_preview(self, canvas, pil_img, is_ela=False):
        """Scales image to fit canvas preserving aspect ratio."""
        canvas.update_idletasks()
        cw = canvas.winfo_width()
        ch = canvas.winfo_height()
        if cw < 50 or ch < 50:
            cw, ch = 500, 350

        # Calculate fit dimensions
        iw, ih = pil_img.size
        scale = min((cw - 16) / iw, (ch - 16) / ih)
        new_w = max(1, int(iw * scale))
        new_h = max(1, int(ih * scale))

        resized = pil_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        tk_img = ImageTk.PhotoImage(resized)

        canvas.delete("all")
        cx = cw // 2
        cy = ch // 2
        canvas.create_image(cx, cy, image=tk_img)

        if is_ela:
            self.photo_ela = tk_img
        else:
            self.photo_original = tk_img

    def save_ela_image(self):
        """Saves generated ELA image to user-selected location."""
        if not self.ela_image:
            messagebox.showwarning("Warning", "No ELA analysis available. Please select an image first.")
            return

        base_name = os.path.splitext(os.path.basename(self.current_image_path))[0]
        default_file = f"{base_name}_ela.png"

        save_path = filedialog.asksaveasfilename(
            title="Save ELA Result Image",
            initialfile=default_file,
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg"), ("All Files", "*.*")]
        )
        if save_path:
            try:
                self.ela_image.save(save_path)
                messagebox.showinfo("Success", f"ELA image saved successfully to:\n{save_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save image:\n{e}")

    def clear_all(self):
        """Resets all previews and report text."""
        self.current_image_path = None
        self.original_image = None
        self.ela_image = None
        self.photo_original = None
        self.photo_ela = None

        self.canvas_orig.delete("all")
        self.canvas_ela.delete("all")
        self.report_text.config(state=tk.NORMAL)
        self.report_text.delete("1.0", tk.END)


def main():
    initial_file = None
    if len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
        initial_file = sys.argv[1]

    root = tk.Tk()
    app = ImageForensicsApp(root, initial_image=initial_file)
    root.mainloop()


if __name__ == "__main__":
    main()
