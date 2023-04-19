from django.urls import path
from ngblog.views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('story/', Content.as_view(), name='story'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('details/<str:slug>', DetatiledPage.as_view(), name='details'),
    path('create-post/', createPost, name='create'),
    path('update-post/<str:slug>', updatePost, name='update'),
]
