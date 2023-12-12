from django.db.models.signals import m2m_changed, pre_save
from .models import *
from django.dispatch.dispatcher import receiver


@receiver(m2m_changed, sender=Station.transfer.through)
def transfer_add(sender, instance, action, **kwargs):
    from_station = instance
    if action == 'pre_add' or action == 'post_add':
        for to_station in from_station.transfer.all():
            if from_station not in to_station.transfer.all():
                to_station.transfer.add(from_station)


@receiver(pre_save, sender=Station)
def transfer_delete(sender, instance, **kwargs):
    from_station = instance
    for to_station in from_station.transfer.all():
        if from_station in to_station.transfer.all():
            to_station.transfer.remove(from_station)
            to_station.save()
