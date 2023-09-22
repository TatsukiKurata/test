from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import os
import signal



driver = webdriver.Chrome()
try:
    #指定したURLに遷移する
    driver.get("https://plus-info-tech.com")
    # driver.get("https://www.google.co.jp")

    #キーワード入力ウインドウ要素取得
    element = driver.find_element(By.ID, "menu-item-2030")
    #検索テキストボックスに"abc"を入力
    # element.send_keys("abc")
    element.click()


    element = driver.find_element(By.NAME, "your-name")
    element.send_keys("たっつー")

    element = driver.find_element(By.NAME, "your-email")
    element.send_keys("tattsu0323@gmail.com")

    element = driver.find_element(By.NAME, "your-subject")
    element.send_keys("テスト")

    element = driver.find_element(By.NAME, "your-message")
    element.send_keys("テストテスト")

    element = driver.find_element(By.NAME, "your-consent")
    element.click()

    # element = driver.find_element(By.CLASS_NAME, "wpcf7-form-control has-spinner wpcf7-submit")
    # element.click()

    element = driver.find_element(By.CSS_SELECTOR, "input[value='送信']")
    element.click()






    # #Google検索ボタン取得
    # element2 = driver.find_element(By.NAME, "btnK")
    # #検索ボタンクリック
    # element2.click()

    # タブを閉じる
    # driver.close()

    # driver.quit()


    # from selenium import webdriver

    # browser = webdriver.Chrome()
finally:
    os.kill(driver.service.process.pid,signal.SIGTERM)