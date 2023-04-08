# Lesson 01 后端基础

## 一、Linux运维基础
   终端软件推荐使用 windterm
   推荐课程[黑马程序员新版Linux零基础快速入门到精通](https://www.bilibili.com/video/BV1n84y1i7td?p=41&vd_source=600ade11f4b28f4c8a22c9f96b7acd69)

   ### 1.基础命令
   - 文件列表 ls -al
   - 目录切换 cd ..
   - 当前目录 pwd
   - 移动文件 mv
   - 删除文件 rm -rf
   - 查看文件 cat
   - 创建目录 mkdir
   - 创建文件 touch   
   - 文件查找 find
   - 文件路径 which
   - 文件权限 chmod +r +w +x
   - 文件归属 chown
   - 查询 grep
   - 进程查看 ps -ef 
   - 管道命令 |
   - 网络查看 netstat -nal
   - 网卡查看 ifconfig -nal
   - 清屏 clear
   - 终止 ctrl + c  ctrl + \
   - 切换shell chsh -s /bin/zsh
   - 软连接 ln -s
   - 日期时间 date

   ### 2.运维命令
   - 别名 alias ll ls -al
   - 环境变量文件 cat ~/.zsh
   - 用户管理 useradd
   - 群组管理 groupadd
   - 密码修改 passwd
   - 包安装 yum apt-get
   - 安装oh-my-zsh
   - root身份 sudo
   - 机器运行状态 top   
   - 文件压缩 tar -cvzf 
   - 文件解压 tar -zxvf
   - zip压缩 zip  gzip 
   - zip 解压 unzip gunzip 
   - 远程连接 telnet ssh
   - 软件启动 systemctl


   ### 3.复杂命令
   - [Vim编辑器常用命令](https://blog.csdn.net/zhang_yu_ling/article/details/103777714)
   - [git常用命令速查表](https://www.w3cschool.cn/git/git-cheat-sheet.html)
   -  [Docker常用命令](https://blog.csdn.net/qiaoshaw/article/details/117048140)   
   -  [一篇教会你写90%的shell脚本](https://zhuanlan.zhihu.com/p/264346586) 了解即可


## 二、软件工程

   推荐电影，[《黑客帝国 The Matrix》](https://movie.douban.com/subject/1291843/)
   ### 1. 软件工程
   推荐书籍，[《人月神话》](http://product.dangdang.com/25295797.html)
   软件工程主要用于解决问题，因此一定要多写项目；
   项目是用技术编写能够解决问题、实现需求的具体工具，这个工具能够运行于计算机的世界，硅基世界；
   软件工程相对于建筑工程、机械工程有类似的模式可以参考；但另一方面又有其独特的特点，更加强调智慧协作，因此衍生出敏捷开发；
   

   ### 2. 项目过程
   - 业务设计：从现实中总结出规则和流程，比如游戏中的梳理背景、玩法、主要元素、运作规则.
   - 架构设计：根据业务选择适合的技术体系设计合理的程序，比如程序结构、技术体系、美术设计.
   - 技术实现：落实到工程代码、资源文件、运行环境

   ### 3. 能力要求
   - 对现实的总结能力 + 过关的工程技术能力
   - 写不出代码?
      - 先理思路，找到可以模拟的对象，梳理规则和运作逻辑
      - 比如炒菜:起锅烧油下菜翻炒放调料.
   - 程序结构设计
      - 经验的积累需要时间，完美也是需要阶段去逐渐优化
      - 由能用到能更好的用，能解决问题到能更好的解决问题
   - 技术分层
      - 第一层：奠定学科基础的体系结构，计算机是什么?怎么构成?核心是追求更快的速度
      - 第二层：给技术从业者使用的技术工具，比如开发C、C++、Java这类编程语言本身，开发数据库这类存储工具
      - 第三层：解决现实需求的产品应用，比如写个APP、写个网页等等
      - 第四层：计算机结合某个领域的特定解决方案，比如CAD这类工业软件、医学人工智能、计算化学、地理信息这类自成一派的交叉学科
      - 第五层:科技是第一生产力
   ### 4. 开发过程
   - 使用第二个层面设计好的技术工具去完成第三层面设计好的具体产品开发
   - 如果现有的工具并不能完全满足需求，必要的情况下可以自己去设计一些技术工具
   - 小公司以用现成技术工具为主，更强调员工技能的广度
   - 大公司会研发技术工具，有自己的技术体系，更强调员工基础扎实
   
   ### 5.三层开发架构 MVC
   演示层：前端，负责用户交互，形式有app、客户端、小程序、网页。。。
   应用层：后端，负责业务逻辑处理，比如权限、下单等
   数据层：负责数据存储、处理和维护，比如数据库、文件等

   ### 6.领域驱动设计 DDD
   实现中台（分层）和微服务化（模块化）


   ### 7. 敏捷开发模型
   对应于瀑布开发模型，参考精益思想
   应对需求的快速变化；
   参考课程： [敏捷开发管理](https://www.bilibili.com/video/BV1pz4y1R7WK/)


## 三、Python编程基础
   ### 1. 开发环境
   - vs
      - copilot
      - copilot labs
      - cursor code
   - pycharm

   ### 2. python语言基础
   参考图书： [人工智能开发语言：Python](https://weread.qq.com/web/bookDetail/a7232a1071c95f09a7256dc)、[Python编程从小白到大牛](https://weread.qq.com/web/bookDetail/、[Effective Python：编写高质量Python代码的90个有效方法（原书第2版）](https://weread.qq.com/web/bookDetail/c2932f9072620d81c29c1ed)af832c5072398304af8d0b2)、[编写整洁的Python代码（第2版）](https://weread.qq.com/web/bookDetail/1e632a60813ab73e5g015988)
   图书阅读建议采用查阅式；

   - 基本语法可以在B站自主学习
   - 重要概念
     - [浅析Python的进程、线程与协程](https://zhuanlan.zhihu.com/p/445467379)
     - [python的列表，字典，元组，集合的区别和各自使用方法](https://blog.csdn.net/qq_42554007/article/details/90489570)
     - [python try 异常处理](https://zhuanlan.zhihu.com/p/63877158)
     - [Python3包管理](https://blog.csdn.net/Pythonlaowan/article/details/101290087)
     - 面向对象 Class
     - 网络编程 
     - Web应用



