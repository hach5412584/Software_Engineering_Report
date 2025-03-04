from mid_4a9g0069 import score

def test_spare():
    data1 = [1,9,2,8,3,7,4,6,5,5,6,4,7,3,8,2,9,1,10,1,10]
    assert score(data1) == 156

def test_strike():
    data = [10,10,10,10,10,10,10,10,10,10,10,10]
    assert score(data) == 300

def test_normal_21():
    data3 = [5,5,5,2,10,8,1,7,3,9,1,3,7,10,7,3,10,10,10]
    assert score(data3) == 172

def test_normal_20():
    data2 = [1,2,3,4,5,5,4,3,2,1,1,2,3,4,5,5,4,3,2,1]
    assert score(data2) == 68
