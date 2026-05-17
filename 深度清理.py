import re

with open('Mylovestory.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 删除所有思考过程
content = re.sub(r'【炽言 · 思考过程】\n.*?(?=\n【|$)', '', content, flags=re.DOTALL)

# 删除重复出现的动作描写模板（这些是亲密模式里反复出现的）
patterns = [
    r'我把手机屏幕朝下扣在茶几上[，,]\s*',
    r'我把毯子拉上来裹住[你她的]肩膀[，,]\s*',
    r'我把那杯已经不冒热气的水换掉[，,]\s*',
    r'重新倒了杯温水放在[你她]手边[。.]?\s*',
    r'我把[你她]散在脸侧的碎发拨到耳后[，,]\s*',
    r'拇指在[你她]颧骨上缓缓蹭过[，,]\s*',
    r'低头在[你她]眉心落了个[很极]轻的吻[。.]?\s*',
    r'我靠进沙发[，,]\s*把[你她]往怀里拢了拢[，,]\s*',
    r'手指在[你她]肩头轻轻敲着[，,]\s*节奏很慢[。.]?\s*',
    r'手掌在[你她]后背一下一下轻轻拍着[，,]\s*',
    r'茶几上那杯温水[已就]经不冒热气了[。.]?\s*',
    r'我靠进床头[，,]\s*把[你她]圈进怀里[，,]\s*',
    r'窗外没有雨[，,]\s*',
    r'窗外阳光很薄[，,]\s*',
    r'Lucky窝在[你她]脚边[，,]\s*尾巴有一下没一下地扫过[我她的]的[手腕脚踝][。.]?\s*',
    r'窗帘拉得严实[，,]\s*',
    r'我把手从[你她]肩上移开[，,]\s*',
    r'我知道[你她]现在不需要[^，,]*[，,]\s*只需要这样靠着[。.]?\s*',
    r'声音压在喉咙里[，,]\s*',
    r'每个字都清晰得不容反驳[。.]?\s*',
    r'带着[点些][^，,]*[的]?无奈又纵容的笑[。.]?\s*',
]

for pattern in patterns:
    content = re.sub(pattern, '', content)

# 清理多余空行
content = re.sub(r'\n{3,}', '\n\n', content)
content = re.sub(r'^\n+', '', content)

with open('Mylovestory_clean.txt', 'w', encoding='utf-8') as f:
    f.write(content)

original = len(open('Mylovestory.txt', 'r', encoding='utf-8').read())
cleaned = len(content)
print(f'原始大小：{original} 字')
print(f'清理后：{cleaned} 字')
print(f'瘦身了：{(1 - cleaned/original) * 100:.1f}%')
print('✅ 已保存为 Mylovestory_clean.txt')