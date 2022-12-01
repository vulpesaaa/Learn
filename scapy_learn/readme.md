## scapy 库的学习
## 小例子
### 1.构造随机IP的数据包，并保存为pcap包
### 2.渗透测试，安装环境
2.1 安装虚拟机VMware16，虚拟机可以构建计算机网络，不会影响到真实的机器
下载安装包，破解版
2.2 下载kail虚拟机版
https://www.kali.org/get-kali/#kali-live
选择VMware虚拟机版
参考下列导入
https://www.kali.org/docs/virtualization/import-premade-vmware/
下载VMware虚拟机版是.7z后缀的安装包，使用7z解压安装包后，直接VMware打开解压的文件即可导入成功。
默认用户名/密码：kali/kali
普通版安装
https://blog.csdn.net/qq_42545206/article/details/82788119

2.3 安装VMwaretools
主要是VMware增强模拟显卡和硬盘性能、同步虚拟机与主机时钟的驱动程序。

主机与虚拟机之间的文件共享

2.4 升级操作系统
2.4.1 查看操作系统

cat /etc/issue

查看内核信息
uname -a

2.4.2 图形界面升级
应用程序。。。。系统工具。。。。软件更新

命令行升级
update更新软件列表信息，包括版本和依赖关系等
dist-upgrade 改变配置文件，改变旧的依赖关系，升级操作系统等

sudo apt update
sudo apt dist-upgrade
