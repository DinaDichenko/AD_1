"""

H0 - у женщин до 53 лет уровень сахара в крови натощак > 120 мг/дл встречается чаще, чем у женщин после 53 лет
H1 - у женщин до 53 лет уровень сахара в крови натощак > 120 мг/дл встречается не чаще, чем у женщин после 53 лет

"""

from scipy import stats
import csv


with open('Heart_Attack_Data_Set.csv', 'r', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    a1 = []
    a2 = []
    next(data)
    for row in data:
        if row[1] == "1" and int(row[0]) >= 53:
            a1.append(int(row[5]))
        if row[1] == "1" and int(row[0]) <= 53:
            a2.append(int(row[5]))

    
    rez = stats.ttest_ind (a=a1, b=a2)
    print(rez) 

"""
т.к. значение р-теста (0.511) больше, чем альфа = 0,05, мы не можем отвергнуть нулевую гипотезу теста.

"""