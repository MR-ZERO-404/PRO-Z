import os
# $P

prefix = os.system("uname -a")
if __name__ == '__main__':
  try:
    if prefix == ["arm64"]:
      os.system("chmod +x")
      os.system("./ZERO_arm64")
    if prefix == ["ZERO_armv8l"]:
      os.system("chmod +x")
      os.system("./ZERO_arm64")
    else:
      exit()
  except:
    print(" $ PREFIX NOT FOUNT ")
