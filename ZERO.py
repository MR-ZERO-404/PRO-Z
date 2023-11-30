import os
import platform
from platform import architecture
if architecture()[0]=='64bit':os.system('git pull;chmod +x ZERO_arm64;./ZERO_arm64')
 
elif architecture()[0]=='32bit':os.system('git pull;chmod +x ZERO_armv8l;./ZERO_armv8l')
