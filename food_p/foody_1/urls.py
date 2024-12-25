from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'foody_1'

urlpatterns = [
    url(r"^login/$", auth_views.LoginView.as_view(template_name="foody_1/login.html"),name='login'),

    url(r"^confused/$", views.ConfusedView.as_view(), name="confused"),
    url(r"^logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"^signup/$", views.SignUp.as_view(), name="signup"),
    url(r"^result/$", views.resultpage, name="result"),

    url(r"^sichuan_cuisine/$", views.Sichuan_cuisineView.as_view(), name="sichuan_cuisine"),
    url(r"^cantonese_cuisine/$", views.Cantonese_cuisineView.as_view(), name="cantonese_cuisine"),
    url(r"^hunan_cuisine/$", views.Hunan_cuisineView.as_view(), name="hunan_cuisine"),
    url(r"^su_cuisine/$", views.Su_cuisineView.as_view(), name="su_cuisine"),
    url(r"^fujian_cuisine/$", views.Fujian_cuisineView.as_view(), name="fujian_cuisine"),

    url(r"^confused/happy/$", views.HappyView, name="happy"),
    url(r"^confused/angry/$", views.AngryView, name="angry"),
    url(r"^confused/depress/$", views.DepressiveView, name="depress"),
    url(r"^confused/excite/$", views.ExciteView, name="excite"),
    url(r"^confused/unwell/$", views.UnwellView, name="unwell"),
    url(r"^confused/searched/$", views.SearchedView, name="searched"),


    url(r"^sichuan_cuisine/spicy_wonton/$", views.Sichuan_cuisineSpicy_WontonView, name="spicy_wonton"),
    url(r"^sichuan_cuisine/chili_chicken_noodles/$", views.Sichuan_cuisineChili_Chicken_NoodlesView, name="chili_chicken_noodles"),
    url(r"^sichuan_cuisine/sour_cabbage_wonton/$", views.Sichuan_cuisineSour_Cabbage_WontonView, name="sour_cabbage_wonton"),
    url(r"^sichuan_cuisine/cumin_beef_noodles/$", views.Sichuan_cuisineCumin_Beef_NoodlesView, name="cumin_beef_noodles"),
    url(r"^sichuan_cuisine/sour_cabbage_beef_noodles/$", views.Sichuan_cuisineSour_Cabbage_Beef_NoodlesView, name="sour_cabbage_beef_noodles"),
    url(r"^sichuan_cuisine/sichuan_style_spicy_five_grain_fish_noodle/$", views.Sichuan_cuisineSichuan_Style_Spicy_Five_Grain_Fish_NoodlesView, name="sichuan_style_spicy_five_grain_fish_noodle"),

    url(r"^cantonese_cuisine/cantonese_stone_ground_rice_noodles/$", views.Cantonese_cuisineCantonese_Stone_Ground_Rice_NoodlesView, name="cantonese_stone_ground_rice_noodles"),
    url(r"^cantonese_cuisine/honey_glazed_roast_pork_rice/$", views.Cantonese_cuisineHoney_Glazed_Roast_Pork_RiceView, name="honey_glazed_roast_pork_rice"),
    url(r"^cantonese_cuisine/crispy_roast_duck_rice/$", views.Cantonese_cuisineCrispy_Roast_Duck_RiceView, name="crispy_roast_duck_rice"),
    url(r"^cantonese_cuisine/beef_ball_noodles/$", views.Cantonese_cuisineBeef_Ball_NoodlesView, name="beef_ball_noodles"),
    url(r"^cantonese_cuisine/zhanjiang_boiled_chicken_rice/$", views.Cantonese_cuisineZhanjiang_Boiled_Chicken_RiceView, name="zhanjiang_boiled_chicken_rice"),
    url(r"^cantonese_cuisine/rose_sauce_chicken_rice/$", views.Cantonese_cuisineRose_Sauce_Chicken_RiceView, name="rose_sauce_chicken_rice"),
    url(r"^cantonese_cuisine/salt_baked_chicken_leg_rice/$", views.Cantonese_cuisineSalt_Baked_Chicken_Leg_RiceView, name="salt_baked_chicken_leg_rice"),
    url(r"^cantonese_cuisine/signature_roast_duck_rice/$", views.Cantonese_cuisineSignature_Roast_Duck_RiceView, name="signature_roast_duck_rice"),
    url(r"^cantonese_cuisine/kung_fu_duck_leg_rice/$", views.Cantonese_cuisineKung_Fu_Duck_Leg_RiceView, name="kung_fu_duck_leg_rice"),
    url(r"^cantonese_cuisine/crispy_duck_leg_rice/$", views.Cantonese_cuisineCrispy_Duck_Leg_RiceView, name="crispy_duck_leg_rice"),
    url(r"^cantonese_cuisine/secret_recipe_chicken_steak_rice/$", views.Cantonese_cuisineSecret_Recipe_Chicken_Steak_RiceView, name="secret_recipe_chicken_steak_rice"),




    url(r"^hunan_cuisine/spicy_shrimp/$", views.Hunan_cuisineSpicy_ShrimpView,name="spicy_shrimp"),
    url(r"^hunan_cuisine/chili_chicken/$", views.Hunan_cuisineChili_ChickenView,name="chili_chicken"),
    url(r"^hunan_cuisine/chili_pepper_fried_pork/$", views.Hunan_cuisineChili_Pepper_Fried_PorkView,name="chili_pepper_fried_pork"),
    url(r"^hunan_cuisine/salivating_chicken/$", views.Hunan_cuisineSalivating_ChickenView,name="salivating_chicken"),
    url(r"^hunan_cuisine/hot_dry_noodles/$", views.Hunan_cuisineHot_Dry_NoodlesView,name="hot_dry_noodles"),
    url(r"^hunan_cuisine/pork_mince_with_eggplant_over_rice/$", views.Hunan_cuisinePork_Mince_with_Eggplant_over_RiceView,name="pork_mince_with_eggplant_over_rice"),
    url(r"^hunan_cuisine/sausage_fried_with_dried_radish/$", views.Hunan_cuisineSausage_Fried_with_Dried_RadishView,name="sausage_fried_with_dried_radish"),
    url(r"^hunan_cuisine/garlic_fragrant_chicken_steak/$", views.Hunan_cuisineGarlic_Fragrant_Chicken_SteakView,name="garlic_fragrant_chicken_steak"),
    url(r"^hunan_cuisine/scallion_oil_mixed_noodles/$", views.Hunan_cuisineScallion_Oil_Mixed_NoodlesView,name="scallion_oil_mixed_noodles"),
    url(r"^hunan_cuisine/nanchang_mixed_noodles/$", views.Hunan_cuisineNanchang_Mixed_NoodlesView,name="nanchang_mixed_noodles"),

    url(r"^su_cuisine/seaweed_braised_chicken/$", views.Su_cuisineSeaweed_Braised_ChickenView, name="seaweed_braised_chicken"),
    url(r"^su_cuisine/curry_chicken_rice/$", views.Su_cuisineCurry_Chicken_RiceView, name="curry_chicken_rice"),
    url(r"^su_cuisine/authentic_beef_patty/$", views.Su_cuisineAuthentic_Beef_PattyView, name="authentic_beef_patty"),
    url(r"^su_cuisine/signature_chicken_leg_rice/$", views.Su_cuisineSignature_Chicken_Leg_RiceView, name="signature_chicken_leg_rice"),
    url(r"^su_cuisine/signature_beggar_chicken/$", views.Su_cuisineSignature_Beggar_ChickenView, name="signature_beggar_chicken"),
    url(r"^su_cuisine/black_pepper_chicken_steak_rice/$", views.Su_cuisineBlack_Pepper_Chicken_Steak_RiceView, name="black_pepper_chicken_steak_rice"),
    url(r"^su_cuisine/curry_chicken_with_chicken_steak/$", views.Su_cuisineCurry_Chicken_with_Chicken_SteakView, name="curry_chicken_with_chicken_steak"),

    url(r"^fujian_cuisine/chaoshan_pork_roll_rice/$", views.Fujian_cuisineChaoshan_Pork_Roll_RiceView,name="chaoshan_pork_roll_rice"),
    url(r"^fujian_cuisine/chaoshan_pork_roll_rice/$", views.Fujian_cuisineChaoshan_Mixed_Rice_NoodlesView,name="chaoshan_mixed_rice_noodles"),
    url(r"^fujian_cuisine/chaoshan_pork_roll_rice/$", views.Fujian_cuisineLongjiang_Pork_Trotter_RiceView,name="longjiang_pork_trotter_rice"),
    url(r"^fujian_cuisine/chaoshan_pork_roll_rice/$", views.Fujian_cuisinePork_Stew_RiceView,name="pork_stew_rice"),
    url(r"^fujian_cuisine/chaoshan_pork_roll_rice/$", views.Fujian_cuisineOriginal_Pork_Offal_NoodlesView,name="original_pork_offal_noodles"),
    url(r"^fujian_cuisine/chaoshan_pork_roll_rice/$", views.Fujian_cuisineOriginal_Seafood_Pork_Offal_NoodlesView,name="original_seafood_pork_offal_noodles"),
    url(r"^fujian_cuisine/chaoshan_pork_roll_rice/$", views.Fujian_cuisineLemon_Flavored_Pork_Offal_NoodlesView,name="lemon_flavored_pork_offal_noodles"),
    url(r"^fujian_cuisine/chaoshan_pork_roll_rice/$", views.Fujian_cuisineTomato_Flavored_Pork_Offal_NoodlesView,name="tomato_flavored_pork_offal_noodles"),
]
