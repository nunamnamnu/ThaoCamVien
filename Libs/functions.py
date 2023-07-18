import streamlit as st
import base64
import pandas as pd
from unidecode import unidecode
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import re
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import smtplib
import qrcode
from io import BytesIO
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_image = base64.b64encode(file.read()).decode("utf-8")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('data:image/jpeg;base64,{encoded_image}');
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
        }}
        .stApp > div {{
            background-color: rgba(255, 255, 255, 0.5);
            padding: 20px;
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def chuyen_doi_du_lieu_thu():
    # thu=pd.read_excel('Files/excel/thu.xlsx')
    # thu.to_csv("Files/csv/thu.csv")
    animal=pd.read_csv("Files/csv/thu.csv",index_col=0)
    return animal
thu=chuyen_doi_du_lieu_thu()


def chuyen_doi_du_lieu_chim():
    # chim=pd.read_excel('Files/excel/chim.xlsx')
    # chim.to_csv("Files/csv/chim.csv")
    birds=pd.read_csv("Files/csv/chim.csv",index_col=0)
    return birds
chim=chuyen_doi_du_lieu_chim()


def chuyen_doi_du_lieu_bosat():
    # bosat=pd.read_excel('Files/excel/bosat.xlsx')
    # bosat.to_csv("Files/csv/bosat.csv")
    bo_sat=pd.read_csv("Files/csv/bosat.csv",index_col=0)
    return bo_sat
bo_sat=chuyen_doi_du_lieu_bosat()


def tabs2():
    st.image("Files/picture/saigonzoo.jpg")
    st.markdown('''<font color='black'><h2><b>Động vật</b></h2><br>
<font color='black'>7 lớp với hơn 1000 cá thể gồm hàng chục loài có vú, hàng chục giống chim, nhiều giống bò sát và giống có cánh các loại, như: khỉ, gấu ngựa, gấu chó, hổ Đông Dương, hổ Bengal, báo hoa mai, báo lửa, sư tử, tinh tinh, ngựa vằn, linh dương, hươu, nai, heo rừng, mang, nhím, rùa, rái cá, voi châu Á, tê giác trắng, cá sấu hoa cà, cá sấu nước ngọt, trăn đất, công, bò tót,  hà mã, báo đốm Mỹ , hươu cao cổ…    
<h2><font color='black'><b>Thực vật</b></h2><br>
<font color='black'>Thực vật có 1.800 cây gỗ thuộc 260 loài, 23 loài lan nội địa, 33 loài xương rồng, 34 loại bonsai và thảm cỏ xanh trên diện tích 20 ha. Trong đó có những cây cổ thụ hàng trăm năm tuổi, vào hàng quý hiếm nhất Việt Nam
<h2><font color='black'><b>Giáo dục</b></h2><br> 
<font color='black'>Chương trình Giáo dục Bảo tồn và Bảo vệ Môi trường tại Thảo Cầm Viên Sài Gòn được xây dựng theo mô hình của các nước tiên tiến trên thế giới, nhằm mang đến cho các em học sinh những trải nghiệm trực quan, sinh động nhất về thiên nhiên, đồng thời tiếp thu thêm nhiều kiến thức bổ ích về môi trường, các loài cây cỏ và các loài thú trong tự nhiên
<h2><font color='black'><b>Bảo tồn</b></h2><br> 
<font color='black'>Bên cạnh công tác chăm sóc và bảo vệ các giống loài động thực vật đang có nguy cơ bị tuyệt chủng hoặc cạn kiệt, Thảo Cầm Viên Sài Gòn còn nhân giống thành công các loài động thực vật quý hiếm, với mục đích gia tăng số lượng cá thể các loài này và thông qua đó, góp phần bảo tồn nguồn gen và duy trì sự đa dạng của các loài trong tự nhiên.
''',unsafe_allow_html=True)
    
def tabs3():
    tb1, tb2, tb3, tb4=st.tabs(["Chim","Thú","Bò sát","Số loài"])
    index=0
    with tb1:
        for i in chim["Tên loài chim"]:
            chim_1=chim["Tên loài chim"]
            chim_2=chim["Mô tả"]
            chim_3=chim["Nơi sống tự nhiên"]
            chim_4=chim["Types"]
            chim_5=chim["Trạng thái bảo tồn"]
            series = pd.Series(chim_1)
            series_2=pd.Series(chim_2)
            series_3=pd.Series(chim_3)
            series_4=pd.Series(chim_4)
            series_5=pd.Series(chim_5)
            st.markdown(f"<h1><b><font color='black'>{series[index]}</b></h1>",unsafe_allow_html=True)
            list_chim = [unidecode(chim).lower().replace(" ", "_") for chim in chim_1]
            st.image(f'Files/picture/chim/{list_chim[index]}.jpg', width=1600)
            with st.expander("Đọc thêm:"):
                st.markdown(f"<p><font color='black'>{series_2[index]}</p>",unsafe_allow_html=True)
                st.markdown(f'''<ul><font color='black'>
                            <li>Nơi sinh sống: {series_3[index]}</li>
                            <li>Số loài: {series_4[index]}</li>
                            <li>Trạng thái bảo tồn: {series_5[index]}</li>  
                            </ul>
                            ''',unsafe_allow_html=True)
            index+=1
    index=0
    with tb2:
        for i in thu["Tên loài"]:
                thu_1=thu["Tên loài"]
                thu_2=thu["Mô tả"]
                thu_3=thu["Nơi sống tự nhiên"]
                thu_4=thu["Type"]
                thu_5=thu["Trạng thái bảo tồn"]
                series = pd.Series(thu_1)
                series_2=pd.Series(thu_2)
                series_3=pd.Series(thu_3)
                series_4=pd.Series(thu_4)
                series_5=pd.Series(thu_5)
                st.markdown(f"<h1><b><font color='black'>{series[index]}</b></h1>",unsafe_allow_html=True)
                list_thu = [unidecode(thu).lower().replace(" ", "_") for thu in thu_1]
                st.image(f'Files/picture/thu/{list_thu[index]}.jpg', width=1600)
                with st.expander("Đọc thêm:"):
                    st.markdown(f"<p><font color='black'>{series_2[index]}</p>",unsafe_allow_html=True)
                    st.markdown(f'''<ul><font color='black'>
                                <li>Nơi sinh sống: {series_3[index]}</li>
                                <li>Số loài: {series_4[index]}</li>
                                <li>Trạng thái bảo tồn: {series_5[index]}</li>  
                                </ul>
                                ''',unsafe_allow_html=True)
                index+=1
    index=0
    with tb3:
        for i in bo_sat["Tên loài"]:
                bo_sat_1=bo_sat["Tên loài"]
                bo_sat_2=bo_sat["Mô tả"]
                bo_sat_3=bo_sat["Nơi sống tự nhiên"]
                bo_sat_4=bo_sat["Type"]
                bo_sat_5=bo_sat["Trạng thái bảo tồn"]
                series = pd.Series(bo_sat_1)
                series_2=pd.Series(bo_sat_2)
                series_3=pd.Series(bo_sat_3)
                series_4=pd.Series(bo_sat_4)
                series_5=pd.Series(bo_sat_5)
                st.markdown(f"<h1><b><font color='black'>{series[index]}</b></h1>",unsafe_allow_html=True)
                list_bo_sat = [unidecode(bo_sat).lower().replace(" ", "_") for bo_sat in bo_sat_1]
                st.image(f'Files/picture/bosat/{list_bo_sat[index]}.jpg', width=1600)
                with st.expander("Đọc thêm:"):
                    st.markdown(f"<p><font color='black'>{series_2[index]}</p>",unsafe_allow_html=True)
                    st.markdown(f'''<ul><font color='black'>
                                <li>Nơi sinh sống: {series_3[index]}</li>
                                <li>Số loài: {series_4[index]}</li>
                                <li>Trạng thái bảo tồn: {series_5[index]}</li>  
                                </ul>
                                ''',unsafe_allow_html=True)
                index+=1
    with tb4:
        fig = plt.figure(figsize=(12,9))
        sort=chim.sort_values("Types")
        sns.barplot(data=sort,x="Types",y="Tên loài chim",palette="OrRd")
        plt.title("Thống kê theo loài chim")
        st.pyplot(fig)
        for i in range(5):
            st.markdown("\n")
        fig = plt.figure(figsize=(12,9))
        sort=thu.sort_values("Type",ascending=False)
        sns.barplot(data=sort,x="Type",y="Tên loài",palette='YlGn_r')
        plt.title("Thống kê theo loài Thú")
        st.pyplot(fig)
        for i in range(5):
            st.markdown("\n")
        fig = plt.figure(figsize=(12,9))
        sort=bo_sat.sort_values("Type",ascending=False)
        sns.barplot(data=sort,x="Type",y="Tên loài")
        plt.title("Thống kê theo loài Bò Sát")
        st.pyplot(fig)


def validate_email(email):
    # Email format regex pattern
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False
def ve():
    # ve_1=pd.read_excel("Files/excel/tickets.xlsx")
    # ve_1.to_csv("Files/csv/ve.csv",index= False)
    ve=pd.read_csv("Files/csv/ve.csv")
    return ve
dt_ve=ve()
def image_to_base64(image):
    buff = BytesIO()
    image.save(buff, format="JPEG")
    img_str = base64.b64encode(buff.getvalue())
    return img_str
def create_content_qrcode(content, ticket_code):
    data = f"{content} - {ticket_code}"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    encoded_string = image_to_base64(qr_img)
    return encoded_string
    
def tabs4():
    st.image("Files/picture/ve.jpg")
    st.markdown('''<font color='black'>
    #### Mua Vé Online - Nhanh Gọn Tiện Lợi -  Không Lo Xếp Hàng    
    ''',unsafe_allow_html=True) 
    dt_ve['Giá vé (VNĐ)'] = dt_ve['Giá vé'].map(lambda x: f"{x:,.0f}")

    st.dataframe(dt_ve[["Loại vé", "Giá vé (VNĐ)"]],width=700)
    st.markdown('''<font color='black'>
            - (Trẻ em dưới 1m, đi kèm phụ huynh được miễn phí vé vào cổng)
        ''',unsafe_allow_html=True)
    st.markdown("<font color='black'>Mua vé online",unsafe_allow_html=True)
    
    # Input fields
    fullname = st.text_input("Họ tên")
    email_reciever = st.text_input("Email")
    
    # Combo boxes
    num_adult_tickets = st.selectbox(dt_ve.iloc[1,0], range(1, 11), index=0)
    num_child_tickets = st.selectbox(dt_ve.iloc[0,0], range(1, 11), index=0)
    

    
    # Submit button
    if st.button("Mua vé"):
        if validate_email(email_reciever):
            ticket_code = f"YW01{datetime.now().strftime('%Y%m%d%H%M%S')}"
            thanh_tien = num_adult_tickets * dt_ve.iloc[1,1] + num_child_tickets * dt_ve.iloc[0,1]

            # Lưu và csv
            order = {
                'Ho_ten': fullname,
                'Ve_tre_em': num_child_tickets,
                'Ve_nguoi_lon': num_adult_tickets,
                'Tong_cong': thanh_tien,
                'Ma_ve': ticket_code
            }
            tickets = pd.read_csv('Files/csv/ve.csv')
            df = pd.DataFrame([order])
            tickets = pd.concat([tickets, df], ignore_index=True)
            tickets.to_csv('Files/csv/ve.csv', index=False)

            # Gọi hàm để tạo mã QR
            noidung = f'''Họ tên: {fullname}
Số vé người lớn: {str(num_adult_tickets)}
Số vé trẻ em: {str(num_child_tickets)}
Thành tiền: {str('{:,.0f}').format(thanh_tien)}
'''
            image_string = create_content_qrcode(noidung, ticket_code).decode()

            # Gửi mail
            email_sender = 'ltvpython@csc.hcmus.edu.vn'
            password = 'wvahyrllmszdatpb'
            connection = smtplib.SMTP('smtp.gmail.com', 587)
            connection.starttls()
            connection.login(email_sender, password)
            msg = MIMEMultipart()
            msg['Subject'] = f"{ticket_code} - Xác nhận đặt vé thành công"
            msg['From'] = email_sender
            msg['To'] = email_reciever      
            content = f'''
            <style>
        p, b, small {{
            color: black;
        }}
    </style><p>Họ tên: {fullname}</p>
<p>Email: {email_reciever}</p>
<p>Số vé người lớn: {str(num_adult_tickets)}</p>
<p>Số vé trẻ em: {str(num_child_tickets)}</p>
<p>Thành tiền: <b>{str('{:,.0f}'.format(thanh_tien))}</b></p>
<p>Địa chỉ: <a href="https://goo.gl/maps/J64xhAMEKspgdJ5K6" target="_blank">https://goo.gl/maps/J64xhAMEKspgdJ5K6</a></p>
<p><small><a href="https://thaocamvien.streamlit.app/">Thảo Cầm Viên</a></small></p>'''
            mtext = MIMEText(content, "html")
            msg.attach(mtext)
            connection.sendmail(msg["From"], msg["To"], msg.as_string())
            connection.quit()

            # Xuất kết quả
            st.success("Đặt mua vé thành công")
            st.markdown(content, unsafe_allow_html=True)
            
            st.image(f'data:image/{"jpg"};base64,{image_string}', width=200)
        else:
            st.error("Vui lòng nhập email chính xác để chúng tôi gửi vé đến quý khách.")
