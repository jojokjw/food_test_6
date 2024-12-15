from django.db import models

# 在这里新建模型.
class Restaurants(models.Model):
    name = models.CharField(max_length=256, verbose_name='餐厅名称')
    latitude = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='纬度')
    longitude = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='经度')
    rating = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='评分')
    cost = models.IntegerField(verbose_name='花费')
    count = models.IntegerField(verbose_name='数量')

    # 以下为具体例子.
    pasta = models.IntegerField(verbose_name='意大利面')
    tea = models.IntegerField(verbose_name='茶')
    juices = models.IntegerField(verbose_name='果汁')

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