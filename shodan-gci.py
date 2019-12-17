
import os

os.system("shodan init OwjatLMmmCqakfjyhvvK8mEoC81H5Z9W")

while True:
    print("1.What is my ip?")
    print("2.Scan ip,hostname")
    print("3.Scanning host")
    print("0.Exit")
    query = input("SHODAN>")
    query2 = int(query)
    if query2 == 1:
        os.system("shodan myip")
    elif query2 == 2:
        host = input("Search:")
        gg = "shodan search " + host
        os.system(gg)
    elif query2 == 3:
        host = input("Host:")
        gg = "shodan scan submit " + host
        os.system(gg)
    elif query2 == 0:
        exit(0)
