from django.urls import path
from . import views #.は現在のディレクトリから取得するということ
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete,TaskListLoginView, RegisterTodoApp
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", TaskList.as_view(), name="tasks"), #tasklisという関数を渡している
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"), #taskの番号を自動的に持ってくる その場合<データ型:pk>で取得
                    #pk=主キー
    path("create-task/", TaskCreate.as_view(), name="create-task"),
    path("edit-task/<int:pk>/", TaskUpdate.as_view(), name="edit-task"),
    path("delete-task/<int:pk>/", TaskDelete.as_view(), name="delete-task"),
    path("login/", TaskListLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name='logout'), #next_pageで遷移先を指定
    path('register/', RegisterTodoApp.as_view(), name='register')
    ]