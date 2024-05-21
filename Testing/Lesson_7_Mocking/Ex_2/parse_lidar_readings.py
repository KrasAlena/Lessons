from lidar_readings import get_lidar_readings


def get_obstacle_data():
    """Refer to previous example docstring"""
    readings = get_lidar_readings()
    if readings is not None:
        angles, distances = parse_lidar_data(readings)
        return {'angles': angles, 'distances': distances}
    else:
        return None


def parse_lidar_data(data) -> tuple:
    angles = [d[0] for d in data]
    distances = [d[1] for d in data]
    return angles, distances