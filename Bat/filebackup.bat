set backupdate=%date:~0,4%%date:~5,2%%date:~8,2%
set backupbegintime=%time%
set SrcDir=D:\Filebackup
set DaysAgo=14
echo Backup Date:%backupdate%>D:\Filebackup\backup.log &echo Backup Begin Time:%backupbegintime%>>D:\Filebackup\backup.log
echo f|xcopy Z:\Hq\mktdt00.txt D:\Filebackup\mktdt00_%backupdate%.txt
echo f|xcopy Z:\szhq\sjsxxn.dbf D:\Filebackup\sjsxxn_%backupdate%.dbf
set backupendtime=%time%
echo Backup END Time:%backupendtime%>>D:\Filebackup\backup.log
echo Backup Success>>D:\Filebackup\backup.log
forfiles /p %SrcDir% /s /m *.* /d -%DaysAgo% /c "cmd /c echo del /f /q /a @path"