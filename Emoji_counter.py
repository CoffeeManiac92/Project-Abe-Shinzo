import csv

media = ["CCTV com", "CCTV News", "Huanqiu", "Xinhua"]
type = ["1st Day (Censored)", "2nd Batch", "Common"]
#type = ["2nd Batch fake"]

emoji_count = []


def main(med, typ):
    data_filename = f"Data - {med} {typ}.csv"
    print(f"\nNow processing Abe Shinzo data from: {data_filename}...")
    file = open(data_filename, encoding='utf_16', newline='')
    csvreader = csv.reader(file)
    content = []
    for row in csvreader:
        content.append(row)
    data_filename_2 = f"tempData - {med} {typ} ver 2.csv"
    with open(data_filename_2, 'w', encoding='utf-16', newline='') as f:
        print(f"\nNow writing processed data into: {data_filename_2}")
        for row in content:
            left_b = 0
            #right_b = 0
            f.write(row[0]+'\t')
            for chara in str(row[0]):
                if chara == '[':
                    left_b +=1
                #if chara == ']':
                    #right_b +=1
            f.write(f'{left_b}\t')
            #print(row[0][0:len(row[0])])
            for idx in range(1,len(row[0])):
            #注意range后面是圆括号，两个参数之间用逗号隔开而不是冒号。否则会引起TypeError（Python认为你定义了一个名叫range的列表）。
                if str(row[0])[idx] == '[':
                    end = idx+1
                    txt = '['
                    while str(row[0])[end] != ']':
                        txt += str(row[0])[end]
                        end +=1
                    txt += ']'
                    #保存每个找到的表情符号（不带方括号）
                    if txt not in emoji_lib:
                        emoji_lib.append(txt)
                        emoji_count.append(0)
                    if txt in emoji_lib:
                        emoji_count[emoji_lib.index(txt)] +=1
            #if left_b is not right_b :
                #f.write('not same\t')'''
            #这里为了探测左右方括号出现次数不一样的情况。经过测试，发现没有不一样的，故而删去原语句。
            f.write('\n')
    file.close()

emoji_lib = []

for med in media:
    for typ in type:
        try:
            main(med, typ)
        #因为之前的原始数据格式有时候有问题，多出来的换行会引发本程序的IndexError，所以用了Try。
        except IndexError:
            print (f"Error: List index out of range! Please check later...")

for num in range(0,len(emoji_lib)):
    print(f"{emoji_lib[num]}")
    #print(f"{emoji_count[num]}")
    #print(f"\"{emoji_lib[num]}\", {emoji_count[num]} times")
