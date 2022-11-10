


# -------------------------------------------------
# FIXTURE EXAMPLE    
@pytest.fixture
def input_value():
    height = 1
    weight = 50
    return height, weight


def test_bmifix(input_value, height, weight):
    bmi = cal_bmi(height, weight)
    assert cal_health_status == "HEALTH STAUS: you are obsese"