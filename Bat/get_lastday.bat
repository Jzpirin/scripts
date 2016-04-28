@echo off  
set YE=%date:~0,4%  
set MO=%date:~5,2%  
set DA=%date:~8,2%  
set DG=1  
set/a vY1=%YE% %% 400  
set/a vY2=%YE% %% 4  
set/a vY3=%YE% %% 100  
if %vY1%==0 (set var=true) else (if %vY2%==0 (if %vY3%==0 (set var=false) else (set var=true)) else (set var=false))  
set LY=%YE%  
set LM=%MO%  
if %MO:~0,1%==0 (set MO=%MO:~1,1%)  
if %DA:~0,1%==0 (set DA=%DA:~1,1%)  
if %DA% GTR %DG% (set/a LD=%DA%-%DG%) else (  
if %MO%==1 (set/a LY=%YE%-1) & (set/a LM=12) & (set/a LD=31+%DA%-%DG%) else (  
set/a LM=%MO%-1  
if %MO%==3 (if %var%==false (set/a LD=28+%DA%-%DG%) else (set/a LD=29+%DA%-%DG%))  
for %%a in (2 4 6 8 9 11) do (if "%MO%"=="%%a" (set/a LD=31+%DA%-%DG%))  
for %%b in (5 7 10 12) do (if "%MO%"=="%%b" (set/a LD=30+%DA%-%DG%))))  
if %LM% LSS 10 set LM=0%LM:~-1%  
if %LD% LSS 10 set LD=0%LD:~-1%  
set strLstDt=%LY%%LM%%LD%  
echo 昨天的日期为：%strLstDt%  
pause
