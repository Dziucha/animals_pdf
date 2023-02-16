from fpdf import FPDF
from pathlib import Path
import glob

pdf = FPDF(orientation="P", unit="mm", format="A4")

filepaths = glob.glob("info_files/*.txt")
for filepath in filepaths:
    file_name = Path(filepath).stem.capitalize()

    pdf.add_page()

    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.set_text_color(0, 0, 50)
    pdf.set_font(family="Times", size=16, style="B")

    pdf.cell(w=0, h=12, txt=f"{file_name}", align="L", ln=1)

    with open(filepath, 'r') as file_local:
        animal_info = file_local.readlines()

    pdf.set_font(family="Times", size=10)
    pdf.multi_cell(w=0, h=8, txt=animal_info[0], align="L")

pdf.output("animals_info.pdf")
