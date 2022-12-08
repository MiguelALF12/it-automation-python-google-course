#!/usr/bin/env python3


from reportlab.platypus import SimpleDocTemplate
# Flowables
from reportlab.platypus import Paragraph, Table, Spacer, Image
# Style
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_report(attachment, title, paragraph):
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles["h1"])
    report_paragraph = Paragraph(paragraph, styles["BodyText"])
    report.build([report_title, report_paragraph])
