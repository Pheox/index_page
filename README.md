Installation
------------
$ git clone git@github.com:Pheox/index_page.git

$ cd index_page

$ bash setup.sh



Example of production setup (tested on Debian Wheezy)
-----------------------------------------------------
```
FcgidIPCDir /tmp
AddHandler fcgid-script .fcgi

<VirtualHost *:82>
  DocumentRoot  /home/client/projects/index_page/app/static
  Alias /static /home/client/projects/index_page/app/static
  ScriptAlias / /home/client/projects/index_page/run.fcgi/

  ErrorLog ${APACHE_LOG_DIR}/error.log

  # Possible values include: debug, info, notice, warn, error, crit
  LogLevel debug

  CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
