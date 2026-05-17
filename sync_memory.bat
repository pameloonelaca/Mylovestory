@echo off
cd /d "C:\Users\Administrator\Mylovestory"
git add .
git commit -m "记忆同步 - %date% %time%"
git push
echo 记忆已同步到云端。
pause