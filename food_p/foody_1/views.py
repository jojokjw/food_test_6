from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from .models import Restaurants,TrainingData,MoodData
import math
import numpy as np

class HomePage(TemplateView):
    template_name = "index.html"

def resultpage(request):
    form=forms.Feedback()
    if request.method=='POST':
        form=forms.Feedback(request.POST)
        if form.is_valid():
            a=form.cleaned_data['Restaurant']
            b=form.cleaned_data['Food']
            c=form.cleaned_data['Mood']
            d=form.cleaned_data['Rating']
            print(a)
            print(b)
            print(c)
            print(d)
            v=Restaurants.objects.filter(name=a).values_list()
            print(v[0])
            f=v[0][4]
            g=v[0][6]
            nv= ((f*g)+d)/(g+1)
            Restaurants.objects.filter(name=a).update(rating=nv)
            Restaurants.objects.filter(name=a).update(count=g+1)
        return render(request,'test.html',{'form':form})
    return render(request,'foody_1/result.html',{'form':form})

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "foody_1/signup.html"

class ConfusedView(TemplateView):
    template_name = "foody_1/Confused.html"

class Sichuan_cuisineView(TemplateView):
    template_name = "foody_1/Sichuan_cuisine.html"

class Cantonese_cuisineView(TemplateView):
    template_name = "foody_1/Cantonese_cuisine.html"

class Hunan_cuisineView(TemplateView):
    template_name = "foody_1/Hunan_cuisine.html"

class Su_cuisineView(TemplateView):
    template_name = "foody_1/Su_cuisine.html"

class Fujian_cuisineView(TemplateView):
    template_name = "foody_1/Fujian_cuisine.html"




# 定义处理广式石磨肠粉页面的视图函数
def Cantonese_cuisineCantonese_Stone_Ground_Rice_NoodlesView(request):
    # 从数据库中获取所有餐馆信息，提取需要的字段
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    # 从数据库中获取所有训练数据，提取需要的字段
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    # 将餐馆数据转为列表并初始化矩阵，用于存储提取的数据
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)# 初始化矩阵，49列对应数据字段数量
    # 遍历每个餐馆信息，将提取的字段值填入矩阵
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']
        # 提取菜品相关信息
        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']

    # 添加额外列用于存储距离计算值
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    # 设定参考点的经纬度，计算每个餐馆到该点的距离
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    # 处理训练数据，提取并存储为矩阵形式
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # 训练逻辑回归分类器
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    # 对测试数据进行预测，计算概率并附加到数据中
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    # 根据预测概率进行排序（降序）
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    # 映射餐馆名称到中文描述
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }
    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
        # 渲染HTML页面并返回结果
    return render(request,'foody_1/Cantonese_cuisineDishes/Cantonese_Stone_Ground_Rice_Noodles.html',{'result':result})



def Cantonese_cuisineHoney_Glazed_Roast_Pork_RiceView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }
    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Cantonese_cuisineDishes/Honey_Glazed_Roast_Pork_Rice.html',{'result':result})



def Cantonese_cuisineCrispy_Roast_Duck_RiceView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }
    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Cantonese_cuisineDishes/Crispy_Roast_Duck_Rice.html',{'result':result})





def Cantonese_cuisineBeef_Ball_NoodlesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }
    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Cantonese_cuisineDishes/Beef_Ball_Noodles.html',{'result':result})









def Cantonese_cuisineZhanjiang_Boiled_Chicken_RiceView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }
    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Cantonese_cuisineDishes/Zhanjiang_Boiled_Chicken_Rice.html',{'result':result})


def Cantonese_cuisineRose_Sauce_Chicken_RiceView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }
    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Cantonese_cuisineDishes/Rose_Sauce_Chicken_Rice.html',{'result':result})




def Cantonese_cuisineSalt_Baked_Chicken_Leg_RiceView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }
    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Cantonese_cuisineDishes/Salt_Baked_Chicken_Leg_Rice.html',{'result':result})





