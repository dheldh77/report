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
from .create_csv import MakeCSV
from django.utils import timezone

def home(request):
    return render(request, "home.html")
# Create your views here.

def search(request):
    # 각 속성값이 0이 아닌 value check
    fact_value = request.GET['fact']
    fact_line = request.GET['line']
    fact_maker = request.GET['maker']
    fact_model = request.GET['model']

    records = Record.objects.all()

    # 0이 아닌 속성만 필터링
    if fact_value != '0':
        records = records.filter(fact=fact_value)
    if fact_line != '0':
        records = records.filter(line=fact_line)
    if fact_maker != '0':
        records = records.filter(maker=fact_maker)
    if fact_model != '0':
        records = records.filter(model=fact_model)

    return render(request, "search.html", {'records' : records})

def list(request):
    records = Record.objects.all().order_by('-id')
    return render(request, "list.html", {'records' : records})

def input(request):
    # post 요청 시
    # pdf 추출
    if request.method == 'POST' and 'report' in request.POST:
        record = Record()
        record.fact = request.POST['fact']
        record.line = request.POST['line']
        record.date = timezone.now()
        record.maker = request.POST['maker']
        record.model = request.POST['model']
        record.part = request.POST['part']
        record.fault = request.POST['fault']
        record.cause = request.POST['cause']
        record.phenomenon = request.POST['phenomenon']
        record.measure = request.POST['measure']

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
        pdf_content = ("공 장 명 : " + record.fact + "<br/><br/>" + 
                        "공 정 명 : " + record.line + "<br/><br/>" + 
                        "날   짜 : " + str(record.date) + "<br/><br/>" + 
                        "Maker : " + record.maker + "<br/><br/>" +
                        "model : " + record.model + "<br/><br/>" +
                        "고장부분 : " + record.part + "<br/><br/>" +
                        "fault명 : " + record.fault + "<br/><br/>" +
                        "원   인 : " + record.cause + "<br/><br/>" +
                        "현   상 : " + record.phenomenon + "<br/><br/>" +
                        "조치내용 : " + record.measure + "<br/><br/>")
        para = Paragraph(pdf_content, styles["Title"])
        p = canvas.Canvas(buffer)

        # 이미지
        p.drawImage('./simple.jpg', x=0, y=height-100, width=width, height=100)
        
        #
        para.wrap(width, height)
        para.drawOn(p, 50, height/4)

        # 저장
        p.save()
        p.showPage()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='report.pdf')
    elif request.method == 'POST' and 'save' in request.POST:
        record = Record()
        record.fact = request.POST['fact']
        record.line = request.POST['line']
        record.date = timezone.now()
        record.maker = request.POST['maker']
        record.model = request.POST['model']
        record.part = request.POST['part']
        record.fault = request.POST['fault']
        record.cause = request.POST['cause']
        record.phenomenon = request.POST['phenomenon']
        record.measure = request.POST['measure']
        record.save()
        return redirect('list')
    # get 요청 시
    else:
        record = Record()
    return render(request, 'input.html', {'record':record})

def createCsv(request):
    records = Record.objects.all()
    list_records = []

    for record in records:
        record_dic = {}
        record_dic["fact"] = record.fact
        record_dic["line"] = record.line
        record_dic["date"] = record.date
        record_dic["maker"] = record.maker
        record_dic["model"] = record.model
        record_dic["part"] = record.part
        record_dic["fault"] = record.fault
        record_dic["cause"] = record.cause
        record_dic["phenomenon"] = record.phenomenon
        record_dic["measure"] = record.measure
        list_records.append(record_dic)
    
    MakeCSV(list_records)
    return redirect('list')

def graph(request):
    records = Record.objects.all().order_by('-id')
    # 전체 수
    total = 0

    # 전체 공장수
    fact_cnt = {"제선":0, "제강":0, "압연":0}

    for record in records:
        total += 1
        fact_cnt[record.fact] += 1


    return render(request, 'graph.html', {'fact_cnt' : fact_cnt})