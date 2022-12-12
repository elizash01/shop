from django.db import models

# Create your models here.


CLOTHES_TYPES = [
    ('man', 'Мужской'),
    ('woman', 'Женский'),
    ('kid', 'Детский'),
    ('uni', 'Универсальный'),
]


SEASON_TYPES = [
    ('winter', 'Зима'),
    ('spring', 'Весна'),
    ('summer', 'Лето'),
    ('autumn', 'Осень'),
]


class Category(models.Model):
    category_name = models.CharField(verbose_name='Название категории', max_length=100)
    category_description = models.TextField(max_length=200, verbose_name='Описание')
    category_slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'    


class Brand(models.Model):
    brand_name = models.CharField(max_length=100, verbose_name='Название Бренда')
    brand_description = models.TextField(max_length=200, verbose_name='Описание')
    brand_slug = models.SlugField(max_length=100, unique=True)


    def __str__(self):
        return self.brand_name
    
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

class Clothes(models.Model):
    clothes_name = models.CharField(max_length=100, verbose_name='Название')
    clothes_description = models.TextField(max_length=200, verbose_name='Описание')
    clothes_slug = models.SlugField(max_length=100, unique=True)
    clothes_type = models.CharField(max_length=10, choices=CLOTHES_TYPES)
    clothes_season = models.CharField(max_length=10, choices=SEASON_TYPES, verbose_name='Сезон')
    clothes_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    clothes_image = models.ImageField(upload_to='clothes', verbose_name=' Изобрежение')
    clothes_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='clothes')
    clothes_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='clothes')
    owner = models.ForeignKey('auth.User', related_name='clothes', on_delete=models.CASCADE)

    def __str__(self):
        return self.clothes_name

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'   



class ClothesSize(models.Model):
    cn = models.CharField(max_length=10, verbose_name='Китайский размер')
    eu = models.CharField(max_length=10, verbose_name='Европейский размер')
    us = models.CharField(max_length=10, verbose_name='Американский размер')

    def __str__(self):
        return  self.cn

    def european(self):
        return self.eu

    def american_size(self):
        return self.us
        
    class Meta:
        verbose_name = 'Размер одежды'
        verbose_name_plural = 'Размеры одежды'    

class ClothesColor(models.Model):
    color_name = models.CharField(max_length=100, verbose_name='Название цвета')
    color_slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.color_name

    class Meta:
        verbose_name = 'Цвет одежды'
        verbose_name_plural = 'Цвета одежды'    


class ClothesInStock(models.Model):
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE, related_name='clothes')
    clothes_size = models.ForeignKey(ClothesSize, on_delete=models.CASCADE, related_name='clothes_size')
    clothes_color = models.ForeignKey(ClothesColor, on_delete=models.CASCADE, related_name='clothes_color')
    clothes_count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.clothes}'

    class Meta:
        verbose_name = 'Одежда в наличии'
        verbose_name_plural = 'Одежды в наличии'    