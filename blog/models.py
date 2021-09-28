from django.db import models
from django.db.models.fields import CharField


# Create your models here.
# class Blogs(models.Model):
#     title = models.CharField(max_length=150)
#     email = models.CharField(max_length=50)
#     desc = models.TextField()
#     img = models.ImageField(upload_to="blogImages")
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
    


class ModernBlogs(models.Model):
    status = (
    ("p", "Public"),
    ("r", "Private"),
    )
    publist_status = models.CharField(max_length=50, choices=status,default="")
    btitle = models.CharField(max_length=150)
    tag = models.CharField(max_length=15,default="")
    email = models.CharField(max_length=50)
    coverimg = models.ImageField(upload_to="blogImages")
    desc = models.TextField(default="")
    point1 = models.CharField(max_length=200,default="",blank=True, null=True)
    img1 = models.ImageField(upload_to="blogImages",default="",blank=True, null=True)
    desc1 = models.TextField(default="",blank=True, null=True)
    point2 = models.CharField(max_length=200,default="",blank=True, null=True)
    img2 = models.ImageField(upload_to="blogImages",default="",blank=True, null=True)
    desc2 = models.TextField(default="",blank=True, null=True)
    point3 = models.CharField(max_length=200,default="",blank=True, null=True)
    img3 = models.ImageField(upload_to="blogImages",default="",blank=True, null=True)
    desc3 = models.TextField(default="",blank=True, null=True)
    point4 = models.CharField(max_length=200,default="",blank=True, null=True)
    img4 = models.ImageField(upload_to="blogImages",default="",blank=True, null=True)
    desc4 = models.TextField(default="",blank=True, null=True)
    point5 = models.CharField(max_length=200,default="",blank=True, null=True)
    img5 = models.ImageField(upload_to="blogImages",default="",blank=True, null=True)
    desc5 = models.TextField(default="",blank=True, null=True)
    point6 = models.CharField(max_length=200,default="",blank=True, null=True)
    img6 = models.ImageField(upload_to="blogImages",default="",blank=True, null=True)
    desc6 = models.TextField(default="",blank=True, null=True)
    point7 = models.CharField(max_length=200,default="",blank=True, null=True)
    img7 = models.ImageField(upload_to="blogImages",default="",blank=True, null=True)
    desc7 = models.TextField(default="",blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.btitle

class UserIp(models.Model):
    blog = models.ForeignKey(ModernBlogs,on_delete=models.CASCADE, default="")
    user = models.TextField(max_length=250)
    def __str__(self):
        return self.user
    


class Comment(models.Model):
    post = models.ForeignKey(ModernBlogs,on_delete=models.CASCADE)
    name = models.CharField(max_length=40) 
    email = models.EmailField() 
    cmt = models.CharField(max_length=150) 
    date = models.DateTimeField(auto_now_add=True) 
    like = models.IntegerField()
    

    def __str__(self):
        return self.name


class News(models.Model):
    news = models.CharField(max_length=50)
    coverimg = models.ImageField(upload_to="newsImages")
    info = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news