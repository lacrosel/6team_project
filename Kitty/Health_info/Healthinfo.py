# 흡연 유무에 따른 시력 / 청력 / 혈압 / 혈당 / 콜레스테롤 / 간 상태

import csv
import matplotlib.pyplot as plt
import numpy as np
import copy


# CSV 파일 읽어오기.

def compare(input_pr):
    tempList1 = []
    for x in Smoker:
        if x[input_pr] == '-':
            continue
        tempList1.append(x[input_pr])
    # 비흡연자의 건강상태 20% / 50% /80%
    tempList2 = []
    for x in Non_smoker:
        if x[input_pr] == '-':
            continue
        tempList2.append(x[input_pr])
    Smoker1 = round(0.01 * len(tempList1))
    Smoker20 = round(0.2 * len(tempList1))
    Smoker50 = round(0.5 * len(tempList1))
    Smoker80 = round(0.8 * len(tempList1))
    Smoker95 = round(0.95 * len(tempList1))
    nSmoker1 = round(0.01 * len(tempList2))
    nSmoker20 = round(0.2 * len(tempList2))
    nSmoker50 = round(0.5 * len(tempList2))
    nSmoker80 = round(0.8 * len(tempList2))
    nSmoker95 = round(0.95 * len(tempList2))

    tempList1.sort(key=float)
    tempList2.sort(key=float)
    print(f"흡연자의 상위 20%의 수치는 {tempList1[Smoker20]}입니다.")
    print(f"비흡연자의 상위 20%의 수치는 {tempList2[nSmoker20]}입니다.")
    print(f"흡연자의 상위 50%의 수치는 {tempList1[Smoker50]}입니다.")
    print(f"비흡연자의 상위 50%의 수치는 {tempList2[nSmoker50]}입니다.")
    print(f"흡연자의 상위 80%의 수치는 {tempList1[Smoker80]}입니다.")
    print(f"비흡연자의 상위 80%의 수치는 {tempList2[nSmoker80]}입니다.")
    print(f"흡연자의 상위 95%의 수치는 {tempList1[Smoker95]}입니다.")
    print(f"비흡연자의 상위 95%의 수치는 {tempList2[nSmoker95]}입니다.")
    Graphtemp1 = []
    Graphtemp2 = []
    Cnt = 0
    for i in range(0, len(tempList1), Smoker1):
        if Cnt == 99:
            break
        Graphtemp1.append(tempList1[i])
        Cnt += 1
    Cnt = 0
    for j in range(0, len(tempList2), nSmoker1):
        print(Cnt)
        if Cnt == 99:
            break
        Graphtemp2.append(tempList2[j])
        Cnt += 1

    if tempList1[len(tempList1)-1] > tempList2[len(tempList2)-1] :
        ymax = tempList1[len(tempList1)-1]
    else :
        ymax = tempList2[len(tempList2)-1]
    if tempList1[0] < tempList2[0] :
        ymin = tempList1[0]
    else :
        ymin = tempList2[0]
    tempList3 = tempList1 + tempList2
    x = []
    for i in range (0,99):
        x.append(i)
    with open('Compare_list.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerows(Graphtemp1)
    with open('Compare_list2.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerows(Graphtemp2)
    for i in range(0,len(Graphtemp1)):
        Graphtemp1[i] = float(Graphtemp1[i])
    for i in range(0,len(Graphtemp2)):
        Graphtemp2[i] = float(Graphtemp2[i])
    print(Graphtemp1)
    print(Graphtemp2)
    #
    plt.title('Compare')
    plt.plot(Graphtemp2, label='non-Smkoer',marker='o')
    plt.plot(Graphtemp1,label = 'smoker',marker='o')
    plt.legend()
    plt.show()








f = open('Healthinfo.csv', 'rt', encoding='cp949')  # 읽어올 파일.
data = csv.reader(f)
HealthInfo = []
Smoker = []
Non_smoker = []
header = next(data)
print(header)
for line in data:
    for i in range(0, 30):
        if line[i] == '':
            line[i] = '-'
    if line[-6] == '1':
        Non_smoker.append(line)
    else:
        Smoker.append(line)
    HealthInfo.append(line)
f.close()

# 기준년도0,가입자 일련번호1,시도코드2,성별코드3,연령대 코드(5세단위)4,신장(5Cm단위)5,체중(5Kg 단위)6,허리둘레7,시력(좌)8,시력(우)9,청력(좌)10,청력(우)11,
# 수축기 혈압12,이완기 혈압13,식전혈당(공복혈당)14,총 콜레스테롤15,트리글리세라이드16,HDL 콜레스테롤17,LDL 콜레스테롤18,혈색소19,요단백20,혈청크레아티닌21,(혈청지오티)AST22,
# (혈청지오티)ALT23,감마 지티피24,흡연상태25,음주여부26,구강검진 수검여부27,치아우식증유무28,치석29,데이터 공개일자30
select = int(input("데이터를 분류할 기준을 알려주세요. 8.시력(좌) 9.시력(우) 10.청력(좌) 11.청력(우) 12.수축기 혈압 "
                   "13.이완기 혈압 14. 식전혈당 15.총 콜레스테롤 17. HDL 18.LDL 19.혈색소 20.요단백"
                   "22.AST 23.ALT 24.GTP"))
compare(select)
