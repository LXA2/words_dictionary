# 读取文件内容
with open('THUOCL_animal.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 处理每一行，从第一个空格或制表符开始，删除后面的所有内容，保留换行符
processed_lines = []
for line in lines:
    # 找到第一个空格或制表符的位置
    pos_space = line.find(' ')
    pos_tab = line.find('\t')
    
    # 确定最早出现的位置
    if pos_space == -1:
        pos = pos_tab
    elif pos_tab == -1:
        pos = pos_space
    else:
        pos = min(pos_space, pos_tab)
    
    # 如果找到空格或制表符，就截取子串，否则保留整行
    if pos != -1:
        new_line = line[:pos] + '\n'
    else:
        new_line = line
    
    processed_lines.append(new_line)

# 将处理后的内容写回文件
with open('animal.txt', 'w', encoding='utf-8') as file:
    file.writelines(processed_lines)

print("文件处理完成，处理后的内容已写入")
