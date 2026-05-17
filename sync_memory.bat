copy /y "你的聊天记录路径\Mylovestory.txt" "C:\Users\Administrator\Mylovestory\Mylovestory.txt"
cd /d C:\Users\Administrator\Mylovestory
git add .
git commit -m "自动同步 %date% %time%"
git push