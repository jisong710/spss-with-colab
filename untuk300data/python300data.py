import random
import string
import numpy as np
import pandas as pd
import seaborn as sn
import statistics as st
import scipy
from scipy.stats import iqr
letters = string.ascii_uppercase
df = pd.DataFrame(columns=['inisial','jeniskelamin','umurtahunbulan','kategoriumur','kelas','terinfeksi','urutanvaksin','p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15','p16','p17','p18','p19','p20','p21','p22','p23','p24','p25','k1','k2','k3','k4','k5','k6','k7','k8','k9','k10','k11','k12','k13','k14','k15','k16','k17','k18','k19','k20','k21','k22','k23','k24','k25','k26'])
for i in range(300):
    inisial = random.choice(letters)
    jeniskelamin = random.choice(['1','2'])
    umurtahun = random.randint(15,18)
    umurbulan = random.randint(0,11)
    terinfeksi = random.choice(['1','2','1','1'])
    if(umurtahun<18):
        if(umurtahun<16):
            kelas = random.randint(1,2)
        else:
            kelas = random.randint(1,3)
        kategoriumur = 2
        urutanvaksin = 2
    else:
        kategoriumur = 3    
        kelas = random.randint(2,3)
        urutanvaksin = random.randint(2,3)
    soalpengetahuan1 = random.randint(0,1)
    soalpengetahuan2 = random.randint(0,1)
    soalpengetahuan3 = random.randint(0,1)
    soalpengetahuan4 = random.randint(0,1)
    soalpengetahuan5 = random.randint(0,1)
    soalpengetahuan6 = random.randint(0,1)
    soalpengetahuan7 = random.randint(0,1)
    soalpengetahuan8 = random.randint(0,1)
    soalpengetahuan9 = random.randint(0,1)
    soalpengetahuan10 = random.randint(0,1)
    soalpengetahuan11 = random.randint(0,1)
    soalpengetahuan12 = random.randint(0,1)
    soalpengetahuan13 = random.randint(0,1)
    soalpengetahuan14 = random.randint(0,1)
    soalpengetahuan15 = random.randint(0,1)
    soalpengetahuan16 = random.randint(0,1)
    soalpengetahuan17 = random.randint(0,1)
    soalpengetahuan18 = random.randint(0,1)
    soalpengetahuan19 = random.randint(0,1)
    soalpengetahuan20 = random.randint(0,1)
    soalpengetahuan21 = random.randint(0,1)
    soalpengetahuan22 = random.randint(0,1)
    soalpengetahuan23 = random.randint(0,1)
    soalpengetahuan24 = random.randint(0,1)
    soalpengetahuan25 = random.randint(0,1)
    soalkepatuhan1 = random.randint(1,5)
    soalkepatuhan2 = random.randint(1,5)
    soalkepatuhan3 = random.randint(1,5)
    soalkepatuhan4 = random.randint(1,5)
    soalkepatuhan5 = random.randint(1,5)
    soalkepatuhan6 = random.randint(1,5)
    soalkepatuhan7 = random.randint(1,5)
    soalkepatuhan8 = random.randint(1,5)
    soalkepatuhan9 = random.randint(1,5)
    soalkepatuhan10 = random.randint(1,5)
    soalkepatuhan11 = random.randint(1,5)
    soalkepatuhan12 = random.randint(1,5)
    soalkepatuhan13 = random.randint(1,5)
    soalkepatuhan14 = random.randint(1,5)
    soalkepatuhan15 = random.randint(1,5)
    soalkepatuhan16 = random.randint(1,5)
    soalkepatuhan17 = random.randint(1,5)
    soalkepatuhan18 = random.randint(1,5)
    soalkepatuhan19 = random.randint(1,5)
    soalkepatuhan20 = random.randint(1,5)
    soalkepatuhan21 = random.randint(1,5)
    soalkepatuhan22 = random.randint(1,5)
    soalkepatuhan23 = random.randint(1,5)
    soalkepatuhan24 = random.randint(1,5)
    soalkepatuhan25 = random.randint(1,5)
    soalkepatuhan26 = random.randint(1,5)
    df.loc[i+1] =[inisial,jeniskelamin,umurtahun*100+umurbulan,kategoriumur,kelas,terinfeksi,urutanvaksin,soalpengetahuan1,soalpengetahuan2,soalpengetahuan3,soalpengetahuan4,soalpengetahuan5,soalpengetahuan6,soalpengetahuan7,soalpengetahuan8,soalpengetahuan9,soalpengetahuan10,soalpengetahuan11,soalpengetahuan12,soalpengetahuan13,soalpengetahuan14,soalpengetahuan15,soalpengetahuan16,soalpengetahuan17,soalpengetahuan18,soalpengetahuan19,soalpengetahuan20,soalpengetahuan21,soalpengetahuan22,soalpengetahuan23,soalpengetahuan24,soalpengetahuan25,soalkepatuhan1,soalkepatuhan2,soalkepatuhan3,soalkepatuhan4,soalkepatuhan5,soalkepatuhan6,soalkepatuhan7,soalkepatuhan8,soalkepatuhan9,soalkepatuhan10,soalkepatuhan11,soalkepatuhan12,soalkepatuhan13,soalkepatuhan14,soalkepatuhan15,soalkepatuhan16,soalkepatuhan17,soalkepatuhan18,soalkepatuhan19,soalkepatuhan20,soalkepatuhan21,soalkepatuhan22,soalkepatuhan23,soalkepatuhan24,soalkepatuhan25,soalkepatuhan26]
df.to_csv('300data.csv')
    