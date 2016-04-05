# serverapi
顺道儿服务端(后台服务接口)

### 本地运行
1. git clone https://github.com/carpaanddonkey/serverapi.git
2. cd serverapi
3. 确保本地数据库的配置正确(MySQL,数据库名、用户名、密码都是：byway)
4. 执行命令 python manage.py syncdb
5. 运行脚本startserver.sh或执行python manage.py runserver 0.0.0.0:8000(推荐执行startserver.sh)
6. 退出用ctrl+c

### 架构设计、编码规范、简洁开发流程等参见Wiki  
[Serverapi WIKI](https://github.com/carpaanddonkey/serverapi/wiki)  
[ServerAPI顺道儿服务架构设计](https://github.com/carpaanddonkey/serverapi/wiki/ServerAPI顺道儿服务架构设计)

@ByWay 
