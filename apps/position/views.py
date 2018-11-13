from django.shortcuts import render
from django.views.generic.base import View
from .models import *
import json
from django.http import HttpResponse

# Create your views here.
class PositionListView(View):
    '''尝试用接口的方式将后台的所有的岗位以json方式传给前端，显示岗位列表'''
    def get(self,request):
        all_position = PositionModel.objects.all() #取出所有的岗位对象，这是一个列表
        posi_names = [position.name for position in all_position] #将所有岗位的名字组成一个列表
        posi_deses = [position.desc for position in all_position] #讲所有岗位的描述组成一个列表
        posi_dicts = []
        for x,y in zip(posi_names,posi_deses):
            '''将每一个岗位的名称和描述读出来，并组合成一个内容为字典的列表'''
            posi_dict = {'岗位名称':x,'岗位描述':y}
            posi_dicts.append(posi_dict)
        return HttpResponse(json.dumps(posi_dicts),content_type='application/json')
