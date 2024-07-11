from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, email, password = None, **extrafields):
        if not email:
            raise ValueError('Email address is required to create a new User.')

        user = self.model(email = self.normalize_email(email), **extrafields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        superuser = self.create_user(email, password)
        superuser.is_staff = True
        superuser.is_superuser = True

        superuser.save(using=self._db)

        return superuser

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
