from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def message(to="Harshit Behar",message='test'):
    """this a simple function to send a whatsapp message to your friends
	and group using python and selenium an automated tool to parse the HTML 
	content and to change the properties. 
	
	paramters:
	to - enter a name from your contacts it can be friend's name or a group's title.
	message - message to be deliever"""
    d = webdriver.Chrome()		# directory to chromedriver
    d.get('https://web.whatsapp.com/')					# URL to open whatsapp web
    wait = WebDriverWait(driver = d, timeout = 900)			# inscrease or decrease the timeout according to your net connection

    message += '\nthis is a system generated message'			# additional text to with your message to identify that it is send via software
    
    name_argument = f'//span[contains(@title,\'{to}\')]'		# HTML parse code to identify your reciever
    title = wait.until(EC.presence_of_element_located((By.XPATH,name_argument)))
    title.click()							# to open the receiver messages page in the browser
	
	# many a times class name or other HTML properties changes so keep a track of current class name for input box by using inspect elements
    input_path = '//div[@class="pluggable-input-body copyable-text selectable-text"][@dir="auto"][@data-tab="1"]'
    box = wait.until(EC.presence_of_element_located((By.XPATH,input_path)))

    box.send_keys(message + Keys.ENTER)	