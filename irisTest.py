from sklearn import svm,metrics
import random,re

csv = []
with open('iris.csv','r',encoding='utf-8') as fp:
    #한줄에 읽기
    for line in fp:
        line = line.strip()   #/n 줄바꿈 제거
        cols = line.split(',') #쉼표로 자르기
        # 문자열데이터를 숫자로 변환
        fn = lambda n: float(n) if re.match(r'^[0-9\.]+$',n) else n  #n이 숫자이면 실수로 처리하고 문자면 그대로....
        cols = list(map(fn,cols))
        # for c in cols:
        #   temp = fn(c)
        #   cols.append(temp)
        csv.append(cols)

    del csv[0]            #가장 앞 줄의 헤더 제거
    random.shuffle(csv)          #데이타 랜덤으로 섞기

    total_len = len(csv)
    train_len = int(total_len*2/3)
    train_data = []
    train_label = []
    test_data = []
    test_label =[]

    for i in range(total_len):
        data = csv[i][0:4]
        label = csv[i][4]
        if i < train_len:
            train_data.append(data)
            train_label.append(label)
        else:
            test_data.append(data)
            test_label.append(label)

    clf = svm.SVC()
    clf.fit(train_data,train_label)
    pre = clf.predict(test_data)

    ac_score = metrics.accuracy_score(test_label,pre)
    print("정답률",ac_score)



