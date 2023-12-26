import time
import matplotlib.pyplot as plt
import numpy as np


def calculate_normals(triangles):
    normals = []
    for triangle in triangles:

        # Вычисление векторов для двух сторон треугольника
        side1 = np.array(triangle[1]) - np.array(triangle[0])
        side2 = np.array(triangle[2]) - np.array(triangle[0])

        # Вычисление нормали как векторного произведения сторон
        normal = np.cross(side1, side2)
        normals.append(normal)

    return normals


def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time


# Генерация миллиона треугольников
triangles = np.random.randint(0, 100, size=(1000000, 3, 3))

# Измерение времени выполнения для подсчета нормалей
normal_times = []
for i in range(1, 7):
    sample_size = 10**i
    sample_triangles = triangles[:sample_size]

    normal_time = measure_time(calculate_normals, sample_triangles)
    normal_times.append(normal_time)

# Построение графика для времени выполнения подсчета нормалей
plt.plot(range(1, 7), normal_times, label='Normals Calculation')
plt.xlabel('Log10(Sample Size)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
