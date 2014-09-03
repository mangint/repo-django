from django.contrib import admin
from blog.models import Contact, Categorie, Article, Moteur, Voiture, Produit, Vendeur, Offre


class ArticleAdmin(admin.ModelAdmin):
	# Configuration de la liste d'articles
	list_display = ('titre', 'auteur', 'date', 'categorie', 'apercu_contenu')
	list_filter = ('auteur', 'categorie',)
	date_hierarchy = 'date'
	ordering = ('date',)
	search_fields = ('titre', 'contenu')

	# Configuration du formulaire d'édition
#	fields = ('titre', 'auteur', 'categorie', 'contenu')
	fieldsets = (
		# Fieldset 1 : meta-info (titre, auteur…)
		('Général', 
			{
			'classes':['collapse',],

			'fields': ('titre', 'auteur', 'categorie')
			}),
		# Fieldset 2 : contenu de l'article
		( 'Contenu de l\'article', 
			{
			'description':'Le formulaire accepte les balises HTML. Utilisez-les à bon escient!',
			'fields': ('contenu',)
			}),
		)

	# Colonnes personnalisées
	def apercu_contenu(self, article):
		"""
		Retourne les 40 premiers caratères du contenu de l'articlre. S'il 
		y a plus de 40 caractères, il faut ajouter des points de suspensions.
		"""
		text = article.contenu[0:40]
		if len(article.contenu) > 40:
			return '%s...' % text

	apercu_contenu.short_description = 'Aperçu du contenu'

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Contact)
