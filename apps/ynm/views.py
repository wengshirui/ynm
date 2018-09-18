from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 这里是处理业务逻辑的地方，比如y=3x，这里写的就是这样的逻辑

def index(request):
    return render(request,'index.html')
