set bakdate=%date:~0,4%%date:~5,2%%date:~8,2%
set backuptime=%time%
echo Backup Date:%bakdate%>D:\DBBAK\backup.log &echo Backup Time:%backuptime%>>D:\DBBAK\backup.log
cd D:\TOOLS\SetupH3_Yun
DebugTools.exe project=升级--分片A--备份数据 env=测试安装 show=1
echo Backup Success and Begin Winrar>>D:\DBBAK\backup.log
"D:\Program Files (x86)\WinRAR\WinRAR.exe" a D:\DBBAK\DBBAK_%bakdate%.rar dbbak
echo ALL Success>>D:\DBBAK\backup.log
pause