from django.db import models

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_superuser(self, email, password,name,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)

        if other_fields.get('is_staff') is not True:
            return ValueError('Superuser must have is_staff True')
        
        if other_fields.get('is_superuser') is not True:
            return ValueError('Superuser must have is_superuser True')
        
        return self.create_user(email,password,name,other_fields)
    
    def create_user(self,email,password,name,**other_fields):
        if not email:
            raise ValueError('You must be provided valid email')
        
        email = self.email.normalize_email(email)

        user = self.model(email=email,name=name, password=password,**other_fields)

        user.set_password(password)

        user.save()

        return user
