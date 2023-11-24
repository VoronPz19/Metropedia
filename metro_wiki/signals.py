from django.db.models.signals import post_save, post_delete
from .models import *
from django.dispatch.dispatcher import receiver


@receiver(post_save, sender=Station)
def transfer_update(sender, instance, created, **kwargs):
    if created:
        from_station = instance
        to_station = Station.objects.set(
            transfer=from_station.transfer,
        )


@receiver(post_save, sender=Station)
def update_transfer(sender, instance, created, **kwargs):
    from_station = instance
    to_station = from_station.transfer
    if created is False:
        to_station.transfer = from_station.transfer
        to_station.save()


@receiver(post_delete, sender=Station)
def delete_transfer(sender, instance, **kwargs):
    to_station = instance.transfer
    to_station.delete()


