投稿管理系统
==========

某人让我做的一个投稿管理系统，用于管理投递出去的文章。当一段时间过后，如果文章没有被录用，就可以吧这篇文章投给其他杂志。
某人写了很多文章，以至于用excel管理都非常困难了，于是找我做了这么一个系统来管理自己投递的文章。

这是一个很简单的系统，我把它做成了一个单页应用。
使用bootstrap作为前端模板，AngularJs作为前端数据交互，
后端逻辑用web.py实现，数据库采用轻量级的SQLite，并使用sqlAlchemy作为ORM来操作。

整个前后端均采用RESTful的设计模式。
