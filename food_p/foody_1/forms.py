from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "显示名称"  # 修改label
        self.fields["email"].label = "电子邮件地址"  # 修改label

MOOD_CHOICES = [
    ('Happie', '开心'),
    ('Angrie', '生气'),
    ('Dehydratie', '脱水'),
    ('Depressie', '抑郁'),
    ('Excitie', '兴奋'),
    ('Unwellie', '不适'),
]

RESTAURANT_CHOICES = [
   (1, '江西粉面'), (2, '金源香粉面'), (3, '兰州牛肉面'), (4, '五谷鱼粉'), (5, '广式石磨肠粉'),
   (6, '肥仔烧腊'), (7, '湘味小炒'), (8, '金源香盖浇饭'), (9, '湘味小炒'), (10, '万有引力叫花鸡'), (11, '港式烧腊'),(12, '潮汕正宗粿条汤'),
]

FOOD_CHOICES = [
    (1, '辣子鸡面'), (2, '麻辣抄手'), (3, '酸菜抄手'), (4, '孜然牛肉盖面'), (5, '酸菜牛肉面'), (6, '川香麻辣口味五谷鱼粉'),
    (7, '广式石磨肠粉'), (8, '蜜汁叉烧饭'), (9, '脆皮烧鸭饭'), (10, '牛筋丸面'), (11, '湛江白切鸡饭'),
    (12, '玫瑰豉油鸡饭'), (13, '盐焗鸡腿饭'), (14, '招牌烧鸭饭'), (15, '功夫鸭腿饭'), (16, '脆皮鸭腿饭'), (17, '秘制鸡排饭'), (18, '香辣虾'),
    (19, '辣子鸡'), (20, '辣椒炒肉'), (21, '口水鸡'), (22, '热干面'), (23, '肉沫茄子盖饭'), (24, '腊肠炒萝卜干'),
    (25, '蒜香鸡排'), (26, '葱油拌面'), (27, '南昌拌面'), (28, '南昌拌面'), (29, '海苔碎焖鸡'),
    (30, '咖喱鸡饭'), (31, '正点牛肉饼'), (32, '招牌鸡腿饭'), (33, '招牌叫花鸡'), (34, '黑椒鸡扒饭'), (35, '咖喱鸡拼鸡扒'), (36, '潮汕肉卷饭'),
(37, '潮汕拌粿条'), (38, '隆江猪脚饭'), (39, '卤肉饭'), (40, '原味猪杂面'), (41, '原味海鲜猪杂面'), (42, '柠檬味猪杂面'),
   (43, '番茄味猪杂面'),
]

class Feedback(forms.Form):
    Restaurant = forms.CharField(widget=forms.Select(choices=RESTAURANT_CHOICES), label='餐厅')  # 修改label
    Food = forms.CharField(widget=forms.Select(choices=FOOD_CHOICES), label='菜品')  # 修改label
    Mood = forms.CharField(label='今天感觉如何？', widget=forms.Select(choices=MOOD_CHOICES))  # 修改label
    Rating = forms.DecimalField(label='评分（满分5分）', max_value=5, min_value=0)  # 修改label