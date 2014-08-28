#-*- coding: utf-8 -*-
from django.db import models

# Exemple de ForeignKey

class Categorie(models.Model):
		nom = models.CharField(max_length=30)
		def __str__(self):
			return self.nom

class Article(models.Model):
		titre = models.CharField(max_length=100)
		auteur = models.CharField(max_length=42)
		contenu = models.TextField(null=True)
		date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
		categorie = models.ForeignKey(Categorie)
		def __str__(self):
			return self.titre

# Exemple de OneToOne

class Moteur(models.Model):
	nom = models.CharField(max_length=25)
	def __str__(self):
		return self.nom

class Voiture(models.Model):
	nom = models.CharField(max_length=25)
	moteur = models.OneToOneField(Moteur)
	def __str__(self):
		return self.nom

# Exemple de ManyToMany  

class Produit(models.Model):
	nom = models.CharField(max_length=30)
	def __str__(self):
		return self.nom

class Vendeur(models.Model):
	nom = models.CharField(max_length=30)
	produits = models.ManyToManyField(Produit, through='Offre')
	def __str__(self):
		return self.nom

class Offre(models.Model):
	prix = models.IntegerField()
	produit = models.ForeignKey(Produit)
	vendeur = models.ForeignKey(Vendeur)
	def __str__(self):
		return "{0} vendu par {1}".format(self.produit, self.vendeur)

""" 
Cette méthode que nous définirons dans tous les modèles
nous permettra de reconnaître facilement les différents objets que nous
traiterons plus tard et dans l'administration
"""