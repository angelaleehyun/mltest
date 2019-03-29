from sklearn import svm

xor_data = [[0,0,0],[0,1,1],[1,0,1],[1,1,0]]

data = []
label = []
for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p,q])
    label.append(r)

clf = svm.SVC()
clf.fit(data, label)

pre = clf.predict(data)
print("예측결과:", pre)

ok= 0
total = len(label)
for i in range(len(label)):
    answer = label[i]
    p = pre[i]
    if answer == p:
        ok = ok +1
print("예측결과:", ok/total)