import os
import re
import sys
import time
sys.path.append('..')

from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys

from utils import *
from config import url, path

def parsing_lang(recrawler):
    if os.path.exists(path['lang']) and not recrawler:
        return [line.rstrip('\n') for line in open(path['lang'])]

    driver = webdriver.Chrome(path['driver'])
    driver.implicitly_wait(3)
    driver.get(url['base'])
    
    lang_list = []
    soup = bs(driver.page_source, 'html.parser')

    for tag in soup.select("li label"):
        if 'language' in tag['for']:
            lang_list.append(tag['for'].split('_')[-1] + ' ' + tag.contents[1].text)
            
    with open(path['lang'], 'w') as fout:
        fout.write('\n'.join(lang_list))

    driver.close()
    return lang_list



def parsing_keynum():
    if os.path.exists(path['keynum']) and not recrawler:
        return [line.rstrip('\n') for line in open(path['keynum'])]
    driver = webdriver.Chrome(path['driver'])
    driver.implicitly_wait(3)
    driver.get(url['base'])
    
    keynum_list = []
    keys = []
    while(True):
        html = driver.page_source
        soup = bs(html, 'html.parser')
        keys_cp = keys[:]
        keys = []
        for tag in soup.find_all(href=re.compile("lessons/[\d]*$")):
            keys.append(tag['href'].split('/')[-1])
        if keys_cp == keys:
            break
        driver.find_elements_by_class_name('page-link')[-1].click()
        time.sleep(1)
        keynum_list += keys
    
    with open(path['keynum'], 'w') as fout:
        fout.write('\n'.join(keynum_list))

    driver.close()
    return keynum_list

def parsing():
    pass 
