from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self,username, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        try:
            self.model.objects.get(username=username)
            raise ValueError('Username already exists')
        except:
            pass
        user.username=username
        user.set_password(password)
        user.save(using=self._db)
    
        return user

    def create_staffuser(self,username, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        try:
            self.model.objects.get(username=username)
            raise ValueError('Username already exists')
        except:
            pass
        user.username=username
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self,username, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        try:
            self.model.objects.get(username=username)
            raise ValueError('Username already exists')
        except:
            pass
        user.username=username
        user.staff = True
        user.superuser = True
        user.save(using=self._db)
        return user