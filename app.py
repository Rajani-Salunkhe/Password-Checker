import re
import streamlit as st

def check_password_strength(password):
    issues = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        issues.append("at least 8 characters")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        issues.append("at least one digit")

    if any(char.isupper() for char in password):
        score += 1
    else:
        issues.append("an uppercase letter")

    if any(char.islower() for char in password):
        score += 1
    else:
        issues.append("a lowercase letter")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        issues.append("a special character")

    return score, issues

# --- Page Setup ---
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")
st.title("🔐 Password Strength Checker")
st.write("Check how strong your password is — instantly!")

# --- Input ---
password = st.text_input("Enter your password", type="password")

if password:
    score, issues = check_password_strength(password)

    if score == 5:
        st.success("✅ Very Strong — Your password is excellent!")
    elif score == 4:
        st.info("💪 Strong — Almost perfect!")
    elif score == 3:
        st.warning("⚠️ Medium — Could be stronger.")
    else:
        st.error("❌ Weak — Please improve your password.")

    st.write("**Strength Score:**")
    st.progress(score / 5)
    st.caption(f"{score} out of 5 criteria met")

    if issues:
        st.write("**Missing:**")
        for issue in issues:
            st.write(f"  ❌ {issue}")
    else:
        st.write("✅ All criteria met!")