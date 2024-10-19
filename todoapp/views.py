from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from todoapp.models import Task

# Create your views here.
class TaskList(LoginRequiredMixin, ListView): #djangoが用意してくれているクラス
    model = Task
    context_object_name = "tasks" #データを取り出す際の名前の指定
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #親が持っているデータを取得する
        # print(context)
        context["tasks"] = context["tasks"].filter(user=self.request.user) #ユーザーごとにタスクにフィルタリングする
        searchInputText = self.request.GET.get("search") or "" #検索したい値を取りに行く nullの場合空白
        if searchInputText: #値が入力されている場合
            context["tasks"] = context["tasks"].filter(title__startswith=searchInputText) #最初の文字が一致するものだけ取ってくる
        
        context["search"] = searchInputText
        return context
class TaskDetail(LoginRequiredMixin, DetailView): 
    model = Task
    context_object_name = "task"

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "completed"] #必要なデータに絞る
    success_url = reverse_lazy("tasks") #classベース
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks") #classベース

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
    context_object_name = "task"

class TaskListLoginView(LoginView):
    feilds = "__all__"
    template_name = "todoapp/login.html" #templateのフォルだ指定の名前をかえる
    def get_success_url(self):
        return reverse_lazy("tasks")

class RegisterTodoApp(FormView):
    template_name = "todoapp/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("tasks")

    def form_valid(self, form): 
        user = form.save() #保存
        if user is not None:
            login(self.request, user) #認証を行ってくれる
        return super().form_valid(form)


