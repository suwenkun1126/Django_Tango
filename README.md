# 1.创建项目、创建rango应用、编写视图函数、映射URL
## 创建Django项目
- 创建Django项目:`python manage.py startproject <name>`
## 创建Django应用
- 创建Django应用:`python manage.py startapp <appname>`
- 在**项目配置目录**的settings.py文件中的INSTALLED_APPS列表中加入所创建的应用名字
- 在**应用**的views.py中编写视图函数,返回一个HTTPResponse对象
- 在**应用**的目录下新建urls.py,把入站URL与所写的视图函数对应起来
- 在**项目配置目录**的urls.py文件添加一个映射,指向我们新建的应用
