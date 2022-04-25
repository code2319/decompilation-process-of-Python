import os, requests, webbrowser
from bs4 import BeautifulSoup
server = input('Server:')
dosid = input('SID:')
os.system('color e')
os.system('title DarkSHOP')
os.system('cls')
selectedpack = 0
cookies = {'dosid': dosid}

def printMenu():
    print('\n /$$$$$$$                      /$$        /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$ \n| $$__  $$                    | $$       /$$__  $$| $$  | $$ /$$__  $$| $$__  $$\n| $$  \\ $$  /$$$$$$   /$$$$$$ | $$   /$$| $$  \\__/| $$  | $$| $$  \\ $$| $$  \\ $$\n| $$  | $$ |____  $$ /$$__  $$| $$  /$$/|  $$$$$$ | $$$$$$$$| $$  | $$| $$$$$$$/\n| $$  | $$  /$$$$$$$| $$  \\__/| $$$$$$/  \\____  $$| $$__  $$| $$  | $$| $$____/ \n| $$  | $$ /$$__  $$| $$      | $$_  $$  /$$  \\ $$| $$  | $$| $$  | $$| $$      \n| $$$$$$$/|  $$$$$$$| $$      | $$ \\  $$|  $$$$$$/| $$  | $$|  $$$$$$/| $$      \n|_______/  \\_______/|__/      |__/  \\__/ \\______/ |__/  |__/ \\______/ |__/      \n\n                                    by botorbit & HeparinX for DarkBot Community\n                                    language changed by code2319                                                                                                                                             \n    [1] Level Up-booster\n    [2] 50% booster\n    [3] Best subscription\n    [4] Tyrannos Centurion\n    [5] Zephyr\n    [6] Berserker ve Solaris\n    [7] Retiarus\n    [8] Agatus Roketi\n    [9] Orcus\n    \n    ')


def getPaymentLink(layername):
    try:
        brnews = BeautifulSoup(requests.post(('https://' + server + '.darkorbit.com/flashAPI/brNews.php'), cookies=cookies).content, 'html.parser')
        layer = brnews.find('layer', {'name': layername})
        paymentreq = layer.find('payment').get('package')
        payment = requests.head(('https://' + server + '.darkorbit.com' + paymentreq), allow_redirects=True, cookies=cookies)
        webbrowser.open_new_tab(payment.url)
    except:
        print('There was an error, but believe me, I don\'t know what it is and I won\'t try to fix it even if you tell me.')


while True:
    os.system('cls')
    printMenu()
    if selectedpack == 1:
        print(str(selectedpack) + ' the link is loading...')
        getPaymentLink('level_up_ascend_booster')
    else:
        if selectedpack == 2:
            print(str(selectedpack) + ' the link is loading...')
            getPaymentLink('50cent_deal')
        else:
            if selectedpack == 3:
                print(str(selectedpack) + ' the link is loading...')
                getPaymentLink('subscriptions')
            else:
                if selectedpack == 4:
                    print(str(selectedpack) + ' the link is loading...')
                    getPaymentLink('unification_special_sale')
                else:
                    if selectedpack == 5:
                        print(str(selectedpack) + ' the link is loading...')
                        getPaymentLink('blacklightranking2nov2020')
                    else:
                        if selectedpack == 6:
                            print(str(selectedpack) + ' the link is loading...')
                            getPaymentLink('valentine2021')
                        else:
                            if selectedpack == 7:
                                print(str(selectedpack) + ' the link is loading...')
                                getPaymentLink('blacklightranking3nov2020')
                            else:
                                if selectedpack == 8:
                                    print(str(selectedpack) + ' the link is loading...')
                                    getPaymentLink('agatusBreachJan2021')
                                else:
                                    if selectedpack == 9:
                                        print(str(selectedpack) + ' the link is loading...')
                                        getPaymentLink('blacklightnov2020')
                                    print()
                                    try:
                                        selectedpack = int(input('Your choice: '))
                                    except ValueError:
                                        selectedpack = 0
