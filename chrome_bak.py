from selenium import webdriver
from selenium.webdriver.chrome import service as fs
import os

# path_driver = os.getcwd()+'\chromedriver.exe'
# # ドライバー指定でChromeブラウザを開く
# chrome_service = fs.Service(executable_path=path_driver)
# driver = webdriver.Chrome(service=chrome_service)

driver = webdriver.Chrome()

#指定したURLに遷移する
driver.get("https://www.google.co.jp")
#キーワード入力ウインドウ要素取得
element = driver.find_element(By.NAME, "q")
#検索テキストボックスに"abc"を入力
element.send_keys("abc")
#Google検索ボタン取得
element = driver.find_element(By.NAME, "btnK")
#検索ボタンクリック
element.click()

# タブを閉じる
driver.close()

driver.quit()


# from selenium import webdriver

# browser = webdriver.Chrome()