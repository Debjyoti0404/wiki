from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def default_route(request, name):
    print(name)
    html_content = util.md_to_html(name)
    return render(request, "encyclopedia/content.html", {
        "name": name,
        "contents": html_content
    })

def srch(request):
    if request.method == "POST":
        text = request.POST
        content = text['q']
        for item in util.list_entries():
            if content.lower() == item.lower():
                return redirect(f"wiki/{item}")
 
