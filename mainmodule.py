import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Libs.functions import *

st.set_page_config(layout="wide")

add_bg_from_local("Files/picture/nen.jpg")
chim=chuyen_doi_du_lieu_chim()
thu=chuyen_doi_du_lieu_thu()
bo_sat=chuyen_doi_du_lieu_bosat()
dt_ve=ve()

tab1, tab2, tab3, tab4=st.tabs(["Trang chủ","Giới thiệu","Các loài ","Mua vé"])

with tab1:
    st.markdown("""
    <h1><center><b><font color='red' class='highlight-text' style='white-space: nowrap;'>THẢO CẦM VIÊN MỞ CỬA TẤT CẢ CÁC NGÀY TRONG TUẦN<br>BAO GỒM LỄ TẾT TỪ 6h ĐẾN 18h</font></b></center></h1>
    """, unsafe_allow_html=True)
    st.markdown("""
    <style>
    .highlight-text {
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        background-color: yellow;
        padding: 10px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("<div class='center-image'>", unsafe_allow_html=True)
    st.image("Files/picture/ban_do.jpg", caption="Bản đồ thảo cầm viên", width=1600)
    st.markdown("</div>", unsafe_allow_html=True)
with tab2:
	tabs2()
with tab3:
    tabs3()
with tab4:
    tabs4()