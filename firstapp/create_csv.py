import pandas as pd
# 데이터베이스에 있는 환자들에 대한 정보를 csv로 저장

def MakeCSV(records):
    fact = []
    line = []
    date = []
    maker = []
    model = []
    part = []
    fault = []
    cause = []
    phenomenon = []
    measure = []

    for record in records:
        fact.append(record['fact'])
        line.append(record['line'])
        date.append(record['date'])
        maker.append(record['maker'])
        model.append(record['model'])
        part.append(record['part'])
        fault.append(record['fault'])
        cause.append(record['cause'])
        phenomenon.append(record['phenomenon'])
        measure.append(record['measure'])


    data = {
        "fact" : fact,
        "line" : line,
        "date" : date,
        "maker" : maker,
        "model" : model,
        "part" : part,
        "fault" : fault,
        "cause" : cause,
        "phenomenon" : phenomenon,
        "measure" : measure,
    }

    # 데이터 프레임 만들고 -> csv파일로 저장
    df = pd.DataFrame(data)
    # 인코딩 옵션으로 한글 깨지는거 해결!, index, 속성 필드 없애줌
    df.to_csv('./database.csv', encoding='euc-kr')
