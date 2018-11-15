#!/usr/bin/python
# -*- coding: UTF-8 -*-

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
c = canvas.Canvas("template.pdf")
# for size in range(12, 36, 4):
#     c.drawString(10+size*2, 10+size*2, 'Hello World')
file_name = "origin_eng.txt"
words = []
count = 1
with open(file_name, 'r') as f:
    for line in f:
        if count % 3 is 2:
            # print line
            words.append(line)
        count = count + 1
f.close()

textobject = c.beginText()
# textobject.setTextOrigin(inch, 11 * inch)
textobject.setFont('Calibri', size=10)


count = 0
page = 1
while count < len(words):
    textobject = c.beginText()
    # textobject.setTextOrigin(inch, 11 * inch)
    str_page = str(page)
    textobject.setTextOrigin(0.25 * inch, 11.5 * inch)
    textobject.textLines("Date: 20181115 Task: 53001 Page: " + str_page.zfill(3))
    textobject.setFont('Calibri', size=14)
    for i in range(20):
        for j in range(6):
            if count < len(words):
                textobject.setTextOrigin(inch * (0.4 + j * 1.3), (10.5 - 0.5 * i) * inch)
                textobject.textLines(words[count].strip())
                count = count + 1

    page = page + 1
    c.drawText(textobject)
    c.showPage()

# count = 84
# for i in range(14):
#     for j in range(6):
#         textobject.setTextOrigin(inch * (0.5 + j * 1.3), (10 - 0.7 * i) * inch)
#         textobject.textLines(words[count].strip())
#         count = count + 1
#
# c.drawText(textobject)
# c.showPage()
c.save()
print "finished"
