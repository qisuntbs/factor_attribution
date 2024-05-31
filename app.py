import numpy as np
import streamlit as st
import plotly.express as px
import data_gen

st.set_page_config(page_icon="🧊", page_title="Factor App", layout="wide", initial_sidebar_state="expanded")
st.elements.utils._show_default_value_warning=True

def pix_counts(factors):
    if len(factors) > 11: pn = len(factors)+1
    elif len(factors) > 9: pn = len(factors)+4
    else: pn = len(factors)+3
    return pn

def app():
    st.markdown("""<style> 
                footer {visibility: hidden;}
                .stDeployButton {visibility: hidden;}
                </style>
                """, unsafe_allow_html=True)
    df, corr, rets = data_gen.main()

    t0, t1 = st.tabs(["Return Analysis", "Correlation Analysis"])

    with t0:
        # return attribution
        ret_cols, tstat_cols = data_gen.col_names()
        df_final = df.style.background_gradient(axis=0, cmap="RdYlGn", subset=ret_cols).\
            format('{:.2%}', subset=ret_cols).format('{:.2f}', subset=tstat_cols)

        st.dataframe(df_final,
                     column_config={
                        "ts_ret": st.column_config.LineChartColumn("cumu_ret", y_min=0., y_max=.02),
                        "ts_turnover": st.column_config.LineChartColumn("turnover", y_min=0., y_max=.2),
                     }, height=(len(df)+1)*35+3)

    with t1:
        pn = pix_counts(df.index.to_list())
        corr_df = rets.corr().round(2)
        hml_corr = corr_df.where(np.tril(np.ones(corr_df.shape)).astype(bool))
        fig_corr = px.imshow(hml_corr,
                             height=min(pn*40,1300),
                             text_auto=True,
                             color_continuous_scale='RdYlGn')
        fig_corr.update(layout_coloraxis_showscale=False)
        fig_corr.update_layout(yaxis_title=None, xaxis_title=None)
        st.plotly_chart(fig_corr, use_container_width=False, config={'displayModeBar': False})

if __name__ == "__main__":
    app()