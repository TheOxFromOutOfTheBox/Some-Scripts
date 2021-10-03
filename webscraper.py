#from selenium import webdriver
#browser=webdriver.Chrome("E:\DOWNLOADS\chromedriver_win32\chromedriver")
import requests
import pyperclip as pcp
from qbittorrent import Client
from bs4 import BeautifulSoup as soup
qb=Client('http://127.0.0.1:8080/')
qb.login()
cont='y'
while cont=='y':
    obj=input('Which topic are you searching for?')
    obj=obj.replace(' ','+')
    url='https://www.1337x.to/search/'
    headers={'User-Agent':'Mozilla/5.0 (X11; OpenBSD i386; rv:72.0) Gecko/20100101 Firefox/72.0'}
    request1=requests.get('{}{}/1/'.format(url,obj))
    soup1=soup(request1.text,'lxml')
    #print(soup.prettify())
    tr=soup1.find_all('tr')
    links=[]
    for i in range(1,len(tr)):
        try:    
            size=(tr[i].find(class_='coll-4 size mob-vip').contents[0])
        except AttributeError:
            try:
                size=(tr[i].find(class_='coll-4 size mob-user').contents[0])
            except:
               try:
                   size=(tr[i].find(class_='coll-4 size mob-uploader').contents[0])
               except:
                   size=(tr[i].find(class_='coll-4 size mob-trial-uploader').contents[0])
                   
        links.append(tr[i].find('a',class_=None).get('href'))
        print('{}){}\n Seeds:{} Leeches:{} Size:{}\n'.format(i,tr[i].find(class_='coll-1 name').text,tr[i].find(class_='coll-2 seeds').contents[0],tr[i].find(class_='coll-3 leeches').contents[0],size))
    
    which=int(input('Which one do you want to download?'))
    if (which==0):
        continue
    newurl='https://www.1377x.to'
    search=newurl+links[which-1]
    request2=requests.get(search)
    soup2=soup(request2.text,'lxml')
    all_links=[]
    all_a=soup2.find_all('a')
    for item in all_a:
        all_links.append(item.get('href'))
    no_copy_links=[]
    for item in all_links:
        if item not in no_copy_links:
            no_copy_links.append(item)
    for item in no_copy_links:
        if 'magnet' in item:
            magnet_link=item
#    print(magnet_link)
#    pcp.copy(magnet_link)
    qb.download_from_link(magnet_link)
    print('We have added it to your qb.')
    cont=input('Do you want to continue?(y/n)')
    #print(soup2.title)
