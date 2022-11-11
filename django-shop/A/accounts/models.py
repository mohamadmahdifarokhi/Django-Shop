from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from .managers import UserManger


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    # bayad unique bashe chon ba phone mikhaym validate konim
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManger()

    USERNAME_FIELD = 'phone_number'
    # bara dastore createsuperuser azat email beporse kenare USERNAME_FIELD va pass
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self):
        return self.email

    # in 2 tatabe ro hazf mikonim ta adminhaye mahdod shode mahdod beshan

    # # har permissiony khast behesh midim
    # def has_perm(self, perm, obj=None):
    #     return True
    #
    # # karbar be modela datresi dare ya na
    # def has_module_perms(self, app_label):
    #     return True

    # property kardim ta raftareh mese is_admin va is_active bashe
    # is_staff bara admin bodane
    @property
    def is_staff(self):
        return self.is_admin


# one time password
class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    code = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created}'
