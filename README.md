Django 项目配置与数据库修改流程

**1. 配置邮箱服务（以 QQ 邮箱为例）**

1.1 修改 settings.py

在 blog_project/blog_project/settings.py 中添加或修改以下配置：

`EMAIL_HOST_USER = 'your_email@qq.com'  # 你的QQ邮箱

EMAIL_HOST_PASSWORD = 'your_authorization_code'  # 邮箱授权码（非登录密码）`

1.2 如何获取QQ邮箱授权码？

登录QQ邮箱 → 设置 → 账号

找到 POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务

开启 IMAP/SMTP服务，按提示生成授权码（16位字符串）

**2. 启动开发服务器**

在项目根目录（blog_project/）下运行：`python manage.py runserver`

**3. 修改数据库模型后的操作**

如果修改了 models.py（如新增字段、修改表结构），需按以下步骤更新数据库：

生成迁移文件，在项目根目录下运行：`python manage.py makemigrations `

应用迁移到数据库，接着运行：`python manage.py migrate`
