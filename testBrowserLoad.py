from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import sys


def test_browsing(url):
  options = webdriver.ChromeOptions()
  #options.binary_location = '/usr/lib/chromium-browser/chromedriver'
  options.add_argument('--headless')
  options.add_argument('--no-sandbox')

  driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=options)
  #driver = webdriver.Chrome(chrome_options=options)
  #driver.set_window_size(1024, 768)

  driver.get(url)
  navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
  dnsLookupStart = driver.execute_script("return window.performance.timing.domainLookupStart")
  dnsLookupEnd = driver.execute_script("return window.performance.timing.domainLookupEnd")
  connStart = driver.execute_script("return window.performance.timing.connectStart")
  connEnd = driver.execute_script("return window.performance.timing.connectEnd")
  reqStart = driver.execute_script("return window.performance.timing.requestStart")
  responseStart = driver.execute_script("return window.performance.timing.responseStart")
  responseEnd = driver.execute_script("return window.performance.timing.responseEnd")
  domComplete = driver.execute_script("return window.performance.timing.domComplete")
  loadEventEnd = driver.execute_script("return window.performance.timing.loadEventEnd")
  secureHndShkStart = driver.execute_script("return window.performance.timing.secureConnectionStart")

  dnsLookupTime = abs((dnsLookupEnd - dnsLookupStart)/1000)
  connTime = abs((connEnd - connStart)/1000)
  reqTime = abs((responseStart - reqStart)/1000)
  respTime = abs((responseEnd - responseStart)/1000)
  reqrespTime = abs((responseEnd - reqStart)/1000)
  secureLoadTime = abs((connEnd - secureHndShkStart)/1000)
  loadTime = abs((domComplete - responseEnd)/1000)
  totalPageLoadTime = abs((loadEventEnd - navigationStart)/1000)
  driver.close()
  driver.quit()

  loadTime = [dnsLookupTime,connTime,reqTime,respTime,reqrespTime,secureLoadTime,totalPageLoadTime]

  print(loadTime)

urls = ['https://www.cnn.com/']
test_browsing(urls[0])
