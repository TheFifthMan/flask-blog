# Flask 初始化模板
## 项目结构
```
app    --------- 应用
   admin  --------- 后台系统蓝图
   index  --------- 初始化蓝图
   auth   --------- 认证/登陆蓝图
   posts  --------- 功能蓝图
   __init__.py ---- app 初始化文件

common --------- 应用需要的功能集合
   email.py ------ 发送邮件功能
   __init__ ------ 空文件

config --------- 配置文件
   __init__.py ----- 初始化文件
   dev.py
   prod.py
   testing.py  ------ 各环境配置文件

e2e    --------- UI 测试
test   --------- 单元测试
.gitignore ----- git 忽略文件
pipfile -------- 虚拟环境安装文件
run.py  -------- 应用运行文件
```