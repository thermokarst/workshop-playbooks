import csv
import io
import os
import sys

import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes


def write_cheat_sheet(base_template, name, username, password, output_dir):
    bytez = io.BytesIO()
    url = 'https://workshop-server.qiime2.org/%s' % username
    out_fn = os.path.join(output_dir, '%s.pdf' % username)

    c = canvas.Canvas(bytez, pagesize=pagesizes.A4)
    c.setFillColorRGB(1, 1, 1)

    # You will need to update these, if the layout changes
    row_1_y, row_2_y = 518, 490
    col_1_x, col_2_x = 23, 370

    # Write out the dynamic content
    c.drawString(col_1_x, row_1_y, name)
    c.drawString(col_1_x, row_2_y, url)
    c.drawString(col_2_x, row_1_y, username)
    c.drawString(col_2_x, row_2_y, password)

    c.save()

    bytez.seek(0)
    overlay = PyPDF2.PdfFileReader(bytez)

    with open(base_template, 'rb') as fh_in, open(out_fn, 'wb') as fh_out:
        template = PyPDF2.PdfFileReader(fh_in)
        output_pdf = PyPDF2.PdfFileWriter()
        page = template.getPage(0)
        page.mergePage(overlay.getPage(0))
        output_pdf.addPage(page)
        output_pdf.write(fh_out)


if __name__ == '__main__':
    base_template = sys.argv[1]
    roster = sys.argv[2]
    output_dir = sys.argv[3]
    os.mkdir(output_dir)
    # Name, Email, Cohort, Username, Password, + extra columns
    with open(roster) as fh:
        reader = csv.reader(fh, delimiter=',')
        next(reader)  # skip first row
        for row in reader:
            name, username, password = row[0], row[2], row[3]
            print('writing `%s` `%s` `%s`' % (name, username, password))
            write_cheat_sheet(base_template, name, username, password, output_dir)
