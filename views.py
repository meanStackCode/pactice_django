from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html', {'name':'THis is a name to test the word count'})

def countpage(request):
    data = request.GET['fulltextarea']
    word_ls = data.split()
    totalCount = len(word_ls)

    wordDict = {}

    for word in word_ls:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    return render(request, 'count.html', {'fulltext': data, 'totalCount':totalCount, 'wordDictionary':wordDict})

def aboutpage(request):
    return render(request,'about.html')