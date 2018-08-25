from django.shortcuts import redirect

def login_required(func):
    def _is_login(self,req,*args,**kwargs):
        if req.user.is_authenticated:
            return func(self,req,*args,**kwargs)
        return redirect('/user/login/')
    return _is_login