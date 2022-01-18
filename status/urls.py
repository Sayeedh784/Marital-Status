from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
  path('',views.home,name='home'),
  path('register/',views.marriageregister,name='register'),
  path('bridenid/',views.checkbridesNid,name='bridenid'),
  path('bridebc/',views.checkbridesbc,name='bridebc'),
  path('bridepassport/',views.checkbridespp,name='bridepp'),

  path('groomsnid/',views.checkgroomsNid, name='groomsnid'),
  path('groomsbc/',views.checkgroomsbc, name='groomsbc'),
  path('groomspp/',views.checkgroomspp, name='groomspp'),
  path('bridenidshow/',views.checkbridesNid,name='bridenidshow'),
  # path('generatepdf/',views.generatepdf,name='generatepdf'),
  # path('pdf/',views.generatepdf,name='pdf')
  # path('bridenid/success/',views.success),
  # path('bridenid/fail/',views.fail)
  #path('test/', views.render_pdf_view,name='test-view'),
  #path('list/', views.CustomerListview.as_view(),name='list-view'),
  path('pdf/<int:pk>/', views.customer_render_pdf_view,name='pdf-view'),
 #path('create-pdf', views.pdf_report_create, name='create-pdf'),
  
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)