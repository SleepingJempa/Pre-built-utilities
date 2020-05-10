from selenium import webdriver

links = []

url = 'https://www.youtube.com/playlist?list=PLcacUGyBsOIBlGyQQWzp6D1Xn6ZENx9Y2'
start = 1
end = 63

item = lambda i : '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-video-list-renderer/div[3]/ytd-playlist-video-renderer[{}]/div[2]/a'.format(i)

driver = webdriver.Chrome()
driver.get(url)

for i in range(start, end + 1):
    content = driver.find_element_by_xpath(item(i)).get_attribute('href')
    links.append(content)

f = open('index.htm', 'w')

result = ''

index = 1
for link in links:
    result += '<a href="{' + link + '}">LINK</a><br>\n'
    index += 1

message = "<html><head></head><body>{}</body></html>".format(result)

print(len(links), message)
f.write(message)
f.close()