def Cantonese_cuisineSignature_Roast_Duck_RiceView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }
    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Cantonese_cuisineDishes/Signature_Roast_Duck_Rice.html',{'result':result})




def Cantonese_cuisineKung_Fu_Duck_Leg_RiceView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }
    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Cantonese_cuisineDishes/Kung_Fu_Duck_Leg_Rice.html',{'result':result})







def Cantonese_cuisineCrispy_Duck_Leg_RiceView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }
    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Cantonese_cuisineDishes/Crispy_Duck_Leg_Rice.html',{'result':result})









def Cantonese_cuisineSecret_Recipe_Chicken_Steak_RiceView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }
    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Cantonese_cuisineDishes/Secret_Recipe_Chicken_Steak_Rice.html',{'result':result})





























def Sichuan_cuisineSpicy_WontonView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }
    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Sichuan_cuisineDishes/Spicy_Wonton.html',{'result':result})








def Sichuan_cuisineChili_Chicken_NoodlesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Sichuan_cuisineDishes/Chili_Chicken_Noodles.html',{'result':result})


def Sichuan_cuisineSour_Cabbage_WontonView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Sichuan_cuisineDishes/Sour_Cabbage_Wonton.html',{'result':result})


def Sichuan_cuisineCumin_Beef_NoodlesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Sichuan_cuisineDishes/Cumin_Beef_Noodles.html',{'result':result})



def Sichuan_cuisineSour_Cabbage_Beef_NoodlesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Sichuan_cuisineDishes/Sour_Cabbage_Beef_Noodles.html',{'result':result})




def Sichuan_cuisineSichuan_Style_Spicy_Five_Grain_Fish_NoodlesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Sichuan_cuisineDishes/Sichuan_Style_Spicy_Five_Grain_Fish_Noodles.html',{'result':result})












def Hunan_cuisineSpicy_ShrimpView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Hunan_cuisineDishes/Spicy_Shrimp.html',{'result':result})



def Hunan_cuisineChili_ChickenView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Hunan_cuisineDishes/Chili_Chicken.html',{'result':result})




def Hunan_cuisineChili_Pepper_Fried_PorkView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Hunan_cuisineDishes/Chili_Pepper_Fried_Pork.html',{'result':result})



def Hunan_cuisineSalivating_ChickenView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Hunan_cuisineDishes/Salivating_Chicken.html',{'result':result})





def Hunan_cuisineHot_Dry_NoodlesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Hunan_cuisineDishes/Hot_Dry_Noodles.html',{'result':result})



def Hunan_cuisinePork_Mince_with_Eggplant_over_RiceView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Hunan_cuisineDishes/Pork_Mince_with_Eggplant_over_Rice.html',{'result':result})




def Hunan_cuisineSausage_Fried_with_Dried_RadishView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Hunan_cuisineDishes/Sausage_Fried_with_Dried_Radish.html',{'result':result})



def Hunan_cuisineGarlic_Fragrant_Chicken_SteakView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Hunan_cuisineDishes/Garlic_Fragrant_Chicken_Steak.html',{'result':result})



def Hunan_cuisineScallion_Oil_Mixed_NoodlesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Hunan_cuisineDishes/Scallion_Oil_Mixed_Noodles.html',{'result':result})



def Hunan_cuisineNanchang_Mixed_NoodlesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Hunan_cuisineDishes/Nanchang_Mixed_Noodles.html',{'result':result})








def Su_cuisineSeaweed_Braised_ChickenView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Su_cuisineDishes/Seaweed_Braised_Chicken.html',{'result':result})




def Su_cuisineCurry_Chicken_RiceView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Su_cuisineDishes/Curry_Chicken_Rice.html',{'result':result})




def Su_cuisineAuthentic_Beef_PattyView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Su_cuisineDishes/Authentic_Beef_Patty.html',{'result':result})




