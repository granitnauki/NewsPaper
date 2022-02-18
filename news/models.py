from django.db import models




class Author(models.Model):
    name = models.CharField(max_length=255)
    rating_Author = models.IntegerField(default=0)
    User = models.OneToOneField(User, on_delete=models.CASCADE)

sport = 'SP'
politic = 'PL'
education = 'ED'
culture = 'CL'


TEMA = [
    (sport, 'Спорт'),
    (politic, 'Политика'),
    (education, 'Образование'),
    (culture, 'Культура')
]
class Category(models.Model):
    tema = models.CharField(max_length=2, choices=TEMA, default=sport, unique=True)




class Post(models.Model):
    header = models.CharField(max_length=255)
    datetime_Post = models.DateTimeField(auto_now_add=True)
    rating_Post = models.IntegerField(default=0)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Category = models.ManyToManyField(Category, through='PostCategory')




class PostCategory(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)



class Comment(models.Model):
    datetime_Comment = models.DateTimeField(auto_now_add=True)
    rating_Comment = models.IntegerField(default=0)
    Comment = models.TextField()
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
