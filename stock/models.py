from django.db import models

# Create your models here.
from accounts.models import CustomUser

class Category(models.Model):
    title = models.CharField(
        verbose_name= 'カテゴリ',
        max_length= 20
    )
    def __str__(self):
        return self.title
    
class StockPost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
    )

    title = models.CharField(
        verbose_name='商品名',
        max_length=50
    )

    posted_at = models.DateTimeField(
        verbose_name='入荷日時',
        auto_now_add=True
    )
    
    many = models.IntegerField(
        verbose_name='入荷数',
        blank=True,
        null=True,
    )
    
    comment = models.TextField(
        verbose_name='備考',
    )

    def __str__(self):
        return self.title

