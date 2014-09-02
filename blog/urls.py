from django.conf.urls import patterns, url

# !!!!! Ne jamais oublier d'importer les le module appX/views.py 
# autrement Django ne trouvera pas les fonctions
from blog import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

"""
Deux facons d'indiquer à Django où sont les fonctions de appX.views.py 
et de les assigner à une url de appX.urls.py
			=> urlpatterns = pattern('',
					url(r'^/', views.ma_fonction),
					url(r'^/, 'appX.views.mafonction'),   => ajoute directement le 1er paramètre passé à pattern() en début de chemin
		(! DANGER!)	url(r'^/', views.ma_fonction.as_view())
			=> urlpatterns = pattern('appX.views',
				url(r'^/', 'nom_de_ma_fonction_view')
"""

urlpatterns = patterns('',
	url(r'^(\d+)/$', views.accueil_bobo_app),

# test sur le renvoi de données de la BDD dans le template
	url(r'^url_view_bdd_tpl/$', views.url_view_bdd_tpl),
	url(r'^url_view_bdd_tpl/(?P<id>\d+)$', views.url_id_view_bdd_tpl),

#test sur la génération de templates
	url(r'^tpl_app/$', views.tpl_app),
	url(r'^tpl_root/$', views.tpl_root),
	url(r'^tpl_app/addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)$', views.tpl_addition),

# 2,5 façons d'indiquer comment aller cehrcher la fonction view à aller chercher
	url(r'^facon_chercher_fonction_dans_module_importe_views', views.chercher_fonction_dans_module_importe_views),
	url(r'^facon_appX/views/chercher_par_ce_chemin', 'blog.views.chercher_par_ce_chemin'),
#	url(r'^facon_fonction_avecparentheses', views.test_aller_chercher_ma_fonction_view_avecparentheses()),

# passage de 3 types de paramètres aux fonctions views
	url(r'^param/d/(?P<param_digit>\d+)/$', views.pass_param_to_my_view_digit),
	url(r'^param/w/(?P<param_str>\w+)/$', views.pass_param_to_my_view_w),
	url(r'^param/regex/(?P<param_regex>[0-9a-zA-Z]+)/$', views.pass_param_to_my_view_regex),

# support pour tester les 3 types de redirections dans les views
	url(r'^redirection/(\d+)$', views.accueil_bobo_app),
	url(r'^redirection_chemin/$', views.param_redirection_chemin),
	url(r'^redirection_fonction/$', views.param_redirection_fonction),
#	url(r'^redirection_nom_vue/$', 'bobo.views.param_redirection_nom_vue', name="youlou"),
	url(r'^redirection_nom_vue/$', views.param_redirection_view_name, name="view_youlou"),
)

urlpatterns += staticfiles_urlpatterns()

"""
urlpatterns = patterns('bobo.views',

	url(r'^(\d+)/$', 'accueil_bobo_app'),

# test sur les passages de paramètres par l'url
	url(r'^param/d/(?P<param_digit>\d+)/$', 'pass_param_to_my_view_digit'),
	url(r'^param/w/(?P<param_str>\w+)/$', 'pass_param_to_my_view_w'),
	url(r'^param/regex/(?P<param_regex>[0-9a-zA-Z]+)/$', 'pass_param_to_my_view_regex'),

# test sur les redirections
	url(r'^redirection_chemin/$', 'param_redirection_chemin'),
	url(r'^redirection_fonction/$', 'param_redirection_fonction'),
#	url(r'^redirection_nom_vue/$', 'bobo.views.param_redirection_nom_vue', name="youlou"),
	url(r'^redirection_nom_vue/$', 'param_redirection_name', name="param_redir_name"),

)
"""