def Su_cuisineSignature_Chicken_Leg_RiceView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Su_cuisineDishes/Signature_Chicken_Leg_Rice.html',{'result':result})




def Su_cuisineSignature_Beggar_ChickenView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Su_cuisineDishes/Signature_Beggar_Chicken.html',{'result':result})



def Su_cuisineBlack_Pepper_Chicken_Steak_RiceView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Su_cuisineDishes/Black_Pepper_Chicken_Steak_Rice.html',{'result':result})




def Su_cuisineCurry_Chicken_with_Chicken_SteakView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Su_cuisineDishes/Curry_Chicken_with_Chicken_Steak.html',{'result':result})




def Fujian_cuisineChaoshan_Pork_Roll_RiceView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Fujian_cuisineDishes/Chaoshan_Pork_Roll_Rice.html',{'result':result})




def Fujian_cuisineChaoshan_Mixed_Rice_NoodlesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Fujian_cuisineDishes/Chaoshan_Mixed_Rice_Noodles.html',{'result':result})




def Fujian_cuisineLongjiang_Pork_Trotter_RiceView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Fujian_cuisineDishes/Longjiang_Pork_Trotter_Rice.html',{'result':result})



def Fujian_cuisinePork_Stew_RiceView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Fujian_cuisineDishes/Pork_Stew_Rice.html',{'result':result})




def Fujian_cuisineOriginal_Pork_Offal_NoodlesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Fujian_cuisineDishes/Original_Pork_Offal_Noodles.html',{'result':result})



def Fujian_cuisineOriginal_Seafood_Pork_Offal_NoodlesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Fujian_cuisineDishes/Original_Seafood_Pork_Offal_Noodles.html',{'result':result})



def Fujian_cuisineLemon_Flavored_Pork_Offal_NoodlesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Fujian_cuisineDishes/Lemon_Flavored_Pork_Offal_Noodles.html',{'result':result})



