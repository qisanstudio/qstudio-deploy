```Shell
sudo apt-get install postgresql

# http://stackoverflow.com/questions/17399622/postgresql-9-2-installation-on-ubuntu-12-04
sudo pg_createcluster 9.3 main --start

$ sudo service postgresql restart   # 重启DB
$ sudo su postgres                  # 切到 postgres 用户
postgres=# createuser username -P   # 新建用户
postgres=# dropuser username        # 删除用户
postgres=# createdb dbname -Ousername   为username 用户创建数据库
```

完美卸载
```Shell
sudo apt-get --purge remove postgresql
dpkg -l | grep postgres
sudo apt-get --purge remove # those dpkg list front

sudo rm -rf /var/lib/postgresql
sudo rm -rf /var/log/postgresql
```

全新安装
```Shell
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo dpkg-reconfigure locales
sudo pg_createcluster 9.3 main --start

```