import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize_scalar, root_scalar
from scipy.integrate import trapezoid


def get_sensor_data():
    hours = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 23]
    temps = [17.5, 16.8, 16.2, 17.4, 20.1, 23.0, 25.4, 26.1, 24.5, 21.8, 19.6, 18.4, 18.0]
    x_data = np.array(hours, dtype=float)
    y_data = np.array(temps, dtype=float)
    return x_data, y_data


def print_hourly_temperatures(spline):
    print("Восстановленная температура по часам:")
    for hour in range(24):
        temp_value = float(spline(hour))
        print(f"  {hour}:00 -> {temp_value:.2f} C")


def find_min_temperature(spline):
    result = minimize_scalar(spline, bounds=(0.0, 23.0), method="bounded")
    min_hour = float(result.x)
    min_temp = float(spline(min_hour))
    return min_hour, min_temp


def negate_spline(x):
    return float(-spline_global(x))


def find_max_temperature(spline):
    global spline_global
    spline_global = spline
    result = minimize_scalar(negate_spline, bounds=(0.0, 23.0), method="bounded")
    max_hour = float(result.x)
    max_temp = float(spline(max_hour))
    return max_hour, max_temp


def calculate_average_temperature(x_grid, y_grid):
    integral_value = trapezoid(y_grid, x_grid)
    duration = float(x_grid[-1] - x_grid[0])
    avg_temp = float(integral_value / duration)
    return avg_temp


def find_threshold_crossings(spline, x_grid, threshold): 
    crossings = []
    for i in range(len(x_grid) - 1):
        left_x = float(x_grid[i])
        right_x = float(x_grid[i + 1])
        left_diff = float(spline(left_x) - threshold)
        right_diff = float(spline(right_x) - threshold)
        if left_diff * right_diff < 0:
            root_res = root_scalar(
                lambda x: float(spline(x) - threshold),
                bracket=[left_x, right_x],
            )
            if root_res.converged:
                crossings.append(float(root_res.root))
    return crossings


def build_plot(x_data, y_data, x_grid, y_grid, min_point, max_point, threshold, crossings):
    min_hour, min_temp = min_point
    max_hour, max_temp = max_point

    plt.figure(figsize=(10, 5))
    plt.plot(x_grid, y_grid, label="Плавная кривая (CubicSpline)")
    plt.scatter(x_data, y_data, color="black", zorder=5, label="Исходные точки датчика")
    plt.axhline(threshold, color="green", linestyle="--", label=f"Норма ({threshold:.0f} C)")
    plt.scatter([min_hour], [min_temp], color="blue", zorder=6, label="Минимум")
    plt.scatter([max_hour], [max_temp], color="red", zorder=6, label="Максимум")

    for point in crossings:
        plt.scatter([point], [threshold], color="orange", edgecolors="black", zorder=7)

    plt.title("Температура воздуха в теплице за сутки")
    plt.xlabel("Время, ч")
    plt.ylabel("Температура, C")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("sensor_report.png", dpi=150)
    plt.show()


spline_global = None


def main():
    x_data, y_data = get_sensor_data()
    spline = CubicSpline(x_data, y_data)

    x_grid = np.linspace(0.0, 23.0, 400)
    y_grid = spline(x_grid)

    print_hourly_temperatures(spline)

    min_hour, min_temp = find_min_temperature(spline)
    max_hour, max_temp = find_max_temperature(spline)
    avg_temp = calculate_average_temperature(x_grid, y_grid)

    threshold = 22.0
    crossings = find_threshold_crossings(spline, x_grid, threshold)

    print("")
    print(f"Самая низкая температура: {min_temp:.2f} C в {min_hour:.2f} ч")
    print(f"Самая высокая температура: {max_temp:.2f} C в {max_hour:.2f} ч")
    print(f"Средняя температура за день: {avg_temp:.2f} C")
    print("Время пересечения нормы 22.0 C:")
    for point in crossings:
        print(f"  {point:.2f} ч")

    build_plot(
        x_data,
        y_data,
        x_grid,
        y_grid,
        (min_hour, min_temp),
        (max_hour, max_temp),
        threshold,
        crossings,
    )


main()