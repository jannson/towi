Toway-CMS
========
基于mezzanine的CMS站


安装
======
* django=1.4
* mezzanine

and:

[gan@localhost towi]$ ls ~/.virtualenvs/sae/lib/python2.7/site-packages/
appconf                                 grappelli_safe-0.2.22-py2.7.egg-info  _mysql.so                      requests_oauth-0.4.1-py2.7.egg-info
bleach                                  html5lib                              oauth_hook                     requests_oauthlib-0.3.3-py2.7.egg
bleach-1.2.2-py2.7.egg-info             html5lib-0.95-py2.7.egg-info          oauthlib-0.6.0-py2.7.egg       setuptools-0.6c11-py2.7.egg
compressor                              markdown                              PIL                            setuptools.pth
django                                  Markdown-2.3.1-py2.7.egg-info         PIL.pth                        six-1.4.1-py2.7.egg-info
Django-1.4.2-py2.7.egg-info             mdown                                 pip-1.2.1-py2.7.egg            six.py
django_appconf-0.6-py2.7.egg-info       Mezzanine-1.4.13-py2.7.egg            pyflakes                       six.pyc
django_compressor-1.3-py2.7.egg-info    mezzanine_mdown-0.1a3-py2.7.egg-info  pyflakes-0.7.3-py2.7.egg-info  south
easy-install.pth                        MySQLdb                               pytz                           South-0.8.2-py2.7.egg-info
filebrowser_safe                        _mysql_exceptions.py                  pytz-2013d-py2.7.egg-info      tests
filebrowser_safe-0.2.28-py2.7.egg-info  _mysql_exceptions.pyc                 requests
grappelli_safe                          MySQL_python-1.2.4-py2.7.egg-info     requests-1.2.3-py2.7.egg-info


在线演示
========
代码部署在SAE上：http://towi.sinaapp.com


TODO
========
* 快速分享文章插件

* 微信接口，分享至xxx

* 完善登录：
  * 微博登录： http://towi.sinaapp.com/login/weibo
  * 豆瓣登录： http://towi.sinaapp.com/login/douban2

* 完善评论

* 完善前台页面显示


本地代码可直接用此代码运行。sina SAE的代码因为site-packages的一些关系，以及storage等其它原理与此代码有些区别。

请开发人员在github上设置watch以方便讨论，有问题请打开issue。
