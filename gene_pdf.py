#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import subprocess
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
# pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, LongTable, TableStyle, tableofcontents, PageBreak


from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Calibri', './ttf/Calibri_Light.ttf'))
pdfmetrics.registerFont(TTFont('Arial', './ttf/Arial.ttf'))
pdfmetrics.registerFont(TTFont('Tahoma', './ttf/tahoma.ttf'))

row_gap = 0.5
col_gap = 1.55

def disk_report():                # 查看磁盘空间使用量
    p=subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE)
    return p.stdout.readlines()




def create_pdf(input, output="disk_report.pdf"):   # 创建PDF文件
    now = datetime.datetime.today()
    date = now.strftime("%h %d %Y %H:%M:%S")
    c=canvas.Canvas(output)
    textobject = c.beginText()
    textobject.setTextOrigin(inch, 11*inch)
    textobject.textLines('''
    Disk Capacity Report: %s
    ''' % date)

    for line in input:
        textobject.textLine(line.strip())
    c.drawText(textobject)
    c.showPage()
    c.save()

# report=disk_report()
# create_pdf(report)

def footer(canvas, doc):
    """
    设置页脚
    :param canvas:Canvas类型  pdf画布
    :param doc:doc类型   整个pdf文件
    """
    canvas.saveState()                                                                                    #先保存当前的画布状态
    pageNumber = ("%s" %canvas.getPageNumber())                                                           #获取当前的页码
    p = Paragraph(pageNumber, styleN)
    w, h = p.wrap(1*cm, 1*cm)                                                                             #申请一块1cm大小的空间，返回值是实际使用的空间
    p.drawOn(canvas, foot_coordinate_x, foot_coordinate_y)                                                #将页码放在指示坐标处
    canvas.restoreState()


def header(canvas, doc):
    """
    设置页眉
    :param canvas:Canvas类型  pdf画布
    :param doc:doc类型     整个pdf文件
    """
    canvas.saveState()
    p = Paragraph("<img src='%s' width='%d' height='%d'/>" %(img_address, header_img_width, header_img_height), styleN)
    w, h = p.wrap(doc.width, doc.bottomMargin)
    p.drawOn(canvas, doc.leftMargin, doc.topMargin + doc.height - 0.5*cm)
    p = Paragraph("<font size=10 face='STSong-Light'>报告</font>", styleN)
    w,h = p.wrap(doc.width, doc.bottomMargin)
    p.drawOn(canvas, doc.leftMargin+doc.width-2.2*cm, doc.topMargin+ doc.height-0.3*cm)
    canvas.line(doc.leftMargin, doc.bottomMargin+doc.height + 0.5*cm, doc.leftMargin+doc.width, doc.bottomMargin+doc.height + 0.5*cm)
    canvas.restoreState()


# from reportlab.lib.styles import getSampleStyleSheet
# stylesheet=getSampleStyleSheet()
# normalStyle = stylesheet['Normal']
#
# doc = BaseDocTemplate("template.pdf", topMargin=3.5 * cm)
# frame_footer = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
# template = PageTemplate(id='test', frames=frame_footer, onPage=header, onPageEnd=footer)
# doc.addPageTemplates([template])

# text = ['a']
# doc.build(text)

# d = Drawing(400, 200)

file_name = "origin_eng.txt"
words = []
count = 1
# with open(file_name, 'r') as f:
#     for line in f:
#         if count % 3 is 2:
#             # print line
#             words.append(line)
#         count = count + 1
# f.close()
eng_all_file = "eng_all.txt"
with open(eng_all_file, 'r') as f:
    for line in f:
        line = line.strip('\n')
        words.append(line)
f.close()
while '' in words:
    words.remove('')

random.shuffle(words)

count = 1
tmp = ""
row = 1
out_lable = 'label.txt'
with open(out_lable, 'w') as f:
    for word in words:
        word = word.strip('\n')
        tmp = tmp + word.ljust(18)
        if count % 100 is 1:
            f.write("@" + str((count / 100 + 1)).zfill(3) + '\n')
        if count % 5 is 0:
            print tmp + '\n'
            f.write(tmp + '\n')
            row = row + 1
            tmp = ""
        count = count + 1
