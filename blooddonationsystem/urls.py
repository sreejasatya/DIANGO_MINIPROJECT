from django.conf.urls import url
from blooddonationsystem import views
	
urlpatterns=[
    url(r'^$', views.AboutView,name='about'),
    url(r'^$', views.FeedbackView, name='feedback'),
    url(r'^$', views.ContactView,name='contact'),
    url(r'^$',views.AddView,name='donor'),

    url(r'^Contact_details/$',views.Contact_details,name='Contact_details'),
    url(r'^donor_details_form/$',views.donor_details_form,name='donor_details_form'),
    url(r'^need_blood_details/$', views.need_blood_details, name='need_blood_details')

]
