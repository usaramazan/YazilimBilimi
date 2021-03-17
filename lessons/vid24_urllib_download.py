import urllib.request

url1 ="https://unsplash.com/photos/r2nJPbEYuSQ"
url2 ="https://unsplash.com/photos/MG8c-4n1QVE"
url3 ="https://unsplash.com/photos/odxB5oIG_iA"

urlList =[url1,url2,url3]
number =0
for url in urlList:
    urllib.request.urlretrieve(url,'resim'+str(number)+'.npg')
    number+=1