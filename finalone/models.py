from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.postgres.fields import JSONField
from django.db import models

# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, name, password=None, **extra_fields):
        if not name:
            raise ValueError('The Name field must be set')
        user = self.model(name=name, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(name, password, **extra_fields)

# Role Model
class Role(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name

# Custom User Model 
class User(AbstractBaseUser):
    name = models.CharField(max_length=256, unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=254, unique=True)
    # email = models.EmailField(unique=True, default="default@example.com")  
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Custom field   blank=True, null=True
    custom_fields = models.JSONField(blank=True, null=True)  #  JSON field
    
    # Additional fields for authentication
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Custom user manager
    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email', 'phone_number']

    def __str__(self):
        return self.name
