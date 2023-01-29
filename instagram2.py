from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://instagram.com')
time.sleep(5)
username = driver.find_element("xpath",'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
username.send_keys('hatori6362')
password = driver.find_element("xpath",'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
password.send_keys('shin chan')
login = driver.find_element("xpath",'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]')
login.click()
time.sleep(8)
driver.get('https://www.instagram.com/explore/tags/birdsphotography/?next=%2F')
time.sleep(5)
photo1 = driver.find_element("xpath",'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[1]/div[3]/a/div/div[2]')
photo1.click()
time.sleep(2)
import random
listofcomment = ["awesome!!", "cool bird", "nice picture"]

for num in range(5):
    like = driver.find_element("xpath",'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
    like.click()
    time.sleep(5)
    save = driver.find_element("xpath",'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[4]/div/div/button')
    save.click()
    time.sleep(2)
    comment = driver.find_element("xpath",'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
    comment.click()
    comment = driver.find_element("xpath",'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
    comment.click()
    comment.send_keys(random.choice(listofcomment))
    time.sleep(2)
    post = driver.find_element("xpath",'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div[2]/div')
    post.click()
    time.sleep(2)
    next = driver.find_element("xpath",'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button')
    next.click()
    time.sleep(5)
time.sleep(5)
driver.quit()





