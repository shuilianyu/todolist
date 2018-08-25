from django.shortcuts import render
def home(req):
    if req.method == 'GET':
        return render(req,'index.html')