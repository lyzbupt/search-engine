from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse, FileResponse
from .query import search_engine



def home(request):
    if request.method == "GET":
        print("home get ")
        funcID = request.GET.get("funcID", None)
        # upload file, if existed, it will be override
        if funcID == "1":
            try:
                input = request.GET.get('q')
                se = search_engine()
                query = input
                hits, snippets = se.query(query)  #
            except KeyboardInterrupt as e:
                print('\nExit.')
            except Exception as e:
                print(e)
            print("home get and return")
            return render_to_response('index.html',{'hits': hits, 'snippets': snippets})

    return render_to_response("home.html")