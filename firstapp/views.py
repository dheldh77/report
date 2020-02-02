from django.shortcuts import render, redirect
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .models import Record
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

def home(request):
    return render(request, "home.html")
# Create your views here.

def input(request):
    # post 요청 시
    # pdf 추출
    if request.method == 'POST' and 'report' in request.POST:
        record = Record()
        record.tmp1 = request.POST['tmp1']
        record.tmp2 = request.POST['tmp2']
        record.tmp3 = request.POST['tmp3']
        record.tmp4 = request.POST['tmp4']
        record.tmp5 = request.POST['tmp5']
        # 버퍼 만들고 스타일 저장
        buffer = io.BytesIO()
        font_file = './NanumMyeongjo-YetHangul.ttf'
        symbola_font = TTFont('Symbola', font_file)
        pdfmetrics.registerFont(symbola_font)
        width, height = defaultPageSize
        styles = getSampleStyleSheet()
        styles["Title"].fontName = 'Symbola'
        styles["Title"].alignment = 0

        # 내용 쓰기
        pdf_content = "공장명 : " + record.tmp1 + "<br/><br/>" + "공정명 : " + record.tmp2 + "<br/><br/>" + "날짜 : " + record.tmp3 + "<br/><br/>" + "원인 : " + record.tmp4 + "<br/><br/>" + "현상 : " + record.tmp5
        para = Paragraph(pdf_content, styles["Title"])
        p = canvas.Canvas(buffer)

        # 이미지
        p.drawImage('./simple.jpg', x=0, y=height-100, width=width, height=100)
        
        #
        para.wrap(width, height)
        para.drawOn(p, 50, height/2)

        # 저장
        p.save()
        p.showPage()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='report.pdf')
    elif request.method == 'POST' and 'save' in request.POST:
        record = Record()
        record.tmp1 = request.POST['tmp1']
        record.tmp2 = request.POST['tmp2']
        record.tmp3 = request.POST['tmp3']
        record.tmp4 = request.POST['tmp4']
        record.tmp5 = request.POST['tmp5']
        record.save()
        return redirect('home')
    # get 요청 시
    else:
        record = Record()
    return render(request, 'input.html', {'record':record})



def create(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    

    first = request.GET('first_name')
    last = request.GET('last_name')
    pw = request.GET('password')
    email = request.GET('email')

    text = first + '\n' + last + '\n' + pw + '\n' + email

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, text)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
