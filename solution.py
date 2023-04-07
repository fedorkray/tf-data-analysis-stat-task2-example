import pandas as pd
import numpy as np
from scipy.stats import t


chat_id = 217552503 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    t = 68
    return 2*(-1/2 - (-x).min() )/(t*t), \
           2*(-np.log(1-p)/(x.size) - 1/2 - (-x).min() )/(t*t)
