import pandas as pd
import numpy as np
from scipy.stats import t


chat_id = 217552503 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    t_alpha_2 = t.ppf(1 - alpha / 2, n - 1)
    x_mean = x.mean()
    s = np.sqrt(np.var(x))
    interval = (x_mean - t_alpha_2 * s / np.sqrt(n), x_mean + t_alpha_2 * s / np.sqrt(n))
    return interval
