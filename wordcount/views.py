from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, "home.html")

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    mostfreq = None
    maxtimes = 0
    for x in wordlist:
        if wordlist.count(x) > maxtimes:
            mostfreq = x
            maxtimes = wordlist.count(x)
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    ordered = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)


    return render(request, "count.html",
                  {'fulltext':fulltext,
                   'count':len(wordlist),
                   'winnerword':mostfreq,
                   'winnertimes': maxtimes,
                   'worddictionary':ordered
                   }
        )

def aboutme(request):
    return render(request, 'about.html')
