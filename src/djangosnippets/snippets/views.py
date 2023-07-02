from django.shortcuts import render
from django.http import HttpResponse
from snippets.models import Snippet

# Create your views here.
def top(request):
    snippets = Snippet.objects.all()
    context = {"snippets":snippets}
    return render(request, "snippets/top.html", context)

def snippet_new(request):
    return HttpResponse("新規作成")

def snippet_edit(request):
    return HttpResponse("編集")

def snippet_detail(request):
    return HttpResponse("詳細")
