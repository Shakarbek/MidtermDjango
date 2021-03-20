from django.db import models

# Create your models here.
class BookQuerySet(models.QuerySet):

    def get_related(self):
        return self.select_related('journal')

class BookJournalBase():
    name =models.CharField(max_length=30, blank=True)
    price= models.IntegerField(verbose_name='Цена', blank=True)
    description = models.TextField(blank=True, verbose_name='description' )
    created_at=models.DateField(verbose_name='date', blank=True)
    objects=BookQuerySet.as_manager()



    class Meta:
        abstract=True
        ordering=['name']


class  Book(BookJournalBase):
    num_pages=models.IntegerField(verbose_name='pages', blank=True)
    genre=models.CharField(max_length=255, verbose_name='genre', blank=True)



class Journal(BookJournalBase):
    objects = BookQuerySet.as_manager()
    type_of_journal=('Bullet', 'Food', 'Travel', 'Sport')

    type=models.CharField(max_length=255, choices=type_of_journal, blank=True)
    publisher=models.CharField(max_length=255, verbose_name='Publisher', blank=True)
