from django.conf.urls import url

from users import views

urlpatterns = [
    # 测试视图路由
    url(r'^test/$', views.test),

]
