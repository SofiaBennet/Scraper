import requests as REQ
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json
import ast
import re
import time
import threading
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
#Chrome options
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument("--log-level=1")
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--ignore-certificate-errors')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.84 Safari/537.36")
options.add_argument("start-maximized")
#options.add_argument("--allow-cors") SECURITY ISSUE, DON'T USE!!
options.add_argument('--lang=en_US')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


##############CONFIG###############

#Probably wanna keep this login info, if the account gets banned, I believe this will run without a roblox account, unsure
#Sometimes an error will be thrown if captcha is deployed, so use login info here and complete captcha, then run bot in that case
UsernameEnter = "ViewerOfTrades"
PasswordEnter = "Password22"

#I suggest 10k or less difference between min and max
Min_Price = "100"
Max_Price = "5000"
#DOES NOT TAKE INTO ACCOUNT OF ROBLOX 30% CUT
Profit_Percentage = 0.30
#Hook Url
URL = "https://discord.com/api/webhooks/1013467613399101460/SlVhyiFPEKacmITYIq5769GtrIInu3fWHeytMriQA41_pPDIFsrk-hxXPRYGMjPumPDS"

#########END OF CONFIG#############
def Logo():
	print("________00000000000___________000000000000_________")
	print("______00000000_____00000___000000_____0000000______")
	print("____0000000_____________000______________00000_____")
	print("___0000000_______________0_________________0000____")
	print("__000000____________________________________0000___")
	print("__00000_____________________________________ 0000__")
	print("_00000________________EVIL__________________00000__")
	print("_00000_______________STUFF_________________000000__")
	print("__000000_________________________________0000000___")
	print("___0000000______________________________0000000____")
	print("_____000000____________________________000000______")
	print("_______000000________________________000000________")
	print("__________00000_____________________0000___________")
	print("_____________0000_________________0000_____________")
	print("_______________0000_____________000________________")
	print("_________________000_________000___________________")
	print("_________________ __000_____00_____________________")
	print("______________________00__00_______________________")
	print("________________________00_________________________")
#calculate Percentage function
def getPercent(first, second):
   percent = first * second
   print("Percent: "+str(int(percent)))
   return int(percent)
#Thread 1
#Drivers
driver = webdriver.Chrome(options=options)
driver2 = webdriver.Chrome(options=options)

#Action chain
action = ActionChains(driver)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
#Main function
def Initialize(Random):
	Index = 0
	Price_Index = 2
	Session = HTMLSession()
	Login = "https://www.roblox.com/login"
	Catalogue = "https://www.roblox.com/catalog?Category=2&Subcategory=2"
	driver.get(Login)
	#print(driver)
	#Get Web page
	#page = Session.get(Login)
	time.sleep(random.randint(1, Random))
	#Standard login drive
	UserName = driver.find_element("id","login-username")
	Password = driver.find_element("id","login-password")
	EnterField = driver.find_element("id","login-button")
	print("\033[33m")
	Logo()

	#Logs In
	print("\033[33m"+"[*] Logging into Account")

	UserName.send_keys(UsernameEnter)

	time.sleep(random.randint(2, Random))

	Password.send_keys(PasswordEnter)
	time.sleep(0.5)
	#Clicks enter Button
	EnterField.click()
	time.sleep(random.randint(2, Random))
	print("[*] Accessing Shop")
	#Directs bot to catalogue
	driver.find_element(By.LINK_TEXT,"Avatar Shop").click()
	time.sleep(random.randint(2, Random))

	#Gets roblox website
	driver.get("https://www.roblox.com/catalog?Category=2&Subcategory=2&CurrencyType=3&pxMin="+Min_Price+"1&pxMax=" + Max_Price)
	
	time.sleep(3)
	#Creates another window
	print("[*] Prepping Rap Data")
	driver2.get("https://www.rolimons.com/?adlt=strict&toWww=1&redig=C91EB15E358E48C5A329C26DEC5F4DB5")
	time.sleep(5)
	#Find search thing
	driver2.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/div[1]/div[8]/a/div[2]').click()
	#WebDriverWait(driver, 2000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/div[8]/a'))).click()
	print("[*] Starting \033[0m")
	time.sleep(2)
	#Seach bar
	search_bar = driver2.find_element(By.XPATH, '//*[@id="global_item_search_textbox"]')
	scroll = 0
	while(Index < 300):
		#If on wrong page, navigate to shop
		#Main bulk
		try:
			if(Index > 200):
				Index = 20
				driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
				time.sleep(0.5)
				driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
				time.sleep(0.5)
				driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
				time.sleep(0.5)
				driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
				time.sleep(0.5)
			scroll += 1
			if(scroll > 5):
				scroll = 0
				driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
				time.sleep(0.2)
				driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
			Names = driver.find_elements(By.CLASS_NAME,"item-card-name") 
			List = driver.find_elements(By.CLASS_NAME,"text-robux-tile")
			#Retires until A list o f items is provided
			while(len(List) < 2 or len(Names) < 2):
				time.sleep(0.5)
				List = driver.find_elements(By.CLASS_NAME,"text-robux-tile")
			#Moves mouse to item and clicks
			#print(List)
			
			#Names = driver.find_element(str(List[Index])).get_attribute('outerHTML').get_attribute('outerHTML').get_attribute('innerHTML')
			Names = driver.find_element(By.XPATH, '//*[@id="results"]/ul/li['+str(Index + 1)+']/a/div[2]/div[1]/div')
			#Sends name to Rollimon searchup
			search_bar.send_keys(Names.get_attribute('textContent'))
			
			#Get Rap
			Href = driver.find_element(By.XPATH, '//*[@id="results"]/ul/li['+str(Index+1)+']/a').get_attribute('href')
			Rap = driver2.find_element(By.CLASS_NAME, 'global_item_search_stat_data').get_attribute('textContent')
			#OutPut Data to Terminal
			print("\033[34m" + "Name:" + Names.get_attribute('textContent') + "\033[0m")
			print("\033[32m"+"RAP:"+Rap)
			print("\033[31m" + "Price:" + List[Index].get_attribute('textContent') + "\033[0m")
			StrippedPrice = str(List[Index].get_attribute('textContent')).replace(",","")
			StrippedRAP = str(Rap).replace(",","")
			
			#resets Search
			search_bar.clear()
			#Debug Info
			print(Index)
			#Send WebHook if condiotions are met
			if(int(StrippedPrice) < int(StrippedRAP) - getPercent(Profit_Percentage,int(StrippedRAP))):
				Message = {
					
    				"title": "Google it!",
    				"url": Href,
  					
    				"content":"-Item: " + Names.get_attribute('textContent') +"\n +Price: "+StrippedPrice + "\n +RAP: "+StrippedRAP + "\n +Percentage:"+ str(round(getPercent(Profit_Percentage,int(StrippedRAP))/int(StrippedPrice),2))+"%" + "\n [Item]( "+Href+" )"
					}
				REQ.post(URL,Message)
			Index = Index + 1
			time.sleep(0.1)
		except():
			print("E")

	#Parse Content
	#print(List)
	

#Thread 1
T1 = threading.Thread(target = Initialize,args=(3,))
T1.start()

#soup = BeautifulSoup(page.html.html, "html.parser")



time.sleep(20)