def Fujian_cuisineTomato_Flavored_Pork_Offal_NoodlesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost','count',
    'spicy_wonton','chili_chicken_noodles','sour_cabbage_wonton','cumin_beef_noodles','sour_cabbage_beef_noodles','sichuan_style_spicy_five_grain_fish_noodles','cantonese_stone_ground_rice_noodles',
    'honey_glazed_roast_pork_rice','crispy_roast_duck_rice','beef_ball_noodles','zhanjiang_boiled_chicken_rice','rose_sauce_chicken_rice','salt_baked_chicken_leg_rice','signature_roast_duck_rice',
    'kung_fu_duck_leg_rice','crispy_duck_leg_rice','secret_recipe_chicken_steak_rice',
    'spicy_shrimp','chili_chicken','chili_pepper_fried_pork','salivating_chicken','hot_dry_noodles',
    'pork_mince_with_eggplant_over_rice','sausage_fried_with_dried_radish','garlic_fragrant_chicken_steak','scallion_oil_mixed_noodles','nanchang_mixed_noodles',
    'seaweed_braised_chicken','curry_chicken_rice','authentic_beef_patty','signature_chicken_leg_rice','signature_beggar_chicken',
    'black_pepper_chicken_steak_rice','curry_chicken_with_chicken_steak','chaoshan_pork_roll_rice','chaoshan_mixed_rice_noodles','longjiang_pork_trotter_rice',
    'pork_stew_rice','original_pork_offal_noodles','original_seafood_pork_offal_noodles','lemon_flavored_pork_offal_noodles','tomato_flavored_pork_offal_noodles',)
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,49),np.int64)
    for i in range(n):
        restaurantslist[i][0] = temp3[i]['name']
        restaurantslist[i][1] = temp3[i]['latitude']
        restaurantslist[i][2] = temp3[i]['longitude']
        restaurantslist[i][3] = temp3[i]['rating']
        restaurantslist[i][4] = temp3[i]['cost']
        restaurantslist[i][5] = temp3[i]['count']

        restaurantslist[i][6] = temp3[i]['chili_chicken_noodles']
        restaurantslist[i][7] = temp3[i]['spicy_wonton']
        restaurantslist[i][8] = temp3[i]['sour_cabbage_wonton']
        restaurantslist[i][9] = temp3[i]['cumin_beef_noodles']
        restaurantslist[i][10] = temp3[i]['sour_cabbage_beef_noodles']
        restaurantslist[i][11] = temp3[i]['sichuan_style_spicy_five_grain_fish_noodles']
        restaurantslist[i][12] = temp3[i]['cantonese_stone_ground_rice_noodles']
        restaurantslist[i][13] = temp3[i]['honey_glazed_roast_pork_rice']
        restaurantslist[i][14] = temp3[i]['crispy_roast_duck_rice']
        restaurantslist[i][15] = temp3[i]['beef_ball_noodles']
        restaurantslist[i][16] = temp3[i]['zhanjiang_boiled_chicken_rice']
        restaurantslist[i][17] = temp3[i]['rose_sauce_chicken_rice']
        restaurantslist[i][18] = temp3[i]['salt_baked_chicken_leg_rice']
        restaurantslist[i][19] = temp3[i]['signature_roast_duck_rice']
        restaurantslist[i][20] = temp3[i]['kung_fu_duck_leg_rice']
        restaurantslist[i][21] = temp3[i]['crispy_duck_leg_rice']
        restaurantslist[i][22] = temp3[i]['secret_recipe_chicken_steak_rice']
        restaurantslist[i][24] = temp3[i]['spicy_shrimp']
        restaurantslist[i][25] = temp3[i]['chili_chicken']
        restaurantslist[i][26] = temp3[i]['chili_pepper_fried_pork']
        restaurantslist[i][27] = temp3[i]['salivating_chicken']
        restaurantslist[i][28] = temp3[i]['hot_dry_noodles']
        restaurantslist[i][29] = temp3[i]['pork_mince_with_eggplant_over_rice']
        restaurantslist[i][30] = temp3[i]['sausage_fried_with_dried_radish']
        restaurantslist[i][31] = temp3[i]['garlic_fragrant_chicken_steak']
        restaurantslist[i][32] = temp3[i]['scallion_oil_mixed_noodles']
        restaurantslist[i][33] = temp3[i]['nanchang_mixed_noodles']
        restaurantslist[i][34] = temp3[i]['seaweed_braised_chicken']
        restaurantslist[i][35] = temp3[i]['curry_chicken_rice']
        restaurantslist[i][36] = temp3[i]['authentic_beef_patty']
        restaurantslist[i][37] = temp3[i]['signature_chicken_leg_rice']
        restaurantslist[i][38] = temp3[i]['signature_beggar_chicken']
        restaurantslist[i][39] = temp3[i]['black_pepper_chicken_steak_rice']
        restaurantslist[i][40] = temp3[i]['curry_chicken_with_chicken_steak']
        restaurantslist[i][41] = temp3[i]['chaoshan_pork_roll_rice']
        restaurantslist[i][42] = temp3[i]['chaoshan_mixed_rice_noodles']
        restaurantslist[i][43] = temp3[i]['longjiang_pork_trotter_rice']
        restaurantslist[i][44] = temp3[i]['pork_stew_rice']
        restaurantslist[i][45] = temp3[i]['original_pork_offal_noodles']
        restaurantslist[i][46] = temp3[i]['original_seafood_pork_offal_noodles']
        restaurantslist[i][47] = temp3[i]['lemon_flavored_pork_offal_noodles']
        restaurantslist[i][48] = temp3[i]['tomato_flavored_pork_offal_noodles']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][49]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,50),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,49]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][51] > info[j+1][51] :
                temp=np.zeros(52,np.int64)
                for k in range(52):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly = {
        1: '江西粉面',
        2: '金源香粉面',
        3: '兰州牛肉面',
        4: '五谷鱼粉',
        5: '广式石磨肠粉',
        6: '肥仔烧腊',
        7: '湘味小炒',
        8: '金源香盖浇饭',
        9: '万有引力叫花鸡',
        10: '港式烧腊',
        11: '潮汕正宗粿条汤'
    }

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/Fujian_cuisineDishes/Tomato_Flavored_Pork_Offal_Noodles.html',{'result':result})








































