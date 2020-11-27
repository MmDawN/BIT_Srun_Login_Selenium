# 基于Selenium的BIT-Web登录脚本

> 最近有这么个需求，用了几位大佬基于的urlib和request的脚本都出现了假登录的现象，于是乎就基于Selenium写了个脚本实现了一下。

## 1. Selenium与chromedriver安装

可以参考以下链接进行安装与配置
[参考链接](https://www.cnblogs.com/lfri/p/10542797.html)

## 2. 基本逻辑

1.  间隔10s进行数次ping，若ping不通说明网络已断开，执行```login_func```子函数。
2.  在```login_func```中调用```selenium.webdriver```获取校园网登录网页信息。
3.  通过```find_element_by_id```找到用户名与密码输入框，利用```send_keys```输入并登陆。