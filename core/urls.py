from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload-document/', views.upload_document_view, name='upload_document'),
    path('upload-questionnaire/', views.upload_questionnaire_view, name='upload_questionnaire'),
    path('questionnaire/<int:pk>/process/', views.process_questionnaire_view, name='process_questionnaire'),
    path('questionnaire/<int:pk>/generate/', views.generate_answers_view, name='generate_answers'),
    path('questionnaire/<int:pk>/review/', views.review_answers_view, name='review_answers'),
    path('questionnaire/<int:pk>/export/', views.export_questionnaire_view, name='export_questionnaire'),
    path('questionnaire/<int:pk>/delete/', views.delete_questionnaire_view, name='delete_questionnaire'),
    path('document/<int:pk>/delete/', views.delete_document_view, name='delete_document'),
    path('answer/<int:pk>/update/', views.update_answer_view, name='update_answer'),
    path('question/<int:pk>/regenerate/', views.regenerate_answer_view, name='regenerate_answer'),
]
