# imports

import streamlit as st
import pandas as pd
import os
from io import BytesIO
import random

# Work Starts

st.set_page_config(page_title="Data Sweeper", layout="wide",  page_icon="🧹")

# List of growth mindset challenges
challenges = [
    "💡 Try learning a new skill for 10 minutes today.",
    "📖 Read about someone who overcame challenges.",
    "✍️ Write down 3 things you learned this week.",
    "💬 Ask for feedback and use it to improve.",
    "🚀 Step out of your comfort zone today.",
    "🧘 Practice mindfulness and reflect on your progress.",
    "🎯 Set a small goal and achieve it today!",
    "🤝 Help someone else learn something new."
]

# Streamlit app
st.title("🚀 Growth Mindset Challenge 🌟")

st.write("Embrace challenges, learn from mistakes, and grow every day! 🎯")

if st.button("Get a Challenge 🎲"):
    challenge = random.choice(challenges)
    st.success(challenge)

st.write("🌱 Keep growing and embracing challenges! 💪")  
st.title("🧹 Data Sweeper: Clean & Convert Like a Pro! 🚀")  
st.write("✨ *Growth Mindset Challenge created by Ansharah Khan.* ✨")  
st.write("Effortlessly **convert** your files between **CSV and Excel**, while enjoying **built-in data cleaning** and **powerful visualizations**! ✨")  

uploaded_files = st.file_uploader("📂 **Upload your file (CSV or Excel) & let the magic begin!**", type=["csv", "xlsx"], accept_multiple_files=True)


if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        
        
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue
        
        
        
        
        # Display about the file
        st.write(f"**File Name : ** {file.name}")
        st.write(f"**File Size : ** {file.size/1024}")
        
        
        # Show 5 rows of our df
        st.write(f"**Preview the Head of the DataFrame**")
        st.dataframe(df.head())
        
        
        # Options for data cleaning
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace= True)
                    st.write("Duplicates Removed!")
            
            with col1:
                if st.button(f"Fill Missing Vlaues for {file.name}"):
                    numric_cols = df.select_dtypes(include=['numbers']).column
                    df[numric_cols] = df[numric_cols].fillna(df[numric_cols].mean)
                    st.write("Missing Values have been Filled!")
                    
                    
         
         # Choose Specific to keep or convert     
        st.subheader("📊 Select Columns to Convert")
        columns = st.multiselect(f"📝 Choose Columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]

                    
        # Create Some Visualization
        st.subheader("📊 Data Visualization")     
        if st.checkbox(f"Show Visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])       
            
            
        # Convert the File --> CSV to excel
        st.subheader("⚙️ Conversion Options")
        Conversion_type = st.radio(f"Convert {file.name} to: ", ["CSV",  "Excel"], key=file.name)    
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if Conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mine_type = "text/csv"
                
            elif Conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mine_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)
            
            
            
            # Download Button
            
            st.download_button(
                label=f"Download {file.name} as {Conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mine_type
            )
            
            
            
st.success("✅ All files processed!")        