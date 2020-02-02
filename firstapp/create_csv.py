import pandas as pd
# 데이터베이스에 있는 환자들에 대한 정보를 csv로 저장

def MakeCSV(records):
    tmp1 = []
    tmp2 = []
    tmp3 = []
    tmp4 = []
    tmp5 = []

    for record in records:
        tmp1.append(record['tmp1'])
        tmp2.append(record['tmp2'])
        tmp3.append(record['tmp3'])
        tmp4.append(record['tmp4'])
        tmp5.append(record['tmp5'])

    data = {
        "tmp1" : tmp1,
        "tmp2" : tmp2,
        "tmp3" : tmp3,
        "tmp4" : tmp4,
        "tmp5" : tmp5,
    }

    # 데이터 프레임 만들고 -> csv파일로 저장
    df = pd.DataFrame(data)
    # 인코딩 옵션으로 한글 깨지는거 해결!, index, 속성 필드 없애줌
    df.to_csv('./database.csv', encoding='euc-kr')
