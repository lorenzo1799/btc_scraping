import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs

driver = webdriver.Chrome()

url = 'https://www.blockchain.com/explorer/assets/btc'

num_requests = 5

transactions = []

for _ in range(num_requests):

    start_time = time.time()

    driver.get(url)

    time.sleep(6)

    html = driver.page_source

    soup = bs(html, 'html.parser')
    
    soldi = soup.find_all(class_='sc-6c545ecc-2')

    transactions.extend(soldi)
    
    print(transactions)
    print('- - - %s seconds to collect data- - -' % (time.time() - start_time))

driver.quit()


with open('transactions.txt', 'w') as file:
    for transaction in transactions:
        file.write(transaction.get_text() + '\n')

with open('transactions.txt', 'r') as file:
    lines = file.readlines()


numbers = [float(line.strip().replace('$', '').replace(',', '')) for line in lines]


numbers_over_10000 = [num for num in numbers if num > 10000]


for num in numbers_over_10000:
    print('${:,.2f}'.format(num))

    print('- - - %s seconds - - -' % (time.time() - start_time))