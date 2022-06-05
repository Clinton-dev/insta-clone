from django.shortcuts import render

posts = [
    {
        "caption":"new cat video",
        "likes": "5",
        "comments": "5",
        "time_posted":"13hours",
        "author": "clint-dev"
    },
    {
        "caption":"new cat video",
        "likes": "5",
        "comments": "5",
        "time_posted":"13hours",
        "author": "clint-dev"
    },
]

def home(request):
    return render(request,"posts/home.html", {"posts":posts})