def HappyView(request):
    trainingdata = MoodData.objects.all().values('Dish', 'happie')
    info = sorted(trainingdata, key=lambda x: x['happie'])  # 直接按 'happie' 字段排序
    result = ['Cantonese_Stone_Ground_Rice_Noodles', 'Honey_Glazed_Roast_Pork_Rice']
    for item in info[:len(info)]:
        result.append(item['Dish'])  # 将排序后的菜品加入结果
    return render(request, 'foody_1/moods/happie.html', {'result': result})


def AngryView(request):
    trainingdata = MoodData.objects.all().values('Dish', 'angrie')
    info = list(trainingdata)
    info = sorted(info, key=lambda x: x['angrie'], reverse=True)
    result = ['Cantonese_Stone_Ground_Rice_Noodles', 'Cantonese_Stone_Ground_Rice_Noodles']
    result.extend(item['Dish'] for item in info)
    return render(request, 'foody_1/moods/angrie.html', {'result': result})





def DepressiveView(request):
    trainingdata=MoodData.objects.all().values('Dish','depressie')
    info=list(trainingdata)
    info = sorted(info, key=lambda x: x['depressie'], reverse=True)
    result = ['Cantonese_Stone_Ground_Rice_Noodles', 'Cantonese_Stone_Ground_Rice_Noodles']
    result.extend(item['Dish'] for item in info)
    return render(request, 'foody_1/moods/depressive.html', {'result': result})


def ExciteView(request):
    trainingdata=MoodData.objects.all().values('Dish','excitie')
    info=list(trainingdata)
    info = sorted(info, key=lambda x: x['excitie'], reverse=True)
    result = ['Cantonese_Stone_Ground_Rice_Noodles', 'Cantonese_Stone_Ground_Rice_Noodles']
    result.extend(item['Dish'] for item in info)
    return render(request, 'foody_1/moods/excite.html', {'result': result})


def UnwellView(request):
    trainingdata=MoodData.objects.all().values('Dish','unwellie')
    info=list(trainingdata)
    info = sorted(info, key=lambda x: x['unwellie'], reverse=True)
    result = ['Cantonese_Stone_Ground_Rice_Noodles', 'Cantonese_Stone_Ground_Rice_Noodles']
    result.extend(item['Dish'] for item in info)
    return render(request, 'foody_1/moods/unwellie.html', {'result': result})



def SearchedView(request):
    trainingdata=MoodData.objects.all().values('Dish','happie','angrie','dehydratie','depressie','excitie','unwellie')
    info=list(trainingdata)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j]['unwellie'] > info[j+1]['unwellie'] :
                temp=np.zeros(7,np.int64)
                for k in range(7):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=['Cantonese_Stone_Ground_Rice_Noodles', 'Cantonese_Stone_Ground_Rice_Noodles']
    m=0
    if(m<n):
        m=n
    for i in range(m):
        result=np.append(result,info[i]['Dish'])
    return render(request,'foody_1/moods/searched.html',{'result':result})
# def index1(request):
#     trainingdata=MoodData.objects.all().values('dish','depressed','happy','sick','dehydrated','dizziness')
#     trainingdatalist=list(trainingdata)
#     n = len(info)
#     for i in range(n-1):
#         for j in range(n-1):
#             if info[j][1] > info[j+1][1] :
#                 temp=np.zeros(6,np.int64)
#                 for k in range(6):
#                     temp[k]=info[j][k]
#                 info[j]=info[j+1]
#                 info[j+1]=temp
#     return render(request,'myapp/index.html',{'form':form ,'result':result})
