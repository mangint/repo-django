from django import forms
from models import Article

class ArtcileForm(forms.ModelForm):
	class Meta:
		model = Article
		exclude = ('auteur', 'categorie')
		fields = ('titre','contenu')

class ContactForm(forms.Form):
	sujet = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	envoyeur = forms.EmailField(label="Votre adresse mail")
	renvoi = forms.BooleanField(required=False, help_text="Cochez si vous souhaitez obtenir une copie du mail emvoyé")
