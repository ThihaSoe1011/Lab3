import Lab00002_2420.bmi as BMI

def test_calc_bmi_underweight():
    excepted = -1
    result = BMI.calculate_bmi(weight=35.0, height=1.80)
    assert(result == excepted)

def test_calc_bmi_normalweight():
    excepted = 0
    result = BMI.calculate_bmi(weight=65.0, height=1.80)
    assert(result == excepted)

def test_calc_bmi_overweight():
    excepted = 1
    result = BMI.calculate_bmi(weight=95.0, height=1.80)
    assert(result == excepted)