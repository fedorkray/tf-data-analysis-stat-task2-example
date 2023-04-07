import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    mu = 2 * x.mean() / 68**2  # среднее значение ускорения
    sigma = np.sqrt(1/12)  # стандартное отклонение ошибки измерения пути
    alpha = 1 - p
    z = norm.ppf(1 - alpha/2)
    h = z * sigma / np.sqrt(n)  # половина длины доверительного интервала
    return (mu - h, mu + h)
