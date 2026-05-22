"""
build_polyglot.py
Creates:  output.pdf.zip  — a single file that is simultaneously:
  • A valid PDF   (PDF readers see the document)
  • A valid ZIP   (zip tools extract activity_logger.py)
  • Runnable by Python via:  python output.pdf.zip
"""

import zipfile
import io
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


#python script that is my logger script that goes inside the zip
with open("c1.py", "r") as f:
    PYTHON_SCRIPT = f.read()

#generating the pdf bytes in memory
def make_pdf_bytes() -> bytes:
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=letter,
                            leftMargin=0.75*inch, rightMargin=0.75*inch,
                            topMargin=0.75*inch,  bottomMargin=0.75*inch)
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle("T", parent=styles["Title"],
                                 fontSize=18, spaceAfter=8,
                                 textColor=colors.HexColor("#1a1a2e"))
    body_style  = ParagraphStyle("B", parent=styles["Normal"],
                                 fontSize=10, leading=15,
                                 textColor=colors.HexColor("#333333"))
    note_style  = ParagraphStyle("N", parent=styles["Normal"],
                                 fontSize=9,  leading=13,
                                 textColor=colors.HexColor("#666666"))
    c = canvas.Canvas(buf, pagesize=letter)
    """img = ImageReader(image path)"""

    