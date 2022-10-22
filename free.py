import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from v13 import main

    main()

elif bit == '32bit':

    from v13s import main

    main()
