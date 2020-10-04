import io

from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes


def write_cheat_sheet(name, username, password):
    bytez = io.BytesIO()
    url = 'https://workshop-server.qiime2.org/%s' % username

    c = canvas.Canvas(bytez, pagesize=pagesizes.letter)
    c.setFillColorRGB(1, 1, 1)

    row_1_y = 518
    row_2_y = 490
    col_1_x = 25
    col_2_x = 310
    col_3_x = 437

    c.drawString(col_1_x, row_1_y, name)
    c.drawString(col_1_x, row_2_y, url)
    c.drawString(col_2_x, row_1_y, username)
    c.drawString(col_3_x, row_2_y, password)

    c.save()

    bytez.seek(0)
    overlay = PdfFileReader(bytez)

    with open('sheet.pdf', 'rb') as fh_in:
        template = PdfFileReader(fh_in)

        output = PdfFileWriter()
        page = template.getPage(0)
        page.mergePage(overlay.getPage(0))
        output.addPage(page)

        with open('%s.pdf' % username, 'wb') as fh_out:
            output.write(fh_out)


if __name__ == '__main__':
    # TODO: read roster.csv (or some variant) and iterate
    write_cheat_sheet('Matthew Ryan Dillon', 'spicy-lobster', '1234567890')
