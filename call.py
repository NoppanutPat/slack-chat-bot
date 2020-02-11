import os
from datetime import datetime
import time

work_list = ['<@UTHDBAZ1D>','P JAY'] #PAT,P'JAY

print(str(datetime.now().date()))

while True:

    if str(datetime.now().date()) == "2020-02-11":
        os.system('''curl -X POST -H 'Content-type: application/json' --data '{"text":"'''+work_list[0]+" !! Please send computer to "+work_list[1]+'"}'+link)
        print
        time.sleep(86400)


        

