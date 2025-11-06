import json
import streamlit as st

# ---------------- Load Data ----------------
def load_data():
    try:
        with open("books.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        with open("books.json", "w", encoding="utf-8") as file:
            json.dump([], file)
        return []


# ---------------- Save Data ----------------
def save_data(data):
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# ---------------- UI ----------------
st.title("📚 Book Manager App")

books = load_data()

menu = st.sidebar.radio("القائمة", ["عرض الكتب", "إضافة كتاب", "حذف كتاب"])

if menu == "عرض الكتب":
    st.header("📚 قائمة الكتب")
    if len(books) == 0:
        st.warning("⚠️ لا توجد كتب مسجلة")
    else:
        for book in books:
            st.write(f"**{book['title_book']}** - {book['author_book']} - {book['number_pages']} صفحة")

elif menu == "إضافة كتاب":
    st.header("➕ إضافة كتاب")
    title = st.text_input("عنوان الكتاب")
    author = st.text_input("اسم المؤلف")
    pages = st.number_input("عدد الصفحات", min_value=1)

    if st.button("إضافة"):
        books.append({"title_book": title, "author_book": author, "number_pages": pages})
        save_data(books)
        st.success("✅ تمت إضافة الكتاب")

elif menu == "حذف كتاب":
    st.header("🗑️ حذف كتاب")
    titles = [book["title_book"] for book in books]
    choice = st.selectbox("اختاري كتابًا للحذف", titles)

    if st.button("حذف"):
        for book in books:
            if book["title_book"] == choice:
                books.remove(book)
                save_data(books)
                st.success("🗑️ تم حذف الكتاب")
                break
