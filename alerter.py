import unittest
from unittest.mock import patch

alert_failure_count = 0

def simulate_network_alert(celsius):
    # Return 200 for success and 500 for failure based on celsius threshold
    return 500 if celsius > 200 else 200

def temperature_alert_in_celsius(fahrenheit):
    global alert_failure_count
    celsius = (fahrenheit - 32) * 5 / 9
    response_code = simulate_network_alert(celsius)
    if response_code != 200:
        alert_failure_count += 1  # Properly increment failure count if alert fails

# Sample alerts for verification
temperature_alert_in_celsius(400.5)
temperature_alert_in_celsius(303.6)
assert simulate_network_alert(204.2) == 500
assert alert_failure_count == 2, "Failure count does not match expected value"

class TemperatureAlertTests(unittest.TestCase):

    @patch('__main__.simulate_network_alert')
    def test_failure_count_increment(self, mock_alert):
        global alert_failure_count
        alert_failure_count = 0  # Reset counter for the test
        mock_alert.return_value = 500
        temperature_alert_in_celsius(100)
        self.assertEqual(alert_failure_count, 1, "Failure count should increment when alert fails.")

# Run the unit tests
if __name__ == '__main__':
    unittest.main()
