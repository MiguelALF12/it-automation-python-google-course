from reportlab.platypus import SimpleDocTemplate
# Flowables
from reportlab.platypus import Paragraph, Table
# Style
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
# Graphics
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}

report = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

# ---- Adding tables
table_data = []
for k, v in fruit.items():
    table_data.append([k, v])

table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]
report_table = Table(data=table_data)  # This always receives a list of lists
report_table.setStyle(table_style)
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

# ---- Adding graphics
report_pie = Pie(width=3 * 10, height=3 * 10)

report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

report_chart = Drawing()  # We use Drawing because pie is not a flowable.
report_chart.add(report_pie)

report.build([report_title, report_table, report_chart])
