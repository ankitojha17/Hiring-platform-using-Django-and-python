from django.urls import path
from candidate import views
from django.urls import path
from . import views
urlpatterns = [
     path('dash/',views.candidateHome,name='dash'),
     path('applyjob/<int:id>/',views.applyJob,name='apply'),
     path('applylist/',views.myjoblist,name='mylist'),
     path('bookmark/add/<int:job_id>/', views.add_bookmark, name='add_bookmark'),
     path('bookmark/remove/<int:job_id>/', views.remove_bookmark, name='remove_bookmark'),
     path('bookmarks/', views.view_bookmarks, name='view_bookmarks')

]
