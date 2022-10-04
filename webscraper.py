import requests
import os
import pyperclip as pcp
from qbittorrent import Client
from bs4 import BeautifulSoup as soup
import time
qb=Client('http://127.0.0.1:8081/')
qb.login()
cont='y'
while cont=='y':
    print("script start")
    obj=input('Which topic are you searching for? ')
    obj=obj.replace(' ','+')
    url='https://1337x.unblockit.one/search/'
    headers={'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'}
    #print('{}{}/1/'.format(url,obj))
    request1=requests.get('{}{}/1/'.format(url,obj))
    #print(request1)
    time.sleep(5)
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
    try:
        request2=requests.get(search)
    except:
        print("Sorry!,Connection Error.Please try again")
        exit(1)
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
