from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Result
import json

import requests
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseForbidden
import datetime
import os

import re
# Create your views here.
sent = ""

def home(request):
    if request.method == 'POST':
        global sent
        sent = request.POST.get('fname')
        print(sent)
        return redirect(reverse('compute_results'))

    elif request.method == 'GET':
        return render(request, 'incapp/index.html')

def compute_results(request):
    # if request.method == 'POST':
    #     data = request.POST.get(fname)
    #     print(data)

    API_TOKEN = "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"
    API_URL = "https://api-inference.huggingface.co/models/l3cube-pune/hate-multi-roberta-hasoc-hindi"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    def query(payload):
        dataJson = json.dumps(payload)
        response = requests.request("POST", API_URL, headers=headers, data=dataJson)
        return json.loads(response.content.decode("utf-8"))

    data = query(sent)
    result = [res["score"] for res in data[0]]
    tweet_result = Result(sent_text=sent, hate_label=0.90, offn_label=0.05, prfn_label=0.02, not_label=0.03)
    tweet_result.save()

    return redirect(reverse('home'))

def tweets_pool(request):
    # if request.method == 'POST':
    #     data = request.POST.get(fname)
    #     print(data)
    all_tweets = Result.objects.all()
    print(len(all_tweets))
    return render(request, 'incapp/Page2.html', context={'all_tweets': all_tweets})



