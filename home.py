import streamlit as st
import pandas as pd
import sqlite3
import time

db = sqlite3.connect('data/ingredients.db')

st.write("# หวัดดีคับสุดหล่อทั้งหลาย")
st.write('## ใส่ข้อมูลทั้งหมดเป็นภาษาอังกฤษนะ')

menu_name = st.text_input('ชื่อเมนู')
thumb_url = st.text_input('ลิงค์รูปเมนู')

value = st.multiselect('ส่วนประกอบ', options=['apple', 'avocado', 'banana', 'coconut', 'mango', 'pineapple', 'strawberry', 'chicken egg', 'duck egg', 'beef', 'chicken', 'ham', 'clams', 'cockle', 'crab', 'fish', 'mussels', 'octopus', 'oysters', 'cuttlefish', 'salmon', 'scallop', 'shrimp', 'mantis shrimp', 'splendid squid', 'lemon', 'lime'])
def btn_clicked():
    query = "INSERT INTO all_menus (menu_name, ingredients_list, thumb_url, ts) VALUES (?, ?, ?, ?)"
    cur = db.cursor()
    cur.execute(query, (menu_name, str(value), thumb_url, int(time.time())))
    db.commit()
    st.toast('บันทึกเสร็จสิ้น')
    st.balloons()

st.button('บันทึกเลย!!', on_click=btn_clicked)

existing_data = pd.read_sql_query('SELECT * FROM all_menus', db)
st.table(existing_data)
