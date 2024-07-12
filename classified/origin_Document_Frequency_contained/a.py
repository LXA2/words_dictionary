# 读取文件内容
with open('THUOCL_poem.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 处理每一行，删除ASCII码在0到1000之间的字符
processed_lines = []
for line in lines:
    new_line = ''.join(ch for ch in line if ord(ch) > 1000 or ch == '\n')
    processed_lines.append(new_line)

# 将处理后的内容写回文件
with open('../poem.txt', 'w', encoding='utf-8') as file:
    file.writelines(processed_lines)

print("文件处理完成，处理后的内容已写入")
