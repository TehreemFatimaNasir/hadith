import streamlit as st
import requests

st.title("HADITH App")



# ===================== BOOKS =====================
response = requests.get(f"https://www.hadithapi.com/api/books?apiKey=$2y$10$f3nHAEPg8lIwrKUpFqJn8d3LzmAt7alzuSVWFZj9YTFXn8lvPT6S")
books = response.json()["books"]

bookslist = [f"{b['bookName']}|{b['bookSlug']}" for b in books]

booksName = st.selectbox("Select your desired book", bookslist)

books_slug = booksName.split("|")[1].strip()

# ===================== CHAPTERS =====================
chaptersresponse = requests.get(
    f"https://www.hadithapi.com/api/{books_slug}/chapters?apiKey=$2y$10$f3nHAEPg8lIwrKUpFqJn8d3LzmAt7alzuSVWFZj9YTFXn8lvPT6S"
)

chapterbooks = chaptersresponse.json()["chapters"]

chapterbookslist = [
    f"{c['chapterNumber']}|{c['chapterEnglish']}|{c['chapterArabic']}"
    for c in chapterbooks
]

chapterbooksName = st.selectbox("Select your desired chapter", chapterbookslist)

hadithresponse = requests.get(
    f"https://www.hadithapi.com/public/api/hadiths?apiKey=$2y$10$f3nHAEPg8lIwrKUpFqJn8d3LzmAt7alzuSVWFZj9YTFXn8lvPT6S&book=sahih-bukhari&chapter=2&paginate=100000"
)
hadiths=hadithresponse.json()["hadiths"]["data"]

for h in hadiths:
    st.info(f"{h["hadithNumber"]}|{h["status"]}")
    st.success(h["headingArabic"])
    st.warning(h["headingUrdu"])
    st.warning(h["hadithEnglish"])
    