import numpy as np

def one_dim_kmeans(inputs: np.ndarray, iter_num=300) -> np.ndarray:
    """Кластеризировать входные точки (метод k-средних)"""
    
    threshold = 0
    e_tol = 10 ** (-6)
    center = [inputs.min(), inputs.max()]  # Инициализация центральной точки

    for _ in range(iter_num):
        threshold = (center[0] + center[1]) / 2

        # Проверка расстояния между всеми точками и этими k точками,
        # каждая из которых классифицирована до ближайшего центра
        is_class01 = inputs > threshold # is_class01 = [1 > 0.5, 1 > 0.5, 0 > 0.5, 1 > 0.5]
# is_class01 = [True, True, False, True]

        # Вычисление новой центральной точки
        center = [inputs[~is_class01].mean(), inputs[is_class01].mean()]

        print(f'inputs[~is_class01] = {inputs[~is_class01]}')
        print(f'inputs[is_class01] = {inputs[is_class01]}')

        '''
если is_class01 = np.array([False, False, False, True, True]), 
то ~is_class01 будет np.array([True, True, True, False, False])


если inputs = np.array([1.0, 2.0, 3.0, 4.0, 5.0]) и is_class01 = np.array([False, False, False, True, True]),
то ~is_class01 будет np.array([True, True, True, False, False]). 
В этом случае inputs[~is_class01] вернет:
np.array([1.0, 2.0, 3.0])
        '''

        # Условие остановки
        if np.abs((center[0] + center[1]) / 2 - threshold) < e_tol:
            threshold = (center[0] + center[1]) / 2
            break

    is_class01 = inputs > threshold

    return is_class01

# Пример использования функции
if __name__ == "__main__":
    inputs = np.array([1, 0.25, 0.75, 0])
    iter_num = 3
    result = one_dim_kmeans(inputs, iter_num)
    print(result)  

# Вывод результата
# inputs[~is_class01] = [0.25 0.  ]
# inputs[is_class01] = [1.   0.75]
# [ True False  True False]