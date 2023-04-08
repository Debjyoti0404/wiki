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
        "type": "str",
        "contents": html_content
    })

def srch(request):
    if request.method == "POST":
        form_content = request.POST
        content = form_content['q']
        for item in util.list_entries():
            if content.lower() == item.lower():
                return redirect(f"wiki/{item}")
        else:
            possible_items = list()
            for item in util.list_entries():
                if content.lower() in item.lower():
                    possible_items.append(item)
            if len(possible_items) != 0:
                return render(request, "encyclopedia/content.html", {
                    "name": "Suggested pages",
                    "type": "list",
                    "contents": possible_items
                })
            else:
                return render(request, "encyclopedia/content.html", {
                    "name": "Error",
                    "type": "str",
                    "contents": "Error, No such entry exists"
                })
            
def create_pg(request):
    if request.method == "POST":
        form_content =  request.POST
        title = form_content['title']
        for item in util.list_entries():
            if title.lower() == item.lower():
                return render(request, "encyclopedia/content.html", {
                    "name": "Error",
                    "type": "str",
                    "contents": "Error, Given entry name already exists"
                })
        else:
            pg_content = form_content['content']
            util.save_entry(title, pg_content)
            return redirect(f"wiki/{title}")
    else:
        return render(request, "encyclopedia/create.html", {
            "textarea_content": ""
        })
