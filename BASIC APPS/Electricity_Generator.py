# --- PACKAGES ---

import streamlit as st
import io
import pyqrcode
from base64 import b64encode
import base64
from streamlit_option_menu import option_menu
from fpdf import FPDF
import datetime


# --- PAGE SETTINGS AND STYLING ---

currency = "INR"
page_title = "Electricity Bill Generator"
page_icon = ":bulb:"
layout = "centered"

st.set_page_config(page_title, page_icon, layout)

col1, col2 = st.columns(2)
st.title(page_title + " " + page_icon)
st.subheader("By Mihir Pesswani")

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                <style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["Generate Bill", "Bill Payment"],
    icons=["receipt", "cash-coin"],
    orientation="horizontal"
)

# --- DATE AND TIME ---

dt = datetime.date.today()
now = datetime.datetime.now()
tm = now.strftime("%H:%M:%S")


# --- BILL GENERATION ---

def generate_bill(units):
    total = 0
    if units == 0:
        amount = 0
        add_charge = 0
    elif 0 < units <= 100:
        amount = units * 3.15
        add_charge = 25
    elif 100 < units <= 200:
        amount = units * 4.60
        add_charge = 50
    elif 200 < units <= 300:
        amount = units * 5.15
        add_charge = 75
    elif 300 < units <= 350:
        amount = units * 7.20
        add_charge = 100
    else:
        amount = 0
        add_charge = 3000

    total = amount + add_charge
    bill = float("{:.2f}".format(total))
    return currency + " " + str(bill)


# --- PDF GENERATION LINK ---
def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'


# --- BILL PAYMENT ---

def payment():
    output = "Your Payment Successful !!!"
    img = pyqrcode.create(output)
    buffers = io.BytesIO()
    img.png(buffers, scale=8)
    encoded = b64encode(buffers.getvalue()).decode('ascii')
    print('QR Code Generation Successful')
    im = 'data:image/png;base64, ' + encoded
    return im


# --- MAIN FUNCTION ---

def main():

    if selected == "Generate Bill":
        st.subheader("Generate Bill")
        with st.expander("Consumer Details"):
            name = st.text_input("Enter Name of the Consumer:")
            id = st.text_input("Enter Consumer Id:")

        st.text("""
        No. of units a Bulb takes: 30 \n
        
        """)
    st.image(
        "https://static.vecteezy.com/system/resources/previews/008/525/611/original/air-conditioner-device-electronic-icon-3d-illustration-png.png",
        width=400,  # Manually Adjust the width of the image as per requirement
    )
    bulb = st.number_input(
        "Enter Number of Bulbs:", min_value=0, step=1)

    bulb_unit = 30 * bulb
    if st.button("Generate Bulb Amount"):
        st.text("Your Bulb Amount")
        result = f"""
        Bulbs Amount: {generate_bill(bulb_unit)}
        """
        st.success(result)

    st.markdown("---")

    st.text("""
        No. of units a Tubelight takes: 55 \n
        
        """)

    tubelight = st.number_input(
        "Enter Number of Tubelights:", min_value=0, step=1)

    tubelight_unit = 55 * tubelight
    if st.button("Generate Tubelight Amount"):
        st.text("Your Tubelight Amount")
        result = f"""
        Tubelight Amount: {generate_bill(tubelight_unit)}
        """
        st.success(result)
    st.markdown("---")

    st.text("""
       No. of units a Air Conditioner takes: 120 \n 
        """)
    ac = st.number_input(
        "Enter Number of Air Conditioner:", min_value=0, step=1)
    ac_unit = 120 * ac
    if st.button("Generate Air Conditioner Amount"):
        st.text("Your Air Conditioner Amount")
        result = f"""
        Air Conditioner Amount: {generate_bill(ac_unit)}
        """
        st.success(result)

    st.markdown("---")

    st.text("""
        No. of units a Fan takes: 20 \n
        """)

    fan = st.number_input(
        "Enter Number of Fans:", min_value=0, step=1)
    fan_unit = 20 * fan
    if st.button("Generate Fans Amount"):
        st.text("Your Fans Amount")
        result = f"""
        Fans Amount: {generate_bill(fan_unit)}
        """
        st.success(result)

    total_units = bulb_unit + tubelight_unit + ac_unit + fan_unit

    if st.button("Generate Amount"):
        st.text("Your Bill Amount")
        result = f"""
        Total Amount: {generate_bill(total_units)}
        """
        st.success(result)
        '---'
        export = st.button("Generate Reciept")
        if export:
            st.text("Your Bill Reciept Generated")
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font('Times', 'B', 16)
            pdf.cell(50)
            pdf.cell(80, 12, 'Bangalore Electricity Bill', 1, 0, 'C')
            pdf.ln(20)
            pdf.cell(30, 10, f'{dt}')
            pdf.ln(6)
            pdf.cell(30, 10, f'{tm}')
            pdf.ln(15)
            pdf.cell(30, 10, f'Consumer Name: {name}')
            pdf.ln(7)
            pdf.cell(30, 10, f'Consumer ID: {id}')
            pdf.ln(10)
            pdf.cell(30, 10, f'No. of Bulb Units: {str(bulb_unit)}')
            pdf.ln(7)
            pdf.cell(30, 10, f'No. of Tubelight Units: {str(tubelight_unit)}')
            pdf.ln(7)
            pdf.cell(30, 10, f'No. of Air Conditioner Units: {str(ac_unit)}')
            pdf.ln(7)
            pdf.cell(30, 10, f'No. of Fan Units: {str(fan_unit)}')
            pdf.ln(7)
            pdf.cell(30, 10, f'Total No. of Units: {str(total_units)}')
            pdf.ln(15)
            pdf.cell(
                30, 10, f'Bulbs Amount: {str(generate_bill(bulb_unit)).encode("UTF-8").decode("latin-1")}')
            pdf.ln(7)
            pdf.cell(
                30, 10, f'Tubelights Amount: {str(generate_bill(tubelight_unit)).encode("UTF-8").decode("latin-1")}')
            pdf.ln(7)
            pdf.cell(
                30, 10, f'Air Conditioner Amount: {str(generate_bill(ac_unit)).encode("UTF-8").decode("latin-1")}')
            pdf.ln(7)
            pdf.cell(
                30, 10, f'Fans Amount: {str(generate_bill(fan_unit)).encode("UTF-8").decode("latin-1")}')
            pdf.ln(12)
            pdf.cell(
                30, 10, f'Your Total Bill Amount: {str(generate_bill(total_units)).encode("UTF-8").decode("latin-1")}')
            html = create_download_link(
                pdf.output(dest="S").encode("latin-1"), name)
            st.markdown(html, unsafe_allow_html=True)
            

    if selected == "Bill Payment":
        st.subheader("Bill Payment")

        if st.button("Generate Payment Code"):
            st.text("Your Payment Code. Scan to Pay")
            st.image(payment())
            st.download_button('hello', payment(), mime='image/png', file_name='hello.png') 
        


if __name__ == "__main__":
    main()
