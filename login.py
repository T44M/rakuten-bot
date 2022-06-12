if __name__ == '__main__':    
    from time import sleep
    from tracemalloc import stop
    from webdriver_manager.chrome import ChromeDriverManager
    import undetected_chromedriver as uc
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    import hashtag_interi

    Chrome = ChromeDriverManager().install()
    driver = uc.Chrome()

    driver.get("https://grp01.id.rakuten.co.jp/rms/nid/vc?__event=login&service_id=top")

    driver.implicitly_wait(10)

    id = driver.find_element(By.ID, "loginInner_u")
    id.send_keys("your_e-mail_address")

    passwd = driver.find_element(By.ID, "loginInner_p")
    passwd.send_keys("your_password")

    sleep(3)

    driver.find_element(By.CLASS_NAME, "loginButton").click()

    sleep(5)

    driver.find_element(By.CLASS_NAME, "ranking").click()
    driver.implicitly_wait(20)

    driver.find_element(By.LINK_TEXT, "インテリア・寝具・収納").click()

    sleep(5)

    driver.find_elements(By.CLASS_NAME, "rnkRanking_itemName")[3].click() 

    driver.refresh()

    driver.implicitly_wait(20)
    sleep(5)

    element = driver.find_element(By.CLASS_NAME, "susumeruRoom")

    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()

    sleep(5)

    element.click()

    driver.implicitly_wait(60)

    driver.find_element(By.CLASS_NAME, "susumeruRoom").click()
    
    sleep(5)

    handle_array = driver.window_handles
    driver.switch_to.window(handle_array[-1]) #-1にしないとダミータブを選んでしまう。

    htags = driver.find_element(By.ID, "collect-content")

    htags.send_keys(hashtag_interi)  #ハッシュタグをランダムで抽出
    
    driver.save_screenshot('data.png')

    sleep(5)

    driver.find_element(By.CLASS_NAME, "submit-btn-centered").click() #投稿完了

    driver.close()