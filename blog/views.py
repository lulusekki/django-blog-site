from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    #TOP画面を表示する関数
    return render(request, 'blog/index.html')

class IndexView(TemplateView):
    #TOP画面を表示するクラス
    template_name = 'blog/index.html'