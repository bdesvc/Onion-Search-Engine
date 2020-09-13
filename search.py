from torpy.http.requests import TorRequests
import os,time,subprocess,string,random,ctypes
from colorama import *

def randstr():
	chars = string.ascii_lowercase+string.digits
	return ''.join(random.choice(chars) for _ in range(17))

def randomurl():
	url = 'http://'+randstr()+'.onion'
	return url

banner = Fore.MAGENTA+'''

████████  ██████  ██████      ███████ ███████  █████  ██████   ██████ ██   ██ 
   ██    ██    ██ ██   ██     ██      ██      ██   ██ ██   ██ ██      ██   ██ 
   ██    ██    ██ ██████      ███████ █████   ███████ ██████  ██      ███████ 
   ██    ██    ██ ██   ██          ██ ██      ██   ██ ██   ██ ██      ██   ██ 
   ██     ██████  ██   ██     ███████ ███████ ██   ██ ██   ██  ██████ ██   ██ 
                                                                              
                                                                              

'''

init(convert=True)

def main():
	subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)
	print(banner)
	print(f'                                  Made by @Akex64')

	keyword = input('    [~] Keyword => ')
	time.sleep(1)
	checked = 0
	while True:
		ctypes.windll.kernel32.SetConsoleTitleW(f" Tor Search | Checked {str(checked)}")
		url = randomurl()
		try:
			with TorRequests() as tr:
				with tr.get_session() as sess:
					ret = sess.get(url).text
					checked += 1
					if keyword in ret:
						print(f'{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}Found web-server {str(url)}')
		except:
			checked += 1
if __name__ == '__main__':
	main()
