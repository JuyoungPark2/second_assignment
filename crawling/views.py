from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen
# Create your views here.


def crawling(request):
    html = urlopen(
        'http://computer.cnu.ac.kr/index.php?mid=notice')
    bsObj = BeautifulSoup(html.read(), 'html.parser')
    recent_blog_post = []
    crawled_data = bsObj.find_all('td', {"class": "title"})

    individual_data = []
    for post in crawled_data:
        if post.a.strong is not None:
            recent_blog_post.append(post.a.strong.get_text())
        # individual_data.append(post.find_all('a'))

    # for post2 in individual_data:
    return render(request, 'crawling.html', {"posts": recent_blog_post})
