# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 13:37:23 2021

@author: Tetsuo Nakano
"""

def download_csv():

    import time                            # スリープを使うために必要
    from selenium import webdriver         # Webブラウザを自動操作する（python -m pip install selenium)
    import chromedriver_binary             # パスを通すためのコード

    #ログイン操作
    driver = webdriver.Chrome()           # Chromeを準備
    driver.get('https://v2.nex-pro.com/admin/login?enterprise_code=＜企業用コード＞')  #ログイン画面を開く
    driver.find_element_by_id('admin_login_new_form_login').send_keys('<IDを入力>')
    driver.find_element_by_id('admin_login_new_form_password').send_keys('＜パスワードを入力＞')
    driver.find_element_by_class_name("btn-info").click()

    time.sleep(3)


    #アンケート取得画面での操作
    for i in range(10247,10283):
        driver.get('https://v2.nex-pro.com/admin/enquetes/' + str(i))
        driver.find_element_by_class_name("btn-info").click()
        time.sleep(1)
        driver.find_element_by_class_name("btn-danger").click()
        time.sleep(1)
        driver.find_element_by_class_name("swal2-styled").click()
        time.sleep(1)
        driver.refresh()
        time.sleep(3)
        driver.find_element_by_link_text("ダウンロード").click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[normalize-space()='×']").click()
        time.sleep(1)

    time.sleep(5)         # 5秒間待機
    driver.quit()         # ブラウザを閉じる
