from django.shortcuts import render, get_object_or_404 #該当するページが無ければ404エラーを返す。
from django.http import HttpResponse
from .models import Post #Postモデルを参照するための定義

def index(request):
    # return HttpResponse("Hello, World! indexページです")
    posts = Post.objects.order_by('-published') #投稿データの配列を格納
    return render(request, 'posts/index.html', {'posts': posts}) #HTML側で「posts」という変数でデータを表示出来る様に宣言
# Create your views here.

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})