f.close()


out_pdf = "eng_word_Calibri.pdf"
c = canvas.Canvas(out_pdf)
textobject = c.beginText()
# textobject.setTextOrigin(inch, 11 * inch)
textobject.setFont('Calibri', size=10)


count = 0
page = 1
while count < len(words):
    textobject = c.beginText()
    # textobject.setTextOrigin(inch, 11 * inch)
    str_page = str(page)
    textobject.setTextOrigin(0.25 * inch, 11.25 * inch)
    textobject.textLines("Date: 20181115 Task: 53002 Page: " + str_page.zfill(3))
    textobject.setFont('Calibri', size=14)
    for i in range(20):
        for j in range(5):
            if count < len(words):
                textobject.setTextOrigin(inch * (0.4 + j * col_gap), (10.5 - row_gap * i) * inch)
                textobject.textLines(words[count].strip())
                count = count + 1

    page = page + 1
    c.drawText(textobject)
    c.showPage()

c.save()


out_pdf = "eng_word_Arial.pdf"
c = canvas.Canvas(out_pdf)
textobject = c.beginText()
# textobject.setTextOrigin(inch, 11 * inch)
textobject.setFont('Arial', size=10)


count = 0
page = 1
while count < len(words):
    textobject = c.beginText()
    # textobject.setTextOrigin(inch, 11 * inch)
    str_page = str(page)
    textobject.setTextOrigin(0.25 * inch, 11.25 * inch)
    textobject.textLines("Date: 20181115 Task: 53001 Page: " + str_page.zfill(3))
    textobject.setFont('Arial', size=14)
    for i in range(20):
        for j in range(5):
            if count < len(words):
                textobject.setTextOrigin(inch * (0.4 + j * col_gap), (10.5 - row_gap * i) * inch)
                textobject.textLines(words[count].strip())
                count = count + 1

    page = page + 1
    c.drawText(textobject)
    c.showPage()

c.save()



out_pdf = "eng_word_Tahoma.pdf"
c = canvas.Canvas(out_pdf)
textobject = c.beginText()
# textobject.setTextOrigin(inch, 11 * inch)
textobject.setFont('Tahoma', size=10)


count = 0
page = 1
while count < len(words):
    textobject = c.beginText()
    # textobject.setTextOrigin(inch, 11 * inch)
    str_page = str(page)
    textobject.setTextOrigin(0.25 * inch, 11.25 * inch)
    textobject.textLines("Date: 20181115 Task: 53003 Page: " + str_page.zfill(3))
    textobject.setFont('Tahoma', size=14)
    for i in range(20):
        for j in range(5):
            if count < len(words):
                textobject.setTextOrigin(inch * (0.4 + j * col_gap), (10.5 - row_gap * i) * inch)
                textobject.textLines(words[count].strip())
                count = count + 1

    page = page + 1
    c.drawText(textobject)
    c.showPage()

c.save()

out_pdf = "eng_word_Times_Roman.pdf"
c = canvas.Canvas(out_pdf)
textobject = c.beginText()
# textobject.setTextOrigin(inch, 11 * inch)
textobject.setFont('Times-Roman', size=10)


count = 0
page = 1
while count < len(words):
    textobject = c.beginText()
    # textobject.setTextOrigin(inch, 11 * inch)
    str_page = str(page)
    textobject.setTextOrigin(0.25 * inch, 11.25 * inch)
    textobject.textLines("Date: 20181115 Task: 53004 Page: " + str_page.zfill(3))
    textobject.setFont('Times-Roman', size=14)
    for i in range(20):
        for j in range(5):
            if count < len(words):
                textobject.setTextOrigin(inch * (0.4 + j * col_gap), (10.5 - row_gap * i) * inch)
                textobject.textLines(words[count].strip())
                count = count + 1

    page = page + 1
    c.drawText(textobject)
    c.showPage()

c.save()
print "finished"
