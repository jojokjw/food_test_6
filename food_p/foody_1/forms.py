from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "显示名称" 
        self.fields["email"].label = "电子邮件地址"  

MOOD_CHOICES = [
    ('Happie', '开心'),
    ('Angrie', '生气'),
    ('Dehydratie', '脱水'),
    ('Depressie', '抑郁'),
    ('Excitie', '兴奋'),
    ('Unwellie', '不适'),
]

RESTAURANT_CHOICES = []

FOOD_CHOICES = []

class Feedback(forms.Form):
    Restaurant = forms.CharField(widget=forms.Select(choices=RESTAURANT_CHOICES), label='餐厅')  
    Food = forms.CharField(widget=forms.Select(choices=FOOD_CHOICES), label='菜品') 
    Mood = forms.CharField(label='今天感觉如何？', widget=forms.Select(choices=MOOD_CHOICES)) 
    Rating = forms.DecimalField(label='评分（满分5分）', max_value=5, min_value=0)  