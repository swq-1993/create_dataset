import random
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Calibri', './ttf/Calibri_Light.ttf'))
pdfmetrics.registerFont(TTFont('pinyin', './ttf/pinyin.ttf'))
pdfmetrics.registerFont(TTFont('simsun', './ttf/simsun.ttf'))
pdfmetrics.registerFont(TTFont('yuanti', './ttf/yuanti.ttf'))

pinyin_file = "pinyin_op.txt"
row_gap = 0.5
col_gap = 1

pinyins = []
with open(pinyin_file, 'r') as f:
    for line in f:
        line = line.strip('\n')
        pinyins.append(line)
f.close()

random.shuffle(pinyins)

out_label = "label_pinyin.txt"
count = 1
tmp = ""
row = 1
with open(out_label, 'w') as f:
    for word in pinyins:
        word = word.strip()
        tmp = tmp + word.ljust(15)
        if count % 160 is 1:
            f.write("@" + str((count / 160 + 1)).zfill(3) + '\n')
        if count % 8 is 0:
            print tmp + '\n'
            f.write(tmp + '\n')
            row = row + 1
            tmp = ""
        count = count + 1
    if tmp is not "":
        f.write(tmp + '\n')
f.close()


out_pdf = "pinyin_popular_four.pdf"
c = canvas.Canvas(out_pdf)
textobject = c.beginText()
textobject.setFont('pinyin', size=10)

count = 0
page = 1
while count < len(pinyins):
    textobject = c.beginText()
    str_page = str(page)
    textobject.setTextOrigin(0.25 * inch, 11.25 * inch)
    textobject.textLines("Date: 20181115 Task: 54001 Page: " + str_page.zfill(3))
    textobject.setFont('pinyin', size=14)
    for i in range(20):
        for j in range(8):
            if count < len(pinyins):
                textobject.setTextOrigin(inch * (0.4 + j * col_gap), (10.5 - row_gap * i) * inch)
                textobject.textLines(pinyins[count].strip())
                count = count + 1
    page = page + 1
    c.drawText(textobject)
    c.showPage()
c.save()

out_pdf = "pinyin_popular_two.pdf"
c = canvas.Canvas(out_pdf)
textobject = c.beginText()
textobject.setFont('pinyin', size=10)

count = 0
page = 1
while count < len(pinyins):
    textobject = c.beginText()
    str_page = str(page)
    textobject.setTextOrigin(0.25 * inch, 11.25 * inch)
    textobject.textLines("Date: 20181115 Task: 54002 Page: " + str_page.zfill(3))
    textobject.setFont('pinyin', size=18)
    for i in range(20):
        for j in range(8):
            if count < len(pinyins):
                textobject.setTextOrigin(inch * (0.4 + j * col_gap), (10.5 - row_gap * i) * inch)
                textobject.textLines(pinyins[count].strip())
                count = count + 1
    page = page + 1
    c.drawText(textobject)
    c.showPage()
c.save()

out_pdf = "pinyin_calibri.pdf"
c = canvas.Canvas(out_pdf)
textobject = c.beginText()
textobject.setFont('Calibri', size=10)

count = 0
page = 1
while count < len(pinyins):
    textobject = c.beginText()
    str_page = str(page)
    textobject.setTextOrigin(0.25 * inch, 11.25 * inch)
    textobject.textLines("Date: 20181115 Task: 54003 Page: " + str_page.zfill(3))
    textobject.setFont('Calibri', size=14)
    for i in range(20):
        for j in range(8):
            if count < len(pinyins):
                textobject.setTextOrigin(inch * (0.4 + j * col_gap), (10.5 - row_gap * i) * inch)
                textobject.textLines(pinyins[count].strip())
                count = count + 1
    page = page + 1
    c.drawText(textobject)
    c.showPage()
c.save()

out_pdf = "pinyin_simsun.pdf"
c = canvas.Canvas(out_pdf)
textobject = c.beginText()
textobject.setFont('simsun', size=10)

count = 0
page = 1
while count < len(pinyins):
    textobject = c.beginText()
    str_page = str(page)
    textobject.setTextOrigin(0.25 * inch, 11.25 * inch)
    textobject.textLines("Date: 20181115 Task: 54004 Page: " + str_page.zfill(3))
    textobject.setFont('simsun', size=14)
    for i in range(20):
        for j in range(8):
            if count < len(pinyins):
                textobject.setTextOrigin(inch * (0.4 + j * col_gap), (10.5 - row_gap * i) * inch)
                textobject.textLines(pinyins[count].strip())
                count = count + 1
    page = page + 1
    c.drawText(textobject)
    c.showPage()
c.save()


out_pdf = "pinyin_yuanti.pdf"
c = canvas.Canvas(out_pdf)
textobject = c.beginText()
textobject.setFont('yuanti', size=10)

count = 0
page = 1
while count < len(pinyins):
    textobject = c.beginText()
    str_page = str(page)
    textobject.setTextOrigin(0.25 * inch, 11.25 * inch)
    textobject.textLines("Date: 20181115 Task: 54005 Page: " + str_page.zfill(3))
    textobject.setFont('yuanti', size=14)
    for i in range(20):
        for j in range(8):
            if count < len(pinyins):
                textobject.setTextOrigin(inch * (0.4 + j * col_gap), (10.5 - row_gap * i) * inch)
                textobject.textLines(pinyins[count].strip())
                count = count + 1
    page = page + 1
    c.drawText(textobject)
    c.showPage()
c.save()
print "finished"

