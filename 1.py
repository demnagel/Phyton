# coding:utf-8
import re
from scipy.spatial.distance import cosine

text = open('text.txt', 'r', encoding='utf-8')

def counter(text):
    result = []
    arr = []
    matr = []
    for st in text:
        st = re.sub('[!()\\/?><\d\"\'\.\,-]', '', st)
        st = st.lower().split()
        arr.extend(st)
        matr.append(st)
    res_dict = {el: arr.count(el) for el in arr}

    for str in matr:
        c_str = []
        for word, count in res_dict.items():
            if word in str:
                c_str.append(count)
            else:
                c_str.append(0)
        if result[0]:
            print(cosine(result[0]), c_str)
        result.append(c_str)
    return result
print(counter(text))
