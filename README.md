一、后端启动命令
myproject目录下，执行
```& C:/Users/pku10/AppData/Local/Microsoft/WindowsApps/python3.12.exe c:/Users/pku10/myproject/manage.py runserver```

二、前端启动
frontend目录下，执行

```npm run serve```

三、后台账号密码
admin/qatest11


注意事项：
1、在使用 Vue CLI 时遇到以下错误​
vue : File C:\Users\pku10\AppData\Local\nvm\node_global\vue.ps1 cannot be loaded because running scripts is disabled on this system.
该错误通常是由于 PowerShell 的执行策略限制导致的。​默认情况下，PowerShell 的执行策略设置为“Restricted”，这会阻止脚本的运行。

解决方法：
临时更改执行策略：
在 PowerShell 中运行以下命令，以临时允许脚本执行：
```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process```
此命令仅在当前 PowerShell 会话中生效，关闭 PowerShell 后将恢复默认设置。

永久更改执行策略：
如果您希望永久更改执行策略，可以使用以下命令：
```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser```
这将允许当前用户运行本地脚本，并要求从互联网下载的脚本具有有效的签名。

2、执行"python manage.py createsuperuser"报错django.db.utils.OperationalError: no such table: auth_user。
因为数据库迁移没有成功执行，导致 Django 的数据库表没有正确创建。auth_user 表是 Django 默认的用户认证表，通常在进行数据库迁移时创建
解决方法:
```python manage.py migrate```
这将执行所有未应用的迁移，创建必要的数据库表，包括 auth_user 表。

