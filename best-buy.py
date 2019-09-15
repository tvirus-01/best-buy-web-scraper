# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:44:54 2019

@author: adnan

"""
import bs4
import requests as re

q = "gaming+laptop"
prdlink = "https://www.bestbuy.com/site/dell-g3-15-6-gaming-laptop-intel-core-i5-8gb-memory-nvidia-geforce-gtx-1660ti-512gb-solid-state-drive-black/6350872.p?skuId=6350872"

def bestBuyList(query):
    headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
    url = "https://www.bestbuy.com/site/searchpage.jsp?intl=nosplash&st="+query
    data = re.get(url,headers=headers)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    items = soup.find('ol', {"class":"sku-item-list"})
    
    for item in items.find_all("li", {"class":"sku-item"}):
        header = item.find("h4", {"class":"sku-header"})
        title = header.text
        link = "https://bestbuy.com"+header.find("a", href=True)['href']
        
        pricediv = item.find("div", {"class":"priceView-customer-price"})
        price = pricediv.find("span").text
        
        img = item.find("img", {"class":"product-image"})["src"]
        imgsrc = img.split(';')[0]
        
        print("product title:-"+title+"| product link:-"+link+"| product price:-"+price+"| Product image:-"+imgsrc)
      
        
        
def bestBuyPrdDtl(link):        
    headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
    url = link+"&intl=nosplash"
    data = re.get(url,headers=headers)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    
    title = soup.find("div", {"class":"sku-title"}).text
    
    pricediv = soup.find("div", {"class":"priceView-customer-price"})
    price = pricediv.find("span").text
    
    carousel = soup.find("ol", {"class":"carousel-indicate"})
    
    imgsrc = {}
    i = 1
    for liist in carousel.find_all("li", {"class":"thumbnail-wrapper"}):
        img = liist.find("img", src=True)["src"]
        src = img.split(';')[0]
        imgsrc[i] = src
        i = i+1
        
    print("product title:-"+title+"| product price:-"+price+"| Product image:-"+str(imgsrc))
       