# 1.创建项目、创建rango应用、编写视图函数、映射URL

## 创建Django项目
- 创建Django项目:`python manage.py startproject <name>`

## 创建Django应用
- 创建Django应用:`python manage.py startapp <appname>`
- 在**项目配置目录**的settings.py文件中的INSTALLED_APPS列表中加入所创建的应用名字
- 在**应用**的views.py中编写视图函数,返回一个HTTPResponse对象
- 在**应用**的目录下新建urls.py,把入站URL与所写的视图函数对应起来
- 在**项目配置目录**的urls.py文件添加一个映射,指向我们新建的应用

# 2.模板的使用

## 模板的创建与使用
- 在templates目录中创建要使用的模板，模板中可以使用Django模板变量或者是模板标签
- 在views.py文件中新建一个所需的视图
- 把视图相关的逻辑写在视图函数中
- 在视图函数中构建一个字典,通过模板上下文穿点给模板
- 使用render()辅助函数生产响应
- 如果还没把视图映射到URL上，修改**项目**的urls.py文件和**应用**的urls.py文件

## 引入静态文件
- 将静态文件如(images、css、js)放在项目的static目录中
- 在模板中应用静态文件
- 在模板中加上`{% load staticfiles %}`,然后使用`{% static "<filename>" %}`标签引入静态文件
