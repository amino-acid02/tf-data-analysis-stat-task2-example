import pandas as pd
import numpy as np

from scipy.stats import uniform


chat_id = 1022285388 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    # loc = x.mean()
    # scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return (x - 0.008)/(uniform.ppf(1 - alpha)) + 0.008, \
           (x - 0.008)/(uniform.ppf(alpha)) + 0.008
