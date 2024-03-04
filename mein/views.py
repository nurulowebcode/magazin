from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(['GET'])
def get_banner(request):
    banner = Banner.objects.all().order_by('-id')[:3]
    ser = BannerSer(banner, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_about(request):
    about = About.objects.all().order_by('-id')[:4]
    ser = AboutSer(about, many=True)
    return Response(ser.data)



@api_view(['GET'])
def get_servise(request):
    servise = Servise.objects.all().order_by('-id')[:4]
    ser = ServaseSer(servise, many=True)
    return Response(ser.data)



@api_view(['GET'])
def get_project(request):
    project = Project.objects.all().order_by('-id')[:4]
    ser = ProjectSer(project, many=True)
    return Response(ser.data)



@api_view(['GET'])
def get_ourtem(request):
    ourtem = Ourtem.objects.all().order_by('-id')[:4]
    ser = OurtemSer(ourtem, many=True)
    return Response(ser.data)



@api_view(['GET'])
def get_partyor(request):
    partyor = Partyor.objects.all().order_by('-id')[:4]
    ser = PartyorSer(partyor, many=True)
    return Response(ser.data)



@api_view(['GET'])
def get_info(request):
    info = Info.objects.all()
    ser = InfoSer(info, many=True)
    return Response(ser.data)



@api_view(['GET'])
def get_news(request):
    news = News.objects.all().order_by('-id')[:2]
    ser = NewsSer(news, many=True)
    return Response(ser.data)



@api_view(['POST'])
def get_contact(request):
    name = request.POST['name']
    text = request.POST['text']
    message = request.POST['message']
    contact = Contact.objects.create(
        name=name,
        text=text,
        message=message,
    )
    ser = ContactSer(contact, many=True)
    return Response(ser.data)















