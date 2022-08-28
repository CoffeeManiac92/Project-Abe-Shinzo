import csv

media = ["CCTV com", "CCTV News", "Huanqiu", "Xinhua"]
type = ["1st Day (Censored)", "2nd Batch", "Common"]
#type = ["2nd Batch", "Common"]
#type = ["2nd Batck fake"]

#测试区

#定义主程序
def purify(med, typ):
    data_filename = f"Data - {med} {typ}.csv"
    print(f"\nNow processing Abe Shinzo data from: {data_filename}...")
    file = open(data_filename, encoding='utf_16', newline='')
    csvreader = csv.reader(file)
    content = []
    for row in csvreader:
        content.append(row)
    data_filename_purified = f"Purified Data - {med} {typ}.csv"
    with open(data_filename_purified, 'w', encoding='utf-16', newline='') as f:
        print(f"\nNow writing processed data into: {data_filename_purified}")
        for row in content:
            #把\t换成别的字符串，以免之后无法扫描出来
            r_row = str(row[0]).replace("\t", "%t")
            new_text = r_row[0:3]
            idx = 3
            #这里要注意，跳过3个而不是4个字符。之前跳过4个字符导致采用“时间”而非“时间1/2”的Common数据无法被处理
            t_count = 0
            print(r_row)
            #去除回复头
            while t_count <3:
                new_text += r_row[idx]
                idx += 1
                if r_row[idx-2:idx] == "%t":
                    t_count += 1
            if len(r_row)>idx+4:
                #print("long comment")
                initial4 = str(r_row[idx:idx+4])
                if initial4 == "回复 @":
                    idx += 5
                    while str(r_row[idx-2:idx]) != " :":
                        idx += 1
                # 去除表情符号
                # 现在idx是冒号之后的第一个字符
            ok = True
            temp_txt = ""
            for idx_2 in range(idx, len(r_row)):
                if r_row[idx_2] in ["[", "]"]:
                    ok = False
                if r_row[idx_2 - 1] == "]" and (r_row[idx_2] != "["):
                    ok = True
                if ok:
                    temp_txt += r_row[idx]
                idx += 1
            if temp_txt != "":
                print("将该评论输出到文件：", temp_txt)
                new_text += temp_txt
                new_text = new_text.replace("%t", "\t")
                f.write(new_text)
                f.write('\n')
            else:
                print("该评论仅包含表情符号，不输出到文件！")
    file.close()

emoji_lib = []

#执行主程序
for med in media:
    for typ in type:
        try:
            purify(med, typ)
        #因为之前的原始数据格式有时候有问题，多出来的换行会引发本程序的IndexError，所以用了Try。
        except IndexError:
            print (f"Error: List index out of range! Please check later...")

#purify(media[1], type[2])

