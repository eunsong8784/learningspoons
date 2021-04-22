#from 다음 마침표의 의미는 현재 디렉토리 혹은 어플리케이션 의미미def post_list(request):


from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})