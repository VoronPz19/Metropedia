from django.db.models.signals import post_save
from .models import *
from django.dispatch.dispatcher import receiver


@receiver(post_save, sender=Station)
def transfer_update(sender, instance, **kwargs):
    from_station = instance
    for stations in Station.objects.all():
        stations.transfer.remove(from_station)
    for to_station in instance.transfer.all():
        to_station.transfer.add(from_station)
