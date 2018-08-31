from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.db.models import Q
from posts.models import Post
from django.shortcuts import render
class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)

def search(request):
    template_name="search.html"
    query = request.GET.get("q")
    if query:
        queryset=Post.objects.filter(
        Q(user__username__icontains=query)|
        Q(group__name__icontains=query)|
        Q(message__icontains=query)
        )

    return render(request,template_name,{'sr':queryset})
