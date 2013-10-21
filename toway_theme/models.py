from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from mezzanine.pages.models import Page
from mezzanine.utils.models import AdminThumbMixin, upload_to
from mezzanine.core.fields import FileField
from mezzanine.core.models import Displayable, Orderable, RichText

#from social_auth.models import pre_update
from social_auth.signals import socialauth_registered

# Create your models here.
'''
class Activity(Page, RichText):
    cover_image = FileField(verbose_name=_("cover_image"), 
            upload_to=upload_to("toway_theme.Activity.cover_image", "activity"),
            format="Image", max_length=255, null=True, blank=True)
    admin_thumb_field = "cover_image" '''

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

#post_save.connect(create_user_profile, sender=User)
#socialauth_registered.connect(create_user_profile, sender=User)
#User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

