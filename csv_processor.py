import csv

media = ["CCTV com", "CCTV News", "Huanqiu", "Xinhua"]
medium = media[1]
print("\nNow processing Abe Shinzo data from:", medium, "...\n")

csv_name_1st = f"{medium}.csv"
csv_name_2nd = f"{medium} ver 2.csv"
csv_name_common = f"Data - {medium} Common.csv"
csv_name_original = f"Data - {medium} 1st Day (Censored).csv"
csv_name_next_day = f"Data - {medium} 2nd Batch.csv"
print("File 1:", csv_name_1st)
print("File 2:", csv_name_2nd, "\n")

file_1 = open(csv_name_1st)
csvreader_1 = csv.reader(file_1)
file_2 = open(csv_name_2nd)
csvreader_2 = csv.reader(file_2)
content_1 = []
content_2 = []
content_common = []


for row in csvreader_2:
    content_2.append(row)

print("Here are the common comments in both datasets:", "\n")
for row in csvreader_1:
    if row in content_2:
        content_common.append(row)
        print(row)
        num_2 = content_2.index(row)
        del content_2[num_2]
    else:
        content_1.append(row)



print("\nHere are the comments that got censored the next day:\n")
for cc in content_1:
    print(cc)
print("\nHere are the comments that only seen in the second dataset:\n")
for nc in content_2:
    print(nc)

while True:
    try:
        with open(csv_name_original, 'w', encoding='utf-16', newline='') as fp:
            for row in content_1:
                fp.write(row[0]+'\t')
                fp.write(row[1]+'\t')
                fp.write(row[2]+'\t')
                fp.write(row[3]+'\t')
                fp.write('\n')
        break
    except PermissionError:
        input('文件被占用!!! (关闭占用的程序后,回车重试)')

while True:
    try:
        with open(csv_name_next_day, 'w', encoding='utf-16', newline='') as fp:
            for row in content_2:
                fp.write(row[0]+'\t')
                fp.write(row[1]+'\t')
                fp.write(row[2]+'\t')
                fp.write(row[3]+'\t')
                fp.write('\n')
        break
    except PermissionError:
        input('文件被占用!!! (关闭占用的程序后,回车重试)')

while True:
    try:
        with open(csv_name_common, 'w', encoding='utf-16', newline='') as fp:
            fp.write("时间\tuid\t用户名\t评论内容\n")
            for row in content_common:
                fp.write(row[0]+'\t')
                fp.write(row[1]+'\t')
                fp.write(row[2]+'\t')
                fp.write(row[3]+'\t')
                fp.write('\n')
        break
    except PermissionError:
        input('文件被占用!!! (关闭占用的程序后,回车重试)')

file_1.close()
file_2.close()
print("\nTask finished successfully!")

