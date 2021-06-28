from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Менеджер для профилей пользователей"""

    def create_user(self, email, name, password=None):
        """Создание нового пользователя"""
        if not email:
            raise ValueError("User mast have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Создание нового суперпользователя"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Модель данных для пользователей"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Возвращает полное имя пользователя"""
        return self.name

    def get_short_name(self):
        """Возвращает короткое имя пользователя"""
        return self.name

    def __str__(self):
        """Возвращает текстовое представление пользователя"""
        return self.email
