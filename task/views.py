from django.shortcuts import render,redirect
from utils.decorators import login_required
from django.views import View
from task.models import Task

#restful风格创建任务的增删改查
class task_list(View):
    @login_required
    def get(self,req):
        user = req.user
        tasks = Task.objects.filter(user_id=user.id)
        return render(req, 'mains/list.html', {'tasks': tasks, 'user': user})
    @login_required
    def post(self,req):
        title = req.POST['title']
        task = Task(title=title)
        task.user = req.user
        task.save()
        return redirect('/task/task_list/')

#接受get(查询一个),PUT(更新状态),delete(删除)
class task_detail(View):
    @login_required
    def post(self,req,task_id):
        task = Task.objects.get(id = task_id)
        if req.GET['X-Method-Override'] == 'PUT':
            task.completed = not task.completed
            task.save()
            return redirect('/task/task_list/')
        elif req.GET['X-Method-Override'] == 'DELETE':
            task.delete()
            return redirect('/task/task_list/')
