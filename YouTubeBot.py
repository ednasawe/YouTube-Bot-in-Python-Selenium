from selenium import webdriver
import time


number_of_drivers = int(input("Enter the number of drivers : " ))
time_to_refresh = int(input("Enter refresh rate time in seconds : " ))
url = input("Enter URL : " )
drivers =[]

for i in range(number_of_drivers):
    drivers.append(webdriver.Chrome(executable_path = "chromedriver"))
    drivers[i].get(url)
while True:
    time.sleep(time_to_refresh)
    for i in range(number_of_drivers):
        drivers[i].refresh()
