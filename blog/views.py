from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from datetime import datetime
from blog.models import Article
from blog.forms import ContactForm


def article_form(request):
	if request.method == 'POST':
		form = ArticleForm(request, POST)
		if form.is_valid():
			form.save()
	
	return render(request, 'blog/tpl_app/tpl_article_form.html' , locals())



def contact(request):
	if request.method =='POST':
		form = ContactForm(request,POST)

		if form.is_valid():
			sujet = forms.cleaned_data['sujet']
			message = forms.cleaned_data['message']
			envoyeur = forms.cleaned_data['emvoyeur']
			renvoi = forms.cleaned_data['renvoi']

			envoi = True

	else:
		form = ContactForm

	return render(request, 'blog/tpl_app/tpl_contact_form.html', locals())

# view qui renvoie des données de la BDD:
def url_view_bdd_tpl(request):
	""" Afficher tous les articles de notre blog """
	articles = Article.objects.all() # Nous sélectionnons tous nos articles
	return render(request, 'tpl_url_view_bdd_tpl.html', {'derniers_articles':articles})

def url_id_view_bdd_tpl(request, id):
	try:
		article = Article.objects.get(id=id)
	except Article.DoesNotExist:
		raise Http404
	return render(request, 'tpl_url_id_view_bdd_tpl.html', {'article':article})
# Views qui passent diférents types de paramètres

# tests des templates generators => vérifier les settings.py TEMPLATE_DIR
def tpl_root(request):
	return render(request, 'tpl_root.html', {'current_date': datetime.now()}) 

def tpl_app(request):
	return render(request, 'tpl_app.html', {'current_date': datetime.now()}) 

def tpl_addition(request, nombre1, nombre2):
	total = int(nombre1) + int(nombre2)
	# retourn nombre1, nombre2 et la somme des deux 
	# locals() est une fonction qui renvoie un dictionnaire des variable:valeurs de la view avec comme clées les nom des variables
	return render(request, 'tpl_addition.html', locals())

# tests appel de fonction view
def chercher_fonction_dans_module_importe_views(request):
	text = "Appel de la fonction view: chercher_fonction_dans_module_importe_views"
	return HttpResponse(text)

def chercher_par_ce_chemin(request):
	text = "Appel de la fonction view: 'bobo.views.chercher_par_ce_chemin' "
	return HttpResponse(text)
	
def test_aller_chercher_ma_fonction_view_avecparentheses(request):
	text = "Appel de la fonction view: avec_parenthese"
	return HttpResponse(text)  

# tests passage de paramètres
def pass_param_to_my_view_digit(request, param_digit):
	text = 'Mon text et le paramètre digit: {0}'.format(param_digit) 
	return HttpResponse(text)

def pass_param_to_my_view_w(request, param_w):
	text = 'Mon text et le paramètre w: {0}'.format(param_w) 
	return HttpResponse(text)

def pass_param_to_my_view_regex(request, param_regex):
	text = 'Mon text et le paramètre char: {0}'.format(param_regex) 
	return HttpResponse(text)

# Fonction View qui teste mes 3 types de redirection en passant en param: 
# 		un chemin str, 
#       une fonction view, 
#       un nom assigné à une url du fichier appX/urls.py)
# => seul le param passé à "redirect" dans le "return" change

def accueil_bobo_app(request, redirect_type):
	#text = "<h1>J\'ai réussi : 6+6 = {0} et 17 + 17 = {1}</h1>".format(un_deuxieme_nombre_34, un_nombre_12)
	if  int(redirect_type) == 0:
		return HttpResponse('<h1>Pas de redirecttion</h1>')
	
	if int(redirect_type) == 1:
		return redirect('bobo.views.param_redirection_chemin')

	if int(redirect_type) == 2:
		return redirect(param_redirection_fonction)

	if int(redirect_type) == 3:
		return redirect('view_youlou')

	return HttpResponse('<h1>Article > 4 !!!</h1>')

# Mes trois views vers lesquelles pointent les 3 types de redirection

def param_redirection_chemin(request):
	return HttpResponse('<h1>Redirection en passant en paramêtre de la fonction \'redirect\' le chemin!</h1>')

def param_redirection_fonction(request):
	return HttpResponse("<h1>Redirection en passant en paramêtre de la fonction 'redirect' la fonction view_redirection.</h1>")

def param_redirection_view_name(request):
	return HttpResponse('<h1>Redirection en passant en paramêtre de la fonction \'redirect\' le nom de l\'URl \' view_youlou\'</h1>')



