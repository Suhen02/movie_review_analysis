import streamlit as st
import joblib

model = joblib.load("sentiment_model.pkl") 


st.title("🎬 Sentiment Analysis App")
st.write("Enter a movie review and I'll predict whether it's **Positive** or **Negative**.")

user_input = st.text_area("Your Review:", "")
if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review.")
    else:
        prediction = model.predict([user_input])[0]
        
        if hasattr(model, "predict_proba"):
            prob = model.predict_proba([user_input])[0]
            confidence = prob.max() * 100
        else:
            confidence = None  
        classes = model.classes_
        if isinstance(prediction, (int, float)):
            label = classes[prediction]
        else:
            label = prediction

      
        if label == "positive" or label == 1:
            if confidence:
                st.success(f"✅ Positive Sentiment (Confidence: {confidence:.2f}%)")
            else:
                st.success("✅ Positive Sentiment")
        else:
            if confidence:
                st.error(f"❌ Negative Sentiment (Confidence: {confidence:.2f}%)")
            else:
                st.error("❌ Negative Sentiment")