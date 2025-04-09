from django.db import models

class Quartier(models.Model):
    nom = models.CharField(max_length=100)
    superficie = models.FloatField(help_text="Superficie totale du quartier en m²")

    def __str__(self):
        return self.nom

    def superficie_restante(self):
        total = sum(maison.superficie for maison in self.maisons.all())
        return self.superficie - total


class Maison(models.Model):
    quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE, related_name="maisons")
    nom = models.CharField(max_length=100)
    superficie = models.FloatField()
    nb_chambres = models.PositiveIntegerField()
    nb_douches = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nom} ({self.quartier.nom})"

    def save(self, *args, **kwargs):
        if self.pk is None:  # Création
            if self.quartier.superficie_restante() < self.superficie:
                raise ValueError("Superficie du quartier dépassée")
        super().save(*args, **kwargs)

# Create your models here.
