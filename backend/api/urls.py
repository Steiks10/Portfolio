# from home.views import index, people, login, PersonAPI, PeopleViewSet, RegisterAPI, LoginAPI
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from base.views.company import CompanyViewSet
from base.views.login import RegisterAPI, LoginAPI
from base.views.skill import SkillViewSet
from base.views.course import CourseViewSet
from base.views.project import project_general, project_detail

router = DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'skill', SkillViewSet, basename='skill')
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('project/', project_general),
    path('project/<int:pk>/', project_detail)
]

urlpatterns += router.urls