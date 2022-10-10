from django.db import models

# Create your models here.


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


# 商品图片表（GoodsPicture）
class GoodsPicture(models.Model):
    g_picture = models.CharField(max_length=64)
    sku_goods = models.ForeignKey(to="GoodsSku", on_delete=models.CASCADE)


# 商品种类表（GoodsType）
class GoodsType(models.Model):
    g_type = models.CharField(max_length=32)
    logo = models.CharField(max_length=64)


# 首页轮播图表（Carousel）
class Carousel(models.Model):
    index_picture = models.CharField(max_length=64)
    index = models.CharField(max_length=32, db_index=True)
    sku_carousel = models.ForeignKey(to="GoodsSku", on_delete=models.CASCADE)


# 首页促销表图（Discount）
class Discount(models.Model):
    dp_picture_urls = models.CharField(max_length=64)
    dp_urls = models.CharField(max_length=64)


# # 评论
# class Article(models.Model):  # 定义文章模型类
#     title = models.CharField(max_length=100, verbose_name='文章标题')  # verbose_name是
#     content = models.TextField(verbose_name='文章内容')
#     publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
#     author = models.ForeignKey(to="User", on_delete=models.DO_NOTHING, verbose_name='作者')
#
#     class Meta:
#         db_table = 'article_tb'  # 定义表名
#         verbose_name = '文章'  # 后台显示
#         verbose_name_plural = verbose_name  # 后台显示的复数
#
#
# class Comment(models.Model):  # 定义评论模型
#     article = models.ForeignKey(to=Article, on_delete=models.DO_NOTHING, verbose_name='评论文章')
#     comment_content = models.TextField(verbose_name='评论内容')
#     comment_author = models.ForeignKey(to="User", on_delete=models.DO_NOTHING, verbose_name='评论者')
#     comment_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
#     pre_comment = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True,
#                                     verbose_name='父评论id')  # 父级评论，如果没有父级则为空NULL, "self"表示外键关联自己
#
#     class Meta:
#         db_table = 'comment_tb'
#         verbose_name = '评论'
#         verbose_name_plural = verbose_name