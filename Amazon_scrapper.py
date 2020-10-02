import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/YOSUDA-Indoor-Cycling-Bike-Stationary/dp/B07D528W98/ref=gbps_img_m-9_475e_ee3fc623?smid=A2XS9KO5PUQHMV&pf_rd_p=5d86def2-ec10-4364-9008-8fbccf30475e&pf_rd_s=merchandised-search-9&pf_rd_t=101&pf_rd_i=15529609011&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=S6QMXWE7MERVN6TWTA91'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.205'}
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="ProductTitle").get_text()


    price = soup.find(id="priceblock_saleprice").get_text()
    converted_price = float(price[0:4])

    if(converted_price < 1.00):
        send_mail()

    print(converted_price)

    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('the email you want to send to', 'Password of your email')

    subject = 'the price have fell down'
    body = "check the GTMONSTER Racing Style Video Gaming Chair you have been looking for https://www.amazon.com/GTMONSTER-Reclining-Ergonomic-Leather-Computer/dp/B08F9JMLDR/ref=sr_1_4_sspa?crid=9QATVXRWUKCB&dchild=1&keywords=gaming+chair&qid=1601656247&sprefix=gamming%2Caps%2C657&sr=8-4-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFCR1RMNUE1WExEN0smZW5jcnlwdGVkSWQ9QTA0NjY4MTAzOUFSRklPUVBKSElIJmVuY3J5cHRlZEFkSWQ9QTA1MDYyMjBUUlVJUDBKVUdSVTUmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"

    msg = f"Subject: {subject}\n\n{body"

    server.sendmail(
        'email you want to send from',
        'Email you want to recive to',
        msg
    )

    print("the email have been sent")
    server.quit()
while(True):
    check_price(
        time.sleep(60*12)
    )