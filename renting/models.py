from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile',
                                primary_key=True)
    currently_rented = models.ManyToManyField('library.BookInstance',
                                              through='CurrentRental')

    def __str__(self):
        if self.user.first_name != "" or self.user.last_name != "":
            return f"{self.user.first_name} {self.user.last_name}"
        return f"username: {self.user.username}"


class CurrentRental(models.Model):
    profile = models.ForeignKey(Profile,
                                on_delete=models.PROTECT,
                                related_name='rentals')
    book = models.ForeignKey('library.BookInstance',
                             on_delete=models.PROTECT,
                             related_name='rentals')
    date_rented = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User {self.profile.user} is renting {self.book.book.title_short}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
