def style():
    return """<style> 
               footer {visibility: hidden;}
               .stDeployButton {visibility: hidden;}
               </style>
               """
def pix_counts(factors):
    if len(factors) > 11: pn = len(factors)+1
    elif len(factors) > 9: pn = len(factors)+4
    else: pn = len(factors)+3
    return pn
