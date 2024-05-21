from parse_lidar_readings import get_obstacle_data, parse_lidar_data
from unittest.mock import patch
import pytest


def test_get_obstacle_data_no_data():
    with patch('parse_lidar_readings.parse_lidar_data', return_value=None):
        obstacle_data = get_obstacle_data()
        assert obstacle_data is None


def test_get_obstacle_data_with_data():
    with patch('parse_lidar_readings.get_lidar_readings', return_value=[(11, 100), (12, 50), (123, 150)]):
        with patch('parse_lidar_readings.parse_lidar_data', return_value=([11, 12, 123], [100, 50, 150])):
            obstacle_data = get_obstacle_data()
            assert obstacle_data == {'angles': [11, 12, 123], 'distances': [100, 50, 150]}


# @patch("lidar_readings")
# def test_get_obstacle_data(get_lidar_readings):
#     get_lidar_readings.return_value = [(1, 10), (2, 20)]
#     assert get_obstacle_data() == {'angles': [1, 2], 'distances': [10, 20]}
#
#
# @patch("lidar_readings")
# def test_get_obstacle_data2(get_lidar_readings):
#     get_lidar_readings.return_value = [(11, 100), (12, 50), (123, 150)]
#     assert get_obstacle_data() == {'angles': [11, 12, 123], 'distances': [100, 50, 150]}
#     # assert_called checks if functions got called, in this case get_lidar_readings
#     get_lidar_readings.assert_called()
#
#
# @patch("functions_for_07.get_lidar_readings")
# def test_get_obstacle_data_is_none(get_lidar_readings):
#     get_lidar_readings.return_value = None
#     assert get_obstacle_data() is None
#     # assert_called checks if functions got called, in this case get_lidar_readings
#     get_lidar_readings.assert_called()


