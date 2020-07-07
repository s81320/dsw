url= 'https://www.nytimes.com/section/obituaries'
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text , "html.parser")

all_a = soup.findAll('img')

print(len(all_a))
for one_a in all_a:
    #print(one_a)
    print('** ' , one_a['src'])
    try:
        one_a['alt']
    except:
        print('###### no alternative text exists.')
    else:
         print('** ' , one_a['alt'])
        
    print('*******************')