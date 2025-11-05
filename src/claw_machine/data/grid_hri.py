import svgwrite
from svgwrite import cm, mm
from reportlab.lib.pagesizes import A2

# Get A3 page size in points (1 pt = 1/72 inch)
width_pt, height_pt = A2
# Convert to millimeters for svgwrite (1 inch = 25.4 mm)
width_mm = width_pt * 25.4 / 72
height_mm = height_pt * 25.4 / 72

print(width_mm, height_mm)

# Create SVG canvas
dwg = svgwrite.Drawing("3x3cm_grid_A2.svg", size=(f"{width_mm}mm", f"{height_mm}mm"))

# Box size in mm
box_size = 30  # 3 cm = 30 mm

# Draw vertical lines
x = box_size
while x <= width_mm - box_size:
    dwg.add(dwg.line(start=(f"{x}mm", f"{box_size}mm"), end=(f"{x}mm", f"{height_mm - box_size}mm"), stroke='black', stroke_width=0.5))
    x += box_size


# Draw horizontal lines
y = box_size
while y <= height_mm - box_size:
    dwg.add(dwg.line(start=(f"{box_size}mm", f"{y}mm"), end=(f"{width_mm - box_size}mm", f"{y}mm"), stroke='black', stroke_width=0.5))
    y += box_size

# Optional border
dwg.add(dwg.rect(insert=(f"{box_size}mm", f"{box_size}mm"), size=(f"{width_mm - 2*box_size}mm", f"{height_mm - 2*box_size}mm"),
                 fill='none', stroke='black', stroke_width=10))

dwg.save()

print("✅ Vector grid saved as '3x3cm_grid_A2.svg'")


import cairosvg

# Convert SVG file to PDF
cairosvg.svg2pdf(url="3x3cm_grid_A2.svg", write_to="3x3cm_grid_A2.pdf")
print("✅ PDF saved as '3x3cm_grid_A2.pdf'")
