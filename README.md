# Spam Detector 🛡️

Multinomial Naive Bayes দিয়ে তৈরি spam detector।

## Files
```
spam_app/
├── app.py
├── requirements.txt
├── Spam_detector.joblib
└── Count_Vectorizer.joblib
```

## Local এ চালাও
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Cloud এ deploy করো (free)

1. এই folder টা GitHub এ push করো
2. https://share.streamlit.io তে যাও
3. "New app" → তোমার repo → `app.py` select করো
4. Deploy!

## Hugging Face Spaces এ deploy করো (free)

1. https://huggingface.co/new-space এ যাও
2. SDK: Streamlit select করো
3. Files upload করো (app.py, requirements.txt, দুটো .joblib)
4. Done!
