import requests, time, ctypes
import subprocess as sp
site = "https://googlesd.com"
message_displayed, err_msg, succ_msg  = False, site + " IS DOWN :(", site + " is running fine :)"
while True:
    try:
        code = requests.get(site, timeout = 5).status_code
        if code == 200:
            print(succ_msg)
        else:
            print(err_msg + "\a" * 3)
            if not message_displayed:
                print("Response code: " + str(code))
                sp.call(["msg", "*", err_msg], shell = True)
                message_displayed = True
    except Exception as e:
        print( err_msg + "\a" * 3)
        if not message_displayed:
            print(e)
            sp.call(["msg", "*", err_msg], shell = True)
            message_displayed = True
    time.sleep(30)







##  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | No
##  6 : Cancel | Try Again | Continue
# ctypes.windll.user32.MessageBoxW(0, "Error: " + str(e), "SITE IS DOWN", 0)

# Command window as Popup
# START CMD /C "ECHO My Popup Message && PAUSE"

# mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' ); sh.Popup( 'Message!', 10, 'Title!', 64 );close()"
 # sp.call(["mshta", "javascript:var sh=new ActiveXObject( 'WScript.Shell' ); sh.Popup( '%s', 4, 'SITE IS DOWN', 64 );close()"%(err_msg)], shell = True)
