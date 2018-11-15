# coding:utf-8
import re
from scipy.spatial.distance import cosine

text = open('text.txt', 'r', encoding='utf-8')

def counter(text):
    data = {}
    final = {}
    result = []
    arr = []
    matr = []
    for st in text:
        st = re.sub('[!()\\/?><\d\"\'\.\,-]', '', st)
        st = st.lower().split()
        arr.extend(st)
        matr.append(st)
    res_dict = {el: arr.count(el) for el in arr}
    i = 1
    for str in matr:
        c_str = []
        for word, count in res_dict.items():
            if word in str:
                c_str.append(count)
            else:
                c_str.append(0)
        result.append(c_str)
        final[i] = (round(cosine(result[0], c_str),2))
        i += 1
        data={'word': res_dict, 'matrix':result, 'result':final}
    return data

x = counter(text)
