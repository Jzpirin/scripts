set comparedate=%date:~0,4%%date:~5,2%%date:~8,2%
set comparebegintime=%time%
echo Compare Date:%comparedate%>D:\DBBAK\comparesdb.log &echo Compare Begin Time:%comparebegintime%>>D:\DBBAK\comparesdb.log
cd D:\TOOLS\SetupH3_Yun
DebugTools.exe project=运维--对比数据库 env=测试安装 show=1
set compareendtime=%time%
echo Compare END Time:%compareendtime%>>D:\DBBAK\comparesdb.log
D:
cd D:\DBBAK
tail.exe -30 D:\TOOLS\SetupH3_Yun\DebugTools.log>>D:\DBBAK\comparesdb.log