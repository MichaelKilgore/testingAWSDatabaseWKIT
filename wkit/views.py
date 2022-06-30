from django.shortcuts import render

#@login_required(login_url = login_url)
def index(request):
  return render(request, 'wkit/index.html', {})


