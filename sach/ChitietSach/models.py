from django.db import models
from django.conf import settings


# Create your models here.

class Theloai(models.Model):
    thloai = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.thloai


class Danhmuc(models.Model):
    danhmuc = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.danhmuc


class Tacgia(models.Model):
    tacgia = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.tacgia


class Sach(models.Model):
    tieude = models.CharField(max_length=255, null=True, blank=True)
    hinh = models.ImageField(null=True, blank=True)
    tacgia = models.CharField(max_length=255, null=True, blank=True)
    danhmuc = models.ForeignKey(Danhmuc, on_delete=models.PROTECT, max_length=255, null=True, blank=True)
    theloai = models.ForeignKey(Theloai, on_delete=models.PROTECT, max_length=255, null=True, blank=True)
    ngaydang = models.DateTimeField(null=True, auto_now_add=True)
    mota = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.tieude


class Chuong(models.Model):
    sochuong = models.CharField(max_length=255, null=True, blank=True)
    noidung = models.TextField(null=True, blank=True)
    tieude = models.ForeignKey(Sach, on_delete=models.DO_NOTHING, null=True, blank=True, default=None)

    def __str__(self):
        return self.sochuong


class Comment(models.Model):
    post = models.ForeignKey(Chuong, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)