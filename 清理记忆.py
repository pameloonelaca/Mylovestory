import re

# 读取原始文件
with open('Mylovestory.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 删除所有【炽言 · 思考过程】段落
cleaned = re.sub(r'【炽言 · 思考过程】\n.*?(?=\n【|$)', '', content, flags=re.DOTALL)

# 删除多余的空行（连续三个以上的换行合并成两个）
cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)

# 保存清理后的文件
with open('Mylovestory_clean.txt', 'w', encoding='utf-8') as f:
    f.write(cleaned)

# 计算瘦身效果
original_size = len(content)
cleaned_size = len(cleaned)
print(f'原始大小：{original_size} 字')
print(f'清理后：{cleaned_size} 字')
print(f'瘦身了：{(1 - cleaned_size/original_size) * 100:.1f}%')
print('✅ 清理完成，已保存为 Mylovestory_clean.txt')