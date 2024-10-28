import unittest
from unittest.mock import patch

alert_failure_count = 0


def simulate_network_alert(celsius):
    print(f'WARNING: Temperature is {celsius} Celsius')
    # Return 200 for success
    # Return 500 for failure
    # This stub always returns 200 (success)
    if celsius > 200:
        return 500
    return 200


def temperature_alert_in_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    response_code = simulate_network_alert(celsius)
    if response_code != 200:
        # Count failures, but currently it's not working correctly
        global alert_failure_count
        alert_failure_count += 0


# Run some sample alerts
temperature_alert_in_celsius(400.5)
temperature_alert_in_celsius(303.6)
assert(simulate_network_alert(204.2) == 500)
print('System status check complete.')
print(f'Number of failed alerts: {alert_failure_count}')

@patch('simulate_network_alert')
def test_failure_count_increment(mock_alert):
    mock_alert.return_value = 500
    temperature_alert_in_celsius(100)
    assert(alert_failure_count == 1)


# Run the unit test
if __name__ == '__main__':
    unittest.main()
