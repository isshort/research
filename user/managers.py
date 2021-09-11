from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom user model manager where email and phone is the unique identifiers
    for authentication instead of username.
    """
    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError('Phone not provided')

        if not password:
            raise ValueError('The given password must be set')

        user = self.model(phone=phone, **extra_fields)
        user.username = phone
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, password=None, phone=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(password=password, phone=phone, **extra_fields)

    def create_superuser(self, phone=None,
                         password=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(phone, password, **extra_fields)
