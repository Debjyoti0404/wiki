from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def default_route(request, name):
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
                return redirect('entry_route', item)
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
        form_content = request.POST
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
            return redirect('entry_route', title)
    else:
        return render(request, "encyclopedia/create.html")
    
def edit_pg(request, name):
    if request.method == "POST":
        form_content = request.POST
        edited_content = form_content['content']
        util.save_entry(name, edited_content)
        return redirect('entry_route', name)
    
    else:
        md_content = util.get_entry(name)
        return render(request, "encyclopedia/edit.html", {
            "title_content": name,
            "textarea_content": md_content
        })
    
def random_pg(request):
    content_list = util.list_entries()
    selected_entry = random.choice(content_list)
    return redirect('entry_route', selected_entry)
