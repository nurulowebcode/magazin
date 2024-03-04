from rest_framework import serializers
from .models import *


class BannerSer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

class AboutSer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class ServaseSer(serializers.ModelSerializer):
    class Meta:
        model = Servise
        fields = "__all__"


class PartyorSer(serializers.ModelSerializer):
    class Meta:
        model = Partyor
        fields = "__all__"


class ProjectSer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ContactSer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class OurtemSer(serializers.ModelSerializer):
    class Meta:
        model = Ourtem
        fields = "__all__"


class NewsSer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class InfoSer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"





