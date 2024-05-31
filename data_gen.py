"""
Random data generating
"""
import numpy as np
import pandas as pd

def col_names():
    ret_cols = ["1m", "6m", "1y", "5y", "All"]
    tstat_cols = [f"{c}_t" for c in ret_cols]
    return ret_cols, tstat_cols

class Returns:
    def __init__(self, N):
        for i in range(1, 6):
            rets = pd.DataFrame(np.random.randn(100,N)) / 40  + .005
            rets.columns = [f"Factor{i}" for i in range(1, N+1)]
            setattr(self, f"q{i}rets", rets)
        

def main():
    N = 10
    df_ret = pd.DataFrame(np.random.randn(N,5) / 100.)
    df_t = pd.DataFrame(np.random.rand(N,5) + 1)
    df = pd.concat([df_ret, df_t], axis=1)

    ret_cols, tstat_cols = col_names()
    cols = ret_cols + tstat_cols
    df[" "] = [f"Factor{i}" for i in range(1, N+1)]
    df.set_index(" ", inplace=True)
    df.columns = cols

    rt = Returns(N)
    hml = rt.q1rets - rt.q5rets

    to = pd.DataFrame(np.random.randn(100,N))
    corr = hml.corr()

    df["ts_ret"] = ((1 + hml.fillna(.0)).cumprod()-1).T.values.tolist()
    df["ts_turnover"] = (to.fillna(.0)).T.values.tolist()

    return df, corr, hml, rt
