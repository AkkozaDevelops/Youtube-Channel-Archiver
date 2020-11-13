@echo off
cls

echo Attempting to upgrade pip

py -m pip install --upgrade pip

pip install youtube-dl
pip install pytube

echo  
echo  
echo  
echo  
echo Installed all packages.
pause