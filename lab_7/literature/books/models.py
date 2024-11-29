from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=120,verbose_name='Название')
    content = models.TextField(verbose_name='Аннотация')
    year_of_pub = models.DateTimeField(auto_now =False,auto_now_add=True,verbose_name='Дата публикации' )

    post_likes = models.IntegerField(default=0)
    status =(('r1','Роман'),('p1', 'Поэма'),('d1','Детектив'),('k','Комедия'),('d2','Драма'),('f1','Фантастика'),('f2','Фентази'),('p2','Повесть'),('r2','Рассказ'))
    status = models.CharField(max_length=2,choices=status,blank=True,default='r1',verbose_name='Жанр')
    post_author = models.ForeignKey('Author',null=True, blank=True,verbose_name='Автор', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

    def __str_(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книг'
        db_table='book'
        ordering= ["year_of_pub"]

class Author(models.Model):
    id= models.AutoField(primary_key =True)
    first_name = models.CharField(max_length=120, verbose_name='Имя')
    second_name = models.CharField(max_length=120, verbose_name='Фамилия')
    email = models.EmailField(max_length=254,null=True, blank=True, verbose_name='Почта')

    def __unicode__(self):
       return self.first_name+' '+self.second_name

    def __str_(self):
       return self.first_name+' '+self.second_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural ='Авторы'
        db_table = 'author'
        ordering = ["second_name", "first_name"]

class Comments(models.Model):
    id=models.AutoField(primary_key=True)
    comment_text = models.TextField(verbose_name='Комментарий')
    timepublish = models.DateTimeField(auto_now=False,auto_now_add=True,blank =True,null=True,verbose_name='Дата комментария')
    comment_article = models.ForeignKey(Book,  on_delete=models.CASCADE)
    comment_likes = models.IntegerField(default=0)
    rating = ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    rating = models.IntegerField(choices=rating, blank=True, default=0, verbose_name='Оценка')

    def __unicode__(self):
       return self.comment_text

    def __str_(self):
       return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural ='Комментарии'