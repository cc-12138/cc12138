from urllib import request
from urllib import error
import socket
from bs4 import BeautifulSoup as bs

url = 'https://list.tmall.com/search_product.htm?q=%C5%DD%C3%E6&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton'
try:
    resp = request.urlopen(url)
    html_data = resp.read().decode('gbk')
except error.URLError as ex:
    html_data = None
except socket.timeout as ex:
    html_data = None

if html_data:
    soup = bs(html_data,'html.parser')
    paomian_type = soup.find_all('div',class_='attrs j_NavAttrs')
    paomian_type_a = paomian_type[0].find_all('a')
    type_list=[]
    for ahref in paomian_type_a:
        if ahref.string:
            type_list.append(ahref.string)
    t_list=[x.strip() for x in type_list if x.strip()!='']
    l=len(t_list)
    for i in range(2):
        del t_list[l-i-1]
    print("淘宝泡面种类：")
    for i in range(len(t_list)):
        print(t_list[i])
    fa_type = soup.find_all('div',class_='fA-list')
    fa_type_a = fa_type[0].find_all('a')
    ftype_list=[]
    for ahref in fa_type_a:
        if ahref.string:
            ftype_list.append(ahref.string)
    print("可选择收货地点：")
    for i in range(len(ftype_list)):
        print(ftype_list[i])
    