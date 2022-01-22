from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class IgBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Firefox(executable_path='')
		
	def login(self):
		driver = self.driver
		driver.get("https://www.instagram.com")
		btn_login = driver.find_element_by_xpath("x_path")
		btn_login.click()
		campo_user = driver.find_element_by_xpath("input_username")
		campo_user.click()
		campo_user.clear()
		campo_user.send_keys(self.username)
		campo_senha = driver.find_element_by_xpath("seu_xpath")
		campo_senha.click()
		campo_senha.clear()
		campo_senha.send_keys(self.password)
		campo_senha.send_keys(Keys.RETURN)
		self.comente_nas_fotos_com_a_hashtag('calistenia')
		
	@staticmethod
	def digite_como_uma_pessoa(frase, onde_digitar):
		for letra in frase:
			onde_digitar.send_keys(letra)
			time.sleep(random.randint(1,5)/30)
	
	def comente_nas_fotos_com_a_hashtag(self, hashtag):
		driver = self.driver
		driver.get("https://www.instagram.com/explore/tags/"+ hashtag+"/")
		for i in range(1,3):
			driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
			time.sleep(5)
		hrefs = driver.find_elements_by_tag_name('a')
		pic_href = [elem.get_attribute('href') for elem in hrefs]
		[href for href in pic_hrefs if hastag in href]
		print(hashtag+'fotos'+str(len(pic_hrefs)))
		for pic_href in pic_hrefs:
			driver.get(pic_href)
			driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
			try:
				comentarios = ['comentário']
				driver.find_element_by_class_name('Ypffh').click()
				campo_comentario = driver.find_element_by_class_name('Ypffh')
				time.sleep(random.randint(2,5))
				self.digite_como_pessoa(random.choice(comentarios), campo_comentario)
				time.sleep(random.randint(30,40))
				driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
				time.sleep(5)
			except Exception as e:
				print(e)
				time.sleep(5)
				
		
		
		
bot = IgBot('myUsername@gmail.com','12345')
bot.login()


	
		
	





