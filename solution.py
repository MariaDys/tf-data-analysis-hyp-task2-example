import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 734920047 # Ваш chat ID, не меняйте название переменной

import numpy as np
from scipy.stats import f_oneway

def solution(x: np.ndarray, y: np.ndarray) -> bool:
    alpha = 0.05
    _, p_value = f_oneway(x, y)
    return p_value < alpha
