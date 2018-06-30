from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    '''Налаштування відображення в адмін панелі полів'''
    def __str__(self):
        return 'Users %s %s' % (self.name, self.email)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural ='A lot of Subscribers'
