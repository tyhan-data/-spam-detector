# Spam Detector 🛡️

Spam detector created with Multinomial Naive Bayes.

## Files
```
spam_app/
├── app.py
├── requirements.txt
├── Spam_detector.joblib
└── Count_Vectorizer.joblib
```

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Cloud (free)

1. Push this folder to GitHub
2. Go to https://share.streamlit.io
3. "New app" → select your repo → select `app.py`
4. Deploy!

## Deploy on Hugging Face Spaces (free)

1. Go to https://huggingface.co/new-space
2. Select SDK: Streamlit
3. Upload files (app.py, requirements.txt, both .joblib files)
4. Done!