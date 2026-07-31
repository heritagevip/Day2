cos_104_unit = 3
cos_102_unit = 3
cos_124_unit = 3
csc_122_unit = 2
cos_126_unit = 2
phy_102_unit = 2
phy_108_unit = 1
mth_102_unit = 2
gst_112_unit = 2
def totalunit():
    cos_102_unit+ cos_104_unit+ cos_124_unit + csc_122_unit + cos_126_unit +phy_102_unit+ phy_108_unit+mth_102_unit+ gst_112_unit
    print(totalunit)
def scores(x):
    if x >= 70:
        return 5
    elif x >= 60:
        return 4 
    elif x >= 50:
        return 3
    elif x >= 40:
        return 2
    elif x >= 30:
        return 1
    else:
        return 0
def qp(score, unit):
    return scores(score)*unit
cos_104_score = qp(73 ,3)
cos_102_score = qp(70, 3)
gst_112_score = qp(70,2)
csc_122_score = qp(60,2)
cos_124_score = qp(90,3)
cos_126_score =  qp(67,2)
phy_102_score =  qp(72,2)
mth_102_score =  qp(89,2)
phy_108_score =  qp(90,1)
total_unit = cos_102_unit + cos_104_unit+csc_122_unit+cos_126_unit+cos_124_unit+phy_102_unit+phy_108_unit+mth_102_unit+gst_112_unit
tqp =( cos_102_score+cos_104_score+gst_112_score+csc_122_score+cos_124_score+cos_126_score+phy_102_score+phy_108_score+mth_102_score)
gpa = tqp/total_unit
print(totalunit)
print(gpa)
if gpa >= 4.50:
    print("First class")
elif gpa >=3.50:
    print("Second class upper")
elif gpa >= 2.40:
    print("second class lower")
elif gpa >=1.50:
    print("Third class")
elif gpa >= 1.00:
    print("pass")
else:
    print("fail")