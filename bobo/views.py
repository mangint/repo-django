from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from datetime import datetime

# Views qui passent diférents types de paramètres
"""
def pass_no_param_to_my_view(request):
	text = 'No param was passed to this view'
	return HttpResponse(text)
"""

# tests des templates generators
def tpl_root(request):
	return render(request, 'tpl_root.html', {'current_date': datetime.now()}) 

def tpl_app(request):
	return render(request, 'tpl_app.html', {'current_date': datetime.now()}) 


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

# tests passage de paramètre
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

def accueil_bobo_app(request, id_article):
	#text = "<h1>J\'ai réussi : 6+6 = {0} et 17 + 17 = {1}</h1>".format(un_deuxieme_nombre_34, un_nombre_12)
	if  int(id_article) == 0:
		return HttpResponse('<h1>Mon article le numéro 0 !</h1>')
	
	if int(id_article) == 1:
		return redirect('bobo.views.param_redirection_chemin')

	if int(id_article) == 2:
		return redirect(param_redirection_fonction)

	if int(id_article) == 3:
		return redirect('param_redir_name')

	return HttpResponse('<h1>Article > 4 !!!</h1>')

# Mes trois views vers lesquelles pointes les 3 types de redirection
# 

def param_redirection_chemin(request):
	return HttpResponse('<h1>Vous avez été redirigé par le chemin!</h1>')

def param_redirection_fonction(request):
	return HttpResponse("Vous avez été redirigé par la fonction view_redirection.")

def param_redirection_name(request):
	return HttpResponse('<h1>Vous avez été redirigé par le nom de la vue</h1>')