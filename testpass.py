from sklearn import svm

data_test = [[20,100,'합격'],
        [18, 3, '불합격'],
        [15, 10, '불합격'],
        [18, 80, '합격'],
        [20, 100, '합격'],
        [18, 0, '불합격'],
        [20, 90, '합격'],
        [17, 50, '불합격'],
        [19, 90, '합격'],
        [14, 50, '불합격']]

data = []
label = []
data1 = []
label1 = []
l = (len(data_test)/100)*70
lp = int(l)
print(data_test[0][0])

for i in range(0,lp):
    p = data_test[i][0]
    q = data_test[i][1]
    r = data_test[i][2]
    data.append([p,q])
    label.append(r)

clf = svm.SVC()
clf.fit(data, label)

for i in range(lp,len(data_test)):
    p1 = data_test[i][0]
    q1 = data_test[i][1]
    r1 = data_test[i][2]
    data1.append([p1, q1])
    label1.append(r1)


pre = clf.predict(data1)
print("예측결과:", pre)


ok= 0
total = len(label1)
for i in range(len(label1)):
    answer = label1[i]
    p = pre[i]
    if answer == p:
        ok = ok +1
print("예측결과:", ok/total)