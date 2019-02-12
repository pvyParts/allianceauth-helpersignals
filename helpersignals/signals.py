from .models import ApplicationWebhook
from django.db.models.signals import post_save
from django.dispatch import receiver
from allianceauth.hrapplications.models import Application
import requests
import json


@receiver(post_save, sender=Application)
def new_app(sender, instance, created, **kwargs):
    if created:
        print("New Application! %s" % instance.main_character , flush=True)
        try:
            url = "Link to auth"
            main_char = instance.main_character
            corp = instance.form.corp
            embed_list = [{'title':"New Application", 'description':("From %s on auth"%main_char.character_name), 'image':{'url': ('https://imageserver.eveonline.com/Character/%s_128.jpg' % (main_char.character_id))}}]
            hooks = ApplicationWebhook.objects.filter(corp=corp)
        
            for hook in hooks:
                if hook.enabled:
                    custom_headers = {'Content-Type': 'application/json'}
                    alertText = ""

                    r = requests.post(hook.webhook, headers=custom_headers, data=json.dumps({'content':alertText, 'embeds': embed_list}))
                #logger.error("Got status code %s after sending ping" % r.status_code)
                    r.raise_for_status()
        except:
            pass # shits fucked... 
