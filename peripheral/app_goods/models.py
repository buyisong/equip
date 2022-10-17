from django.db import models

# Create your models here.

__all__ = ['GoodsSpu', 'GoodsSku', 'GoodsPicture',
           'GoodsType', 'Carousel', 'Discount']


# 商品sku表（GoodsSpu）
class GoodsSku(models.Model):
    sk_name = models.CharField(max_length=32, null=False)
    description = models.CharField(max_length=128)
    price = models.CharField(max_length=32, null=False)
    sale_volume = models.CharField(max_length=32)
    axios = models.CharField(max_length=32)
    connection = models.CharField(max_length=32)
    refresh = models.CharField(max_length=32)
    size = models.CharField(max_length=32)
    rest = models.IntegerField()
    spu = models.ForeignKey(to="GoodsSpu", on_delete=models.CASCADE)


# 商品spu表（GoodsSpu）
class GoodsSpu(models.Model):
    sp_name = models.CharField(max_length=32)
    sp_details = models.CharField(max_length=256)
    sp_picture = models.ImageField(upload_to='./uploads/thumb/605_605')
    select = models.IntegerField(null=True)
    type = models.ForeignKey(to="GoodsType", on_delete=models.CASCADE)


# 商品图片表（GoodsPicture）
class GoodsPicture(models.Model):
    g_picture = models.ImageField(upload_to='')
    sku_goods = models.ForeignKey(to="GoodsSku", on_delete=models.CASCADE)


# 商品种类表（GoodsType）
class GoodsType(models.Model):
    g_type = models.CharField(max_length=32)



# 首页轮播图表（Carousel）
class Carousel(models.Model):
    index_picture = models.CharField(max_length=64)
    index = models.CharField(max_length=32, db_index=True)
    sku_carousel = models.ForeignKey(to="GoodsSku", on_delete=models.CASCADE)


# 首页促销表图（Discount）
class Discount(models.Model):
    dp_picture = models.ImageField(upload_to='')
    dp_urls = models.CharField(max_length=64)


# # 评论
# class Article(models.Model):  # 定义文章模型类
#     title = models.CharField(max_length=100, verbose_name='文章标题')  # verbose_name是
#     content = models.TextField(verbose_name='文章内容')
#     publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
#     author = models.ForeignKey(to="User", on_delete=models.DO_NOTHING, verb