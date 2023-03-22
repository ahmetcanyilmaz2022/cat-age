# cat-age
#########If our cats were human, how old would they be?###########

def cat_to_human(cat_years):
    if cat_years < 0:
        return "please enter your cat's age."
    elif cat_years <= 18:
        human_years = cat_years / 18.0
    elif cat_years <= 24:
        human_years = 1 + (cat_years - 18) / 10.5
    else:
        human_years = 2 + (cat_years - 24) / 4.0
    return "{:.1f}".format(human_years)

print("Human Age\tCat Age")
for cat_years in range(0, 100):
    human_years = cat_to_human(cat_years)
    print("{:d}\t\t{}".format(cat_years, human_years))
    

Human Age       Cat Age
0               0.0
1               0.1
2               0.1
3               0.2
4               0.2
5               0.3
6               0.3
7               0.4
8               0.4
9               0.5
10              0.6
11              0.6
12              0.7
13              0.7
14              0.8
15              0.8
16              0.9
17              0.9
18              1.0
19              1.1
20              1.2
21              1.3
22              1.4
23              1.5
24              1.6
25              2.2
26              2.5
27              2.8
28              3.0
29              3.2
30              3.5
31              3.8
32              4.0
33              4.2
34              4.5
35              4.8
36              5.0
37              5.2
38              5.5
39              5.8
40              6.0
41              6.2
42              6.5
43              6.8
44              7.0
45              7.2
46              7.5
47              7.8
48              8.0
49              8.2
50              8.5
51              8.8
52              9.0
53              9.2
54              9.5
55              9.8
56              10.0
57              10.2
58              10.5
59              10.8
60              11.0
61              11.2
62              11.5
63              11.8
64              12.0
65              12.2
66              12.5
67              12.8
68              13.0
69              13.2
70              13.5
71              13.8
72              14.0
73              14.2
74              14.5
75              14.8
76              15.0
77              15.2
78              15.5
79              15.8
80              16.0
81              16.2
82              16.5
83              16.8
84              17.0
85              17.2
86              17.5
87              17.8
88              18.0
89              18.2
