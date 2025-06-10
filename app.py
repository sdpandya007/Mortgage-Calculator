import streamlit as st

# Dummy translate function (replace with actual if available)
def translate(text, lang):
    return text  # Placeholder: just returns the text in English

# Simulated app mode
app_mode_key = "MortgageCalculator"
target_lang = "en"

# Streamlit logic
st.set_page_config(page_title="Mortgage Calculator", layout="centered")

if app_mode_key == "MortgageCalculator":
    st.markdown(f"""
    <div style="background-color:#e3f2fd;padding:15px;border-radius:10px;margin-bottom:20px;">
        <h2 style="color:#0d47a1;">{translate('Mortgage Calculator 🏡', target_lang)}</h2>
        <p style="color:#0d47a1;">{translate('Estimate your monthly payments and loan summary.', target_lang)}</p>
    </div>
    """, unsafe_allow_html=True)

    home_price = st.number_input(translate("Home Price (₹)", target_lang), min_value=0.0, value=5000000.0, step=100000.0)
    down_payment = st.number_input(translate("Down Payment (₹)", target_lang), min_value=0.0, value=1000000.0, step=50000.0)
    loan_term_years = st.number_input(translate("Loan Term (Years)", target_lang), min_value=1, value=20)
    interest_rate = st.number_input(translate("Annual Interest Rate (%)", target_lang), min_value=0.0, value=7.5)

    if st.button(translate("Calculate Mortgage", target_lang)):
        loan_amount = home_price - down_payment
        monthly_interest_rate = interest_rate / 1200
        num_payments = loan_term_years * 12

        if monthly_interest_rate == 0:
            monthly_payment = loan_amount / num_payments
        else:
            monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / \
                              ((1 + monthly_interest_rate) ** num_payments - 1)

        total_payment = monthly_payment * num_payments
        total_interest = total_payment - loan_amount

        st.subheader(translate("Mortgage Summary", target_lang))
        st.metric(translate("Monthly Payment", target_lang), f"₹{monthly_payment:,.2f}")
        st.metric(translate("Total Interest", target_lang), f"₹{total_interest:,.2f}")
        st.metric(translate("Total Payment", target_lang), f"₹{total_payment:,.2f}")