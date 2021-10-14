from conversion import distance

def test_km_to_miles_returns_0pt6213712_miles_for_1km():
    # Arrange

    # Act
    miles = distance.km_to_miles(1)

    # Assert
    assert miles == 0.6213712