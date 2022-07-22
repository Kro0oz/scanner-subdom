import requests

domain = input("domain: ")
file = open('wordlist.txt','r')
content = file.read()

subdomains = content.splitlines()

for subdomain in subdomains:
	url1 = f"http://{subdomain}.{domain}"
	url2 = f"https://{subdomain}.{domain}"
	try:
		requests.get(url1)
		print(f" URL: {url1}")
		requests.get(url2)
		print(f" URL: {url2}")
	except requests.ConnectionError:
		pass