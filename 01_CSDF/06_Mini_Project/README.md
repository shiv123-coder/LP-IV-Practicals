# Image Forensics Tool

A desktop application developed in Python for preliminary digital image forensics, file integrity verification, EXIF metadata inspection, and Error Level Analysis (ELA).

**Submitted By:** Shivshankar Mali  
**Roll No:** 49 | **Division:** C  
**Course:** Laboratory Practice-IV (Cyber Security and Digital Forensics)  
**Institute:** JSPM's Bhivarabai Sawant Institute of Technology and Research, Wagholi, Pune  

---

## 1. Features
- **Image Properties**: Formats (JPEG, PNG, etc.), dimensions, color modes, and exact byte size.
- **Integrity Verification**: Generates standard SHA-256 cryptographic digests.
- **Metadata Analysis**: Extracts and parses up to 25 available EXIF metadata tags.
- **Error Level Analysis (ELA)**: Resaves image at 90% JPEG quality, calculates pixel-level difference against the original, and amplifies differences with high brightness enhancement to highlight compression anomalies.
- **Exporting**: Allows forensic examiners to export and save the generated ELA image.

---

## 2. Project Structure
```
06_Mini_Project/
|-- app.py                     # Main Tkinter GUI application
|-- test_image_forensics.jpg   # Sample image for forensic testing
|-- requirements.txt           # Python dependencies
|-- README.md                  # Project documentation
|-- main.tex                   # LaTeX report source
|-- logo.png                   # College logo
|-- 1.png                      # Application screenshot (Figure 5.1)
|-- 2.png                      # ELA result screenshot (Figure 5.2)
|-- Mini_Project_Report.pdf    # Full technical project report
```

---

## 3. Prerequisites & Installation

### Prerequisites
- Python 3.9 or higher
- Tkinter (included by default in Python for Windows)

### Installation
Open PowerShell in this directory and install the required library:
```powershell
python -m pip install -r requirements.txt
```

---

## 4. Execution Steps

Run the application:
```powershell
python app.py
```
*(Or specify an initial image to open directly: `python app.py test_image_forensics.jpg`)*

### Forensic Workflow:
1. Click **Choose Image** and select `test_image_forensics.jpg` (or any image file).
2. Inspect the **Selected Image** and **ELA Analysis Preview** side-by-side.
3. Review the **Forensic Report** text panel for SHA-256 integrity, dimensions, format, and EXIF metadata.
4. Click **Save ELA Image** to export the ELA anomaly map as a PNG/JPEG file.
5. Click **Clear** to reset the workspace.

---

## 5. Forensic Considerations & Limitations
- **Screening Aid**: Error Level Analysis (ELA) is a preliminary screening tool, not conclusive proof of digital tampering.
- **Compression Factors**: High-contrast edges, recurring resaving, and aggressive web optimization naturally exhibit different compression levels.
- **Corroboration**: All forensic findings should be corroborated with hash integrity checks, EXIF timelines, and cross-channel file verification.
