# 對話統計，傳幾個字，傳幾個貼圖/圖片
# [:3] => 0~3，0可省略(不包括3)
# [2:4] => 2~4(不包刮4)
# [-2:] => 倒數第2個位置，到最後

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            line = line.strip()
            lines.append(line)
        return lines

def conv(lines):
    allen_w_c = 0
    allen_s_c = 0
    allen_i_c = 0
    viki_w_c = 0
    viki_s_c = 0
    viki_i_c = 0
    for line in lines:
        line = line.split(' ')
        time = line[0]
        name = line[1]
        if name == 'Allen':
            if line[2] != '貼圖' and line[2] != '圖片':
                for word in line[2:]:
                    allen_w_c += len(word)
            elif line[2] == '貼圖':
                allen_s_c += 1
            elif line[2] == '圖片':
                allen_i_c += 1
        elif name == 'Viki':
            if line[2] != '貼圖' and line[2] != '圖片':
                for word in line[2:]:
                    viki_w_c += len(word)
            elif line[2] == '貼圖':
                viki_s_c += 1
            elif line[2] == '圖片':
                viki_i_c += 1

    print('Allen傳了', allen_w_c, '字')
    print('Allen傳了', allen_s_c, '貼圖')
    print('Allen傳了', allen_i_c, '圖片')
    print('Viki傳了', viki_w_c, '字')
    print('Viki傳了', viki_s_c, '貼圖')
    print('Viki傳了', viki_i_c, '圖片')

def write_file(filename, lines):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for line in lines:
            line = line + '\n'
            f.write(line)

def main():
    lines = read_file('LINE-Viki.txt')
    lines = conv(lines)
    # write_file('output.txt', lines)

main()