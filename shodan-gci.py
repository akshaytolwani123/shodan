import  shodan
import socket

SHODAN_API_KEY = "OwjatLMmmCqakfjyhvvK8mEoC81H5Z9W"
api = shodan.Shodan(SHODAN_API_KEY)

while  True:
    print("1.What is my ip?")
    print("2.Scanning Host ")
    print("3.Shodan search to scan ip,port and hostname")
    print("0.Exit")
    query = input("SHODAN>")
    query2 = int(query)
    if query2 == 1:
        ip = socket.gethostbyname(socket.gethostname())
        print(ip)
    elif query2 == 2:
        search = input("Host: ")
        results = api.host(search)
        try:
            for result in results['data']:
                print(result['ip_str'])
                print("Open Ports: ", end = "")
                print(result['port'])
                print("Operating System: ", end = "")
                print(result['os'])
                print("Hostname: ", end = "" )
                print(result['hostnames'])



        except shodan.APIError as e:
            print(e)

    elif  query2 == 3:
         search = input("Host: ")

         results = api.search(search)
         try:
             for result in results['matches']:
                 print(result['ip_str'], end = "")
                 print(result['hostnames'])


         except shodan.APIError as e:
             print(e)
    elif query2 == 0:
        print("[x] Exitting the program")
        exit(code=0)

