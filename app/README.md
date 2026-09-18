# app/

GUI / deployment code for the bonus track (up to +2 marks in Review 2).

Suggested stack: Streamlit or Gradio, accepting user inputs and returning predictions from a trained model saved in `../models/`.

## Planned layout

```
app/
├── app.py            # Streamlit/Gradio entry point
└── requirements.txt  # If the app needs deploy-only deps beyond the root ones
```

Deployment target (Streamlit Community Cloud / Hugging Face Spaces / Render): TBD.
