import streamlit as st

# util
@st.cache
def calculate_emi(p, n, r):
    first = p * (r / 100)
    numer = (1 + (r / 100)) ** n
    denom = (1 + (r / 100)) ** n - 1
    return round(first * (numer / denom), 3)

@st.cache
def calculate_outstanding_balance(p, n, r, m):
    numer1 = p * (1 + (r / 100)) ** n
    numer2 = (1 + (r / 100)) ** m
    denom = (1 + r / 100) ** n - 1
    return round((numer1 - numer2) / denom, 3)

@st.cache
def update_last_m(val):
    last_m = val

# app creation
st.sidebar.title('Calculate')

to_calc = st.sidebar.selectbox('What to calculate', ('EMI', 'Outstanding Balance'))

principal = st.sidebar.number_input('Principal')
tenure = st.sidebar.number_input('Tenure (in years)')
roi = st.sidebar.number_input('Interest rate (in % per annum)')

if to_calc == 'EMI':
    if st.sidebar.button('Calculate EMI'):
        emi = calculate_emi(principal, tenure * 12, roi / 12)
        st.write('EMI:', emi)
else:
    m = st.sidebar.number_input('Months after')
    
    if st.sidebar.button('Calculate Outstanding Balance'):
        balance = calculate_outstanding_balance(principal, tenure * 12, roi / 12, m)
        st.write('Outstanding balance:', balance)