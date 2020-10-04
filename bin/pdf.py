import io

import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes


def write_cheat_sheet(name, username, password):
    bytez = io.BytesIO()
    url = 'https://workshop-server.qiime2.org/%s' % username
    out_fn = '%s.pdf' % username

    c = canvas.Canvas(bytez, pagesize=pagesizes.A4)
    c.setFillColorRGB(1, 1, 1)

    # You will need to update these, if the layout changes
    row_1_y, row_2_y = 518, 490
    col_1_x, col_2_x, col_3_x = 25, 310, 437

    # Write out the dynamic content
    c.drawString(col_1_x, row_1_y, name)
    c.drawString(col_1_x, row_2_y, url)
    c.drawString(col_2_x, row_1_y, username)
    c.drawString(col_3_x, row_2_y, password)

    c.save()

    bytez.seek(0)
    overlay = PyPDF2.PdfFileReader(bytez)

    with open('sheet.pdf', 'rb') as fh_in, open(out_fn, 'wb') as fh_out:
        template = PyPDF2.PdfFileReader(fh_in)
        output_pdf = PyPDF2.PdfFileWriter()
        page = template.getPage(0)
        page.mergePage(overlay.getPage(0))
        output_pdf.addPage(page)
        output_pdf.write(fh_out)


if __name__ == '__main__':
    # TODO: read roster.csv (or some variant) and iterate
    # TODO: read in base template argv
    write_cheat_sheet('Matthew Ryan Dillon', 'spicy-lobster', '1234567890')
