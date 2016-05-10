# serverapi
顺道儿服务端(后台服务接口)

### 本地运行
1. git clone https://github.com/carpaanddonkey/serverapi.git
2. cd serverapi
3. 确保本地数据库的配置正确(MySQL,数据库名、用户名、密码都是：byway)
4. 执行命令 python manage.py syncdb
5. 运行脚本startserver.sh或执行python manage.py runserver 0.0.0.0:8000(推荐执行startserver.sh)
6. 退出用ctrl+c

### Celery相关
1. 启动Celery worker: python manage.py celery worker --loglevel=info
2. 启动Celery beat(用于定时任务): python manage.py celery beat

### 架构设计、简洁开发流程参见Wiki  
[ServerAPI顺道儿服务架构设计](https://github.com/carpaanddonkey/serverapi/wiki/ServerAPI顺道儿服务架构设计)

@ByWay 
