from django import forms
from .models import Post,PostOBD,PostCar
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("site","contact","capacity","location","mapped","status","description")


class OBDForm(forms.ModelForm):
    class Meta:
        model=PostOBD
        fields=("tag_model","tag_name","tag_mapped","car_asset","site","location","status","description")

class CarForm(forms.ModelForm):
    class Meta:
        model=PostCar
        fields=("car_model","car_brand","site","location","tag_mapped","status","tag_model","demo_model","alerts_time","description")
