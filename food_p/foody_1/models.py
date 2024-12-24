from django.db import models

# Create your models here.
class Restaurants(models.Model):
    name = models.CharField(max_length=256, verbose_name='餐厅名称')
    latitude = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='纬度')
    longitude = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='经度')
    rating = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='评分')
    cost = models.IntegerField(verbose_name='花费')
    count = models.IntegerField(verbose_name='数量')

#川菜(Sichuan_cuisineDishes

    chili_chicken_noodles = models.IntegerField(verbose_name='辣子鸡面')
    spicy_wonton = models.IntegerField(verbose_name='麻辣抄手')
    sour_cabbage_wonton = models.IntegerField(verbose_name='酸菜抄手')
    cumin_beef_noodles = models.IntegerField(verbose_name='孜然牛肉盖面')
    sour_cabbage_beef_noodles = models.IntegerField(verbose_name='酸菜牛肉面')
    sichuan_style_spicy_five_grain_fish_noodles = models.IntegerField(verbose_name='川香麻辣口味五谷鱼粉')

#粤菜(Cantonese_cuisine
    cantonese_stone_ground_rice_noodles = models.IntegerField(verbose_name='广式石磨肠粉')
    honey_glazed_roast_pork_rice = models.IntegerField(verbose_name='蜜汁叉烧饭')
    crispy_roast_duck_rice = models.IntegerField(verbose_name='脆皮烧鸭饭')
    beef_ball_noodles = models.IntegerField(verbose_name='牛筋丸面')
    zhanjiang_boiled_chicken_rice = models.IntegerField(verbose_name='湛江白切鸡饭')
    rose_sauce_chicken_rice = models.IntegerField(verbose_name='玫瑰豉油鸡饭')
    salt_baked_chicken_leg_rice = models.IntegerField(verbose_name='盐焗鸡腿饭')
    signature_roast_duck_rice = models.IntegerField(verbose_name='招牌烧鸭饭')
    kung_fu_duck_leg_rice = models.IntegerField(verbose_name='功夫鸭腿饭')
    crispy_duck_leg_rice = models.IntegerField(verbose_name='脆皮鸭腿饭')
    secret_recipe_chicken_steak_rice = models.IntegerField(verbose_name='秘制鸡排饭')

#湘菜(Hunan_cuisine
    spicy_shrimp = models.IntegerField(verbose_name='香辣虾')
    chili_chicken = models.IntegerField(verbose_name='辣子鸡')
    chili_pepper_fried_pork = models.IntegerField(verbose_name='辣椒炒肉')
    salivating_chicken = models.IntegerField(verbose_name='口水鸡')
    hot_dry_noodles = models.IntegerField(verbose_name='热干面')
    pork_mince_with_eggplant_over_rice = models.IntegerField(verbose_name='肉沫茄子盖饭')
    sausage_fried_with_dried_radish = models.IntegerField(verbose_name='腊肠炒萝卜干')
    garlic_fragrant_chicken_steak = models.IntegerField(verbose_name='蒜香鸡排')
    scallion_oil_mixed_noodles = models.IntegerField(verbose_name='葱油拌面')
    nanchang_mixed_noodles = models.IntegerField(verbose_name='南昌拌面')

#苏菜(Su_cuisine
    seaweed_braised_chicken = models.IntegerField(verbose_name='海苔碎焖鸡')
    curry_chicken_rice = models.IntegerField(verbose_name='咖喱鸡饭')
    authentic_beef_patty = models.IntegerField(verbose_name='正点牛肉饼')
    curry_chicken_with_chicken_steak = models.IntegerField(verbose_name='咖喱鸡拼鸡扒')
    signature_chicken_leg_rice = models.IntegerField(verbose_name='招牌鸡腿饭')
    signature_beggar_chicken = models.IntegerField(verbose_name='招牌叫花鸡')
    black_pepper_chicken_steak_rice = models.IntegerField(verbose_name='黑椒鸡扒饭')

#闽菜(Fujian_cuisine
    chaoshan_pork_roll_rice = models.IntegerField(verbose_name='潮汕肉卷饭')
    chaoshan_mixed_rice_noodles = models.IntegerField(verbose_name='潮汕拌粿条')
    longjiang_pork_trotter_rice = models.IntegerField(verbose_name='隆江猪脚饭')
    pork_stew_rice = models.IntegerField(verbose_name='卤肉饭')
    original_pork_offal_noodles = models.IntegerField(verbose_name='原味猪杂面')
    original_seafood_pork_offal_noodles = models.IntegerField(verbose_name='原味海鲜猪杂面')
    lemon_flavored_pork_offal_noodles = models.IntegerField(verbose_name='柠檬味猪杂面')
    tomato_flavored_pork_offal_noodles = models.IntegerField(verbose_name='番茄味猪杂面')



















    class Meta:
        verbose_name = '餐厅'
        verbose_name_plural = '餐厅'

class TrainingData(models.Model):
    rating = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='评分')
    distance = models.IntegerField(verbose_name='距离')
    cost = models.IntegerField(verbose_name='花费')
    yesno = models.IntegerField(verbose_name='是否')

    class Meta:
        verbose_name = '训练数据'
        verbose_name_plural = '训练数据'

class MoodData(models.Model):
    Dish = models.CharField(max_length=50, verbose_name='菜品')
    happie = models.IntegerField(verbose_name='开心')
    angrie = models.IntegerField(verbose_name='生气')
    dehydratie = models.IntegerField(verbose_name='脱水')
    depressie = models.IntegerField(verbose_name='抑郁')
    excitie = models.IntegerField(verbose_name='兴奋')
    unwellie = models.IntegerField(verbose_name='不适')

    class Meta:
        verbose_name = '情绪数据'
        verbose_name_plural = '情绪数据'