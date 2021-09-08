from django.contrib import admin
from django.urls import path, include

# from django.http import HttpResponse
# urlpatters > list
# list item syntax > path('PATH/', FUNCTION TO RUN)

# FUNCTION THAT RETURNS SOME DATA
# def projects(request):
#     return HttpResponse('Here are our projects')

# def project(request, pk):
#     return HttpResponse('Single Project' + ' ' + str(pk))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('projects.urls'))
    
]

# GO TO URL http://localhost:8000/projects/
# As there is no home route/path so http://localhost:8000/ > return 404

# path('project/<str:pk>', project, name="project")
# REASON FOR str > in  long term in project we may use the id for UUID > basically number and letters
# path('project/<int:prahlad>', project, name="project") > def project(request, prahlad):
# path('project/<slug:madam>', project, name="project") > def project(request, madam):


# path('',include('projects.urls')) > include all the urls in <APP NAME>.urls ie here projects.urls