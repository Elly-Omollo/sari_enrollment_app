from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe



# Creating a user profile image directory
def _userimage(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" %(instance.user.id, filename)
    return "user_{0}/{1}".format(instance.user.id, filename)

# gender choices
gender = [
    ("female","female"),
    ("male","male"),
    ("other","other"),
]


class User(AbstractUser):
    fullname = models.CharField(max_length=100, null= True, blank=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    gender =models.CharField(max_length=20, choices=gender, default='other')

    otp = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return f"{self.username}"



class Profile(models.Model):
    profileId = ShortUUIDField(length=4, max_length=100, alphabet="abcdefghijklmnopqrstuvwxyz12345")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to= _userimage, default='default.jpg', null=True, blank=True)
    fullname = models.CharField(max_length=100, null= True, blank=True)
    phone_number = models.CharField(max_length=20, unique=True, null=True ,blank=True)
    gender =models.CharField(max_length=20, choices=gender, default='other')
    


    def __str__(self):
        if self.fullname:
            return f"{self.fullname}"
        else:
            return f"{self.user}"

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')
        return "No Image"
        
        # image_tage.short_description = "Profile Image"    


def create_user_profile(sender, instance, created, **kwargs):
       if created:
         Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

          