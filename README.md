HiCTO项目管理
=============


# 准备环境
* Python3 
* virtualenv
* postgres

# 安装

```
virtualenv -p python3 pyenv
source pyenv/bin/activatee
pip install -r requirements.txt
```

# 初始化数据库

```
LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 ./odoo-bin --db_host=127.0.0.1 --db_port=5432 -d $PG_DB -r $PG_USER -w $PG_PASSWORD -i base,project_hicto --without-demo=all
```

# 启动
```
LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 ./odoo-bin --db_host=127.0.0.1 --db_port=5432 -d $PG_DB -r $PG_USER -w $PG_PASSWORD
```

# 访问
http://localhost:8069
默认用户admin:admin
