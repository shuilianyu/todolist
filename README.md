# todolist

1.下载
  使用git下载：git clone https://github.com/shuilianyu/todolist.git
  
  
  
2.配置MySQL数据库
  使用mysql数据库，在mysql数据库中创建一个database todolist
  并使用utf8的字符集
  之后在项目中todolist/settings.py中配置DATABASES
  添加USER与PASSWORD
  
  
  
  
3.配置环境
  pip install -r requirements.txt
  ps:python 3.6.4
      django 1.11
      
      
      
      
      
4.测试项目
  python manage.py runserver

  
    
    
ps:结构框架
```├── manage.py
├── README.md
├── static
│   ├── css
│   ├── fonts
│   └── js
├── task
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates
│   ├── base
│   ├── index.html
│   ├── mains
│   ├── parts
│   └── user
├── todolist
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── user
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── utils
    ├── decorators.py
    └── __pycache__
