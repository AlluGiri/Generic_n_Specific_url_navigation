from specific.views import*
from django.urls import path
app_name='some'

urlpatterns=[
    path('sweety/',sweety,name='sweety'),
    # path('babblu/',babblu,name='babblu'),
]
