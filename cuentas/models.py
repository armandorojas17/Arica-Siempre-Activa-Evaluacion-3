from django.db import models
from django.contrib.auth.models import User


class Invitado(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='invitado'
    )

    def __str__(self):
        return 'Invitado: {}'.format(self.usuario.username)



class Turista(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='turista'
    )

    def __str__(self):
        return 'Turista: {}'.format(self.usuario.username)


class Administrador(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='administrador'
    )
    admin_nivel_acceso = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    def __str__(self):
        return 'Administrador: {}'.format(self.usuario.username)


class Gremio(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='gremio'
    )
    gremio_nombre_empresa = models.CharField(max_length=100, blank=True)
    gremio_contacto = models.CharField(max_length=100, blank=True)
    gremio_direccion = models.CharField(max_length=150, blank=True)
    gremio_sitio_web = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return 'Gremio: {}'.format(self.usuario.username)