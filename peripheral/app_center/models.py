from django.db import models

__all__ = ['Address', 'OrderGoods', 'OrderMessage']
# Create your models here.

# 个人信息与修改密码


# 地址表（Address）
class Address(models.Model):
    person = models.CharField(max_length=32, null=False)
    address = models.CharField(max_length=64, null=False)
    a_status = models.IntegerField()
    a_phone = models.IntegerField()
    user = models.ForeignKey(to="app_login.User", on_delete=models.CASCADE)


# 订单信息表（OrderMessage）
class OrderMessage(models.Model):
    number = models.IntegerField()
    # CHOICES = ((1, 'WeChat'), (2, '支付宝'))
    # pay_method = models.IntegerField(choices=CHOICES)
    amount = models.IntegerField()
    count = models.IntegerField()
    pay_status = models.IntegerField(default=0)
    c_time = models.DateField(null=False)
    user_order_mes = models.ForeignKey(to="app_login.User", on_delete=models.CASCADE)
    address_order_mes = models.ForeignKey(to="Address", on_delete=models.CASCADE)


# 订单商品表（OrderGoods）
class OrderGoods(models.Model):
    og_count = models.IntegerField()
    og_price = models.IntegerField()
    og_talk = models.CharField(max_length=256)
    order_mes_goods = models.ForeignKey(to="OrderMessage", on_delete=models.CASCADE)
    sku_goods = models.ForeignKey(to="app_goods.GoodsSku", on_delete=models.CASCADE)
