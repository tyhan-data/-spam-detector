import streamlit as st
import joblib
import re

st.set_page_config(
    page_title="Spam Detector",
    page_icon="🛡️",
    layout="centered"
)

@st.cache_resource
def load_model():
    model = joblib.load("Spam_detector.joblib")
    vectorizer = joblib.load("Count_Vectorizer.joblib")
    return model, vectorizer

model, vectorizer = load_model()

st.title("🛡️ Spam Detector")
st.caption("Powered by Multinomial Naive Bayes")

st.divider()

message = st.text_area(
    "Type or paste your message:",
    placeholder="e.g. Congratulations! You won a free prize. Click here now!",
    height=150
)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    check = st.button("🔍 Check Message", use_container_width=True)

if check:
    if not message.strip():
        st.warning("Please enter a message first!")
    else:
        X = vectorizer.transform([message])
        label = model.predict(X)[0]
        proba = model.predict_proba(X)[0]
        spam_prob = proba[1]
        ham_prob = proba[0]

        st.divider()

        if label == "spam":
            st.error(f"🚨 SPAM detected!")
            st.metric("Spam probability", f"{spam_prob*100:.1f}%")
        else:
            st.success(f"✅ Legitimate message (Ham)")
            st.metric("Ham probability", f"{ham_prob*100:.1f}%")

        st.subheader("Probability breakdown")
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Ham", f"{ham_prob*100:.1f}%")
        with col_b:
            st.metric("Spam", f"{spam_prob*100:.1f}%")

        st.progress(float(spam_prob), text=f"Spam score: {spam_prob*100:.1f}%")

st.divider()

with st.expander("📊 Batch check multiple messages"):
    st.caption("Enter each message on a separate line")
    bulk = st.text_area("Messages:", height=150, key="bulk")
    if st.button("Check all"):
        lines = [l.strip() for l in bulk.strip().split("\n") if l.strip()]
        if lines:
            X_bulk = vectorizer.transform(lines)
            labels = model.predict(X_bulk)
            probas = model.predict_proba(X_bulk)
            for msg, lbl, prob in zip(lines, labels, probas):
                icon = "🚨" if lbl == "spam" else "✅"
                st.write(f"{icon} **[{lbl.upper()}]** ({prob[1]*100:.1f}% spam) — {msg[:80]}")

with st.expander("ℹ️ Model info"):
    st.write("**Model:** Multinomial Naive Bayes (sklearn)")
    st.write("**Vectorizer:** CountVectorizer")
    st.write("**Classes:**", list(model.classes_))
    st.write("**Alpha (smoothing):**", model.alpha)
