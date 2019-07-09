import os

os.chdir(r"C:\Users\student\startcamp\students")
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SSFAY_SSFAY_SSFAY_SAMSUNG_", "SSFAY_"))
