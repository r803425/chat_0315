# 讀取input產生output檔
# 每行變成人名 + :

# 1.讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            line = line.strip()
            lines.append(line)
        # print(lines)
        # print('-------------------------------------------')
        return lines

# 2.轉換內容
def conv(lines):
    converts = []
    name = None
    for chat in lines:
        if chat == 'Allen' or chat == 'Tom':
            name = chat
        else:
            if name:
                chat = name + ': ' + chat
                print(chat)
                converts.append(chat)
    # print('-------------------------------------------')
    # print(converts)
    # print('-------------------------------------------')
    return converts

# 3.儲存檔案
def write_file(filename, converts):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for convert in converts:
            convert = convert + '\n'
            f.write(convert)

def main():
    lines = read_file('input.txt')
    converts = conv(lines)
    write_file('output.txt', converts)

main()