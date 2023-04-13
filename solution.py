import pandas as pd
import numpy as np
from scipy.stats import f_oneway
chat_id = 734920047 # Ваш chat ID, не меняйте название переменной

def solution(x: np.ndarray, y: np.ndarray) -> bool:
    alpha = 0.05
    _, p_value = f_oneway(x, y)
    return p_value < alpha
